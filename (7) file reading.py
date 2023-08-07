# open a file, reading a file
1.
"""
f=open("Hemu.txt","rt")   # rt (i.e is taken as default)
h=f.read()
print(h)
 f.close()
"""

2.
"""
a=open("hemu.txt")
b=a.read(3)
print(b)
a.close()
"""

3.
"""
a=open("hemu.txt")
#b=a.read()             # as your reading file pointer it becomes empty
for lines in a:
    print(lines,end="")
    """
4.
'''
a=open("hemu.txt")
print(a.readline(),end="")  # print statement its self produce a new line character
print(a.readline())
'''
5.
"""
a=open("hemu.txt","rb")     # read in binary mode
b=a.read()                  # as your reading file pointer it becomes empty
for lines in b:
    print(lines,end="")
"""
6. # to store in list (i.e readlines function )
"""
a=open("hemu.txt","rt")     # read in binary mode
print(a.readlines())                 # as your reading file pointer it becomes empty
"""
