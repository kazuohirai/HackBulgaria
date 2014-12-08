def calculate_coins(sum):
    coins = {100: 0, 50: 0, 20: 0,
             10: 0, 5: 0, 2: 0, 1: 0}
    stinki = [100, 50, 20, 10, 5, 2, 1]
    sum = int(sum * 100)
    print sum
    for k in stinki:
        while sum >= k:
            if sum == 0:
                break
            if sum - k >= 0:
                sum -= k
                coins[k] += 1
    return coins
