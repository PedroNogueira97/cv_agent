import os
import sqlite3
from passlib.context import CryptContext

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
USER_DB_FILE = os.path.join(DB_DIR, "cv_agent.db")

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def get_db_connection() -> sqlite3.Connection:
    """Cria/conecta ao banco SQLite."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(USER_DB_FILE)
    conn.row_factory = sqlite3.Row
    
    # Tabela de usuários
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    
    # Tabela de perfil
    conn.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            user_id TEXT PRIMARY KEY,
            nome TEXT DEFAULT '',
            email TEXT DEFAULT '',
            telefone TEXT DEFAULT '',
            linkedin TEXT DEFAULT '',
            github TEXT DEFAULT '',
            formacao TEXT DEFAULT '',
            stack TEXT DEFAULT '',
            projetos TEXT DEFAULT '',
            experiencia TEXT DEFAULT '',
            idiomas TEXT DEFAULT '',
            cursos TEXT DEFAULT '',
            FOREIGN KEY (user_id) REFERENCES users(username)
        )
    """)
    conn.commit()
    return conn

def register_user_db(username, email, password) -> bool:
    conn = get_db_connection()
    try:
        conn.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", 
                     (username, email, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user_db(username):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return dict(row) if row else None

def save_user_profile_db(user_id: str, data: dict) -> None:
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO user_profile (user_id, nome, email, telefone, linkedin, github,
                                  formacao, stack, projetos, experiencia, idiomas, cursos)
        VALUES (:user_id, :nome, :email, :telefone, :linkedin, :github,
                :formacao, :stack, :projetos, :experiencia, :idiomas, :cursos)
        ON CONFLICT(user_id) DO UPDATE SET
            nome=:nome, email=:email, telefone=:telefone, linkedin=:linkedin,
            github=:github, formacao=:formacao, stack=:stack, projetos=:projetos,
            experiencia=:experiencia, idiomas=:idiomas, cursos=:cursos
    """, {"user_id": user_id, **data})
    conn.commit()
    conn.close()

def load_user_profile_db(user_id: str) -> dict:
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM user_profile WHERE user_id = ?", (user_id,)).fetchone()
    conn.close()
    if row is None:
        return {}
    data = dict(row)
    data.pop("user_id", None)
    return data
