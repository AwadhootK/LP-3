# fibonacci

def fibonacci_recursive(n):
    if n < 0:
        print("Incorrect input")
        return -1
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dp(n, dp):
    if n < 0:
        print("Incorrect input")
        return -1
    if n <= 1:
        return n
    if n in dp:
        return dp[n]
    dp[n-1] = fibonacci_dp(n-1, dp)
    dp[n-2] = fibonacci_dp(n-2, dp)
    return dp[n-1] + dp[n-2]


def fibonacci_non_recursive(n):
    if n < 0:
        print("Incorrect input")
        return
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    print(c)


n = 100

# fibonacci_non_recursive(n)
# print(fibonacci_recursive(n))
dp = {}
print(fibonacci_dp(n, dp))
