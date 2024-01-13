names = ["Kumar", "Charith", "Keertha","Hema"] 
names1 = ["Kumar", "Charith", "Keertha","Hema"] 
print(len(names))

for i in names:
    print(i)

print (names[-1])

names.insert(2,"Bangari")
print(names)
names.append("Charith Bnagari")
print(names)

#extend
names.extend(names1)
print(names.extend(names1))
print(names)

#remove
names.remove("Charith")
print(names)

#pop
names.pop(1)
print(names)

#del
del names [1] 
print(names)

names2 =names.copy()
print(names2)

names2.clear()
print(names2.clear())


