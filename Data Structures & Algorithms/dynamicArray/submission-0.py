class DynamicArray:
    
    def __init__(self, capacity: int):
        self.list = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.list[i]


    def set(self, i: int, n: int) -> None:
        self.list[i] = n


    def pushback(self, n: int) -> None:
        if len(self.list) < self.capacity:
            self.list.append(n)
        else:
            self.resize()
            self.pushback(n)


    def popback(self) -> int:
        return self.list.pop()

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.list)
        
    
    def getCapacity(self) -> int:
        return self.capacity
