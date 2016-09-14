import pickle

a=pickle.load(open("images_found.p","rb"))

key=raw_input("Enter the name of the car: ")

print
print key
print a[key]
print