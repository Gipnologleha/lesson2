shkola = [

{'class1' : '4a', 'score' : [5,4,4,5,4,3]},
{'class2' : '6b', 'score' : [4,5,3,2,2,5,4,3]},
{'class3' : '6c', 'score': [4,5,3,2,2,5,4,3,1,1,2,3]},
]


z = len ('scores1') + len ('scores2')+ len ('scores3')
print (z)

print (shkola [0] ['score'] [4]) 

a = (shkola [0] ['score'])

print(a)
print(type(a[2]))

summa1 = 0
for i in a:
    if i in a:
        summa1 += int(i)
print (summa1)

b = (shkola [1] ['score'])
c = (shkola [2] ['score'])

summa2 = 0
for q in b:
    if q in b:
        summa2 += int(q)
print (summa2)

summa3 = 0
for w in c:
    if w in c:
        summa3 += int(i)
print (summa3)

print ((summa1 + summa2 + summa3)/z)