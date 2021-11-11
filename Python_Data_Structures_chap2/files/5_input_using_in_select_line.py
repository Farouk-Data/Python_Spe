try :
    fname=input('Enter name of file: \n')
    fhand=open(fname)
except :
    print('File Not Found')
    quit()

count=0
for line in fhand :
    line=line.rstrip()
    #if not line.find('@uct.ac.za') == -1 :
    #continue
    if '@uct.ac.za' in line :
        print(line)
        count=count+1
print('Line_Count =',count)


#              ------------------------
#for line in fhand :
#    line=line.rstrip()
    #if not '@uct.ac.za' in line :
#    if line.find('@uct.ac.za') == -1 :
#        continue
#    print(line)
#    count=count+1
#print('Line Count=',count)
