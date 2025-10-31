# 📧 Como Obter Senha de Aplicativo do Gmail

## 🎯 Por que preciso disso?

O Gmail não aceita mais sua senha normal por segurança. Você precisa criar uma **Senha de Aplicativo** de 16 caracteres.

---

## 📝 Passo a Passo Visual

### Passo 1: Acessar Configurações

1. Abra este link: https://myaccount.google.com/apppasswords
2. Se necessário, faça login no Google

### Passo 2: Verificar Verificação em Duas Etapas

Se você vir uma mensagem dizendo que precisa ativar, vá em:
- **Verificação em duas etapas** (ao lado)
- Clique em **Ativar**
- Siga as instruções na tela

### Passo 3: Criar Senha de Aplicativo

Na página "Senhas de aplicativos":

1. Em **Selecione o app**: Escolha **"Email"**
2. Em **Selecione o dispositivo**: Escolha **"Outro"** ou **"Outro (Nome personalizado)"**
3. Digite: `API Notificacao Site`
4. Clique em **Gerar** ou **Criar**

### Passo 4: Copiar a Senha

Uma senha de 16 caracteres aparecerá, tipo:
```
    aaaa bbbb cccc dddd
```

⚠️ **COPIE ESSA SENHA!** Você só verá ela uma vez.

### Passo 5: Usar no arquivo `.env`

No arquivo `.env` do projeto:

```env
EMAIL_ADDRESS=biancaalves.silva17@gmail.com
EMAIL_PASSWORD=aaaa bbbb cccc dddd
```

**IMPORTANTE**: 
- Use a senha de 16 caracteres que você copiou
- NÃO remova os espaços
- NÃO use sua senha normal do Gmail

### Passo 6: Testar

Salve o arquivo `.env` e execute:

```bash
python teste_email.py
```

---

## ✅ Sucesso!

Se você ver:
```
SUCESSO! Email enviado com sucesso!
```

Parabéns! Está funcionando! 🎉

---

## ❌ Problemas?

### "Não disponível" ou "Visite Configuração"

**Solução**: Você precisa ativar a Verificação em duas etapas primeiro.

### "Username and Password not accepted"

**Causas**:
1. Está usando senha normal ao invés de senha de aplicativo
2. Copiou a senha incompleta
3. Removeu os espaços da senha

**Solução**: Crie uma nova senha de aplicativo e copie todos os 16 caracteres com os espaços.

### Não encontro "Senhas de aplicativos"

**Solução**: Você precisa ativar a Verificação em duas etapas primeiro.

---

## 🔗 Links Úteis

- **Criar senha**: https://myaccount.google.com/apppasswords
- **Verificação 2 etapas**: https://myaccount.google.com/security

---

## 💡 Dica

Você pode ter múltiplas senhas de aplicativo. Se esta não funcionar, delete e crie uma nova!

---

**Próximo passo**: Após obter a senha, teste com `python teste_email.py`

