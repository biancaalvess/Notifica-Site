import json
import os
from datetime import datetime
import threading

# Configuração dos arquivos
# O uso de /tmp é necessário para ambientes serverless como Vercel (temporário)
VISITAS_FILE = '/tmp/visitas.json' if os.path.exists('/tmp') else 'visitas.json'
ULTIMO_EMAIL_FILE = '/tmp/ultimo_email.json' if os.path.exists('/tmp') else 'ultimo_email.json'

# Lock para evitar erros de escrita simultânea
bloqueio = threading.Lock()

def carregar_visitas():
    """Carrega todas as visitas salvas no arquivo JSON."""
    try:
        if os.path.exists(VISITAS_FILE):
            with open(VISITAS_FILE, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                visitas = []
                for v in dados:
                    try:
                        # Converte string ISO de volta para datetime
                        if isinstance(v['tempo'], str):
                            v['tempo'] = datetime.fromisoformat(v['tempo'].replace('Z', '+00:00'))
                        visitas.append(v)
                    except:
                        continue
                return visitas
    except Exception as e:
        print(f"Erro ao carregar visitas: {e}")
    return []

def salvar_visita(visita):
    """Adiciona uma única visita e salva no arquivo."""
    with bloqueio:
        visitas = carregar_visitas()
        
        # Garante que o tempo esteja em formato serializável (ISO string)
        visita_copy = visita.copy()
        if isinstance(visita_copy['tempo'], datetime):
            visita_copy['tempo'] = visita_copy['tempo'].isoformat()
            
        # Adiciona à lista existente
        visitas_salvar = []
        
        # Prepara a lista atual para salvar (converte datetimes para string)
        for v in visitas:
            v_save = v.copy()
            if isinstance(v_save['tempo'], datetime):
                v_save['tempo'] = v_save['tempo'].isoformat()
            visitas_salvar.append(v_save)
            
        visitas_salvar.append(visita_copy)
        
        _escrever_arquivo(visitas_salvar)

def _escrever_arquivo(dados):
    """Função interna para escrever no JSON."""
    try:
        with open(VISITAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def obter_ultimo_email_enviado():
    """Recupera a data do último envio de e-mail."""
    try:
        if os.path.exists(ULTIMO_EMAIL_FILE):
            with open(ULTIMO_EMAIL_FILE, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                if dados and 'timestamp' in dados:
                    return datetime.fromisoformat(dados['timestamp'].replace('Z', '+00:00'))
    except Exception as e:
        print(f"Erro ao carregar último email: {e}")
    return None

def salvar_ultimo_email_enviado(timestamp):
    """Salva a data do envio de e-mail atual."""
    try:
        dados = {'timestamp': timestamp.isoformat()}
        with open(ULTIMO_EMAIL_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados, f)
    except Exception as e:
        print(f"Erro ao salvar último email: {e}")