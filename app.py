from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def result():
    from mlask import MLAsk
    emotion_analyzer = MLAsk()
    result = emotion_analyzer.analyze(input(request.form.get()))
    return render_template('result.html',result)

print(result)