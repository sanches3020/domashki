from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        data_out = []
        for candidate in data:
            data_out.append(f'<pre>Имя - {candidate["name"]}\n'
                            f'Позиция - {candidate["position"]}\n'
                            f'Навыки - {candidate["skills"]}\n</pre>')
    return ''.join(data_out)

@app.route('/candidates/<int:id>')
def customized_candidates(id):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        data_out = []
        for candidate in data:
            if candidate["id"] == id:
                data_out.append(f'<pre>Имя - {candidate["name"]}\n'
                                f'Позиция - {candidate["position"]}\n'
                                f'Навыки - {candidate["skills"]}\n</pre>'
                                f'<img src="{candidate["picture"]}" alt="{candidate["name"]}">')
                break
    return ''.join(data_out) if data_out else 'Кандидат не найден', 404

@app.route('/skill/<x>')
def skill_search(x):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        data_out = []
        for candidate in data:
            skills = candidate['skills'].lower().split(', ')  
            if x.lower() in skills: 
                data_out.append(f'<pre>Имя - {candidate["name"]}\n'
                                f'Позиция - {candidate["position"]}\n'
                                f'Навыки - {candidate["skills"]}"></pre>')
                                
        return ''.join(data_out) if data_out else 'Кандидаты не найдены', 404

if __name__ == '__main__':
    app.run(debug=True)
