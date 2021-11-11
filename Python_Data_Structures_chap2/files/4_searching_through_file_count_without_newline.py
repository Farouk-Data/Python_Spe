fhand=open('mbox-short.txt')
count=0
for line in fhand :
    line=line.rstrip()
    #if not line.startswith('From:') :
        #continue
    if line.startswith('From') :
        count=count+1
        print(line)
print('Lines Count: ',count)
