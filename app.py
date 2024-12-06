import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de configuração
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Função para enviar o e-mail
def send_email(email_user, email_password, email_to, subject, html_content):
    try:
        # Criando a mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_to
        msg['Subject'] = subject
        
        # Anexando o conteúdo HTML à mensagem
        msg.attach(MIMEText(html_content, 'html'))
        
        # Envio
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email_to, msg.as_string())
        print(f"E-mail enviado com sucesso para {email_to}!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail para {email_to}: {e}")

# Carregar os dados do Excel usando pandas
df = pd.read_excel('vendas.xlsx')  # Carregar o arquivo Excel

# Corpo do e-mail em HTML para vendas acima da meta
html_content_venda_acima_meta = """
<html>
  <body>
    <h1>Parabéns, {nome}!</h1>
    <p>Você superou sua meta de vendas! No período de {periodo}, você vendeu <b>{venda}</b>, superando sua meta de <b>{meta}</b>.</p>
    <p>Continue assim, você está no caminho certo!</p>
    <p>Atenciosamente,<br>Seu Nome</p>
  </body>
</html>
"""

# Corpo do e-mail em HTML para vendas abaixo da meta
html_content_venda_abaixo_meta = """
<html>
  <body>
    <h1>Olá, {nome}!</h1>
    <p>Infelizmente, você não atingiu sua meta de vendas no período de {periodo}. Você vendeu <b>{venda}</b>, abaixo da meta de <b>{meta}</b>.</p>
    <p>Vamos trabalhar juntos para alcançar os resultados esperados no próximo período!</p>
    <p>Atenciosamente,<br>Seu Nome</p>
  </body>
</html>
"""

# Enviar e-mails para todos os funcionários, com base nas condições
for index, row in df.iterrows():
    nome = row['Vendedor']
    email = row['Email']
    periodo = row['Periodo']
    meta = row['Meta']
    venda = row['Venda']

    # Definir o conteúdo dependendo da condição (venda >= meta ou não)
    if venda >= meta:
        # Enviar e-mail parabenizando por atingir a meta
        personalized_content = html_content_venda_acima_meta.format(nome=nome, periodo=periodo, venda=venda, meta=meta)
        subject = "Parabéns pelo resultado de vendas!"
    else:
        # Enviar e-mail com incentivo para melhorar as vendas
        personalized_content = html_content_venda_abaixo_meta.format(nome=nome, periodo=periodo, venda=venda, meta=meta)
        subject = "Vamos alcançar a meta na próxima!"

    # Enviar e-mail
    send_email(EMAIL_USER, EMAIL_PASSWORD, email, subject, personalized_content)
