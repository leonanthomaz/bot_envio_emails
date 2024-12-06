# 📧 Envio de E-mails Personalizados com Python

Este projeto é uma solução prática para automatizar o envio de e-mails personalizados com base em dados de um arquivo Excel. Ele utiliza o servidor SMTP do Gmail para realizar os disparos, com mensagens adaptadas dinamicamente de acordo com a meta e as vendas de cada funcionário.

## 🚀 Funcionalidades

- **Automação de E-mails**: Leitura de dados diretamente de um arquivo Excel.
- **Mensagens Personalizadas**: Conteúdo dinâmico para cada destinatário, formatado em HTML.
- **Condições de Envio**:
  - Parabenizar funcionários que atingiram ou superaram a meta.
  - Motivar aqueles que não conseguiram atingir a meta.

## 🛠️ Stacks Utilizadas

As principais tecnologias e bibliotecas utilizadas no projeto são:

- **Python 3.10+**: Linguagem de programação.
- **pandas**: Para manipulação de dados estruturados no Excel.
- **openpyxl**: Suporte para leitura de arquivos Excel no formato `.xlsx`.
- **smtplib**: Para comunicação com o servidor SMTP do Gmail.
- **email.mime**: Para criação e envio de e-mails em texto e HTML.
