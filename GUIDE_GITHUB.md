# 📤 Guide — Mettre Quiz_TOGO sur GitHub

## ÉTAPE 1 — Créer le dépôt sur GitHub

1. Va sur https://github.com
2. Connecte-toi à ton compte
3. Clique sur le bouton vert **"New"** (ou l'icône +)
4. Remplis le formulaire :
   - **Repository name** : `Quiz_TOGO`
   - **Description** : `🇹🇬 Quiz interactif sur le Togo — terminal & interface graphique`
   - **Visibilité** : ✅ Public (ou Private si tu veux)
   - ❌ NE PAS cocher "Add a README file" (on en a déjà un)
5. Clique sur **"Create repository"**

---

## ÉTAPE 2 — Initialiser Git en local

Ouvre un terminal dans le dossier `Quiz_TOGO` et exécute :

```bash
cd Quiz_TOGO

git init
git add .
git commit -m "🎉 Premier commit — Quiz TOGO"
```

---

## ÉTAPE 3 — Lier au dépôt GitHub

Remplace `TON_USERNAME` par ton nom d'utilisateur GitHub :

```bash
git remote add origin https://github.com/TON_USERNAME/Quiz_TOGO.git
git branch -M main
git push -u origin main
```

GitHub va te demander tes identifiants si c'est la première fois.

---

## ÉTAPE 4 — Vérifier

Retourne sur GitHub → ton dépôt `Quiz_TOGO`.
Tu devrais voir tous tes fichiers en ligne ✅

---

## ✏️ Pour les prochaines modifications

Après chaque modification de tes fichiers :

```bash
git add .
git commit -m "Description de ce que tu as changé"
git push
```

---

## 💡 Astuce — Token GitHub (si mot de passe refusé)

Depuis 2021, GitHub n'accepte plus les mots de passe pour les push.
Il faut utiliser un **Personal Access Token** :

1. Va sur https://github.com/settings/tokens
2. Clique **"Generate new token (classic)"**
3. Coche les permissions : `repo`
4. Copie le token généré
5. Utilise ce token à la place du mot de passe lors du `git push`

---

> Après le premier `git push -u origin main`, les suivants se font simplement avec `git push`.
