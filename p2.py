'''
有一组连续正整数，随机乱序后生成一组数据后，小蓝不小心删掉了其中一个数，
已知所删掉的这个数不是这组数据中最小的也不是最大的，
现在请你编写程序帮助小蓝找到删除的那个数。

输入描述:
    按照“编程实现”中的描述模仿输入一组这样的正整数数(正整数之间以英文逗号隔开)，
    在输入的时候少一个数(这个数不是这组数据中最小的也不是最大的)，这个数作为小蓝删除掉的那个数，且加上小蓝删除的那个数这组数据是连续的
输出描述:
    输出删除掉的是哪个数

样例输入:3,2,4,6,7
样例输出:5
'''

nums = list(map(int,input().split(',')))
#使用split通过逗号分割
#分割后的list每个元素都是字符串,使用map映射为int
#map返回的是迭代器,因此使用list转换为列表

nums.sort()
#复杂度O(N log N)
#改为用集合表示
#num_set=set(nums)
for i in range(nums[0],nums[-1]+1):
    if i not in nums:
        print(i)
        #循环,再加上查找缺省值,复杂度为O(N^2)

'''
AI的方法,使用求和公式

# 读取输入并转换为整数列表
numbers = list(map(int, input().split(',')))

# 找到最小值和最大值
min_num = min(numbers)
max_num = max(numbers)

# 计算完整序列的总和
expected_sum = (min_num + max_num) * (max_num - min_num + 1) // 2

# 计算输入序列的总和
actual_sum = sum(numbers)

# 缺失的数
missing_number = expected_sum - actual_sum

# 输出结果
print(missing_number)

'''
# 整个过程主要涉及 min、max 和 sum 函数，都是 O(N) 的操作。因此，整体时间复杂度为 O(N)，远优于您的方法。

