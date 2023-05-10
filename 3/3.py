from flask import Flask, render_template, request

app = Flask(__name__)

# 初始问题和答案列表
question = "这是一个示例问题"
answers = ["答案1", "答案2", "答案3", "答案4", "答案5", "答案6", "答案7", "答案8", "答案9", "答案10"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 接收答案顺序的POST请求
        ordered_answers = request.form.getlist('answer')
        # 在这里可以将答案顺序保存到后台数据库或进行其他处理
        print("答案顺序：", ordered_answers)
    return render_template('index3.html', question=question, answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
