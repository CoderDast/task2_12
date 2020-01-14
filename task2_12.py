word = input('Type a word: ') 
f1 = word.find('f') 
f2 = word.rfind('f') 
if f1 == f2 == -1:
    pass
elif f1 == f2:
    print (f1)
else:
    print(f1)
    print(f2)