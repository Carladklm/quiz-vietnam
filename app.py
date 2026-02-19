import os
from flask import Flask, render_template, request, redirect

# Chemin absolu vers le dossier templates pour éviter TemplateNotFound
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
app = Flask(__name__, template_folder=template_dir)

# 10 questions du quiz
questions = [
    {"id": 1, "question": "Quelle est la capitale du Vietnam ?", "type": "unique",
     "choices": {"A": "Hô Chi Minh-Ville", "B": "Hanoï", "C": "Da Nang", "D": "Huê"}, "answer": ["B"]},

    {"id": 2, "question": "Quelle est la monnaie officielle du Vietnam ?", "type": "unique",
     "choices": {"A": "Dong", "B": "Yen", "C": "Baht", "D": "Ringgit"}, "answer": ["A"]},

    {"id": 3, "question": "Quels pays partagent une frontière avec le Vietnam ?", "type": "multiple",
     "choices": {"A": "Laos", "B": "Cambodge", "C": "Thaïlande", "D": "Chine"}, "answer": ["A","B","D"]},

    {"id": 4, "question": "Quelle baie est classée au patrimoine mondial de l'UNESCO ?", "type": "unique",
     "choices": {"A": "Baie d'Along", "B": "Baie de Bangkok", "C": "Baie de Tokyo", "D": "Baie de Manille"}, "answer": ["A"]},

    {"id": 5, "question": "Quelle guerre a fortement marqué le Vietnam ?", "type": "unique",
     "choices": {"A": "Première Guerre mondiale", "B": "Guerre du Vietnam", "C": "Guerre de Corée", "D": "Guerre froide"}, "answer": ["B"]},

    {"id": 6, "question": "Quels sont des plats traditionnels vietnamiens ?", "type": "multiple",
     "choices": {"A": "Pho", "B": "Banh Mi", "C": "Sushi", "D": "Bun Bo Hue"}, "answer": ["A","B","D"]},

    {"id": 7, "question": "Quel fleuve traverse le sud du Vietnam ?", "type": "unique",
     "choices": {"A": "Mékong", "B": "Nil", "C": "Danube", "D": "Mississippi"}, "answer": ["A"]},

    {"id": 8, "question": "Quelle est la langue officielle ?", "type": "unique",
     "choices": {"A": "Khmer", "B": "Vietnamien", "C": "Thaï", "D": "Chinois"}, "answer": ["B"]},

    {"id": 9, "question": "Quels sont des sites touristiques célèbres ?", "type": "multiple",
     "choices": {"A": "Sapa", "B": "Hoi An", "C": "Singapour", "D": "Nha Trang"}, "answer": ["A","B","D"]},

    {"id": 10, "question": "En quelle année la guerre du Vietnam s'est-elle terminée ?", "type": "unique",
     "choices": {"A": "1975", "B": "1965", "C": "1980", "D": "1954"}, "answer": ["A"]}
]

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    results = []

    for q in questions:
        qid = str(q["id"])
        if q["type"] == "unique":
            user_answer = request.form.get(qid)
            if not user_answer:
                return redirect("/")
            user_answers = [user_answer]
        else:
            user_answers = request.form.getlist(qid)
            if not user_answers:
                return redirect("/")

        correct = sorted(user_answers) == sorted(q["answer"])
        if correct:
            score += 1

        results.append({
            "question": q["question"],
            "user": user_answers,
            "correct": q["answer"],
            "is_correct": correct
        })

    return render_template("results.html", score=score, results=results)

if __name__ == "__main__":
    app.run(debug=True)
