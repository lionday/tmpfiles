from flask import Flask, render_template, request
import json

app = Flask(__name__)

# 初始问题和答案列表
question = "这是一个问题"
answers = ["答案1", "答案2", "答案3", "答案4", "答案5", "答案6", "答案7", "答案8", "答案9", "答案10"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 获取排序后的答案顺序
        sorted_answers = request.form.getlist('answer[]')
        # 在此处处理提交后的答案顺序
        print("提交的答案顺序:", sorted_answers)
        # 这里可以将答案顺序存入数据库或进行其他操作

    return render_template('index4.html', question=question, answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
