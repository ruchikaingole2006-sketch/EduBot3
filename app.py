from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CHATBOT ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    # Greeting
    if "hello" in user_message or "hi" in user_message:
        reply = (
            "Hello! 👋 I am EduBot, your AI Study Assistant. "
            "How can I help you today?"
        )

    # Artificial Intelligence
    elif "ai" in user_message or "artificial intelligence" in user_message:
        reply = (
            "🤖 Artificial Intelligence (AI) is a technology that enables "
            "computers to perform tasks that normally require human intelligence, "
            "such as learning, reasoning, and problem-solving."
        )

    # Python
    elif "python" in user_message:
        reply = (
            "🐍 Python is a popular programming language. It is widely used "
            "in Artificial Intelligence, Machine Learning, Data Science, "
            "Web Development, and Automation."
        )

    # Computer Science
    elif "computer science" in user_message:
        reply = (
            "💻 Computer Science is the study of computers, programming, "
            "algorithms, software, hardware, and information processing."
        )

    # Data Science
    elif "data science" in user_message:
        reply = (
            "📊 Data Science is the process of collecting, analyzing, "
            "and interpreting data to find useful information and make decisions."
        )

    # Study Tips
    elif "study" in user_message or "study tips" in user_message:
        reply = (
            "📚 Study Tips:\n\n"
            "1. Make a daily study schedule.\n"
            "2. Study in short focused sessions.\n"
            "3. Take regular breaks.\n"
            "4. Practice questions regularly.\n"
            "5. Revise important topics before exams."
        )

    # Quiz
    elif "quiz" in user_message:
        reply = (
            "📝 Quick Quiz!\n\n"
            "Question: What does AI stand for?\n\n"
            "A) Automated Internet\n"
            "B) Artificial Intelligence\n"
            "C) Advanced Information\n\n"
            "Correct Answer: B) Artificial Intelligence ✅"
        )

    # Thank you
    elif "thank" in user_message:
        reply = "You're welcome! 😊 Keep learning and keep improving!"

    # Default
    else:
        reply = (
            "🤔 I'm still learning. Try asking me about:\n\n"
            "• Artificial Intelligence\n"
            "• Python\n"
            "• Computer Science\n"
            "• Data Science\n"
            "• Study Tips\n"
            "• Quiz"
        )

    return jsonify({"reply": reply})


# ---------------- QUIZ API ----------------
@app.route("/quiz", methods=["GET"])
def quiz():
    questions = [
        {
            "question": "What does AI stand for?",
            "options": [
                "A) Automated Internet",
                "B) Artificial Intelligence",
                "C) Advanced Information",
                "D) Automatic Intelligence"
            ],
            "answer": "B"
        },
        {
            "question": "Which language is commonly used in AI and Data Science?",
            "options": [
                "A) Python",
                "B) HTML",
                "C) CSS",
                "D) XML"
            ],
            "answer": "A"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "A) Central Processing Unit",
                "B) Computer Personal Unit",
                "C) Central Program Utility",
                "D) Control Processing User"
            ],
            "answer": "A"
        },
        {
            "question": "Which of these is a database management system?",
            "options": [
                "A) MySQL",
                "B) Python",
                "C) HTML",
                "D) CSS"
            ],
            "answer": "A"
        },
        {
            "question": "What is used to style a web page?",
            "options": [
                "A) Python",
                "B) CSS",
                "C) SQL",
                "D) Java"
            ],
            "answer": "B"
        }
    ]

    return jsonify(questions)


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    app.run(debug=True)