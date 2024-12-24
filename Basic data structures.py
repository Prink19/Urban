grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
res = students.sort()
print(students)
jurnal ={keys:value for (keys, value) in zip(students, grades)}
key = input('Напишите имя ученика: ')
print(jurnal.get(key))
for i in grades:
    mid_grades=sum(i)/len(i)
    print(mid_grades)
#как посчитать среднее через sum(grades[i]) я так и не понял, надеюсь такой вариант тоже сойдет :)



