"""
CV Agent — Agente de RH com Agno + HuggingFace
Analisa compatibilidade de perfil com vagas e gera CVs personalizados.
Dados do usuário e sessões persistidos em SQLite.
"""

import os

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.tools.tavily import TavilyTools

load_dotenv()

# ── Banco de dados SQLite compartilhado ─────────────────────────────
DB_FILE = os.path.join(os.path.dirname(__file__), "data", "cv_agent.db")

db = SqliteDb(
    db_file=DB_FILE,
    session_table="agent_sessions",
    memory_table="agent_memories",
)


def get_agent(user_data: dict, user_id: str, session_id: str = "default") -> Agent:
    """
    Cria e retorna um agente Agno configurado com o modelo OpenAI,
    persistência SQLite e os dados do perfil do usuário.

    Args:
        user_data: Dicionário com os dados do perfil do usuário.
        user_id: ID do usuário para isolamento de dados.
        session_id: ID da sessão para persistência do histórico.

    Returns:
        Agent: Instância do agente Agno configurado.
    """

    def user_experiences() -> str:
        """
        Retorna os dados do perfil profissional do usuário.
        Esta função deve ser chamada SEMPRE antes de qualquer análise de vaga.

        Returns:
            str: Dados formatados do perfil do usuário.
        """
        if not user_data:
            return "Nenhum dado de perfil encontrado. Peça ao usuário para preencher o perfil no painel lateral."

        sections = []

        if user_data.get("nome"):
            sections.append(f"**Nome:** {user_data['nome']}")
        if user_data.get("email"):
            sections.append(f"**Email:** {user_data['email']}")
        if user_data.get("telefone"):
            sections.append(f"**Telefone:** {user_data['telefone']}")
        if user_data.get("linkedin"):
            sections.append(f"**LinkedIn:** {user_data['linkedin']}")
        if user_data.get("github"):
            sections.append(f"**GitHub:** {user_data['github']}")
        if user_data.get("formacao"):
            sections.append(f"**Formação Acadêmica:**\n{user_data['formacao']}")
        if user_data.get("stack"):
            sections.append(f"**Stack Técnica:**\n{user_data['stack']}")
        if user_data.get("projetos"):
            sections.append(f"**Projetos:**\n{user_data['projetos']}")
        if user_data.get("experiencia"):
            sections.append(f"**Experiência Profissional:**\n{user_data['experiencia']}")
        if user_data.get("idiomas"):
            sections.append(f"**Idiomas:**\n{user_data['idiomas']}")
        if user_data.get("cursos"):
            sections.append(f"**Cursos e Certificações:**\n{user_data['cursos']}")

        return "\n\n".join(sections) if sections else "Perfil vazio. Peça ao usuário para preencher os dados."

    # Lê as instruções do prompt de RH
    instructions_path = os.path.join(os.path.dirname(__file__), "prompts", "hr_recruiter.md")
    instructions = open(instructions_path).read()

    agent = Agent(
        name="CV Agent",
        user_id=user_id,
        model=OpenAIChat(
            id="gpt-4.1-mini",
            max_tokens=4096,
        ),
        instructions=instructions,
        tools=[
            TavilyTools(),
            user_experiences,
        ],
        markdown=True,
        # Persistência SQLite — sessões e memória
        db=db,
        session_id=session_id,
        add_history_to_context=True,
        num_history_runs=6,
        # Memória do usuário persistida
        update_memory_on_run=True,
        add_memories_to_context=True,
        description="Analista de RH Sênior especializado em recrutamento para vagas de tecnologia.",
    )

    return agent
