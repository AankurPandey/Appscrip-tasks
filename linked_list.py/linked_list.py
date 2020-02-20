#program to find the lenth of linked list

#Node is the class whose object represent node
class Node:
    def __init__(self, values):#__init__() is a constructor
        self.data = values # make values as data field of node
        self.next = None  # make None as the default value for next field.
        
       
#function count_nodes returns the lenth of linked list

def count_nodes(head):
    count = 1    #count variable to count the number of nodes
    temp = head #temp is a variable to store the value of head
    while temp.next is not None:
        temp = temp.next
        count += 1
    return count

'''here we had created
some objects of class Node'''
node1 = Node(5)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)
'''here we had linked all objects
to form linked list'''
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('linked list id having ',count_nodes(node1),'trems')# calling statement for function count_nodes


###########################################################
'''program to find the middle element of a singly
 linked list in one pass'''

class Node:
    def __init__(self, values):
        self.values = values
        self.next = None  # make None as the default value for next.
    
#function middle_term returns the middle value of linked list
def middle_term(head):
    #temp1 and temp2 are two pointers
    temp1 = head 
    temp2 = head
    while temp2.next is not None:
        temp1 = temp1.next
        temp2 = temp2.next.next
    
    return temp1.values
'''here we had created
some objects of class Node'''       

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
'''here we had linked all objects
to form linked list'''
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('middle term of linked list is ',middle_term(node1))# calling statement for function middle_term
