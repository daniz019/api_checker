# API Status Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-00599C?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Um verificador de integridade de APIs desenvolvido em Python, focado em eficiência, modularidade e boas práticas de engenharia de software. Este projeto exemplifica o uso de **Programação Orientada a Objetos (POO)** e estruturação de pacotes para a criação de ferramentas de monitoramento robustas.

## Visão Geral

O **API Status Checker** é uma solução leve para monitoramento de disponibilidade de serviços HTTP. A ferramenta itera sobre uma lista de endpoints configurados, validando códigos de resposta e tratando exceções de rede de forma graciosa. É ideal para diagnósticos rápidos e pode servir como base para sistemas de monitoramento mais complexos.

## Funcionalidades

*   **Verificação de Múltiplos Endpoints**: Testa uma lista de APIs definidas para garantir disponibilidade.
*   **Relatórios de Status**: Identifica códigos de sucesso HTTP e reporta falhas detalhadas.
*   **Tratamento de Exceções Robusto**: Captura e trata erros comuns como falhas de resolução de DNS (NameResolution) e timeouts de conexão.
*   **Arquitetura Profissional**: Código estruturado de forma modular (packages) visando escalabilidade e facilidade de manutenção.
*   **Configuração de Timeout**: Controle sobre o tempo limite de requisições para evitar gargalos de performance.

## Stack Tecnológico

*   **Linguagem**: Python 3.x
*   **Bibliotecas**: Requests (HTTP for Humans)

## Estrutura do Projeto

A organização do código segue padrões de mercado para separar a lógica de negócio do ponto de entrada da aplicação:

```text
api_status/
├── app/
│   ├── __init__.py    # Inicialização do pacote Python
│   └── checker.py     # Lógica central do verificador (Classe ApiChecker)
├── main.py            # Ponto de entrada (Entrypoint) da aplicação
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação técnica
```

## Instalação e Execução

Siga as instruções abaixo para configurar o ambiente de desenvolvimento.

### 1. Clonar o Repositório

```bash
git clone https://github.com/daniz019/api_checker.git
cd api_checker
```

### 2. Configurar Ambiente Virtual (Recomendado)

Isolar as dependências do projeto previne conflitos com outras bibliotecas do sistema.

```bash
# Criação do ambiente virtual
python -m venv venv

# Ativação do ambiente
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

```bash
python main.py
```

## Exemplo de Uso

Ao executar o script `main.py`, o sistema processará as URLs configuradas e retornará o status de cada uma:

```text
API Online (Status: 200)
API Online (Status: 200)
API Offline ou com Erro (Detalhe: HTTPSConnectionPool(...))
```

---
