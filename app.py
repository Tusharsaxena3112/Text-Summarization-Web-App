from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index(): 
    return "Hello World"


@app.route("/summary")
def summary():
    return "Summary Page"


@app.route("/compareSummary")
def compare_summary():
    return "Compare Summary"


if __name__ == "__main__":
    app.run(debug=True)
