


# lst = [1,22,3,4, ['a','b','c'] , 'hello']
# print (lst [3])
# print (lst[4][1])
# a = [1,2,3,4]
# b = [5,6,7,8]
# a.append (b)
# print (a)
#st = set ([1,2,3,4])
# map_ = {
#     'fname':'harshita',
#     'lname':'soni',
#     'company':'regex'

# }
# print (map_.get ('company','not found'))

# print(map_.pop('company'))
# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in lst [2:9] :
#     print (i)

# for i in [1,2,3]:
#     for j in ['a','b','c'] :
#         print (i,j)
# a = int(input("enter any number"))
# if a>1:

#  for i in range (2 , int(a/2)+1):
#     if (a % i ) == 0:
#         print ("it is  not a prime number" )
#         break  
#     else: 
#         print (" it is a prime number")
# else:
#     print ("no")  
# n = input ("enter any string")
# for i in n:
#     if ord(i) % 2 ==0:
#         print (i, 'is in even number posisition')

# n = int (input ("enter how many number you want in a list "))
# lst = []
# for i in range (n):
#     m=(input ("enter n numbers"))
#     lst.append(m)
# print (lst)


# n = int(input ("enter any number"))
# dist = {
#  'str': [],
#  'int': [],
#  'float':[],
#  'bool': []
# } 
# for i in range (n):
#     dt = input('enter datatype:')
#     value = input('enter value')
#     if dt == 'str':
#         dist['str'].append(value)
#     elif  dt =='int':
#         dist['int'].append(int(value))
#     elif dt == 'float' :
#         dist['float'].append(float(value)) 
#     else:
#         print('please initialise a empty list for {dt}'.format(dt))
# print(dist)    

# from tkinter import N


# n = input ("enter any input")
# # for i in n: 
# if ((n >= 'a' and n <='z' or n >='A' and n <='Z' or n >='0' and n <='9')):
#         print ("you have entered all the requirement")
# else:
#         print("enter the req format")    
    


# n = int(input('how many test cases:'))
# sum = 1
# total = 0
# for i in range (n): 
    
#     op = input ('please enter opration string: ')
#     op_list = op.split()
#     print(op_list)

#     if op_list[0] == 'add' :
#         number=map(int,op_list[1:])
#         for j in number:
#             total = total+j
#         print ('total' , total)

#         # for j in range(1,len(op.split())):
#         #     sum =int(sum) +int(op_list[j])
#         #     print (sum)
#         #         #   list(map(int, 1:split()[:n]))
#     #   sum = int(sum) + int(op_list[i])
#     #   print('n')
#     #elif op_list[0] =='sub':
#         # first_number = int(op_list[1])
#         # second_number = int (op_list[2])
#         # print(first_number - second_number)
#     # elif op_list[0] =='multiply':
#     #     for j in range(1,len(op.split())):
#     #       sum =int(sum) * int(op_list[j])
#     #     print (sum)
#         # first_number = int(op_list[1])
#         # second_number = int (op_list[2])
#         # print(first_number * second_number)
#     #elif op_list[0] =='div':
#         # first_number = int(op_list[1])
#         # second_number = int (op_list[2])
#         # print(first_number % second_number) 


# factorial
# n = int(input("enter any number"))
# fact = 1
# for i in range(1,n+1) :
#     fact = fact * i 
# print(fact)      
#  palandrome
# n = input("enter any string:")
# if n[ : : ] == n [-1: :-1] :
#     print ("it is a plandrome")
# else:
#     print ("it is not a palandrome")    
n = int(input("how many cases are their:"))
p =''
for i in range(n):
    m =int(input ("please enter any number"))
    str=chr(m)
    p = str + p
print (p)










