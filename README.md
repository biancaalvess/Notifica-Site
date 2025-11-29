````markdown
# API de Notificação de Visitas

Este projeto é uma API simples desenvolvida com Flask (Python) que detecta acessos em sites, armazena um histórico persistente de visitas e envia notificações por e-mail.

## O que ela faz?

1.  **Notificação Imediata**: Envia um e-mail instantâneo a cada nova visita recebida no teu site.
2.  **Relatório Diário**: Envia um resumo automático às 17h00 com:
    * Total de visitas do dia.
    * **Total Geral Acumulado** (histórico completo desde o início).
    * Horários detalhados dos acessos.
3.  **Persistência de Dados**: Mantém o histórico de visitas salvo em arquivo JSON, garantindo que a contagem não zere diariamente.
4.  **Anti-AdBlock**: Utiliza rotas neutras (`/api/ping`) para evitar bloqueio por extensões de privacidade e navegadores como Brave.

## 🔗 Endpoints

* **GET /**: Rota de boas-vindas.
* **POST /api/ping**: Rota para registrar uma visita (Substitui a antiga `/track-visit` para evitar bloqueios de AdBlock).
* **GET /health**: Verifica o status da API e exibe o total de visitas registradas.
* **GET /enviar-relatorio-diario**: Rota acionada pelo Cron Job para enviar o resumo do dia.

## 💻 Como integrar no Frontend

Para registrar uma visita no teu site (React, Next.js, HTML puro, etc.), faz uma requisição `POST` para a rota `/api/ping`:

```javascript
// Exemplo de integração
fetch('[https://sua-api.vercel.app/api/ping](https://sua-api.vercel.app/api/ping)', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    // Opcional: enviar dados extras no corpo se necessário
    body: JSON.stringify({}) 
})
.then(response => {
    if (response.ok) console.log("Visita registrada!");
})
.catch(err => console.error("Erro ao registrar visita", err));
````

## 🛠 Tecnologias Utilizadas

  * **Python 3 & Flask**: Backend serverless leve.
  * **JSON Database**: Sistema de persistência de dados em arquivo (`database.py`).
  * **SMTP (Gmail)**: Para envio seguro de notificações.
  * **Vercel Cron**: Para agendamento automático do relatório diário.
  * **User-Agents**: Biblioteca para detecção e bloqueio de bots.

## ⚙️ Configuração Local

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
    cd seu-repo
    ```

2.  Crie um ambiente virtual e instale as dependências:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  Configure as variáveis de ambiente:
    Crie um arquivo `.env` na raiz (baseado no `.env.example`) e adicione:

    ```env
    EMAIL_ADDRESS=seuemail@gmail.com
    EMAIL_PASSWORD=sua_senha_de_aplicativo
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    ```

4.  Execute o servidor:

    ```bash
    python app.py
    ```

## 🚀 Deploy no Vercel

Esta API está pronta para rodar no Vercel. Após fazer o deploy, configure as variáveis de ambiente no painel do projeto (Settings → Environment Variables):

  * `EMAIL_ADDRESS`
  * `EMAIL_PASSWORD` (Use uma Senha de Aplicativo do Google, não a sua senha pessoal)
  * `SMTP_SERVER`
  * `SMTP_PORT`

-----

## 🔄 Histórico de Atualizações Recentes

### ✅ Anti-AdBlock (Mudança de Rota)

A rota principal foi alterada de `/track-visit` para `/api/ping`.

  * **Motivo:** Bloqueadores de anúncios (uBlock Origin, AdBlock) e navegadores focados em privacidade bloqueiam automaticamente URLs contendo a palavra "track".
  * **Solução:** O uso de um nome neutro (`ping`) garante que a requisição chegue ao servidor e a visita seja contabilizada.

### 💾 Persistência de Dados

Implementado novo módulo `database.py`.

  * **Antes:** O sistema limpava as visitas após enviar o relatório diário.
  * **Agora:** O histórico é mantido integralmente. O relatório diário informa quantas visitas ocorreram "Hoje" e qual é o "Total Acumulado" desde o início do projeto.

### 🔒 Anti-duplicatas Inteligente

Sistema que previne spam no seu e-mail.

  * Se o mesmo visitante (ou múltiplos visitantes) acionarem a API várias vezes em menos de 30 segundos, apenas **um** e-mail de notificação imediata será enviado, mas todas as visitas serão contabilizadas no banco de dados.


```
```

````markdown

# Visit Notification API

This project is a simple API developed with Flask (Python) that detects website visits, stores a persistent visit history, and sends email notifications.

## What does it do?

1. **Immediate Notification**: Sends an instant email for each new visit received on your website.

2. **Daily Report**: Sends an automatic summary at 5 PM with:

* Total visits for the day.

* **Grand Total Accumulated** (complete history from the beginning).

* Detailed access times.

3. **Data Persistence**: Keeps the visit history saved in a JSON file, ensuring that the count does not reset daily.

4. **Anti-AdBlock**: Uses neutral routes (`/api/ping`) to avoid blocking by privacy extensions and browsers like Brave.

## 🔗 Endpoints

* **GET /**: Welcome route.

* **POST /api/ping**: Route to register a visit (Replaces the old `/track-visit` to avoid AdBlock blocks).

* **GET /health**: Checks the API status and displays the total number of registered visits.

* **GET /send-daily-report**: Route triggered by the Cron Job to send the daily summary.

## 💻 How to integrate in the Frontend

To register a visit to your website (React, Next.js, pure HTML, etc.), make a `POST` request to the `/api/ping` route:

```javascript
// Integration example
fetch('[https://your-api.vercel.app/api/ping](https://your-api.vercel.app/api/ping)', {

method: 'POST',

headers: {

'Content-Type': 'application/json'

},

/ Optional: send extra data in the body if necessary

body: JSON.stringify({})
})
.then(response => {

if (response.ok) console.log("Visit registered!");

})
.catch(err => console.error("Error registering visit", err));
````

## 🛠 Technologies Used

* **Python 3 & Flask**: Lightweight serverless backend.

* **JSON Database**: Data persistence system in a file (`database.py`).

* **SMTP (Gmail)**: For secure notification delivery.

* **Vercel Cron**: For automatic scheduling of the daily report.

* **User-Agents**: Library for detecting and blocking bots.

## ⚙️ Local Configuration

1. Clone the repository:

``bash
git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)

cd your-repo

``

2. Create a virtual environment and install the dependencies:

``bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt

``

3. Configure the environment variables:

Create a `.env` file in the root directory (based on `.env.example`) and add:

``env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_application_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587


4. Run the server:

``bash
python app.py

``

## 🚀 Deploy on Vercel

This API is ready to run on Vercel. After deploying, configure the environment variables in the project panel (Settings → Environment Variables):

* `EMAIL_ADDRESS`

* `EMAIL_PASSWORD` (Use a Google App Password, not your personal password)

* `SMTP_SERVER`

* `SMTP_PORT`

-----

## 🔄 Recent Update History

### ✅ Anti-AdBlock (Route Change)

The main route has been changed from `/track-visit` to `/api/ping`.

* **Reason:** Ad blockers (uBlock Origin, AdBlock) and privacy-focused browsers automatically block URLs containing the word "track".

* **Solution:** Using a neutral name (`ping`) ensures that the request reaches the server and the visit is counted.

### 💾 Data Persistence

New module `database.py` implemented.

* **Before:** The system cleared visits after sending the daily report.

* **Now:** The history is fully maintained. The daily report informs how many visits occurred "Today" and what the "Total Accumulated" is since the beginning of the project.

### 🔒 Intelligent Anti-Duplicate

System that prevents spam in your email.

* If the same visitor (or multiple visitors) trigger the API several times in less than 30 seconds, only **one** immediate notification email will be sent, but all visits will be counted in the database.

``
```