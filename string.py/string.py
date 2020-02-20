#program to check if a string contains only digits.

#function Check_digits return true if string contains only digits else return false
def check_digits(string):
	digitsNumber=0 #variable to count the number of character in string
	digits='0123456789'
	for character in string:#loop to read character of string one by one 
		if character in digits: #checking whether the character from string is a digit or not
			digitsNumber+=1 #increment in the value of digitsNumber which stores the number of digits in sting

	if digitsNumber==len(string):#comparing value of digitsNumber with length of string
		return True
	else:
		return False


string=input('Enter the string to check\t\t')  #taking a string as an input
answer=check_digits(string) #function calling statement for check_digits

if answer=='True':# comparing the returned result
	print('Your entered string contains only digits')
else:
	print('Your entered string does not contain only digits')


###############################################
#program to check if a given string is a palindrome.	

#function check_palindrome check whether the string is palindrome or not
def check_palindrome(string):
	repeate=len(string)//2
	for characterIndex in range(repeate):# loop for getting character indexes of string
		''' comparing the characters from
    beginning with last in passed string'''
    if string[characterIndex]!=string[-(characterIndex+1)]:
			break
	if characterIndex+1==repeate:
		return True
	else:
		return False

string=input('Enter the string to check\t\t')		#taking a string as an input
answer=check_palindrome(string) #function calling statement for checking palindrome

if answer==True:#comparing the returned result
	print('Your entered string is a palindrome')
else:
	print('Your entered string is not a polindrome')

# #################################################
#program to checkwhether the two strings are anagroms or not

#function to check strings are anagroms or not
def check_anagroms(string1='',string2=''):
	if len(string2)!=len(string1):
		return False
	else:
		for index in string1:
			if string1[index]!=string2[-(index+1)]:
				return False
			else:
				return True
'''taking input from user
		 and calling function in next three lines'''
string1=input('Enter 1st string')
string2=input('Enter 2nd string')
answer=check_anagroms(string1,string2)


if answer=='True':
	print('Your entered strings are anagroms')
else:
	print('Your entered strings are not anagroms')					
# ####################################################################################################
#program to print first non repeated character

#function returning non repeated character
def nonRepeated_char(string): 
	list_string=list(string) #converting the string into list of characters of string
	list2_string=list(dict.fromkeys(list_string)) #removing dublicates from the string
	for character in list_string:
		count=0
		for char in list2_string:
			if character==char:
				count+=1

		if count==1:
			return character
	if count!=1:
		return 'no character'				

string=input('Enter string\t\t') #taking input from user
print('first non-repeated character in a string is ',nonRepeated_char())
# #################################################################################
#program to find and print the dublicates characters in the string

#function to find and print the times of occurance of every character in string 
def find_dublicate(string=''):
	list_string=list(string) #converting the string into list of characters of string
	list_string=list(dict.fromkeys(list_string)) #removing dublicates from the string
	occurance=[]
	for elements in list_string:
		occurance.append(0)

	for value in string:
		occurance[list_string.index(value)]+=1

	for index in range(len(list_string)):
		print(list_string[index],' is occured ',occurance[index],' times.')

print(find_dublicate(input('Enter string'))) #taking input from user and function calling on the same line of code
# #################################################################################
#program to count the number of vowels and consonants in a given string.

#function counts and returns the number of occurance of vowels
def count_vowels(string=''):
	string=string.lower() #converting whole string into lower case
	count=0
	for character in string:
		if character in 'aeiou':
			count+=1
	return count

#function counts and returns the number of occurance of consonents
def count_consonents(string=''):
	string=string.lower() #converting whole string into lower case
	count=0
	for character in string:
		if character in 'bcdfghjklmnpqrstvwxyz':
			count+=1
	return count

string=input('enter string\t')#taking input of string from user

#printing and calling statement on the same line 
print(string,' has ',count_vowels(string),' vowels and ',count_consonents(string),'consonents')	
#########################################################################	

#program to print the occurance of a character in the entered string

#function count_occurance returns the times character ch occured in string
def count_occurance(string='',ch=''):
	count=0 #variable count the occurance of ch
	for character in string:
		if ch==character: #compares the values of character entered by user and character from string
			count+=1
	return count
'''next to lines of code takes 
  the input of string and character to be counted from user'''
string=input('Enter the string\t\t')	
ch=input('enter the character to be count\t\t')

#printing and calling statement on the same line 
print(ch,'occured',count_occurance(string.lower(),ch.lower()),' times in ',string)		
#################################################################################
# Python program to print all permutations 

# Function to print permutations of string  
def permute(list_string, start, length): 
    if start==r: 
        print( list_string)
    else: 
        for character in range(start,r+1): 
            list_string[start], list_string[character] = list_string[character], list_string[start] 
            permute(list_string, start+1, r) ## recursion as we r calling the same function again
            list_string[start], list_string[character] = list_string[character], list_string[start] 
  
# Driver program to test the above function 
string =input('enter the string')
n = len(string) 
list_string = list(string) 
permute(list_string, 0, n-1) 

