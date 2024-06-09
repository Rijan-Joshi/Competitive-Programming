class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._total = 0

    def __str__(self):
        return "🍪" * self._total

    def deposit(self, n):
        if n < 0:
            raise ValueError("Invalid deposit amount")
        self._total += n
        if self._total > self._capacity:
            raise ValueError("Out of capacity")
        return self._total

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Invalid withdrawal amount")
        if n > self._total:
            raise ValueError("Not enough cookies in jar")
        self._total -= n
        return self._total

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._total
