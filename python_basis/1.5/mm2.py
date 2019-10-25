class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity


    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        else:
            return False


    def add(self, v):
        if self.can_add(v):
            self.count += v

b = MoneyBox(10)
b.add(5)
b.add(5)
print(b.can_add(1))