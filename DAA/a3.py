import heapq


class Knapsack01:
    def __init__(self, capacity, n, profits, weights):
        self.capacity = capacity
        self.n = n
        self.profits = profits
        self.weights = weights
        self.mat = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        self.items = sorted([[self.weights[i], self.profits[i]]
                            for i in range(self.n)])

    def print_mat(self):
        for row in self.mat:
            print(" ".join(map(str, row)))

    def fill_dp_matrix(self):
        for i in range(1, self.n + 1):
            curr_wt = self.items[i - 1]
            for j in range(1, self.capacity + 1):
                if j >= curr_wt[0]:
                    self.mat[i][j] = max(
                        self.mat[i - 1][j], self.mat[i - 1][j - curr_wt[0]] + curr_wt[1])
                else:
                    self.mat[i][j] = self.mat[i - 1][j]

    def get_max_profit(self):
        return self.mat[self.n][self.capacity]

    def get_selected_items(self):
        answer = []
        remaining_capacity = self.capacity

        for i in range(self.n, 0, -1):
            if self.mat[i][remaining_capacity] != self.mat[i - 1][remaining_capacity]:
                answer.append(self.items[i - 1])
                remaining_capacity -= self.items[i - 1][0]

        return answer

    def solve(self):
        self.fill_dp_matrix()
        print("DP Matrix:")
        self.print_mat()
        max_profit = self.get_max_profit()
        print("Maximum Profit:", max_profit)
        selected_items = self.get_selected_items()
        print("Selected items (weight, profit):", selected_items)


# Example usage
knapsack = Knapsack01(capacity=8, n=4, profits=[
                      2, 3, 1, 4], weights=[3, 4, 6, 5])
knapsack.solve()
