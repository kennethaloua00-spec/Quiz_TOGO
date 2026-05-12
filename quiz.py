import pandas as pd
import random
import os

# Charger le CSV
df = pd.read_csv("questions_togo.csv")

def lancer_quiz():

    os.system("cls")

    print("======================================")
    print("🇹🇬 CONNAIS-TU LE TOGO ? 🇹🇬")
    print("======================================\n")

    # Afficher catégories
    categories = df["Catégorie"].unique()

    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")

    # Choix catégorie
    try:
        choix = int(input("\nChoisis une catégorie : "))

        if choix < 1 or choix > len(categories):
            print("❌ Choix invalide.")
            return

    except:
        print("❌ Entre un nombre.")
        return

    categorie_choisie = categories[choix - 1]

    # Filtrer les questions
    questions_categorie = df[df["Catégorie"] == categorie_choisie]

    # Mélanger les questions
    questions = questions_categorie.sample(
        n=min(10, len(questions_categorie))
    ).reset_index(drop=True)

    score = 0
    mauvaises_reponses = []

    print(f"\n🎯 Catégorie : {categorie_choisie}")
    print("======================================\n")

    # Boucle quiz
    for i, row in questions.iterrows():

        print(f"❓ Question {i+1}")
        print(row["Question"])

        # Mélanger réponses
        reponses = [
            row["Option 1"],
            row["Option 2"],
            row["Option 3"]
        ]

        random.shuffle(reponses)

        lettres = ["A", "B", "C"]

        choix_reponses = {}

        for lettre, rep in zip(lettres, reponses):
            choix_reponses[lettre] = rep
            print(f"{lettre}. {rep}")

        reponse = input("\nTa réponse (A/B/C) : ").upper()

        # Vérifier si entrée valide
        if reponse not in ["A", "B", "C"]:
            print("❌ Réponse invalide.")
            continue

        # Vérification réponse
        if choix_reponses.get(reponse) == row["Réponse Correcte"]:

            print("✅ Bonne réponse !")
            score += 1

        else:

            print("❌ Mauvaise réponse !")
            print(f"👉 Bonne réponse : {row['Réponse Correcte']}")

            mauvaises_reponses.append({
                "question": row["Question"],
                "bonne_reponse": row["Réponse Correcte"]
            })

        print("\n----------------------------------\n")

    # Fin du quiz
    print("======================================")
    print("🏁 FIN DU QUIZ")
    print("======================================")

    print(f"\n🎯 Score final : {score}/{len(questions)}")

    # Afficher erreurs
    if mauvaises_reponses:

        print("\n📚 QUESTIONS RATÉES :\n")

        for erreur in mauvaises_reponses:

            print(f"❓ {erreur['question']}")
            print(f"✅ {erreur['bonne_reponse']}\n")

    # Message final
    if score == len(questions):
        print("🔥 Tu connais très bien le Togo !")

    elif score >= 7:
        print("👏 Excellent niveau !")

    elif score >= 5:
        print("👍 Pas mal du tout !")

    else:
        print("📚 Continue d'apprendre sur le Togo.")

# Boucle rejouer
while True:

    lancer_quiz()

    replay = input("\n🔁 Veux-tu rejouer ? (oui/non) : ").lower()

    if replay != "oui":
        print("\n👋 Merci d'avoir joué !")
        break