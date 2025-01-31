from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return render_template('index.html', candidates=data)

@app.route('/candidates/<int:id>')
def customized_candidates(id):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        for candidate in data:
            if candidate["id"] == id:
                return render_template('index2.html', candidate=candidate)
    return 'Кандидат не найден', 404

@app.route('/skill/<x>')
def skill_search(x):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        data_out = []
        for candidate in data:
            skills = candidate['skills'].lower().split(', ')
            if x.lower() in skills:
                data_out.append(candidate)
    if data_out:
        return render_template('index3.html', candidates=data_out)
    else:
        return 'Кандидаты не найдены', 404

if __name__ == '__main__':
    app.run(debug=True)
