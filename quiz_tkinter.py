# quiz_tkinter.py


import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Charger les données
try:
    df = pd.read_csv("questions_togo.csv")
except:
    messagebox.showerror(
        "Erreur",
        "Le fichier questions_togo.csv est introuvable."
    )
    exit()

# Variables globales
questions = []
question_index = 0
score = 0
bonne_reponse = ""
mauvaises_reponses = []

# Fenêtre principale
root = tk.Tk()
root.title("🇹🇬 Connais-tu le Togo ?")
root.geometry("900x650")
root.configure(bg="#0b3d0b")

# ------------------------------
# TITRE
# ------------------------------

titre = tk.Label(
    root,
    text="🇹🇬 CONNAIS-TU LE TOGO ? 🇹🇬",
    font=("Arial", 24, "bold"),
    bg="#0b3d0b",
    fg="white"
)

titre.pack(pady=20)

# ------------------------------
# SCORE
# ------------------------------

score_label = tk.Label(
    root,
    text="Score : 0",
    font=("Arial", 16, "bold"),
    bg="#0b3d0b",
    fg="#ffd700"
)

score_label.pack()

# ------------------------------
# CHOIX CATÉGORIE
# ------------------------------

categorie_label = tk.Label(
    root,
    text="Choisis une catégorie",
    font=("Arial", 18),
    bg="#0b3d0b",
    fg="white"
)

categorie_label.pack(pady=10)

categories = list(df["Catégorie"].unique())

categorie_var = tk.StringVar()
categorie_var.set(categories[0])

menu_categories = tk.OptionMenu(root, categorie_var, *categories)
menu_categories.config(font=("Arial", 14))
menu_categories.pack(pady=10)

# ------------------------------
# QUESTION
# ------------------------------

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    wraplength=750,
    justify="center",
    bg="#0b3d0b",
    fg="white"
)

question_label.pack(pady=30)

# ------------------------------
# BOUTONS RÉPONSES
# ------------------------------

frame_boutons = tk.Frame(root, bg="#0b3d0b")
frame_boutons.pack(pady=20)

bouton_a = tk.Button(
    frame_boutons,
    text="",
    width=35,
    height=2,
    font=("Arial", 14),
    bg="#ffffff",
)

bouton_a.grid(row=0, column=0, padx=10, pady=10)

bouton_b = tk.Button(
    frame_boutons,
    text="",
    width=35,
    height=2,
    font=("Arial", 14),
    bg="#ffffff",
)

bouton_b.grid(row=1, column=0, padx=10, pady=10)

bouton_c = tk.Button(
    frame_boutons,
    text="",
    width=35,
    height=2,
    font=("Arial", 14),
    bg="#ffffff",
)

bouton_c.grid(row=2, column=0, padx=10, pady=10)

# ------------------------------
# FONCTIONS
# ------------------------------

def charger_questions():

    global questions
    global question_index
    global score
    global mauvaises_reponses

    categorie = categorie_var.get()

    questions_filtrees = df[df["Catégorie"] == categorie]

    questions = questions_filtrees.sample(
        n=min(10, len(questions_filtrees))
    ).reset_index(drop=True)

    question_index = 0
    score = 0
    mauvaises_reponses = []

    score_label.config(text=f"Score : {score}")

    afficher_question()


def afficher_question():

    global question_index
    global bonne_reponse

    if question_index >= len(questions):
        fin_quiz()
        return

    question = questions.iloc[question_index]

    question_label.config(
        text=f"Question {question_index + 1}\n\n{question['Question']}"
    )

    bonne_reponse = question["Réponse Correcte"]

    reponses = [
        question["Option 1"],
        question["Option 2"],
        question["Option 3"]
    ]

    random.shuffle(reponses)

    bouton_a.config(
        text=f"A. {reponses[0]}",
        command=lambda: verifier_reponse(reponses[0])
    )

    bouton_b.config(
        text=f"B. {reponses[1]}",
        command=lambda: verifier_reponse(reponses[1])
    )

    bouton_c.config(
        text=f"C. {reponses[2]}",
        command=lambda: verifier_reponse(reponses[2])
    )


def verifier_reponse(reponse_choisie):

    global score
    global question_index

    question_actuelle = questions.iloc[question_index]

    if reponse_choisie == bonne_reponse:

        score += 1

        messagebox.showinfo(
            "Bonne réponse",
            "✅ Bonne réponse !"
        )

    else:

        mauvaises_reponses.append({
            "question": question_actuelle["Question"],
            "bonne_reponse": bonne_reponse
        })

        messagebox.showerror(
            "Mauvaise réponse",
            f"❌ Mauvaise réponse !\n\nBonne réponse : {bonne_reponse}"
        )

    score_label.config(text=f"Score : {score}")

    question_index += 1

    afficher_question()


def fin_quiz():

    message = (
        f"🏁 FIN DU QUIZ\n\n"
        f"🎯 Score final : {score}/{len(questions)}\n\n"
    )

    if mauvaises_reponses:

        message += "📚 Questions ratées :\n\n"

        for erreur in mauvaises_reponses:
            message += (
                f"❓ {erreur['question']}\n"
                f"✅ {erreur['bonne_reponse']}\n\n"
            )

    if score == len(questions):
        message += "🔥 Incroyable !"

    elif score >= 7:
        message += "👏 Excellent niveau !"

    elif score >= 5:
        message += "👍 Pas mal du tout !"

    else:
        message += "📚 Continue d'apprendre sur le Togo !"

    replay = messagebox.askyesno(
        "Quiz terminé",
        message + "\n\n🔁 Rejouer ?"
    )

    if replay:
        charger_questions()
    else:
        root.destroy()

# ------------------------------
# BOUTON COMMENCER
# ------------------------------

bouton_commencer = tk.Button(
    root,
    text="🚀 COMMENCER LE QUIZ",
    font=("Arial", 16, "bold"),
    bg="#ffd700",
    fg="black",
    width=25,
    height=2,
    command=charger_questions
)

bouton_commencer.pack(pady=20)

# ------------------------------
# LANCEMENT
# ------------------------------

root.mainloop()
