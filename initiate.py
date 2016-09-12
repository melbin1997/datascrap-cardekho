import pickle
a={1:2}
pickle.dump(a,open("output.p","wb"))
b=pickle.load(open("output.p","rb"))
print b