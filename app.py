from flask import Flask, render_template, request
import re

app = Flask(__name__)


def check_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Decide strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


@app.route("/", methods=["GET", "POST"])
def home():

    strength = ""
    suggestions = []

    if request.method == "POST":

        password = request.form["password"]

        strength, suggestions = check_password(password)

    return render_template(
        "index.html",
        strength=strength,
        suggestions=suggestions
    )


if __name__ == "__main__":
    app.run(debug=True)