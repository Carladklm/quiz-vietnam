# ===============================
# QUIZ - Connaissances sur le Vietnam
# ===============================

def demander_reponse(question, propositions, bonnes_reponses, type_question):
    while True:
        print("\n" + question)
        for lettre, texte in propositions.items():
            print(f"{lettre}) {texte}")

        reponse = input("Votre réponse : ").strip().upper()

        # Refuser entrée vide
        if not reponse:
            print("Entrée vide interdite.")
            continue

        # Question à choix unique
        if type_question == "unique":
            if len(reponse) != 1:
                print("Une seule lettre attendue.")
                continue
            if reponse not in propositions:
                print("Lettre invalide.")
                continue
            return [reponse]

        # Question à choix multiple
        elif type_question == "multiple":
            reponses = reponse.split(",")

            # Nettoyage des espaces
            reponses = [r.strip() for r in reponses]

            # Vérifier lettres valides
            if any(r not in propositions for r in reponses):
                print("Une ou plusieurs lettres sont invalides.")
                continue

            # Vérifier format correct (pas doublons)
            if len(set(reponses)) != len(reponses):
                print("Doublons interdits.")
                continue

            return sorted(reponses)


def corriger(reponse_utilisateur, bonnes_reponses):
    return sorted(reponse_utilisateur) == sorted(bonnes_reponses)


def main():
    print("====================================")
    print("Bienvenue dans le Quiz sur le Vietnam")
    print("====================================")

    questions = [
        {
            "question": "1) Quelle est la capitale du Vietnam ?",
            "propositions": {
                "A": "Hô Chi Minh-Ville",
                "B": "Hanoï",
                "C": "Da Nang",
                "D": "Huê"
            },
            "reponses": ["B"],
            "type": "unique"
        },
        {
            "question": "2) Quelle est la monnaie officielle du Vietnam ?",
            "propositions": {
                "A": "Dong",
                "B": "Yen",
                "C": "Baht",
                "D": "Ringgit"
            },
            "reponses": ["A"],
            "type": "unique"
        },
        {
            "question": "3) Quels pays partagent une frontière avec le Vietnam ?",
            "propositions": {
                "A": "Laos",
                "B": "Cambodge",
                "C": "Thaïlande",
                "D": "Chine"
            },
            "reponses": ["A", "B", "D"],
            "type": "multiple"
        },
        {
            "question": "4) Quelle baie est classée au patrimoine mondial de l'UNESCO ?",
            "propositions": {
                "A": "Baie d'Along",
                "B": "Baie de Bangkok",
                "C": "Baie de Tokyo",
                "D": "Baie de Manille"
            },
            "reponses": ["A"],
            "type": "unique"
        },
        {
            "question": "5) Quelle guerre a fortement marqué le Vietnam ?",
            "propositions": {
                "A": "Première Guerre mondiale",
                "B": "Guerre du Vietnam",
                "C": "Guerre de Corée",
                "D": "Guerre froide"
            },
            "reponses": ["B"],
            "type": "unique"
        },
        {
            "question": "6) Quels sont des plats traditionnels vietnamiens ?",
            "propositions": {
                "A": "Pho",
                "B": "Banh Mi",
                "C": "Sushi",
                "D": "Bun Bo Hue"
            },
            "reponses": ["A", "B", "D"],
            "type": "multiple"
        },
        {
            "question": "7) Quel fleuve traverse le sud du Vietnam ?",
            "propositions": {
                "A": "Mékong",
                "B": "Nil",
                "C": "Danube",
                "D": "Mississippi"
            },
            "reponses": ["A"],
            "type": "unique"
        },
        {
            "question": "8) Quelle est la langue officielle ?",
            "propositions": {
                "A": "Khmer",
                "B": "Vietnamien",
                "C": "Thaï",
                "D": "Chinois"
            },
            "reponses": ["B"],
            "type": "unique"
        },
        {
            "question": "9) Quels sont des sites touristiques célèbres ?",
            "propositions": {
                "A": "Sapa",
                "B": "Hoi An",
                "C": "Singapour",
                "D": "Nha Trang"
            },
            "reponses": ["A", "B", "D"],
            "type": "multiple"
        },
        {
            "question": "10) En quelle année la guerre du Vietnam s'est-elle terminée ?",
            "propositions": {
                "A": "1975",
                "B": "1965",
                "C": "1980",
                "D": "1954"
            },
            "reponses": ["A"],
            "type": "unique"
        }
    ]

    score = 0
    recap = []

    for q in questions:
        reponse = demander_reponse(
            q["question"],
            q["propositions"],
            q["reponses"],
            q["type"]
        )

        est_correct = corriger(reponse, q["reponses"])

        if est_correct:
            print("✔ Correct")
            score += 1
        else:
            print("✘ Incorrect")

        print("Votre réponse :", ",".join(reponse))
        print("Bonne réponse :", ",".join(q["reponses"]))

        recap.append({
            "question": q["question"],
            "donnee": ",".join(reponse),
            "correcte": ",".join(q["reponses"]),
            "resultat": "Correct" if est_correct else "Incorrect"
        })

    print("\n======================")
    print(f"Score final : {score}/10")

    if score <= 4:
        print("Il faut réviser sérieusement.")
    elif score <= 7:
        print("Pas mal, mais améliorable.")
    else:
        print("Excellent niveau !")

    print("\nRécapitulatif :")
    for r in recap:
        print("\n" + r["question"])
        print("Votre réponse :", r["donnee"])
        print("Bonne réponse :", r["correcte"])
        print("Résultat :", r["resultat"])


if __name__ == "__main__":
    main()
