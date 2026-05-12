# Salesforce Test Automation Suite

Projeto de automação de testes para Salesforce utilizando Selenium (testes E2E) e K6 (testes de carga).

## Stack

- Python 3.11
- Selenium 4
- pytest + pytest-html
- simple-salesforce
- K6
- GitHub Actions (CI/CD)

## Como rodar localmente

### 1. Ative o ambiente virtual
```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Instale as dependências
```powershell
pip install -r requirements.txt
```

### 3. Configure o .env
Copie o `.env.example`, renomeie para `.env` e preencha com suas credenciais Salesforce.

### 4. Rode os testes E2E
```powershell
pytest -v --html=reports/report.html
```

### 5. Rode os testes de carga
```powershell
k6 run tests/load/salesforce_api_load.js
```

## Variáveis de ambiente

| Variável | Descrição |
|---|---|
| SF_USERNAME | Usuário Salesforce |
| SF_PASSWORD | Senha Salesforce |
| SF_SECURITY_TOKEN | Token de segurança |
| SF_BASE_URL | URL da org |