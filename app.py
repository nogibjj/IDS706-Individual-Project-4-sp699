from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Set up the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route("/")
def index():
    return render_template("sentiment_input.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        user_input = request.form["text_to_analyze"]

        # Perform sentiment analysis on the user input
        sentiment_result = sentiment_analyzer(user_input)

        return render_template("sentiment_result.html", user_text=user_input, sentiment=sentiment_result[0]['label'])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
