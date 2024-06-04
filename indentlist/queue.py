class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)




a = Stack()
a.push(15)
a.push(25)
a.push(35)
a.push("LOY")
a.push("Python")
print(f" Barcha malumotlar soni :{a.size()}")
print(f" Malumot yoqmi yoki bormi :{a.is_empty()}")
print(f" Barcha Malumotlar :{a.items}")
popped = a.pop()
print(f" Oxirgi malumot: {popped}")
sek = a.peek()
print(sek)
"""
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)

top_item = stack.pop()
print("Popped:", top_item)
print("Stack after pop:", stack.items)

peeked_item = stack.peek()
print("Peeked:", peeked_item)
print("Stack size:", stack.size())"""