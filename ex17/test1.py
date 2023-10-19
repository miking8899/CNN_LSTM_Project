import csv
f = open('新北市食品工廠清冊.csv','r',encoding='utf-8')
rows = csv.reader(f)
list1 = list(rows)
firstColumn = [item[0] for item in list1]
for item in firstColumn: print(item)
f.close()
