# API de Notificação de Visitas por E-mail

Este projeto é uma API simples desenvolvida com Flask (Python) que detecta acessos e envia notificações por e-mail sobre as visitas.

## O que ela faz?

Agora, ao invés de enviar um e-mail a cada acesso, a API gera um relatório diário, contendo:

-  Quantidade total de acessos do dia  
-  Lista com os **horários das visitas** e quantas vezes ocorreram  

##  Funcionalidades

- Detecta acessos via rotas HTTP (`/` e `/track-visit`)
- Envia e-mails de forma segura via SMTP (Gmail)
- Gera **relatórios diários automáticos às 20h42**
- Mostra os horários exatos das visitas, regiões e User-Agents
- Suporte a Senhas de Aplicativo do Google
- Variáveis de ambiente gerenciadas com `python-dotenv`
- Pode ser integrada facilmente com front-ends usando `fetch`
- Proteção contra bots via verificação de User-Agent

## Tecnologias Utilizadas

- Python 3  
- Flask  
- Flask-CORS  
- python-dotenv  
- smtplib (para envio de e-mail)  
- Gmail SMTP  
- schedule (para agendamento do relatório diário)  
- user-agents (para detecção de bots)  

##  Observações

- O servidor precisa estar rodando para que a API responda às requisições.
- As seguintes variáveis de ambiente devem estar corretamente configuradas:

```env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
````

---

##  ATUALIZAÇÕES

###  Relatório Diário Programado

Graças à sugestão do [**Atevilson Araujo**](https://www.linkedin.com/in/atevilson-araujo/), agora o envio de e-mails acontece **somente uma vez ao dia, agrupando todos os acessos. Isso evita sobrecarga no e-mail e dá uma visão geral do tráfego do portfólio de forma organizada.

###  Proteção contra Bots

Essa funcionalidade foi desenvolvida após o [**Angelo Mendes**](https://www.linkedin.com/in/mangelodev/) me questionar sobre a possibilidade de bloquear acessos automatizados. Graças à visão dele, foi implementada uma verificação simples de User-Agent para impedir bots/crawlers indesejados. Resultado? Segurança reforçada e visitas mais precisas! 


Agradeço a cada um pelo estimulo e contribuição, sintam-se sempre a vontade para participar!
------------------------------------------------

# Email Notification API

This project is a simple API developed with Flask (Python) that detects accesses and sends email notifications about the visits.

## What does it do?

Now, instead of sending an email for each access, the API generates a daily report, containing:

- Total number of accesses for the day
- List with the **visit times** and how many times they occurred

## Features

- Detects accesses via HTTP routes (`/` and `/track-visit`)
- Sends emails securely via SMTP (Gmail)
- Generates **automatic daily reports at 8:42 p.m.**
- Shows the exact times of visits, regions and User-Agents
- Support for Google App Passwords
- Environment variables managed with `python-dotenv`
- Can be easily integrated with front-ends using `fetch`
- Protection against bots via User-Agent verification

## Technologies Used

- Python 3
- Flask
- Flask-CORS
- python-dotenv
- smtplib (for sending emails) e-mail)
- Gmail SMTP
- schedule (to schedule the daily report)
- user-agents (to detect bots)

## Notes

- The server must be running for the API to respond to requests.
- The following environment variables must be correctly configured:

```env
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your_application_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
````

---

## UPDATES

### Scheduled Daily Report

Thanks to the suggestion by [**Atevilson Araujo**](https://www.linkedin.com/in/atevilson-araujo/), now emails are sent **only once a day, grouping all accesses. This prevents email overload and provides an organized overview of portfolio traffic.

### Bot Protection

This feature was developed after [**Angelo Mendes**](https://www.linkedin.com/in/mangelodev/) asked me about the possibility of blocking automated access. Thanks to his insight, a simple User-Agent check was implemented to prevent unwanted bots/crawlers. The result? Enhanced security and more accurate visits!

I thank everyone for their encouragement and contribution, always feel free to participate!
---
