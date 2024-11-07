import heapq
import math


class Knapsack01DP:
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


class KnapsackBranchBound:
    class Node:
        def __init__(self, level, value, weight, bound):
            self.level = level  # Level of the node in the tree (item index)
            self.value = value  # Current value of the knapsack
            self.weight = weight  # Current weight of the knapsack
            self.bound = bound  # Bound (upper bound on the maximum value)

    def __init__(self, capacity, weights, values):
        self.capacity = capacity  # Capacity of the knapsack
        self.weights = weights  # Weights of the items
        self.values = values  # Values of the items
        self.n = len(weights)  # Number of items
        self.max_value = 0  # Maximum value found

    # Function to calculate the upper bound for a node
    def bound(self, u):
        # If weight exceeds the capacity, return 0
        if u.weight >= self.capacity:
            return 0

        # Calculate the upper bound
        bound_value = u.value
        j = u.level + 1
        total_weight = u.weight

        # Greedy selection of items to maximize value
        while j < self.n and total_weight + self.weights[j] <= self.capacity:
            total_weight += self.weights[j]
            bound_value += self.values[j]
            j += 1

        # If there are still items left, take the fraction of the next item
        if j < self.n:
            bound_value += (self.capacity - total_weight) * \
                self.values[j] / self.weights[j]

        return bound_value

    # Function to solve 0/1 Knapsack using Branch and Bound
    def solve(self):
        queue = []
        root = self.Node(-1, 0, 0, 0)
        root.bound = self.bound(root)

        # Add root node to the queue
        queue.append(root)

        while queue:
            # Get the node with the highest bound
            queue.sort(key=lambda x: x.bound, reverse=True)
            node = queue.pop(0)

            # If bound is less than the max value, prune the node
            if node.bound < self.max_value:
                continue

            # If we have reached a leaf node, continue
            if node.level == self.n - 1:
                continue

            # Generate the left child (take the current item)
            left = self.Node(node.level + 1, node.value +
                             self.values[node.level + 1], node.weight + self.weights[node.level + 1], 0)
            if left.weight <= self.capacity:
                left.bound = self.bound(left)
                if left.value > self.max_value:
                    self.max_value = left.value
                if left.bound > self.max_value:
                    queue.append(left)

            # Generate the right child (do not take the current item)
            right = self.Node(node.level + 1, node.value, node.weight, 0)
            right.bound = self.bound(right)
            if right.bound > self.max_value:
                queue.append(right)

        return self.max_value


capacity = 50
weights = [10, 20, 30]
profits = [60, 100, 120]

knapsack = KnapsackBranchBound(capacity, weights, profits)
max_value = knapsack.solve()
print(f"Maximum value achievable: {max_value}")


knapsack = Knapsack01DP(capacity=capacity, n=len(
    weights), profits=profits, weights=weights)
knapsack.solve()
