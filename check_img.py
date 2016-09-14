import pickle

a=pickle.load(open("images_found.p","rb"))

'''key=raw_input("Enter the name of the car: ")

print
print key
print a[key]
print 
print len(a)'''

for i in a:
	print
	print i
	print a[i]
	print
	print "Links containing the photos of",len(a),"cars available"