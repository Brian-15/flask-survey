import surveys
from flask import Flask, request, render_template, redirect, flash
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret123"

responses = []

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/question/<int:num>", methods = ["GET"])
def question(num):

    if num != len(responses):
        flash("Error: Invalid Question")
        return redirect(f"/question/{len(responses)}")

    if num == len(surveys.satisfaction_survey.questions) - 1:
        return redirect("/thankyou")    
    
    q = surveys.satisfaction_survey.questions[num]

    return render_template("question.html",
        q=q,
        num=num
    )

@app.route("/answer/<int:num>", methods = ["POST"])
def answer(num):

    # choices = surveys.satisfaction_survey.questions[num].choices

    # for choice in choices:
    #     if request.args.get(choice) == "on":
    #         responses.append(choice)

    responses.append(list(request.form)[0])

    return redirect(f"/question/{num+1}")

@app.route("/thankyou")
def thank_you():
    return render_template("thank_you.html", responses=responses)