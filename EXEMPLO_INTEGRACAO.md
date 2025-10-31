# Exemplo de Integração da API de Notificações no Site

## Como integrar no site https://devbianca.tech/

Para que o site envie notificações para a API, você precisa adicionar um código JavaScript que chame a API quando alguém acessar o site.

### Opção 1: Código JavaScript Simples (Recomendado)

Adicione este código no seu site, preferencialmente no final do arquivo HTML (antes de `</body>`):

```javascript
<script>
// Função para registrar visita na API
async function registrarVisita() {
    try {
        // Substitua pela URL da sua API em produção
        const API_URL = 'http://localhost:5000/track-visit'; // ou sua URL em produção
        
        // Faz a requisição para a API
        const response = await fetch(API_URL, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        // Verifica se a requisição foi bem-sucedida
        if (response.ok) {
            console.log('Visita registrada com sucesso!');
        } else {
            console.log('Erro ao registrar visita:', response.status);
        }
    } catch (error) {
        // Silenciosamente ignora erros para não impactar a experiência do usuário
        console.log('Erro ao conectar com API:', error);
    }
}

// Registra a visita quando a página carrega
window.addEventListener('load', registrarVisita);
</script>
```

### Opção 2: Usando o view counter do seu site

Se o seu site já tem um contador de visualizações (como mostrado no HTML "Loading views..."), você pode integrar a chamada na mesma função:

```javascript
<script>
async function carregarVisualizacoes() {
    // Sua função existente de views
    // ...
    
    // Adicionar o registro de visita
    try {
        const response = await fetch('http://localhost:5000/track-visit', {
            method: 'POST',
            mode: 'cors'
        });
        if (response.ok) {
            console.log('Notificação enviada!');
        }
    } catch (error) {
        console.log('Erro na notificação:', error);
    }
}

// Chama quando a página carrega
window.addEventListener('load', carregarVisualizacoes);
</script>
```

### Opção 3: Integração React/Next.js

Se o seu site usa React ou Next.js:

```javascript
import { useEffect } from 'react';

function NotificationTracker() {
    useEffect(() => {
        // Registra visita quando o componente monta
        async function registrarVisita() {
            try {
                await fetch('http://localhost:5000/track-visit', {
                    method: 'POST',
                    mode: 'cors'
                });
            } catch (error) {
                console.log('Erro ao registrar visita:', error);
            }
        }
        
        registrarVisita();
    }, []); // Executa apenas uma vez quando monta
    
    return null; // Componente invisível
}

export default NotificationTracker;
```

## Configuração de Produção

### 1. Configurar a URL da API

Quando for para produção, você precisa:

1. **Hospedar a API Flask** em um servidor (ex: Railway, Render, Heroku, Vercel)
2. **Atualizar a URL** no código JavaScript:

```javascript
const API_URL = 'https://sua-api.herokuapp.com/track-visit';
// ou
const API_URL = 'https://api-devbianca.railway.app/track-visit';
```

### 2. Configurar CORS na API

A API já está configurada com CORS, mas se tiver problemas, você pode adicionar origins específicos no `app.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/track-visit": {
        "origins": ["https://devbianca.tech", "http://localhost:3000"]
    }
})
```

### 3. Configurar Variáveis de Ambiente

Certifique-se de que o arquivo `.env` está configurado na API em produção:

```env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## Testando a Integração

1. Inicie a API localmente:
```bash
python app.py
```

2. Abra o site no navegador com o código JavaScript integrado

3. Verifique se recebeu o e-mail de notificação

4. Verifique o console do navegador para logs

## Benefícios

- ✅ **Notificação imediata**: Saiba instantaneamente quando alguém visita seu portfólio
- ✅ **Relatório diário**: Receba um resumo às 17h00
- ✅ **Sem impacto na performance**: Executa de forma assíncrona
- ✅ **Privacidade**: Não coleta dados pessoais, apenas IP e User-Agent

## Próximos Passos

1. Integre o código JavaScript no seu site
2. Teste localmente
3. Faça deploy da API em um servidor
4. Atualize a URL da API no site para produção
5. Teste em produção

