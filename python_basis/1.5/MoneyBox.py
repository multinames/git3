class MoneyBox:
    def __init__(self, capacity):
    	self.count = 0
    	self.capacity = capacity
# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
    	if self.count + v <= self.capacity:
    		return True
    	else:
    		return False
# True, если можно добавить v монет, False иначе

    def add(self, v):
    	if self.can_add(v):
    		self.count += v
# положить v монет в копилку
b = MoneyBox(10)
b.add(5)
b.add(5)
print(b.can_add(1))
