from flask import Flask, render_template

app = Flask("jpoop", static_folder="assets/", template_folder="templates/")

@app.get("/")
def home():
    return render_template("index.html")

