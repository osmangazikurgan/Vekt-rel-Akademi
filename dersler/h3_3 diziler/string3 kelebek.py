aa = "Vektörel"
for x in range(len(aa)+1):
    print(aa[:x]," "*(len(aa)+1-x),"|"," "*(len(aa)+1-x),aa[x-1::-1])

for x in range(len(aa)+1):
    print(aa[:len(aa)-x]," "*(len(aa)+1-x),"|"," "*(len(aa)+1-x),aa[:x])
