# Pinterest Lite 📌

Projeto web inspirado no Pinterest, desenvolvido com Flask, com foco em aprendizado de backend, autenticação de usuários e upload de imagens.

## 🚀 Funcionalidades
- Cadastro e login de usuários
- Autenticação com Flask-Login
- Criptografia de senha com Flask-Bcrypt
- Upload de imagens
- Feed com posts
- Perfil de usuário
- Proteção de rotas

## 🛠️ Tecnologias utilizadas
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-WTF
- HTML / CSS
- SQLite

---

## ⚙️ Como rodar o projeto localmente

### 1️⃣ Clone o repositório
```md
git clone https://github.com/edu2899/Pinterest-Lite.git
cd Pinterest-Lite


### 2️⃣ Crie e ative um ambiente virtual
```md
python -m venv venv
venv\Scripts\activate

## Linux / Mac
python3 -m venv venv
source venv/bin/activate


### 3️⃣ Instale as dependências
```md
pip install -r requirements.txt


### 4️⃣ Configure a SECRET_KEY
```md
setx SECRET_KEY "sua_secret_key_aqui"

## No Linux / Mac:
export SECRET_KEY="sua_secret_key_aqui"

## Você pode gerar uma chave segura rodando:
Rode: python secretkey.py


### 5️⃣ Crie o banco de dados
```md
Rode: python criar_banco.py


### 6️⃣ Execute o projeto
```md
Rode: python main.py

## Acesse no navegador:
http://127.0.0.1:5000
