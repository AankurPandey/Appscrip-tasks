				#task1
# program to print the missing numbers from 1 to 100 in the list

# function printing the missing numbers from 1 to 100 in passed list
def find_missing(List):
	for number in range(1,101):
		if number not in List:
			print(number,' not present')

		 '''here we r taking input from user for a list'''
List=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split())) 
find_missing(List)#function calling statement	


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
						#task 3
#program to find the largest and smallest number in an unsorted integer array

#function to return minimum value
def find_minimum(array):
	minimum=array[0] # variable storing first value of list
	for value in array:# loop for getting vlues of list one by one
		if value<minimum:
			minimum=value
	return minimum

#function to return maximum value	
def find_maximum(array):
	maximum=array[0] #variable storing first value of list
	for value in array:
		if value>maximum:
		 	maximum=value
	return maximum
		 
		 '''here we r taking input from user for a list'''
array=list(map(int,input('Enter the values of list on a single line with spaces\t\t ').strip().split())) 

print('Minimum value of list is ',find_minimum(array))#calling statement for finding minimum term
print('Maximum value of list is ',find_maximum(array))#calling statement for finding maximum term
################################################################
						#task4

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
###############################################################
# 					task5
#fnction prints the times of vales of array dublication
def find_dublicates(array=[]):
	array2=list(dict.fromkeys(array))
	for value in array2:
		if array.count(value)>1:
			print(value, 'is dublicated for ',array.count(value),' times')

array=list(map(int,input('Enter the element of array with spaces\n\t').strip().split()))
find_dublicates(array)

############################################################
# 						task8
#program to remove dblicates from list

array=list(map(int,input('Enter the element of array with spaces\n\t').strip().split()))#here we had taken input of array from user
print(array)
'''here we had first converted list into dictionary where keys of
	dictionary is the elements of array and again convert the dictionary into list'''
array=list(dict.fromkeys(array))
print(array)
#############################################################

#					task10
#program to  remove duplicates in an array without using any library.

# function to return array after removing duplicates
def remove_dublicates(array=[]):
	array2=[]
	for value in array:
		if value not in array2:
			array2.append(value)
	return array2
array=list(map(int,input('Enter the element of array with spaces\n\t').strip().split()))
print('after removing dublicates from array entered ,the array looks like ',remove_dublicates(array))
