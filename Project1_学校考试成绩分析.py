#熟练掌握数组的创建、切片（Slicing）、聚合函数（Aggregation）以及按轴计算（Axis）。
"""
任务说明：1.使用 np.random 生成一个 100×5的二维数组，代表 100 名学生在 5 门科目上的考试成绩（分数范围 0-100）。
2.计算每门科目的平均分、最高分和标准差。
3.计算每个学生的总分。
4.找出总分排名前 3 的学生在数组中的索引位置。
5.统计有几名学生的所有科目均及格（大于等于60分）。
"""
import numpy as np
#设置随机种子
np.random.seed(1)
#1.生成二维数组，每行的5个元素代表一个学生的5门成绩
students_scores = np.random.randint(40,101,size=(100,5))

#2.计算每个科目的平均分、最高分、标准差，等价于求每列的平均值、最大值、标准差
print(f"每个科目的平均分：{np.mean(students_scores,axis=0)}")
print(f"每个科目的最高分：{np.max(students_scores,axis=0)}")
print(f"每个科目的标准差：{np.std(students_scores,axis=0)}")

#3.计算每个学生总分，相当于计算每行的和
SumScore_per_Student = np.sum(students_scores,axis=1)

#4.找出总分前3名的学生在数组中的索引位置
top3_student = np.argsort(SumScore_per_Student)[::-1][:3]#切片用法：表示将数组反转，取索引0~2的元素
print(f"总分前三名的学生的索引为：{top3_student}")
print(f"他们的总分分别是：{SumScore_per_Student[top3_student]}")

#5.统计有多少学生的所有科目都及格
#思路，先用布尔条件获取布尔数组，然后使用统计函数np.all，对每行的5个元素断是否均为1
students_pass = np.all(students_scores>=60,axis=1)#检查是否每行的每个元素都满足布尔条件，是就返回1个1
students_pass_count = np.sum(students_pass) #统计所有通过的学生，也就是所有的1
print(f"一共有{students_pass_count}个学生通过")