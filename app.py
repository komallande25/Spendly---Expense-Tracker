from flask import Flask, render_template

app = Flask(__name__)


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
if __name__ == "__main__":
    app.run(debug=True)
