f = open('nameslist.txt')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
print("--------------------------")
print(lines[5-1])

f = open('nameslist.txt')
line = f.read(5)
print(line)
f.close()


count1 = 0
count2 = 0
count3 = 0
f = open('nameslist.txt','r')
lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    if line == "Darth":
       count1 += 1
    elif line =="Luke":
       count2 += 1
    else:
        if line == "Lea":
            count3 += 1
print("Number of Darth =",count1 )
print("Number of Luke =",count2 )
print("Number of Lea =",count3 )

f.close()

# OR
# counts = {
#     'Lea' : 0,
#     'Luke' : 0,
#     'Darth' : 0
# }
# for line in lines:
#     line = line.replace('\n','')
#     if (line == 'Lea'):
#         counts['lea'] += 1


f = open('nameslist.txt','a')
f.write('\nLaelae')
f.close()
