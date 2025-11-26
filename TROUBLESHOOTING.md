# 🔧 Troubleshooting - API não está funcionando

## ✅ Arquitetura Atualizada para Vercel (Serverless)

A API foi refatorada para funcionar corretamente no ambiente serverless do Vercel:

- **Persistência**: Dados salvos em arquivos JSON (funciona no Vercel)
- **Cron Jobs**: Relatório diário via Vercel Cron (configurado em `vercel.json`)
- **Anti-duplicatas**: Usa persistência em arquivo (funciona com múltiplas instâncias)

### Relatório Diário

O relatório diário agora é enviado via **Cron Job do Vercel** às 17:00 (horário de Brasília).

- Rota: `/enviar-relatorio-diario`
- Configurado em: `vercel.json` → `crons`
- Horário: 20:00 UTC (17:00 Brasília)

## Problemas Comuns e Soluções

### 1. API não responde no Vercel

**Sintomas**: Erro 404 ou timeout ao acessar a API

**Soluções**:
- Verifique se o arquivo `vercel.json` existe e está configurado
- Certifique-se que as rotas estão mapeadas corretamente
- Verifique os logs no painel do Vercel

### 2. E-mails não estão sendo enviados

**Sintomas**: API responde mas não recebe e-mails

**Verificações**:
1. **Variáveis de ambiente no Vercel**:
   - Vá em Settings → Environment Variables
   - Verifique se estão configuradas:
     - `EMAIL_ADDRESS`
     - `EMAIL_PASSWORD`
     - `SMTP_SERVER`
     - `SMTP_PORT`

2. **Verificar logs do Vercel**:
   - Acesse o painel do Vercel
   - Vá em Deployments → [seu deployment] → Logs
   - Procure por mensagens como:
     - `[SUCESSO] NOTIFICACAO ENVIADA`
     - `[ERRO] AUTENTICACAO FALHOU`
     - `DEBUG: Função enviar_notificacao_imediata chamada`

3. **Testar SMTP**:
   ```bash
   python teste_email.py
   ```

### 3. Erro "Module not found"

**Sintomas**: Erro ao fazer deploy no Vercel

**Solução**:
- Verifique se `requirements.txt` está completo
- Certifique-se que todas as dependências estão listadas

### 4. Threads não funcionam no Vercel

**Problema**: O Vercel é serverless e pode ter limitações com threads

**Solução**: 
- O código já está adaptado para funcionar sem threads persistentes
- As threads são criadas apenas para envio de email (daemon threads)
- O schedule pode não funcionar bem no Vercel (funcionalidade serverless)

### 5. Timeout no Vercel

**Sintomas**: Requisições demoram muito ou dão timeout

**Soluções**:
- Aumente o timeout no `vercel.json` (se necessário)
- Verifique se o SMTP não está demorando muito
- Considere usar async/await para operações de rede

### 6. Variáveis de ambiente não estão sendo carregadas

**Sintomas**: API não encontra EMAIL_ADDRESS ou EMAIL_PASSWORD

**Solução**:
1. No Vercel:
   - Settings → Environment Variables
   - Adicione todas as variáveis
   - Certifique-se de fazer redeploy após adicionar

2. Verifique no código:
   ```python
   print(f"Email configurado: {EMAIL_ADDRESS}")
   ```

## Teste Local vs Vercel

### Teste Local
```bash
python app.py
# Acesse: http://localhost:5000/track-visit
```

### Teste Vercel
```bash
# Testar tracking
curl -X POST https://sua-api.vercel.app/track-visit

# Testar health check
curl https://sua-api.vercel.app/health

# Testar relatório diário manualmente
curl https://sua-api.vercel.app/enviar-relatorio-diario
```

## Verificar Logs

### Logs Locais
- Execute `python app.py` e veja o console

### Logs Vercel
1. Acesse: https://vercel.com/dashboard
2. Selecione seu projeto
3. Vá em Deployments
4. Clique no deployment mais recente
5. Veja a aba "Logs"

## Checklist de Debugging

- [ ] API responde com 200 OK?
- [ ] Variáveis de ambiente configuradas no Vercel?
- [ ] Logs mostram "Email configurado: ..."?
- [ ] Logs mostram "DEBUG: Função enviar_notificacao_imediata chamada"?
- [ ] Logs mostram "[SUCESSO]" ou "[ERRO]"?
- [ ] Teste local funciona?
- [ ] `vercel.json` existe e está correto (incluindo cron)?
- [ ] `requirements.txt` está completo (sem schedule)?
- [ ] Rota `/health` retorna status ok?
- [ ] Rota `/enviar-relatorio-diario` funciona manualmente?
- [ ] Cron job está configurado no Vercel?

## Próximos Passos

1. Verifique os logs do Vercel
2. Teste a API localmente
3. Compare o comportamento local vs Vercel
4. Verifique variáveis de ambiente
5. Teste o envio de email isoladamente

## Suporte

Se o problema persistir:
1. Verifique os logs completos do Vercel
2. Teste localmente para isolar o problema
3. Compare configurações entre local e Vercel

