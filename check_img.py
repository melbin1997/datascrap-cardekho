import pickle

a=pickle.load(open("pictures.p","rb"))
for key in a:
	print key
	print a[key]
	print
	print