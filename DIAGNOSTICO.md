# 🔍 Diagnóstico: Por que os e-mails não estão sendo enviados

## Problema Identificado

Você não está recebendo e-mails de notificação porque as credenciais de e-mail não estão configuradas corretamente.

---

## ✅ Solução Passo a Passo

### Passo 1: Criar arquivo `.env`

No diretório raiz do projeto, crie um arquivo chamado `.env` com:

```env
EMAIL_ADDRESS=bianca.alvessdasilva@gmail.com
EMAIL_PASSWORD=SUA_SENHA_DE_APLICATIVO_AQUI
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Passo 2: Obter Senha de Aplicativo do Gmail

**IMPORTANTE**: Você precisa criar uma Senha de Aplicativo (não usar sua senha normal).

1. Acesse: https://myaccount.google.com/apppasswords
2. Se necessário, ative a Verificação em duas etapas primeiro
3. Crie uma nova senha:
   - **App**: Email
   - **Device**: Outro (nome: "API Notificação")
4. Copie a senha de 16 caracteres gerada
5. Cole no arquivo `.env`

Exemplo de senha de aplicativo: `abcd efgh ijkl mnop`

### Passo 3: Testar Configuração

Execute o script de teste:

```bash
python teste_email.py
```

Você deve ver:
```
SUCESSO! Email enviado com sucesso!
```

### Passo 4: Testar API

1. Inicie a API:
```bash
python app.py
```

2. Em outro terminal, teste a API:
```bash
curl -X POST http://localhost:5000/track-visit
```

3. Verifique se recebeu o e-mail!

---

## 📋 Checklist

- [ ] Arquivo `.env` criado
- [ ] Senha de Aplicativo do Gmail criada
- [ ] Credenciais adicionadas no `.env`
- [ ] Teste de email executado com sucesso
- [ ] API iniciada
- [ ] Notificação enviada e recebida

---

## ⚠️ Erros Comuns

### Erro: "Username and Password not accepted"

**Causa**: Está usando senha normal ao invés de senha de aplicativo

**Solução**: Crie uma Senha de Aplicativo no Gmail

### Erro: "Configuração de e-mail não encontrada"

**Causa**: Arquivo `.env` não existe ou não está na raiz do projeto

**Solução**: Verifique se o arquivo `.env` existe e está no lugar correto

### Erro: "EMAIL_ADDRESS: Configurado" mas não envia

**Causa**: Credenciais estão erradas ou são placeholders

**Solução**: Use as credenciais reais do Gmail

---

## 🎯 Próximos Passos Após Configurar

1. ✅ Configurar `.env` com senha de aplicativo
2. ✅ Testar envio de email
3. ✅ Iniciar API em produção
4. ✅ Integrar no site https://devbianca.tech
5. ✅ Receber notificações em tempo real!

---

## 📚 Mais Informações

- **Guia completo**: Veja `CONFIGURACAO_EMAIL.md`
- **Exemplos de integração**: Veja `EXEMPLO_INTEGRACAO.md`
- **Testar API**: Use `teste-integracao.html`

---

**Precisa de ajuda?** Execute `python teste_env.py` para verificar sua configuração!

