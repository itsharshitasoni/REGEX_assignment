


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
# n = int(input("how many cases are their:"))
# p =''
# for i in range(n):
#     m =int(input ("please enter any number"))
#     str=chr(m)
#     p = str + p
# print (p)
 
# for i in range(3):
#     p = int(0)
#     q = int(0)
#     r = int(0)
#     s = int(0)
#     psd = input("Enter a password ")
    
    # if len(psd) > 0 and len(psd) <= 16:
            
    #     for j in range(0,len(psd)):
                
    #         if ord(psd[j]) >= 48 and ord(psd[j]) <= 57:
    #             p = int(1)  # numbers
    #         if ord(psd[j]) >= 65 and ord(psd[j]) <= 90:
    #             q = int(1)  # Capital Alphabets
    #         if ord(psd[j]) >= 97 and ord(psd[j]) <= 122:
    #             r = int(1)  # small alphabets
    #         if ord(psd[j]) >= 33 and ord(psd[j]) <= 47 or ord(psd[j])  == 64 :
    #             s = int(1)   # special symbols
    # print (p,q,r,s)
    # if p == 1 and q == 1 and r == 1 and s == 1:
    #     print('valid password')
    #     break
    # else:
    #     continue

# n = input("enter any string")
# m = n.lower()

# dist ={}
# for i in m:
#     if i in dist:
#         dist[i] += 1 
#     else:
#       dist[i] = 1     
# print(dist)


# from setuptools import Command


# m=[]
# while True:
#     command = input ()
#     op, value = Command.split()
#     if command[1] == 'stop':
#         break
#     elif command == 'push':
#         lst= m.append(n)
# print(n)

# m={}
# while True:
#     inp=input("enter any string")
#     if inp == 'stop':
#          break
#     else:
#         inp =inp.split
#         m[0] =='m'
# table function                                                                                                            
# n= int(input("enter any number"))
# def table(n):
#     for i in range(1,11):
#         print (n*i)
# output=table(n)

# list=['1','2','3']
# def hh (list):
#     print(list)
# out=hh(list)        

# n=input("enter any string")
# def harsh(n):
#  for i in n:
#     if i ==i.upper():
#         return("true")
#     else:
#         return("False")  
#         break
# out= harsh(n)
# print(out)        

# n = input("enter any string")
# def ordo (n):
#     sum=0
#     for i in n:
#     #i =i.split(' : :1')
#       sum+= ord(i)
#     return sum
# print(ordo (n))

# def hh (input_string):
#     return sum(map(ord , input_string))
#  
# username=input("enter the username")
# password = input ("enter the password")
# def generate (username ,password):
#   str1= username[0:4] + password[-4:]
#   print(str1)
# generate(username,password)

# n = input("enter any string")
# def fun (n):
#     total=0
#     for i in range(len(n)-1):
#         if ord(n[i]) +1 == ord(n[i+1]):
#             total +=1
#     return total
# print(fun (n))           
 
    
lst=[1,3,100,9,1120]
def p (lst):
    for i in lst:
        if (i% 2==0):
            print(i)
        else:
            print("no")
p(lst)

         






