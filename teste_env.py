from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

print("=" * 50)
print("CONFIGURACAO DE E-MAIL")
print("=" * 50)
print(f"EMAIL_ADDRESS: {'Configurado' if EMAIL_ADDRESS else 'Nao configurado'}")
print(f"EMAIL_PASSWORD: {'Configurado' if EMAIL_PASSWORD else 'Nao configurado'}")
print(f"SMTP_SERVER: {SMTP_SERVER}")
print(f"SMTP_PORT: {SMTP_PORT}")
print("=" * 50)

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    print("\nATENCAO: Variaveis de ambiente nao configuradas!")
    print("\nCrie um arquivo .env com:")
    print("EMAIL_ADDRESS=seuemail@gmail.com")
    print("EMAIL_PASSWORD=sua_senha_de_aplicativo")
else:
    print(f"\nE-mail configurado: {EMAIL_ADDRESS}")

