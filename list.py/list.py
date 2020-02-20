#######################################task 1
#function to return minimum value
def find_minimum(List):
	minimum=List[0] # variable storing first value of list
	for value in List:# loop for getting vlues of list one by one
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

######################################task 2
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
####################################################################
# program to print the missing numbers from 1 to 100 in the list

# function printing the missing numbers from 1 to 100 in passed list
def find_missing(List):
	for number in range(1,101):
		if number not in List:
			print(number,' not present')

		 '''here we r taking input from user for a list'''
List=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split())) 
find_missing(List)#function calling statement
################################################################	
#program to find all pairs of an integer array whose sum is equal to a given number.

#function printing the pairs
def find_pairs(List=[],Sum=0):
	for index in range(len(List)-1):
		for index2 in range(index+1,len(List)):
			if List[index]+List[index2]==Sum:
				print('(',List[index],',',List[index2],')')


'''here we r taking input from user for a list'''

List=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split())) 
Sum=int(input('enter the number \t'))
find_pairs(List,Sum)#function calling statement		
############################################################
