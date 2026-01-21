#listttttt
# it is smae like array but advanced version ,, for example
# l1 = [1,3,43, "anish"] , you can add string , intiger together in a same fucking list

l1 = [1,3,43, "anish"]
print(type(l1))
print(l1)
#strings are mutable , you cannot change the string value (for all cases)
#but here inside the list you can modify anything

l1.remove("anish")
print(l1)

print(l1.count(3)) #count
#operations
l2=[442,23,55,23,1]
print(l2)
l2.sort()
print(l2)
l2.append(452)
print(l2)
l2.pop(1)
print(l2)
l2.extend([43,1,778,521])
print(l2)
l1[0]="Anish" #you can replace elements like this
print(l1)