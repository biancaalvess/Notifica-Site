# 🚀 Deploy no Render.com

## Passo a Passo

### 1️⃣ Criar Conta e Novo Serviço

1. Acesse: https://render.com
2. Faça login com GitHub
3. Clique em **"New +"** → **"Web Service"**

### 2️⃣ Conectar Repositório

1. Selecione o repositório **Notifica-Site**
2. Clique em **"Connect"**

### 3️⃣ Configurar o Serviço

**Configurações básicas**:
- **Name**: `notifica-site-api` (ou outro nome)
- **Environment**: `Python 3`
- **Branch**: `main`

**Configurações de Build**:
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
```

### 4️⃣ Configurar Variáveis de Ambiente

Na seção **"Environment"**, adicione:

```
EMAIL_ADDRESS = bianca.alvessdasilva@gmail.com
EMAIL_PASSWORD = sua_senha_de_aplicativo_aqui
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
```

⚠️ **IMPORTANTE**: Use Senha de Aplicativo do Gmail, não sua senha normal!

### 5️⃣ Deploy

1. Clique em **"Create Web Service"**
2. Aguarde o build e deploy
3. Copie a URL gerada (ex: `https://notifica-site-api.onrender.com`)

### 6️⃣ Testar

```bash
curl -X POST https://SUA-URL.onrender.com/track-visit
```

Ou acesse no navegador:
```
https://SUA-URL.onrender.com/
```

---

## 📊 Verificar Logs

1. No painel do Render, vá em **"Logs"**
2. Você verá logs como:
   - `Email configurado: bianca.alvessdasilva@gmail.com`
   - `DEBUG: Função enviar_notificacao_imediata chamada`
   - `✅ NOTIFICACAO ENVIADA COM SUCESSO`

---

## ⚠️ Problemas Comuns

### "Application failed to respond"

**Causa**: Start command errado

**Solução**: Use:
```
gunicorn app:app --bind 0.0.0.0:$PORT
```

### "No module named 'gunicorn'"

**Causa**: Gunicorn não está no requirements.txt

**Solução**: Adicione ao `requirements.txt`:
```
gunicorn==21.2.0
```

### Email não envia

**Causas possíveis**:
1. Senha de aplicativo errada
2. Variáveis de ambiente não configuradas
3. Firewall bloqueando conexão SMTP

**Solução**: Verifique os logs para ver a mensagem de erro específica

---

## 🔍 Verificar Status

Depois do deploy, verifique:

1. ✅ Serviço está "Live" (verde)
2. ✅ URL responde com 200 OK
3. ✅ Logs mostram "Email configurado"
4. ✅ Logs mostram "NOTIFICACAO ENVIADA" quando testar

---

## 📝 Atualizar o Site

Depois que a API estiver no ar, atualize a URL no seu site:

```javascript
const API_URL = 'https://SUA-URL.onrender.com/track-visit';
```

---

## 🎯 Próximos Passos

1. ✅ Fazer deploy no Render
2. ✅ Testar a API
3. ✅ Verificar logs
4. ✅ Atualizar URL no site
5. ✅ Receber notificações! 🎉

