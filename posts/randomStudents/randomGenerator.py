import numpy as np

randomList = np.random.choice(np.arange(1,44,1),size=3,replace=False)

# 写入文档
file_path = 'random_numbers.txt'
with open(f'./posts/randomStudents/{file_path}', 'w') as file:
    file.write(f'面批学号: {randomList}')

# 输出写入文件的结果
print(f'文件 {file_path} 成功写入！')