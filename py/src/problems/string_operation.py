from stack import Stack

class StringOperation:
    def __init__(self, value):
        self.value = value
    
    def reverse(self):
        stack = Stack()
        left_ptr = 0
        result = ""
        while(left_ptr < len(self.value)):
            stack.push(self.value[left_ptr])
            left_ptr += 1
        while(left_ptr >= 1) :
            result += stack.pop()
            left_ptr -= 1
        return result if len(result) > 1 else None
    
def main():
    print(StringOperation("Test").reverse())
    
if __name__ == "__main__":
    main()