# Multiple input from user

print('output of Multiple input from user:')
print('Enter Two numbers: ')
a, b = input().split()
print('Output: ', a , ' ' , b)
print('sum: ', int(a) + int(b))

print('\n')

# Conditional statement

#if else

print('output of Conditional Statement: ')
print('Enter Two numbers: ')
a, b = input().split()
if  a > b:
    print(a, ' is greater than ', b)
elif a < b:
    print(a, ' is less than ', b)
else :
    print(a, ' is equals to ', b)
    
print('\n')
    
# while loop
print('Enter a number: ')
a = input()
a = int(a)
x = 1
print('numbers from 1 to ', a , 'are: ')
while x <= a:
    print(x, end=' ')
    x = x + 1
    
    
print('\n')
    
# break in while loop


print('output of break and continue inside loop: ')
friends = ["Jarif", "Rafi", "Siyum", "Shakib", "Shawon", "Rakib", "Karim"]
for x in friends:
    print(x, end=' ')
    if x == "Shawon":
        break

print('\n')


#continue in loop

friends = ["Jarif", "Rafi", "Rahim", "Siyum", "Shakib"]
for x in friends:
    if x == "Rahim":
        continue
    print(x, end=' ')

print('\n')

# Range Function

print('output of Range Function: ')
q = int(0)
print('Numbers from 1 to 10')
for x in range(10):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)

print('\n')   

print('Numbers from 20 to 50')
for x in range(20 , 50):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n')    

print('Even Numbers from 20 to 50')
for x in range(20 , 50, 2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    



print('Numbers from 100 to 50')
for x in range(100 , 50, -2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n') 





print('output of Other codes: ')

print('\n') 

print("Hello Python! I am Protik!")

print('\n') 

name = "Independent 2.0"
print(name) 

print('\n') 

age = 18
salary = 20000
name = "Mr X"
print(age)
print(salary)
print(name)

print('\n') 


ID = input("Enter your ID: ") 
print(ID) 

print('\n') 

a = 50
b = 5
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p) 

print('\n') 

a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 



print('\n') 


a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)




print('\n') 


i = 33
if (i < 48): 
    print("i is smaller than 15") 
    print("ami if block a achi") 
else: 
    print("i is greater than 15") 
    print("ami else block a achi") 
print("Ami if block eo nai, else block eo nai, hehe") 




print('\n') 

i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i ekhane nai") 



print('\n') 

for i in range(0, 40, 2): 
    print(i) 


print('\n') 


count = 0
while (count < 5): 
    count = count + 1
    print("Hello 63_N")


print('\n') 


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)


