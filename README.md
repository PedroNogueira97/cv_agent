# 📄 CV Agent — RH Intelligence (API Backend)

Este repositório contém a **API de Backend** do CV Agent, um ecossistema inteligente para recrutamento e seleção construído com **FastAPI** e o framework **Agno (Phidata)**. Ele fornece inteligência artificial para análise de currículos, busca de informações de mercado e gerenciamento de perfis.

O frontend deste projeto foi movido para um repositório separado para garantir uma arquitetura de microserviços escalável.

## 🚀 Funcionalidades da API

- **🔐 Autenticação Segura**: Gerenciamento de usuários com **JWT (JSON Web Tokens)** e hashing de senhas com **Bcrypt**.
- **🧠 Agente de RH Inteligente**: Endpoints que utilizam agentes Agno para analisar compatibilidade de currículos com vagas.
- **🌐 Integração de Busca**: Coleta de dados em tempo real via **Tavily Search API**.
- **👤 Persistência de Dados**: Armazenamento isolado de perfis e histórico de chat via **SQLite**.
- **🛡️ Pronta para Produção**: Inclui Rate Limiting (SlowAPI), Logs estruturados e suporte a variáveis de ambiente seguras.

## 🛠️ Stack Técnica

- **Framework**: FastAPI
- **Segurança**: PyJWT, Passlib (Bcrypt), SlowAPI
- **IA/Agent**: Agno Framework, OpenAI
- **Banco de Dados**: SQLite3 (SQLAlchemy)

## 📋 Pré-requisitos

- Python 3.10+
- Um gerenciador de pacotes como `pip` ou `uv`.

## ⚙️ Configuração

1. Clone o repositório:

   ```bash
   git clone git@github.com:PedroNogueira97/cv_agent.git
   cd cv_agent
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:

   ```env
   # API Keys
   OPENAI_API_KEY=sua_chave_aqui
   TAVILY_API_KEY=sua_chave_aqui

   # Segurança Backend
   JWT_SECRET=gere_uma_chave_segura (ex: openssl rand -hex 32)
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
   ALLOWED_ORIGINS=http://localhost:8501
   ```

## 🏃 Como Rodar

Para iniciar o servidor de API:

```bash
PYTHONPATH=. python run_backend.py
```

- **URL Base**: `http://localhost:8000`
- **Documentação de API (Swagger)**: `http://localhost:8000/docs`
- **Documentação Alternativa (Redoc)**: `http://localhost:8000/redoc`

## 📂 Estrutura do Projeto

```text
cv_agent/
├── api/                # Lógica da API (FastAPI)
│   ├── routes/         # Endpoints: /auth, /chat, /profile
│   ├── auth.py         # Segurança e Tokens JWT
│   ├── database.py     # Camada de Dados (SQLite)
│   └── main.py         # Configuração da Aplicação
├── agent.py            # Definição do Agente Inteligente (Agno)
├── run_backend.py      # Script de inicialização
├── data/               # Banco de Dados (Ignorado pelo Git)
└── requirements.txt    # Dependências do projeto
```

## 🛡️ Segurança

Este backend implementa:

- Hashing de senhas.
- Expiração de tokens de acesso.
- Validação estrita de tipos com Pydantic.
- Isolamento de dados por usuário baseado no `username` extraído do JWT.

---
Desenvolvido com ❤️ por Pedro Nogueira.
