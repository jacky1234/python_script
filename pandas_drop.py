import pandas as pd

# 去重示例
# 1.我有一个在A列中有重复值的数据帧。我想删除重复项，保持列B中值最高的行。https://gxnotes.com/article/105600.html
xx = pd.DataFrame({'A': [1, 1, 2, 2, 3], 'B': [10, 20, 30, 40, 10]})

print(xx)
print('\n')

# def drop1():
#     y = xx.drop_duplicates(subset='A', keep='last')
#     print(y)
#
#
# drop1()


def drop2():
    y = xx.groupby('A', group_keys=False).apply(lambda x: x.ix[x.B.idxmax()])
    print(y)


drop2()
