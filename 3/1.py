from flask import Flask, render_template, request

app = Flask(__name__)

# 列表待排序的数据
numbers = [3,7,9,10,3,2,4,11,45]

# 当前比较的索引
current_index = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取用户的选择
        user_choice = request.form['choice']
        process_choice(user_choice)
    return render_template('index.html', number1=numbers[current_index], number2=numbers[current_index+1])

def process_choice(user_choice):
    global current_index
    # 根据用户的选择交换两个数字的位置
    if user_choice == '1':  # 第一个数字较大
        numbers[current_index], numbers[current_index+1] = numbers[current_index+1], numbers[current_index]
    current_index += 1
    # 如果比较完成，则排序完成
    if current_index == len(numbers) - 1:
        current_index = 0  # 重置比较索引，以便重新开始排序

if __name__ == '__main__':
    app.run()
