import pandas as pd
import numpy as np


# 超过工作时间两小时才算加班

def peak_to_peak(arr):
    return arr.max() - arr.min()


def sign_time_to_week_day(x):
    return x.weekday() + 1


def compute_overtime(x, y):
    if x <= 5:
        return pd.Timedelta(y) - pd.Timedelta(int(workday_hour), unit='h')
    else:
        return pd.Timedelta(y) - pd.Timedelta(0, unit='h')


source_path = input("输入加班记录路径：")
workday_hour = input("输入工作日规定工作时间，单位h，一般为8h：")

try:
    sign = pd.read_excel(source_path)
except OSError:
    print("\nNameError : [%s] No such file or directory\n", source_path)

sign.columns = ['department', 'name', 'number', 'sign_time']
sign.sign_time = pd.to_datetime(sign.sign_time)
sign['sign_date'] = sign['sign_time'].apply(lambda x: x.strftime('%Y-%m-%d'))
sign = sign.set_index('sign_date', drop=True)

# 计算每个人一天的工作时间
sign['delta_time'] = sign.groupby(['sign_date', 'name']).sign_time.transform(peak_to_peak)
# 一周星期为1-7，遵从中国人的习惯
sign['week_day'] = sign.sign_time.apply(sign_time_to_week_day)
# 计算工作超时时间
sign['overtime'] = np.vectorize(compute_overtime)(sign['week_day'], sign['delta_time'])
# delete the duplicates in name and delta_time
sign_filter = sign.drop_duplicates(subset=['name', 'delta_time'])
del sign_filter['sign_time']
# 打印加班信息
sign_overtime = sign_filter[sign_filter['overtime'] > pd.Timedelta(2, unit='h')]

# 输出到文件
writer = pd.ExcelWriter(source_path[:source_path.rindex('/')] + '/output.xlsx')
sign.to_excel(writer, 'middle sheet')
sign_overtime.to_excel(writer, 'overtime detail')
# flush to file
writer.save()
