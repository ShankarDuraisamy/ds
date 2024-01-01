from stack import Stack

class DecimalToBinary:
    def __init__(self, value: int):
        self.value = value
    
    def perform(self):
        stack = Stack()
        value_cpy = self.value
        while(value_cpy > 0):
            stack.push(value_cpy%2)
            value_cpy //= 2
        return stack[::-1] 

def main():
    print(DecimalToBinary(120).perform())
    
if __name__ == "__main__":
    main()