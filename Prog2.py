print ('Print your name : ')
name = input()
print ('What is your age ? : ')
age = int(input())
if name == 'Alice' :
    print ('Hi !! Alice')
elif age < 12 :
    print ('You are not Alice !! Kiddo')
elif age > 100 and age < 200:
    print ('You are not Alice !! Grannie')
elif age > 200 and age < 2000 :
    print ('Unlike you, Alice is not an immortal Vampire')
else:
    print ('Fuck You Stranger')
