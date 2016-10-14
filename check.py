import pickle
a=pickle.load(open("output.p","rb"))
b=[]
for i in a:
	b.append(i)
print sorted(b)
print
print a[raw_input("Enter the name of the vehicle: ")]