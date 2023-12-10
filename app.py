from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = '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'  # OpenAI API Key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = openai.Completion.create(
          engine="davinci",
          prompt=user_input,
          max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return render_template('index.html', user_input=user_input, answer=answer)
    return render_template('index.html', user_input='', answer='')

if __name__ == '__main__':
    app.run(debug=True)
