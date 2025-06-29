import time
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count[coin] = count
            amount -= coin * count
    
    return coin_count

amount = 113

# Тест жадібного алгоритму
start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

# Порівняння результатів і часу
print("Жадібний алгоритм:", greedy_result)
print("Час виконання жадібного алгоритму:", greedy_time)

