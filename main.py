import time
from collections import defaultdict

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(number):
    if number is None or number < 0:
        return {}

    coins_dict = defaultdict(int)
    for c in coins:
        while number >= c:
            coins_dict[c] += 1
            number -= c

    return dict(coins_dict)


def find_min_coins(number):
    infinity = float('inf')
    min_array = [infinity] * (number + 1)
    prev = [None] * (number + 1)

    min_array[0] = 0

    for n in range(1, number + 1):
        for c in coins:
            if c <= n and min_array[n - c] + 1 < min_array[n]:
                min_array[n] = min_array[n - c] + 1
                prev[n] = c

    if min_array[number] == infinity:
        return None

    coins_dict = defaultdict(int)
    while number > 0:
        c = prev[number]
        if c is None:
            break
        coins_dict[c] += 1
        number -= c

    return dict(coins_dict)


print('find_coins_greedy(113):', find_coins_greedy(113))
print('find_min_coins(113):', find_min_coins(113), '\n\n')

start_time = time.time()
res = find_coins_greedy(113)
end_time = time.time()
time_113 = end_time - start_time

start_time = time.time()
res = find_coins_greedy(226)
end_time = time.time()
time_226 = end_time - start_time

start_time = time.time()
res = find_coins_greedy(113113)
end_time = time.time()
time_113113 = end_time - start_time

print(f"Greedy(113) time: {time_113} seconds")
print(f"Greedy(226) time: {time_226} seconds")
print(f"Greedy(113113) time: {time_113113} seconds")

start_time = time.time()
res = find_min_coins(113)
end_time = time.time()
time_113 = end_time - start_time

start_time = time.time()
res = find_min_coins(226)
end_time = time.time()
time_226 = end_time - start_time

start_time = time.time()
res = find_min_coins(113113)
end_time = time.time()
time_113113 = end_time - start_time

print(f"Dynamic(113) time: {time_113} seconds")
print(f"Dynamic(226) time: {time_226} seconds")
print(f"Dynamic(113113) time: {time_113113} seconds")
