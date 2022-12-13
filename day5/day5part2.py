class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
	def __init__(self):
		self.head = Node("head")
		self.size = 0

	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + ","
			cur = cur.next
		return out[:-3]

	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def peek(self):

		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value

	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


def fillstack(list,stack):
    for i in list:
        stack.push(i)
        


if __name__ == "__main__":
    #Creates the 1.stack
    list1=["___B___","___V___","___S___","___N___","___T___","___C___","___H___","___Q___"]
    stack1=Stack()
    fillstack(list1,stack1)
    
    #Creates the 2.stack
    list2=["___W___","___D___","___B___","___G___"]
    stack2=Stack()
    fillstack(list2,stack2)
    
    #Creates the 3.Stack
    list3=["___F___","___W___","___R___","___T___","___S___","___Q___","___B___"]
    stack3=Stack()
    fillstack(list3,stack3)
    
    list4=["___L___","___G___","___W___","___S___","___Z___","___J___","___D___","___N___"]
    stack4=Stack()
    fillstack(list4,stack4)
    
    list5=["___M___","___P___","___D___","___V___","___F___"]
    stack5=Stack()
    fillstack(list5,stack5)
    
    list6=["___F___","___W___","___J___"]
    stack6=Stack()
    fillstack(list6,stack6)
    
    list7=["___L___","___N___","___Q___","___B___","___J___","___V___"]
    stack7=Stack()
    fillstack(list7,stack7)
    
    list8=["___G___","___T___","___R___","___C___","___J___","___Q___","___S___","___N___"]
    stack8=Stack()
    fillstack(list8,stack8)
    
    list9=["___J___","___S___","___Q___","___C___","___W___","___D___","___M___"]
    stack9=Stack()
    fillstack(list9,stack9)
    
    stacks=[None,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
    list=[]
    
    with open ("day5.txt") as file:
        for i in file:
            i=i.strip().split(" ")
            moveamount=int(i[1])
            fromstacknumber=int(i[3])
            tostacknumber=int(i[5])
            
            fromstack=stacks[fromstacknumber]
            tostack=stacks[tostacknumber]
            
            #part 2
            for i in range(moveamount):
                top=fromstack.peek()
                list.insert(0,top)
                fromstack.pop()
            for i in list:
                tostack.push(i)
            list.clear()


print(1,stack1)
print(2,stack2)
print(3,stack3)
print(4,stack4)
print(5,stack5)
print(6,stack6)
print(7,stack7)
print(8,stack8)
print(9,stack9)