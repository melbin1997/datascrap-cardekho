import pickle
a=pickle.load(open("output.p","rb"))
b=pickle.load(open("id.p","rb"))

print b.values()

ip=raw_input("Enter the name of the car: ")


for key in a:
	if(b[key]==ip):
		k=key
		break
print k
print a[k]