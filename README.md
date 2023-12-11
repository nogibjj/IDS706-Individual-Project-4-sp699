![Sentiment Analysis CICD](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/actions/workflows/cicd.yml/badge.svg)</br>
# IDS-706-Data-Engineering :computer:

## Individual Project 4 :page_facing_up:

## :ballot_box_with_check: Requirements
* __`README.md`__: This should clearly explain what the project does, its dependencies, how to run the program, and conclude with actionable and data-driven recommendations to a hypothetical management team.
* __`GitHub Repo`__: A complete GitHub Repo that contains all required scripts and documentation to run your application.
* __`Flask App`__: Achieve functionality within Docker or a platform, and creativity and sophistication are particularly recognized for successfully embedding a functioning Large Language Model within a Flask application.
* __`Use of DockerHub (Or equivalent)`__: Hosting your functioning container on DockerHub.
* __`Azure Web App (Or equivalent)`__: Successfully deploying your container via Azure Web App to a public endpoint. This can be done either directly from Docker or through Azure container registry.
* __`Video Demo`__: A YouTube link in README.md showing a clear, concise (2-5min) walkthrough and demonstration of your application.

## :ballot_box_with_check: To-do List
* __Flask App__: Learn web application development, server-side scripting, and integration of advanced features like Large Language Models.
* __Docker Hub__: Functionality within Docker or a platform is assessed, and embedding a functioning Large Language Model in Flask is valued for creativity and sophistication.
* __Azure Web App__: Learn cloud-based application hosting, scaling, and management, along with integrating cloud services and mastering deployment strategies through the use of Azure Web App.

## :ballot_box_with_check: Web Application
`Sentiment Analysis`
 Sentiment analysis is a natural language processing technique used to determine the emotional tone behind words, enabling the understanding of attitudes, opinions, and emotions expressed in written language. It's commonly applied in business and social media monitoring to gauge public opinion and customer feedback.</br>
1. Index
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/243a70e3-634b-46a4-8c0c-e99037a35d0c)</br>
2. Positive Sentiment
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/4b5bf09b-f4c9-47f2-9a1f-3af34bd3de5b)
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/ee522be0-50a9-45f1-a418-5b0264d5fe96)
3. Negative Sentiment
![image](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/assets/143478016/35792936-791a-4abe-9e96-563c544a321e)
![image](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/assets/143478016/62a68c34-4e49-4b62-a2d2-66c461d837d0)


## :ballot_box_with_check: Main Progress
#### `Section 1` Flask App
##### Build the Flask Application using Docker with functionality embedded LLM within Flask.
* `sentiment_input.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analysis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f3f3f3;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            height: 100px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin: 10px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sentiment Analysis</h2>
        <form action="/analyze" method="post">
            <label for="text_to_analyze">Enter text for sentiment analysis:</label>
            <textarea id="text_to_analyze" name="text_to_analyze" required></textarea>
            <button type="submit">Analyze Sentiment</button>
        </form>
    </div>
</body>
</html>
```
* `sentiment_result.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analysis Result</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f3f3f3;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            width: 60%;
            max-width: 800px;
        }
        .result {
            background-color: #f2f2f2;
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sentiment Analysis Result</h2>
        <div class="result">
            <h3>Your Text:</h3>
            <p>{{ user_text }}</p>
        </div>
        <div class="result">
            <h3>Analyzed Sentiment:</h3>
            <p>{{ sentiment }}</p>
        </div>
        <a href="/">Try Another Analysis</a>
    </div>
</body>
</html>
```
* `app.py`
```Python
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
```
 
#### `Section 2` Docker Hub
##### Host functioning container on DockerHub.
* `Step 1` Docker Build </br>
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/17113faf-897e-4bbd-9553-58c26860122e)

* `Step 2` Docker Tag </br>
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/564b8eba-6be5-40c2-8acb-9fdf23834e3c)

* `Step 3` Docker Push </br>
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/5e21094b-7403-4329-98dc-7f0feb2774db)

* `Step 4` Confirm the successful push of the Docker image by checking if it is listed in Docker Hub repository </br>
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/c63c9a23-ca80-4760-95a8-0d6efae2409f)


#### `Section 3` Azure Web App
##### Deploy container via Azure Web App to a public endpoint.
