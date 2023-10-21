class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)
        print(self.__stack_list)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val



stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

print("#"*20)

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val



push(3)
push(2)
push(1)


print(pop())
print(pop())
print(pop())
    
