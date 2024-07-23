from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    if not session.get("name"):
        # If no name is set in the session, redirect to login
        return redirect("/login")
    return f"Hello, {session['name']}!"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Set the name in the session
        session["name"] = request.form.get("name")
        return redirect("/")
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
