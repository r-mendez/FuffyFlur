file = open("data.txt")
lines = file.readlines()
print ("Employee Number\t", "Employee Name\t\t", "Hours Worked\t")
new_data = []
for i in lines:
    new_data.append(i.split())
for i in new_data:
    print(i[0][0:len(i[0])-1]+'\t'+'\t', (i[1]+' '+i[2][0:len(i[2])-1])+'\t'+'\t', i[3]+'\t')