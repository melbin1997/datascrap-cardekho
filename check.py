import pickle
a=pickle.load(open("output.p","rb"))
print a[raw_input("Enter the name of the vehicle: ")]