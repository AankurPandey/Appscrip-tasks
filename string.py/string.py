#program to check if a string contains only digits.

#function Check_digits return true if string contains only digits else return false
# def check_digits(string):
# 	digitsNumber=0
# 	digits='0123456789'
# 	for character in string:
# 		if character in digits:
# 			digitsNumber+=1

# 	if digitsNumber==len(string):
# 		return True
# 	else:
# 		return False


# string=input('Enter the string to check\t\t')
# answer=check_digits(string)

# if answer=='True':
# 	print('Your entered string contains only digits')
# else:
# 	print('Your entered string does not contain only digits')


###############################################
#program to check if a given string is a palindrome.		
# def check_palindrome(string):
# 	repeate=len(string)//2
# 	for characterIndex in range(repeate):
# 		if string[characterIndex]!=string[-(characterIndex+1)]:
# 			break
# 	if characterIndex+1==repeate:
# 		return True
# 	else:
# 		return False

# string=input('Enter the string to check\t\t')		
# answer=check_palindrome(string)

# if answer==True:
# 	print('Your entered string is a palindrome')
# else:
# 	print('Your entered string is not a polindrome')

# #################################################