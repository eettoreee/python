import time

# 1. 获取当前时间的时间戳（Unix纪元以来的秒数）
current_timestamp = time.time()
print(f"当前时间的时间戳: {current_timestamp}")

# 2. 暂停程序执行指定秒数
print("程序将在2秒后继续...")
time.sleep(2)
print("程序已恢复执行")

# 3. 格式化当前时间（本地时间）为字符串
formatted_local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"当前本地时间: {formatted_local_time}")

# 4. 解析字符串为时间元组
time_string = "2023-03-15 14:30:00"
parsed_time_tuple = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(f"解析出的时间元组: {parsed_time_tuple}")

# 5. 将时间戳转为格林尼治标准时间的时间元组
timestamp_to_convert = 1678901234
gmt_time_tuple = time.gmtime(timestamp_to_convert)
print(f"格林尼治标准时间: {time.strftime('%Y-%m-%d %H:%M:%S', gmt_time_tuple)}")

# 6. 将时间戳转为本地时间的时间元组
local_time_tuple = time.localtime(timestamp_to_convert)
print(f"本地时间: {time.strftime('%Y-%m-%d %H:%M:%S', local_time_tuple)}")

# 7.ctime()的用法是将时间戳转换为字符串
print(time.ctime())
print(time.ctime(1678901234))
print(time.ctime(1678901234.123456))
print(time.ctime(1678901234.123456789))
