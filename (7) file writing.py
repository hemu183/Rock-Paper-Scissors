# writing in a file
1.   #replace content in the file
"""
f=open("Hemu.txt","w")  #text mode is default
f.write("g.o.a.t")
f.close()
"""
2.
"""
f=open("Hemu.txt","a")  # do not replace the content but add the content at the end
f.write("g.o.a.t\n")
f.write("g.o.a.t\n")
f.close()
"""
3. # enni sarlu run cheste anni sarlu append avutai
"""
f=open("Hemu.txt","a")  # do not replace the content but add the content at the end
f.write("g.o.a.t\n")
f.close()
"""
4. # to the no of characters are written
"""
f=open("Hemu.txt","a")
f.write("g.o.a.t\n")
# print(a)
f.close()
"""
5. # read and write 
f=open("Hemu.txt","r+")
h=f.read()
print(h)
f.write("i.e ronaldo")
f.close()

