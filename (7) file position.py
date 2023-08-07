# file pointer acharacter position daggara vundii
1.
"""
f=open("Hemu.txt")
f.seek(2)
print(f.readline())
print(f.tell())
f.seek(3)
print(f.readline())
print(f.tell())
f.close()
"""
2.  #using with block
with open("Hemu.txt","rt")as f:
    print(f.readlines())
f=open("Hemu.txt")
print(f.readline())
f.close()