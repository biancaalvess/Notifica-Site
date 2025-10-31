from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

# Carrega variáveis de ambiente
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

print("Testando envio de e-mail...")
print(f"De: {EMAIL_ADDRESS}")
print(f"Para: {EMAIL_ADDRESS}")
print(f"SMTP: {SMTP_SERVER}:{SMTP_PORT}")

conteudo_html = f"""
<html>
<body>
<h2>Teste de Email</h2>
<p>Este e um email de teste da API de notificacoes.</p>
<p>Data e Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
<p>Se voce recebeu este email, esta funcionando!</p>
</body>
</html>
"""

msg = MIMEText(conteudo_html, 'html')
msg['Subject'] = 'Teste de Email - API Notificacao'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

try:
    print("\nTentando conectar ao servidor SMTP...")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
        print("Iniciando TLS...")
        servidor.starttls()
        print("Fazendo login...")
        servidor.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("Enviando email...")
        servidor.send_message(msg)
    print("\nSUCESSO! Email enviado com sucesso!")
    print("Verifique sua caixa de entrada.")
except smtplib.SMTPAuthenticationError as e:
    print(f"\nERRO: Falha na autenticacao: {e}")
    print("\nPossiveis causas:")
    print("1. Email ou senha incorretos")
    print("2. Senha de aplicativo nao configurada")
    print("3. Verificacao de duas etapas desabilitada")
except Exception as e:
    print(f"\nERRO: {e}")
    print("\nPossiveis causas:")
    print("1. Problemas de conexao")
    print("2. Credenciais incorretas")
    print("3. Firewall bloqueando a conexao")

