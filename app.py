from flask import Flask, request
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os
from flask_cors import CORS
import threading
import schedule
import time
from user_agents import parse

app = Flask(__name__)
CORS(app)

# Carrega variáveis de ambiente
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

# Armazena dados das visitas 
visitas = []
bloqueio = threading.Lock()

# Detecção de bots: bloqueia User-Agents comuns de bots
def eh_bot(user_agent_string):
    if not user_agent_string:
        return True
    user_agent = parse(user_agent_string)
    return user_agent.is_bot or 'bot' in user_agent_string.lower()

# Envia relatório diário por e-mail
def enviar_relatorio_diario():
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("Configuração de e-mail não encontrada. Verifique o arquivo .env")
        return
        
    with bloqueio:
        if not visitas:
            print("Nenhuma visita para relatar hoje.")
            return
        
        agora = datetime.now()
        total_visitas = len(visitas)
        detalhes_visitas = ""
        for visita in visitas:
            detalhes_visitas += f"<p>Visita em: {visita['tempo'].strftime('%d/%m/%Y %H:%M:%S')}</p>"
        
        conteudo_html = f"""
        <html>
        <body>
        <h2>Relatório Diário de Visitas</h2>
        <p>Total de Visitas: {total_visitas}</p>
        <p>Data do Relatório: {agora.strftime('%d/%m/%Y')}</p>
        <p>Vamos torcer por uma entrevista!!</p>

        <h3>Detalhes das Visitas:</h3>
        {detalhes_visitas}
        </body>
        </html>
        """
        msg = MIMEText(conteudo_html, 'html')
        msg['Subject'] = 'Relatório Diário de Visitas'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
                servidor.starttls()
                servidor.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                servidor.send_message(msg)
            print(f"Relatório diário enviado em {agora.strftime('%d/%m/%Y %H:%M:%S')}")
            visitas.clear()  # Limpa a lista de visitas após o envio
        except Exception as e:
            print(f"Erro ao enviar relatório diário: {e}")

# Agenda o relatório diário 
def agendar_relatorio_diario():
    schedule.every().day.at("17:00").do(enviar_relatorio_diario)
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto

# Inicia o agendador em uma thread em segundo plano
threading.Thread(target=agendar_relatorio_diario, daemon=True).start()

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    if eh_bot(user_agent):
        return "Acesso negado: Bots não são permitidos.", 403
    
    with bloqueio:
        visitas.append({
            'tempo': datetime.now(),
            'ip': request.remote_addr,
            'user_agent': user_agent
        })
    return "Bem-vindo ao NotificaSite!"

if __name__ == '__main__':
    app.run(debug=True)