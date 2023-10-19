import random

students=[]
for _ in range(100):
    scores= []   ## clear buffer
    for _ in range(5):
        scores += [random.randint(1,100)]
    students.append(scores)
file=open('students1.txt','w',encoding='utf-8')
file.write(str(students))
file.close()
