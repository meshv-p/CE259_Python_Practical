class Stack: 
    def __init__(self): 
        self.elements = [] 
    
    def push(self, data): 
        self.elements.append(data) 
        return data 
    
    def pop(self): 
        return self.elements.pop() 
        
    def traversal(self):
        for i in self.elements:
            print(i)


if __name__ == '__main__':
    stack = Stack()

    ## pushing the elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)


    ## popping the topmost element -> 5
    stack.pop()


    ## popping all the elements
    stack.pop()
    # stack.pop() 
    # stack.pop() 
    # stack.pop() 


    stack.traversal()
