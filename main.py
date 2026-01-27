import requests
import os
import urllib3
from dotenv import load_dotenv
import logging
urllib3.disable_warnings()

# ======================
# CARREGAR .ENV
# ======================
'''
Essa parte da configuração coloquei em um arquivo separado chamado ".env"
Deixei como exemplo um arquivo .env.example mostrando como ele deve ser

'''
load_dotenv()


# ======================
# CONFIG
# ======================


BASE_URL = os.getenv("BASE_URL")
USER = os.getenv("ZABBIX_USER")
PASSWORD = os.getenv("ZABBIX_PASSWORD")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "relatorios")

#criamos a pasta para salvar o arquivo
os.makedirs(OUTPUT_DIR, exist_ok=True)

#Essa session, guarda cookies, mantém headers  e simula um lavegador logado.
session = requests.Session()
session.verify = False  # cuidado em prod porque aqui não validamos certificado !

# ======================
# 1️⃣ LOGIN
# ======================
login_url = f"{BASE_URL}/index.php"

login_payload = {
    "name": USER,
    "password": PASSWORD,
    "enter": "Sign in"
}

resp = session.post(login_url, data=login_payload)

cookies = session.cookies.get_dict()

if not any("zbx" in c for c in cookies):
    raise Exception("Login falhou, cookie de sessão não recebido")

print("Login OK, cookie obtido")

# ======================
# 2️⃣ DOWNLOAD CSV
# ======================
csv_url = f"{BASE_URL}/zabbix.php"

params = {
    "action": "problem.view.csv"
}

csv = session.get(csv_url, params=params)

if csv.status_code != 200 or b"Zabbix" in csv.content[:100]:
    raise Exception("Erro ao baixar CSV (possível sessão inválida)")

# ======================
# 3️⃣ SALVAR ARQUIVO
# ======================
csv_path = os.path.join(OUTPUT_DIR, "zbx_problems_export.csv")

with open(csv_path, "wb") as f:
    f.write(csv.content)

print(f"CSV salvo em {csv_path}")
