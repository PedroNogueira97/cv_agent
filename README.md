# 📄 CV Agent — RH Intelligence

CV Agent é um ecossistema inteligente para recrutamento e seleção, construído com **FastAPI**, **Streamlit** e o framework **Agno (Phidata)**. Ele permite analisar a compatibilidade de perfis profissionais com vagas de emprego, gerando insights baseados em IA e currículos personalizados.

O projeto utiliza uma arquitetura moderna e desacoplada, separando completamente a lógica de backend (API) da interface de usuário (Frontend).

## 🚀 Funcionalidades

- **🔐 Autenticação Segura**: Sistema de Login e Cadastro utilizando **JWT (JSON Web Tokens)** e hashing de senhas com **Bcrypt**.
- **🧠 Agente de RH Inteligente**: Agente Agno configurado com modelos da OpenAI para analisar currículos e descrições de vagas.
- **🌐 Busca em Tempo Real**: Integração com **Tavily Search** para coletar informações atualizadas sobre o mercado.
- **👤 Perfis Isolados**: Memória e histórico de chat persistidos de forma privada para cada usuário em um banco de dados **SQLite**.
- **🛡️ Segurança de Produção**: Rate Limiting (SlowAPI) integrado para prevenir abusos e CORS configurado.

## 🛠️ Stack Técnica

- **Backend**: FastAPI, SQLAlchemy, Pydantic, Passlib, PyJWT, SlowAPI.
- **Frontend**: Streamlit, Requests.
- **IA/Agent**: Agno Framework, OpenAI.
- **Database**: SQLite3.

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
   HF_TOKEN=sua_chave_huggingface

   # Segurança Backend
   JWT_SECRET=gere_uma_chave_segura (ex: openssl rand -hex 32)
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
   ALLOWED_ORIGINS=http://localhost:8501
   ```

## 🏃 Como Rodar

O projeto requer dois terminais ativos:

### 1. Iniciar o Backend (API)

```bash
PYTHONPATH=. python run_backend.py
```

A API estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa (Swagger) em `http://localhost:8000/docs`.

### 2. Iniciar o Frontend (Streamlit)

```bash
streamlit run app.py
```

A interface abrirá automaticamente no seu navegador em `http://localhost:8501`.

## 📂 Estrutura do Projeto

```text
cv_agent/
├── api/                # Backend layer (FastAPI)
│   ├── routes/         # Endpoints de Auth, Chat e Profile
│   ├── auth.py         # Lógica de JWT e Segurança
│   ├── database.py     # Conexão e Queries SQLite
│   └── main.py         # Configuração do App FastAPI
├── agent.py            # Lógica do Agente Agno
├── app.py              # Frontend layer (Streamlit)
├── run_backend.py      # Wrapper para execução facilitada do backend
├── data/               # Banco de Dados (Ignorado pelo Git)
└── requirements.txt    # Dependências do projeto
```

## 🛡️ Segurança

Este projeto foi auditado para seguir boas práticas de deploy de SaaS, incluindo:

- Hash de senhas.
- Expiração de Tokens.
- Proteção contra SQL Injection e Prompt Injection.
- Isolamento total de sessões por `user_id`.

---
Desenvolvido com ❤️ por Pedro Nogueira.
