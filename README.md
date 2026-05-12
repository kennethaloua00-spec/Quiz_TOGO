# 🇹🇬 Quiz TOGO — Connais-tu le Togo ?

Un quiz interactif sur le Togo disponible en **version terminal** et en **version graphique (Tkinter)**, avec plus de **200 questions** réparties en plusieurs catégories.

---

## 📁 Structure du projet

```
Quiz_TOGO/
│
├── questions_togo.csv     # Base de données des questions
├── quiz.py                # Version terminal (console)
├── quiz_tkinter.py        # Version graphique (interface Tkinter)
├── server.py              # Serveur Flask (bot WhatsApp)
├── requirements.txt       # Dépendances Python
└── README.md              # Ce fichier
```

---

## 🗂️ Catégories disponibles

| Catégorie     | Description                              |
|---------------|------------------------------------------|
| 📜 Histoire   | Colonisation, indépendance, présidents   |
| 🌍 Géographie | Villes, fleuves, régions, frontières     |
| 🏆 Sport      | Football, Jeux Olympiques, athlètes      |
| 🏛️ Institutions | Constitution, gouvernement, drapeau   |

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/TON_USERNAME/Quiz_TOGO.git
cd Quiz_TOGO
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer le quiz

### Version terminal (console)

```bash
python quiz.py
```

### Version graphique (Tkinter)

```bash
python quiz_tkinter.py
```

> **Note :** Tkinter est inclus par défaut avec Python. Si ce n'est pas le cas :
> ```bash
> sudo apt install python3-tk  # Linux
> ```

### Serveur Flask (bot WhatsApp)

```bash
python server.py
```

---

## 📊 Format du fichier CSV

Le fichier `questions_togo.csv` suit ce format :

| Catégorie | Question | Option 1 | Option 2 | Option 3 | Réponse Correcte |
|-----------|----------|----------|----------|----------|------------------|
| Histoire  | Qui fut le premier président du Togo ? | Sylvanus Olympio | Gnassingbé Eyadéma | Faure Gnassingbé | Sylvanus Olympio |

---

## 🛠️ Technologies utilisées

- **Python 3**
- **Pandas** — lecture du fichier CSV
- **Tkinter** — interface graphique
- **Flask** — serveur web léger

---

## 📄 Licence

Ce projet est open-source sous licence [MIT](LICENSE).

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour ajouter des questions :

1. Fork le dépôt
2. Modifie `questions_togo.csv` en respectant le format
3. Crée une Pull Request

---

> Fait avec ❤️ pour valoriser la culture et l'histoire du Togo 🇹🇬
