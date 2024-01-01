from stack import Stack

class Constants:
    open_parentheses = '('
    close_parentheses =')'
    open_square = '['
    close_square =']'
    open_curly = '{'
    close_curly ='}'



class Expression:
    def __init__(self, expression: str):
        self.expression = expression
        
    def __str__(self):
        return self.expression.__str__()
    def __repr__(self):
        return self.expression.__repr__()
    def __len__(self):
        return len(self.expression)
    def __getitem__(self, k: int):
        return self.expression[k]

class ExpressionValidator:
    def __init__(self, expression: Expression):
        self.expression = expression
        self.exp_open =[Constants.open_curly, Constants.open_parentheses, Constants.open_square]
        self.exp_close =[Constants.close_curly, Constants.close_parentheses, Constants.close_square]
    
    @staticmethod
    def is_match(first_brace, second_brace):
        if first_brace == "(" and second_brace == ")":
            return True
        elif first_brace == "{" and second_brace == "}":
            return True
        elif first_brace == "[" and second_brace == "]":
            return True
        return False
    
    def validate(self):
        stack = Stack()
        is_valid = True
        left_ptr = 0
        while(left_ptr < len(self.expression)):
            if(self.expression[left_ptr] in self.exp_open):
                stack.push(self.expression[left_ptr])
            if(self.expression[left_ptr] in self.exp_close):
                is_valid = ExpressionValidator.is_match(stack.pop(), self.expression[left_ptr])
            if not is_valid:
                return False
            left_ptr += 1
        return True

def main():
    print(ExpressionValidator(Expression('[()]')).validate())
    print(ExpressionValidator(Expression('([)]')).validate())
    
if __name__ == "__main__":
    main()