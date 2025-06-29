import time

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суми 0 не потрібно монет

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Визначаємо, які монети використовувати
    coin_count = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i] == dp[i - coin] + 1:
                if coin not in coin_count:
                    coin_count[coin] = 0
                coin_count[coin] += 1
                i -= coin
                break
    
    return coin_count


amount = 113

# Тест алгоритму динамічного програмування
start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print("Динамічне програмування:", dp_result)
print("Час виконання динамічного програмування:", dp_time)
