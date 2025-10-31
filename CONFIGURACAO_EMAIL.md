# 📧 Configuração de E-mail

## Problema: E-mails não estão sendo enviados

Se você não está recebendo e-mails de notificação, o problema geralmente é a configuração do Gmail SMTP.

---

## 🔧 Como Configurar

### 1. Criar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com:

```env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=SUA_SENHA_DE_APLICATIVO
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### 2. Configurar Senha de Aplicativo do Gmail

**IMPORTANTE**: O Gmail não permite mais usar sua senha normal. Você precisa criar uma **Senha de Aplicativo**.

#### Passo a passo:

1. **Acesse**: https://myaccount.google.com/security
2. **Ative** a verificação em duas etapas (se ainda não ativou)
3. Vá em **Senhas de aplicativos** ou **App Passwords**
4. Selecione **App**: Email
5. Selecione **Device**: Outro (Nome personalizado)
6. Digite: "API Notificacao"
7. Clique em **Gerar**
8. **Copie a senha de 16 caracteres** gerada

### 3. Usar a Senha de Aplicativo

Cole a senha de 16 caracteres no arquivo `.env`:

```env
EMAIL_ADDRESS=bianca.alvessdasilva@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
```

**Importante**: 
- A senha de aplicativo tem 16 caracteres
- Pode ter espaços (não precisa remover)
- É diferente da sua senha normal

### 4. Testar

Execute o script de teste:

```bash
python teste_email.py
```

Se funcionar, você verá:
```
SUCESSO! Email enviado com sucesso!
```

---

## ⚠️ Problemas Comuns

### Erro: "Username and Password not accepted"

**Causa**: Senha errada ou usando senha normal ao invés de senha de aplicativo

**Solução**: 
- Crie uma senha de aplicativo (veja passo 2 acima)
- Use a senha de 16 caracteres no `.env`

### Erro: "Less secure app access"

**Causa**: Gmail bloqueando aplicativos menos seguros

**Solução**:
- Use **Senha de Aplicativo** (não precisa habilitar "Less secure apps")
- Certifique-se que a verificação em duas etapas está ativa

### Erro: "Could not connect to server"

**Causa**: Problemas de rede ou firewall

**Solução**:
- Verifique sua conexão de internet
- Desative temporariamente o antivírus
- Verifique se o firewall está bloqueando a porta 587

---

## 🔍 Verificar Configuração

Execute o script de verificação:

```bash
python teste_env.py
```

Você deve ver:
```
EMAIL_ADDRESS: Configurado
EMAIL_PASSWORD: Configurado
```

---

## 📝 Exemplo Completo

**Arquivo `.env`**:

```env
EMAIL_ADDRESS=bianca.alvessdasilva@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Nota**: `abcd efgh ijkl mnop` é um exemplo. Use sua senha de aplicativo real!

---

## ✅ Após Configurar

1. Salve o arquivo `.env`
2. Execute: `python teste_email.py`
3. Se receber "SUCESSO!", está funcionando!
4. Reinicie a API: `python app.py`
5. Acesse o site e teste a notificação

---

## 🎯 Próximos Passos

Após configurar o e-mail:

1. ✅ Testar envio de email
2. ✅ Iniciar a API
3. ✅ Testar acessando o site
4. ✅ Receber notificações por email
5. ✅ Configurar para produção

---

**Precisa de ajuda?** Abra uma issue no repositório!

