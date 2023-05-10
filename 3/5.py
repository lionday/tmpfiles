from flask import Flask, render_template, request

app = Flask(__name__)

# 默认的答案列表
answers = [
    {'id': 1, 'text': '答案1', 'group': 1},
    {'id': 2, 'text': '答案2', 'group': 1},
    {'id': 3, 'text': '答案3', 'group': 1},
    {'id': 4, 'text': '答案4', 'group': 1},
    {'id': 5, 'text': '答案5', 'group': 2},
    {'id': 6, 'text': '答案6', 'group': 2},
    {'id': 7, 'text': '答案7', 'group': 2},
    {'id': 8, 'text': '答案8', 'group': 3},
    {'id': 9, 'text': '答案9', 'group': 3},
    {'id': 10, 'text': '答案10', 'group': 3}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取更新后的答案列表
        updated_answers = request.json['answers']
        # 更新答案列表
        if updated_answers:
            answers.clear()
            answers.extend(updated_answers)
    return render_template('index5.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
