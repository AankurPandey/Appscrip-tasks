#function to return minimum value
def find_minimum(List):
	minimum=List[0] # variable storing first value of list
	for value in List:
		if value<minimum:
			minimum=value
	return minimum

#function to return maximum value	
def find_maximum(List):
	maximum=List[0] #variable storing first value of list
	for value in List:
		if value>maximum:
		 	maximum=value
	return maximum
		 
		 '''here we r taking input from user for a list'''
List=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split())) 

print('Minimum value of list is ',find_minimum(List))#calling statement for finding minimum term
print('Maximum value of list is ',find_maximum(List))#calling statement for finding maximum term

######################################
#program to find the dublicates in list

#function to find the dublicates in list
def find_dublicates(List):
	List2=list(dict.fromkeys(List))
	occurance=[]
	for elements in List2:
		occurance.append(0)

	for value in List:
		occurance[List2.index(value)]+=1

	for index in range(len(List2)):
		print(List2[index],' is occured ',occurance[index],' times.')

List=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split()))		

find_dublicates(List)