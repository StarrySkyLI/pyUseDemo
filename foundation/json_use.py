import json

list= [1,2,3,4,5]

filename = 'list.json'

# 打开文件以写入模式
with open(filename, 'w') as f:
    # 将列表对象序列化为JSON格式并写入文件
    json.dump(list, f)

# 打开文件以读取模式
with open(filename, 'r') as f:
    # 从文件中读取JSON格式的数据并反序列化为Python对象
    print(json.load(f))
