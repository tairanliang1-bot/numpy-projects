#目标：避免使用 for 循环，纯利用 NumPy 的向量化操作解决复杂逻辑。
"""
任务说明：
1.模拟一个醉汉在二维平面上的行走（起点为坐标 [0, 0]）。
2.他一共走 1000 步，每一步只能随机向四个方向（上 [0, 1]、下 [0, -1]、左 [-1, 0]、右 [1, 0]）走一个单位。
使用 np.random.choice 生成这 1000 步的方向。
3.使用 np.cumsum（累积和）计算他每一步所在的实际坐标。
4.计算他在游走过程中距离原点最远时的距离（欧几里得距离）
"""
import numpy as np
#1.定义方向：上下左右
directions = np.array([[0,1],[0,-1],[-1,0],[1,0]])

#2.随机生成1000步，也就是在directions数组里选择1000次
np.random.seed(0)
#随机抽取1000次索引
step_indices = np.random.choice(4,size=1000)
#根据索引获取具体的坐标变换，形成一个1000行2列的数组，每行代表一次坐标变化
steps = directions[step_indices]

#3.计算每一步的实际坐标
#np.cumsum会把每一步的变化叠加起来，比如[步1, 步1+步2, 步1+步2+步3...]
positions = np.cumsum(steps,axis=0) #按照列相加

#4.计算他在游走过程中距离原点最远时的距离（欧几里得距离）
distances = np.sqrt(positions[:,0]**2 + positions[:,1]**2)
max_distance = np.max(distances)

print(f"该过程中距离原点最远为{max_distance}米")
print(f"距离原点最远的坐标为：{positions[np.argmax(distances)]}")
print(f"最终停留坐标为{positions}")