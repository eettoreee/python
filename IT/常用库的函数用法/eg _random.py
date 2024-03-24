# 导入random模块
import random

# 1. random.random()
#   生成一个0到1之间的随机浮点数
example_random_float = random.random()
print(f"Random float between 0 and 1: {example_random_float}")

# 2. random.randint(a, b)
#   生成指定范围内的随机整数（包括a和b两个边界）
example_random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {example_random_int}")

pi_value = 3.141592653589793
# 利用format控制小数点后两位精度，对其和字符总数等等
print(f"Pi value: {pi_value:.2f}")

# 3. random.choice(sequence)
#   从序列中随机选择一个元素
example_list = ["apple", "banana", "cherry"]
example_choice = random.choice(example_list)
print(f"Random choice from list: {example_choice}")

# 4. random.choices(population, weights=None, *, cum_weights=None, k=1)
#   从序列中根据可选权重随机选择多个元素
example_weighted_choices = random.choices(example_list, [1, 2, 3], k=3)
print(f"Weighted random choices (k=3): {example_weighted_choices}")

# 5. random.uniform(a, b)
#   生成指定范围内的随机浮点数，范围包括a和b两个边界
example_uniform_float = random.uniform(0.1, 0.5)
print(f"Random float between 0.1 and 0.5: {example_uniform_float}")

# 6. random.shuffle(x)
#   对列表x就地打乱顺序
example_shuffled_list = [1, 2, 3, 4, 5]
random.shuffle(example_shuffled_list)
print(f"Shuffled list: {example_shuffled_list}")

# 7. random.sample(population, k)
#   不放回地从总体中抽取k个独立随机样本
example_population = [1, 2, 3, 4, 5, 6, 7, 8]
example_sample = random.sample(example_population, 4)
print(f"Random sample without replacement: {example_sample}")

# 8. random.randrange(stop)
#   生成从0（默认）到stop-1的随机整数
example_random_range = random.randrange(10)
print(f"Random integer up to 10: {example_random_range}")

# 也可带起始点和停止点，不包括停止点本身
example_random_range_with_start_stop = random.randrange(1, 10)
print(f"Random integer from 1 to 9: {example_random_range_with_start_stop}")

# 9. random.seed(a=None)
#   设置随机数生成器种子，确保每次运行可复现相同随机序列
random.seed(42)
print("Seeded the random number generator.")

# 以上仅为部分random模块常用函数示例
# 其他函数还包括betavariate(), expovariate(), gauss(), lognormvariate()等用于特定分布的随机数生成
