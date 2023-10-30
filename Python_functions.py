nlist=["Pardhu","P Vamsi","Roopak","Pavan","Naren"]
print(len(nlist))
nlist.append("Sruthi")
print("Added sruthi to last")
print(nlist)
nlist.insert(6,"Ratnesh")
nlist.pop(1)
print(nlist)
nlist.remove("Naren")
print(nlist)
print(nlist.reverse())
rlist=[46,48,49,47,51,50,53]
rlist.sort()
print(rlist)
rlist.sort(reverse=True)
print(rlist)
gen=rlist
print(gen)
nlist=list(rlist)
print(nlist)
b=rlist.copy()
print(b)
nlist.clear()
del nlist
