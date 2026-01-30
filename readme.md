# 📊 Automação de Download de Incidentes do Zabbix

Este projeto automatiza o processo de **download de relatórios de incidentes do Zabbix**, eliminando a etapa manual de acessar a interface web, aplicar filtros e salvar arquivos.

O script realiza:
- Login no Zabbix
- Download do relatório em CSV
- Salvamento local do arquivo
- Geração de logs para acompanhamento e troubleshooting

Ideal para rotinas operacionais, automações e integrações com outros scripts.

---

## 🚀 Tecnologias utilizadas
- Python 3
- Requests
- python-dotenv
- Logging (módulo nativo)

---

## 📁 Estrutura do projeto

download_zabbix_incidentes/

│

├── main.py # Script principal

├── .env # Variáveis de ambiente (não versionado)

├── .env.example # Exemplo de variáveis

├── .gitignore

├── README.md

├── relatorios/ # CSVs baixados (ignorado no Git)

├── logs/ # Logs da aplicação (ignorado no Git)

└── venv/ # Ambiente virtual


---

## ⚙️ Configuração do ambiente

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
