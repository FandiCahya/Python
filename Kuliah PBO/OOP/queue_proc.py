queue = []
# def __init__():
#     queue = []

def put(elem):
    queue.insert(0, elem)

def get():
    if len(queue) > 0:
        elem = queue[-1]
        del queue[-1]
        return elem
    else:
        print("Queue Error")

put(1)
put("dog")
put(False)
try:
    for i in range(4):
        print(get())
except:
    print("Queue error")
    