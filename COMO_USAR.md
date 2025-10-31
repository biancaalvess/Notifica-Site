# 🚀 Como Usar a API de Notificações

## ⚡ Início Rápido

### 1️⃣ Configurar E-mail (OBRIGATÓRIO)

```bash
# Criar arquivo .env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=SUA_SENHA_DE_APLICATIVO

# IMPORTANTE: Use Senha de Aplicativo do Gmail!
# https://myaccount.google.com/apppasswords
```

### 2️⃣ Testar Configuração

```bash
python teste_email.py
```

Se funcionar: `SUCESSO! Email enviado com sucesso!`

### 3️⃣ Iniciar API

```bash
python app.py
```

API estará rodando em: `http://localhost:5000`

### 4️⃣ Testar

```bash
curl -X POST http://localhost:5000/track-visit
```

Ou abra: `teste-integracao.html` no navegador

---

## 📧 Configuração de E-mail Detalhada

**Leia**: `CONFIGURACAO_EMAIL.md` para instruções completas.

### Resumo:
1. Ative verificação em duas etapas no Gmail
2. Crie uma Senha de Aplicativo
3. Use a senha de 16 caracteres no `.env`

---

## 🌐 Integrar no Site

### JavaScript Simples

```javascript
fetch('http://localhost:5000/track-visit', {
    method: 'POST',
    mode: 'cors'
});
```

**Leia**: `EXEMPLO_INTEGRACAO.md` para mais detalhes.

---

## 🐛 Problemas?

### E-mails não estão sendo enviados?

1. Execute: `python teste_env.py` - Verificar configuração
2. Execute: `python teste_email.py` - Testar envio
3. Leia: `DIAGNOSTICO.md` - Solução de problemas

---

## 📚 Arquivos de Ajuda

- `CONFIGURACAO_EMAIL.md` - Como configurar Gmail
- `DIAGNOSTICO.md` - Soluções para problemas
- `EXEMPLO_INTEGRACAO.md` - Exemplos de código
- `teste-integracao.html` - Página de teste

---

## ✅ Checklist

- [ ] Arquivo `.env` criado com credenciais
- [ ] Senha de Aplicativo do Gmail configurada
- [ ] Teste de email funcionando
- [ ] API rodando
- [ ] Notificações sendo enviadas
- [ ] Site integrado (opcional)

---

**Pronto para começar!** 🎉

