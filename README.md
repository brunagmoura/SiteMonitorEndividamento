# Monitor do Endividamento dos Brasileiros 📈💰

Bem-vindo(a) ao **Monitor do Endividamento dos Brasileiros**!

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Fontes de Dados](#fontes-de-dados)
- [Dados Utilizados](#dados-utilizados)
- [Como Utilizar o Monitor](#como-utilizar-o-monitor)
- [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
- [Apresentação e Acesso](#apresentação-e-acesso)
- [Contato](#contato)

---

## 📚 Sobre o Projeto

O **Monitor do Endividamento dos Brasileiros** surgiu como projeto final do bootcamp em análise de dados para mulheres da Escola Nacional de Administração Pública (ENAP).

Nosso objetivo é analisar dados referentes ao endividamento de pessoas físicas e jurídicas fornecidos pelo Banco Central do Brasil. Expandimos o projeto adicionando variáveis macroeconômicas de bases públicas como o IBGE e a Câmara dos Deputados. O Monitor foi automatizado para atualizar as informações sempre que novos dados são disponibilizados.

Desenvolvido em **Python** 🐍, utilizamos diversas bibliotecas para extração, análise e visualização dos dados.

---

## 🗂️ Fontes de Dados

- **Sistema de Informações de Crédito (Banco Central do Brasil)**
- **Sistema Gerenciador de Séries Temporais (Banco Central do Brasil)**
- **Sistema IBGE de Recuperação Automática (IBGE)**
- **Dados Abertos da Câmara dos Deputados**

---

## 📊 Dados Utilizados

- Parcelas de crédito por período de vencimento
- Quantidade de operações de crédito
- Modalidade das operações de crédito
- Porte dos clientes
- Estado da federação do contratante
- Setor de atuação das empresas contratantes

Para mais detalhes sobre a metodologia utilizada pelo Banco Central do Brasil, [clique aqui](https://www.bcb.gov.br/estabilidadefinanceira/scr).

---

## 🛠️ Como Utilizar o Monitor

Todos os gráficos do Monitor são interativos:

- **Download de imagens**: Clique em **"Download plot as png"** para salvar os gráficos.
- **Ampliar visualização**: Use **"Zoom"**, **"Zoom in"** ou **"Zoom out"**.
- **Arrastar gráfico**: Selecione **"Pan"** para mover o gráfico.
- **Visualização inicial**: Clique em **"Autoscale"** para retornar ao padrão.

---

## 📦 Bibliotecas Utilizadas

- **Extração e Análise de Dados**:
  - `zipfile`
  - `os`
  - `pandas`
  - `deflate`
  - `requests`
  - `sidrapy`
- **Visualização de Dados**:
  - `plotly`
  - `seaborn`
  - `streamlit`

---

## 🎥 Apresentação e Acesso

- **Apresentação do Projeto**: [Assista no YouTube](https://youtu.be/ZA7S4IZpe6k)
- **Acesse o Monitor**: [Visite o Site Oficial](https://monitordoendividamento.streamlit.app)

---

## 💌 Contato

O Monitor é uma construção colaborativa. Tem dúvidas ou quer sugerir uma melhoria?

Entre em contato conosco: [monitordoendividamento@gmail.com](mailto:monitordoendividamento@gmail.com)

---

Esperamos que o **Monitor do Endividamento dos Brasileiros** seja uma ferramenta útil para você! 🧡
