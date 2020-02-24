									# task1


#program to find the middle element of a singly linked list in one pass.

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

		#function to display the middle node data in one pass
	def display_middle(self):
		cur=self.head
		if cur==None:
			print('underflow\n')
		else:
			temp=cur
			while True:
				cur=cur.next
				temp=temp.next.next
				if temp.next==None or temp.next.next==None:
					print(cur.data[:-2])
					break	

my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)
print(my_list.display())				
my_list.display_middle()

##################################################################################


											#task3 and task4




#program to reverse a singly linked list without recursion.

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

	#this function reverse the order of the singly linked list
	def reverse(self):
		previous=None
		
		while self.head.next!=None:
			temp=self.head.next
			self.head.next=self.head.next.next
			temp.next=previous
			previous=temp				
		self.head.next=temp


my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)

print(my_list.display())				

my_list.reverse()#function call statement 

print(my_list.display())		
####################################################################################


										#task5



# program to remove duplicate nodes in an unsorted linked list

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

	#this function is called when we have to remove the dublicates from the linked list
	def remove_dublicates(self):
		cur=self.head

		while cur.next!=None:
			cur=cur.next
			value=cur.data
			temp=cur
			while temp.next:
				if value==temp.next.data:
					new = temp.next.next
 	               	temp.next=None
 	               	temp.next=new 	

my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)

print(my_list.display())				

my_list.remove_dublicates()#function call statement 

print(my_list.display())

########################################################################


										# task 6



#Program to find the length of a singly linked list.

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)

print(my_list.display())				

print('length of linked list is ',my_list.length()#function call statement 
#####################################################################

										#task7



#program to find the third node from the end in a singly linked list.

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

	#function to display the data of node of linked list from the end
	def display_last(self, size , n):

		temp=self.head.next
		for nodenum in range(size-n):
			temp=temp.next
		print(temp.data)


my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)

print(my_list.display())#calling statement for displaying the linked list				

size=my_list.length()#function to call for finding the length of linked list
print('the 3rd element from the last is ',my_list.display_last(size,3))#function calling statement

#################################################################

								#task 8



#program to find the sum of two linked lists using Stack.

#here is the class node 
class node:

	#this is the class node constructure to initialise the values with default values
	def __init__(self,data=None):
		self.data=data #this is the data field
		self.next=None #this is the pointer field ,points to the next node

#this is the linked_list function stores all the methods of the class node
class linked_list:

	#constructure for initialising the head pointer
	def __init__(self):
		self.head=node()

		#function to add a node in linked list at the end
	def append(self,data):
		new_node=node(data)
		cur=self.head

		while cur.next!=None:
			cur=cur.next

		cur.next=new_node
	
	#function to find and return the length of the linked list
	def length(self):
		cur=self.head	
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total
	
	#function to return all the nodes data in the form of list
	def display(self):
		elems=[]
		cur=self.head
		while cur.next:
			cur=cur.next
			elems.append(cur.data)

		return elems

#class stack is for making the stake data structure
class Stack:
	def __init__(self): #this is the constructor for forming a stack
		self.datas=[]  #this is the datas array to store the values of the stack

	#this is the function to take and add the value in the stack from last
	def push(self,value):
		self.datas.append(value)

	#this is the function to remove the value from last of the stack
	def pop(self):
		self.datas.pop()

	#this is the function to display the values of the stack
	def display(self):
		return self.datas

my_list=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(50)
my_list.append(60)

my_list1=linked_list()#call statement for the function of constructor for head

'''in these we had inserted 
	some nodes in the linked list'''
my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
my_list1.append(2)
my_list1.append(5)
my_list1.append(6)

#these 3 lines are to make three stacks
s1=Stack()
s2=Stack()
sum_stack=Stack()

llist=my_list.display()

for value in llist:
	s1.append(value)

llist1=my_list1.display()

for value in llist1:
	s2.append(value)

for index in range(len(s1)):
	sum_stack.append(s1[index]+s2[index])

print('linked list first is ',my_list.display())#calling statement for displaying the linked list	
print('linked list second is ',my_list1.display())#calling statement for displaying the linked list
print('sum of the linked list by using stack is ',sum_stack.display())	

			

