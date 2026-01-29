# Pinterest Lite (Flask)

Projeto inspirado no Pinterest, desenvolvido com Flask, com sistema de login, upload de imagens e feed de posts.

## 🚀 Funcionalidades
- Cadastro e login de usuários
- Autenticação com Flask-Login
- Upload de imagens
- Feed de posts
- Perfil do usuário

## 🛠️ Tecnologias
- Python
- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- SQLite

## ⚙️ Como rodar o projeto

```bash
# clone o repositório
git clone https://github.com/seu-usuario/pinterest-lite-flask.git

# crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# instale as dependências
pip install -r requirements.txt

# configure a variável de ambiente
export SECRET_KEY="sua_chave_secreta"
# Windows (PowerShell):
setx SECRET_KEY "sua_chave_secreta"

# crie o banco de dados
python criar_banco.py

# rode o app
python main.py
