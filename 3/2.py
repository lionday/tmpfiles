import json
from flask import Flask, render_template, request

app = Flask(__name__)

# 读取文件中的字典列表
with open('data.txt', 'r') as file:
    data = [json.loads(line.strip()) for line in file]

# 当前比较的行索引
current_index = 0

# 保存结果的列表
sorted_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_index
    if request.method == 'POST':
        # 获取用户的选择
        user_choice = request.form['choice']
        process_choice(user_choice)
        current_index += 1  # 前进到下一行
        # 如果当前行比较完成，则保存结果
        print(current_index,len(data))
        if current_index == len(data)-1:
            save_result()
            # current_index = 0  # 重置索引，以便重新开始下一轮排序
    if current_index < len(data) - 1:  # 更新此处的条件判断
        return render_template('index2.html', key1=data[current_index]['key'], value1=data[current_index]['value'],
                               key2=data[current_index+1]['key'], value2=data[current_index+1]['value'])
    else:
        return "所有行已排序完成！"

def process_choice(user_choice):
    # 根据用户的选择交换两个值的位置
    if user_choice == '1':  # 第一个值较大
        data[current_index]['value'], data[current_index+1]['value'] = data[current_index+1]['value'], data[current_index]['value']

def save_result():
    # 将当前行的所有字典追加到结果列表中
    sorted_data.extend(data)
    # 保存结果到文件
    with open('sorted_data.txt', 'a') as file:
        for item in sorted_data:
            file.write(json.dumps(item) + '\n')
    # 清空结果列表，以便下一轮排序
    sorted_data.clear()

if __name__ == '__main__':
    app.run()
