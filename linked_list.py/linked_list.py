class value:
    def __init__(self, values):
        self.values = values
        self.next = None  # make None as the default value for next.
        
       


def count_nodes(head):
    # assuming that head != None
    count = 1
    temp = head
    while temp.next is not None:
        temp = temp.next
        count += 1
    return count

node1 = value(6)
node2 = value(3)
node3 = value(4)
node4 = value(2)
node5 = value(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('linked list id having ',count_nodes(node1),'trems')


###########################################################
'''program to find the middle element of a singly
 linked list in one pass'''

class Node:
    def __init__(self, values):
        self.values = values
        self.next = None  # make None as the default value for next.
    

def middle_term(head):
    temp1 = head
    temp2 = head
    while temp2.next is not None:
        temp1 = temp1.next
        temp2 = temp2.next.next
    
    return temp1.values
       

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('middle term of linked list is ',middle_term(node1))