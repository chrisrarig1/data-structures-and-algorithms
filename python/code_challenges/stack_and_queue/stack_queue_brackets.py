from code_challenges.stack_and_queue.stack import Stack

class Brackets():
    def __init__(self):
        self.stack1 = Stack()

    def validate_brackets(self,string):
        brack = list(string)
        dict = {'(':')','{':'}','[':']'}
        for i in brack:
            if i in dict.keys():
                self.stack1.push(i)
            elif i in dict.values():
                if self.stack1.empty():
                    return False
                else:
                    self.stack1.pop()
        return self.stack1.empty()
