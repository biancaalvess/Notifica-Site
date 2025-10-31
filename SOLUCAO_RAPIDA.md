# 🚨 SOLUÇÃO RÁPIDA - Criar Senha de Aplicativo Gmail

## ⚡ Passo a Passo

### 1️⃣ Acessar Configurações do Gmail

**Clique aqui**: https://myaccount.google.com/apppasswords

Ou:
1. Acesse: https://myaccount.google.com/
2. Vá em **Segurança** (lado esquerdo)
3. Procure por **Senhas de aplicativos** ou **App Passwords**

### 2️⃣ Ativar Verificação em Duas Etapas (Se Necessário)

Se aparecer "Não disponível", você precisa ativar primeiro:

1. Vá em **Verificação em duas etapas**
2. Clique em **Ativar**
3. Siga as instruções

Depois de ativar, volte para Senhas de Aplicativo.

### 3️⃣ Criar Senha de Aplicativo

1. Selecione **App**: Escolha **Email**
2. Selecione **Device**: Escolha **Outro (Nome personalizado)**
3. Digite: `API Notificacao`
4. Clique em **Gerar**

### 4️⃣ Copiar a Senha

Você verá uma senha de **16 caracteres**, tipo:
```
abcd efgh ijkl mnop
```

**COPIE ESSA SENHA!**

### 5️⃣ Colar no arquivo `.env`

No arquivo `.env`:

```env
EMAIL_ADDRESS=biancaalves.silva17@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop
```

**Use a senha de 16 caracteres que você acabou de copiar!**

### 6️⃣ Salvar e Testar

```bash
python teste_email.py
```

---

## ✅ Se Funcionar

Você verá:
```
SUCESSO! Email enviado com sucesso!
```

---

## ❌ Se Ainda Não Funcionar

1. **Verifique se copiou a senha completa** (16 caracteres)
2. **Não remova os espaços** da senha
3. **Certifique-se que verificou duas etapas** está ativa
4. **Tente criar uma nova senha de aplicativo**

---

## 📞 Link Direto

**Clique aqui para criar senha de aplicativo**:
https://myaccount.google.com/apppasswords

---

**Importante**: A senha de aplicativo é diferente da sua senha normal do Gmail!

