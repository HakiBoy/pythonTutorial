#declare String name and show it
name = "Therachart Wicheanrat"
print 'My name is', name

#then we can access to any character in this string by indexing of array
print 'My first character in my name is', name[0]
#!!please remember first character in string must start at zero and end with n-1
print 'My last character in my name is', name[20]

# About String method
# String len
print 'My name have', len(name), 'character'

# to LowerCase
print 'To LowerCase =', name.lower()

# to UpperCase
print 'To UpperCase =', name.upper()

# to String
my_float = 2.125634245
print 'To String =', str(my_float)

# String Concatenation
str1 = "Walk "
str2 = "with "
str3 = "me"
str123 = str1 + str2 + str3
print 'Concatenation string = ' + str123
#### !!!! Hint !!!! #####
#### when you want to print string and number in the same line
my_money = 300.50
print 'In my pocket have ' + str(my_money)
#### or like this
print 'In my pocket have', my_money
