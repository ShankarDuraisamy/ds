class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]   
    def len(self):    
        return len(self.stack)
    def __str__(self) -> str:
        return self.stack.__str__()
    def is_empty():
        return true if len(stack) == 0 else False
    def __repr__(self) -> str:
        return self.stack.__repr__()
    
    def __getitem__(self, k : int):
        return self.stack[k]
    def __getslice__(self, i : int, j: int):
        return self.stack[i:j]
    
    
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.len())
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)
    print(stack.len())
    print(stack)
    
if __name__ == "__main__":
    main()  
    