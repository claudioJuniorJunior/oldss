# 🚀 Automação de Testes - ViaCEP API

Projeto de automação de testes para a API [ViaCEP](https://viacep.com.br/), desenvolvido em **Ruby** utilizando **Cucumber** com abordagem BDD (Behavior Driven Development).

---

## 📋 Sobre o Projeto

Este projeto realiza testes automatizados na API pública do ViaCEP, validando consultas de CEPs brasileiros. A estrutura segue o padrão Cucumber com separação clara entre especificações, definições de steps e suporte.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| --- | --- |
| **Ruby** | Linguagem de programação |
| **Cucumber** | Framework BDD para escrita de cenários |
| **RSpec** | Framework de expectativas e asserções |
| **HTTParty** | Biblioteca para requisições HTTP |
| **Report Builder** | Geração de relatórios de execução |

## 📁 Estrutura do Projeto

```
├── Gemfile                    # Dependências do projeto
├── Gemfile.lock               # Lock das versões das gems
├── .gitignore                 # Arquivos ignorados pelo Git
└── features/
    ├── specs/                 # Cenários de teste (.feature)
    ├── step_definitions/      # Implementação dos steps
    └── support/               # Configurações e hooks
```

## ⚙️ Pré-requisitos

- **Ruby** (versão 2.5 ou superior)
- **Bundler** (gerenciador de gems)

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/claudioJuniorJunior/oldss.git
cd oldss
```

### 2. Instale as dependências
```bash
bundle install
```

### 3. Execute os testes
```bash
cucumber
```

### 4. Execute com geração de relatório
```bash
cucumber --format json -o results.json
```

## 📊 Relatórios

O projeto utiliza o **Report Builder** para gerar relatórios visuais dos testes executados.

## 🔗 API Testada

- **ViaCEP**: [https://viacep.com.br/](https://viacep.com.br/)
- Endpoint base: `https://viacep.com.br/ws/{cep}/json/`

## 👤 Autor

**Claudio Junior**
- GitHub: [@claudioJuniorJunior](https://github.com/claudioJuniorJunior)

---

⭐ Se este projeto foi útil, deixe uma estrela!
