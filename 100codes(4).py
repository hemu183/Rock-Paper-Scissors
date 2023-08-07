# 19.
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# 21.
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")

# 23.
# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("yes")
# else:
#     print("no")

# 26.
# n=input()
# sum=0
# for i in n:
#     sum+=int(i)
# if int(n)%sum==0:
#     print("is a harshad number")
# else:
#     ("not a harshad number")

# 27.
# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# print(sum)
# if sum>n:
#     print("abundant number")
#     print("abundance is",sum-n)
# else:
#     print("no")

# 29.
# n=int(input())
# sum=0
# a=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
#         print(sum)
#     for j in range(1,sum):
#         if sum%j==0:
#             a+=j
#             print(a)
# if a==n:
#     print("yes")
# else:
#     print("no")

# 32.
# n=input("enter the binary numbers")
# l1=list(n)
# l1.reverse()
# sum=0
# print(l1)
# for i in range (len(l1)):
#     sum+=int(l1[i])*2**i
# print(sum)

# 33.
# n=input()
# l2=list(n)
# # print(l2)
# l2.reverse()
# sum=0
# for i in range(len(l2)):
#     sum+=int(l2[i])*8**i
# print(sum)

# 34.
# n=input()
# l3=list(n)
# sum=0
# l3.reverse()
# for i in range(len(l3)):
#     sum+=int(l3[i])*16**i
# print(sum)

# 35.
# n=int(input())
# l1=list()
# while n!=0:
#     r=n%2
#     l1.append(r)
#     n=n//2
# l1.reverse()
# for i in range(len(l1)):
#     print(l1[i],end="")

# 36.
# n=int(input())
# l1=list()
# while n!=0:
#     r=n%8
#     l1.append(r)
#     n=n//8
# l1.reverse()
# for i in range(len(l1)):
#     print(l1[i],end="")

# 37.
# n=int(input())
# l2=list()
# while n!=0:
#     r=n%16
#     if r<10:
#         l2.append(chr(r+48))
#         print(r+48)
#     else:
#         l2.append(chr(r+55))
#     n=n//16
# l2.reverse()
# for i in range(len(l2)):
#     print(l2[i],end="")

# 40.
# x,y=input("enter the numbers").split()
# x,y=int(x),int(y)
# if x>0 and y>0:
#     print("1st Q")
# elif x<0 and y>0:
#     print("2nd Q")
# elif x<0 and y<0:
#     print("3rd Q")
# elif x==0 and y==0:
#     print("orign")
# elif x>0 and y<0:
#     print("4th Q")

# 42.
# n=int(input())
# print(int(n*(n-1)/2))

# 45.
# n=int(input())
# arr=[]
# for i in range(2,n):
#     flag=0
#     for j in range(2,i):
#         if i%j==0:
#             flag=1
#     if flag==0:
#         arr.append(i)
# print(arr)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if  arr[i]+arr[j]==n:
#             print(str(arr[i]))+ "and" + str(arr[j])+ 'are prime numbers when added gives' +str(n))
#             break

# 48.
# n=int(input())
# for i in range(2,n):
#     flag=0
#     for j in range(2,i):
#         if i%j==0:
#             flag=1
#     if flag==0:
#         print(i,end=" ")

# #49.
# n=int(input())
# count=0
# if n<0:
#     n=-1*n
# elif n==0:
#     count=1
# while n!=0:
#     n=n//10
#     count+=1
# print(count)

#51.
# n=int(input())
# if (n==2) and (n%4==0) or (n%100==0)and(n%400==0):
#     print("no of days is 29")
# elif n==2:
#     print("28 days")
# elif (n==3 )or (n==5 or n==7 or n==1 or n==8 or n==10 or n==12):
#     print("31 days")
# elif n==4 or n==6 or n==9 or n==11:
#     print("30 days")

import math

# 54.
# a,b,c=map(int,input().split())
# d=(b**2)-(4*a*c)
# x1=(-b)+math.sqrt(d))/2*a
# x2=(-b)-math.sqrt(d))/2*a
# if a==0:
#     print("not valid")
# elif a!=0 and d>0:
#     print("roots are real"x1,x2)
# elif a!=0 and d==0:
#     print("roots are equal"x1,x2)
# elif a!=0 and d<0:
#     print("roots are not real")

# 55.(we can use sort() or max())
# a = [10, 89, 9, 56, 4, 80, 8]
# max_element=a[0]
# for i in range(len(a)):
#     if a[i]>max_element:
#         max_element=a[i]
# print(max_element)

# 56.
# a = [10, 89, 9, 56, 4, 80, 8]
# min_element=a[1]
# for i in range(len(a)):
#     if a[i] < min_element:
#         min_element=a[i]
# print(min_element)

# 59.
# a=[1,2,3,4,5]
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
#
# print(sum)

# # 60.
# arr = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
# print(arr[::-1])

#  61.
# arr = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
# n=len(arr)
# arr.sort()
# print(arr)
# for i in range(n//2):
#     print(arr[i],end=" ")
# for j in range(n-1,n//2-1,-1):
#     print(arr[j],end=" ")

# 62.
# arr = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
# arr.sort()
# print(arr)
# n=len(arr)
# for i in range(n-1,0,-1):
#     print(arr[i],end=" ")



h='hemanth'
a=h[0:len(h)//2]
b=h[len(h)//2:len(h)]
c=b+a
print(c)