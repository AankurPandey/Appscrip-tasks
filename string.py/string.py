#program to check if a string contains only digits.

#function Check_digits return true if string contains only digits else return false
# def check_digits(string):
# 	digitsNumber=0 #variable to count the number of character in string
# 	digits='0123456789'
# 	for character in string:#loop to read character of string one by one 
# 		if character in digits:
# 			digitsNumber+=1

# 	if digitsNumber==len(string):#comparing value of digitsNumber with length of string
# 		return True
# 	else:
# 		return False


# string=input('Enter the string to check\t\t')  #taking a string as an input
# answer=check_digits(string) #function calling statement for check_digits

# if answer=='True':
# 	print('Your entered string contains only digits')
# else:
# 	print('Your entered string does not contain only digits')


###############################################
#program to check if a given string is a palindrome.	

#function check_palindrome check whether the string is palindrome or not
# def check_palindrome(string):
# 	repeate=len(string)//2
# 	for characterIndex in range(repeate):
# 		if string[characterIndex]!=string[-(characterIndex+1)]:
# 			break
# 	if characterIndex+1==repeate:
# 		return True
# 	else:
# 		return False

# string=input('Enter the string to check\t\t')		#taking a string as an input
# answer=check_palindrome(string) #function calling statement for checking palindrome

# if answer==True:
# 	print('Your entered string is a palindrome')
# else:
# 	print('Your entered string is not a polindrome')

# #################################################
