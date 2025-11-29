from flask import Flask, request
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os
from flask_cors import CORS
import threading
from user_agents import parse
import pytz
import database  # Importa nosso novo módulo de banco de dados

app = Flask(__name__)
CORS(app)

# Carrega variáveis de ambiente
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    print("AVISO: EMAIL NAO CONFIGURADO! Verifique o .env")

# Função para obter data/hora de Brasília
def agora_brasilia():
    brasilia_tz = pytz.timezone('America/Sao_Paulo')
    return datetime.now(brasilia_tz)

# Detecção de bots
def eh_bot(user_agent_string):
    if not user_agent_string:
        return True
    user_agent = parse(user_agent_string)
    return user_agent.is_bot or 'bot' in user_agent_string.lower()

# Envia notificação imediata de visita
def enviar_notificacao_imediata(ip, user_agent):
    agora = agora_brasilia()
    ultimo_email_enviado = database.obter_ultimo_email_enviado()
    
    # Verifica duplicatas (30 segundos)
    if ultimo_email_enviado:
        if ultimo_email_enviado.tzinfo is None:
            brasilia_tz = pytz.timezone('America/Sao_Paulo')
            ultimo_email_enviado = brasilia_tz.localize(ultimo_email_enviado)
        
        tempo_desde_ultimo = (agora - ultimo_email_enviado).total_seconds()
        if tempo_desde_ultimo < 30:
            print(f"DEBUG: Email duplicado ignorado ({tempo_desde_ultimo:.1f}s)")
            return False
    
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        return False

    conteudo_html = f"""
    <html>
    <body>
    <h2>Nós temos visita Bia!</h2>
    <p>Vamos torcer por uma entrevista, boa sorte!! 🎉</p>
    <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmxzbnNwancyZWxpeDA2emdkdnQ4cmN5M2Joa2Y4d2JraGl6aWY4bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/31lPv5L3aIvTi/giphy.gif" alt="Celebracao GIF" style="width:300px; margin: 20px 0;">
    <p><strong>Data e Hora:</strong> {agora.strftime('%d/%m/%Y %H:%M:%S')} (Horário de Brasília)</p>
    </body>
    </html>
    """
    
    msg = MIMEText(conteudo_html, 'html')
    msg['Subject'] = f'Nova Visita em devbianca.tech - {agora.strftime("%H:%M")}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            servidor.send_message(msg)
        print(f"[SUCESSO] Notificação enviada em {agora.strftime('%d/%m/%Y %H:%M:%S')}")
        database.salvar_ultimo_email_enviado(agora)
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar email: {e}")
        return False

# Envia relatório diário por e-mail (MODIFICADO PARA NÃO ZERAR)
def enviar_relatorio_diario():
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        return {"error": "Email não configurado"}, 500
        
    visitas = database.carregar_visitas()
    
    if not visitas:
        return {"message": "Nenhuma visita registrada no total", "total": 0}, 200
    
    agora = agora_brasilia()
    
    # Filtra visitas APENAS para exibição no relatório de "Hoje"
    visitas_hoje = []
    for visita in visitas:
        try:
            # Garante que temos um objeto datetime
            tempo_visita = visita['tempo']
            if isinstance(tempo_visita, str):
                tempo_visita = datetime.fromisoformat(tempo_visita.replace('Z', '+00:00'))
            
            if tempo_visita.date() == agora.date():
                visitas_hoje.append(visita)
        except:
            continue
    
    total_geral = len(visitas)      # Contagem acumulada (NUNCA ZERA)
    total_hoje = len(visitas_hoje)  # Contagem do dia
    
    # Monta a lista de horários de hoje
    detalhes_visitas_hoje = ""
    if visitas_hoje:
        for visita in visitas_hoje:
            tempo = visita['tempo']
            if isinstance(tempo, str):
                tempo = datetime.fromisoformat(tempo.replace('Z', '+00:00'))
            detalhes_visitas_hoje += f"<li>{tempo.strftime('%H:%M:%S')}</li>"
    else:
        detalhes_visitas_hoje = "<li>Nenhuma visita hoje (até agora).</li>"
    
    conteudo_html = f"""
    <html>
    <body>
    <h2>Relatório Diário de Visitas</h2>
    <p><strong>Data:</strong> {agora.strftime('%d/%m/%Y')}</p>
    <hr>
    <h3>Resumo</h3>
    <ul>
        <li><strong>Visitas Hoje:</strong> {total_hoje}</li>
        <li><strong>Total Geral Acumulado:</strong> {total_geral}</li>
    </ul>
    <p>Vamos torcer por uma entrevista!!</p>

    <h3>Detalhes das Visitas de Hoje:</h3>
    <ul>
        {detalhes_visitas_hoje}
    </ul>
    </body>
    </html>
    """
    
    msg = MIMEText(conteudo_html, 'html')
    msg['Subject'] = f'Relatório Diário - Total: {total_geral} visitas'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            servidor.send_message(msg)
        
        print(f"Relatório enviado. Total acumulado: {total_geral}")
        
        # IMPORTANTE: Não removemos mais as visitas do arquivo!
        # A persistência é mantida integralmente no database.py
        
        return {"message": "Relatório enviado", "total_geral": total_geral, "hoje": total_hoje}, 200
    except Exception as e:
        print(f"Erro ao enviar relatório: {e}")
        return {"error": str(e)}, 500

@app.route('/health')
def health():
    return {
        "status": "ok",
        "total_visitas": len(database.carregar_visitas()),
        "timestamp": agora_brasilia().strftime('%d/%m/%Y %H:%M:%S')
    }

@app.route('/enviar-relatorio-diario', methods=['GET', 'POST'])
def rota_enviar_relatorio():
    resultado, status = enviar_relatorio_diario()
    return resultado, status

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    if eh_bot(user_agent):
        return "Acesso negado: Bots não são permitidos.", 403
    
    ip = request.remote_addr
    
    # Registra visita no banco de dados
    database.salvar_visita({
        'tempo': agora_brasilia(),
        'ip': ip,
        'user_agent': user_agent
    })
    
    threading.Thread(target=enviar_notificacao_imediata, args=(ip, user_agent), daemon=True).start()
    return "Bem-vindo ao NotificaSite!"

@app.route('/track-visit', methods=['GET', 'POST', 'OPTIONS'])
def track_visit():
    user_agent = request.headers.get('User-Agent')
    if eh_bot(user_agent):
        return {"error": "Bots não são permitidos"}, 403
    
    ip = request.remote_addr
    
    # Registra visita no banco de dados
    database.salvar_visita({
        'tempo': agora_brasilia(),
        'ip': ip,
        'user_agent': user_agent
    })
    
    threading.Thread(target=enviar_notificacao_imediata, args=(ip, user_agent), daemon=True).start()
    return {"status": "ok", "message": "Visita registrada"}

if __name__ == '__main__':
    app.run(debug=True)