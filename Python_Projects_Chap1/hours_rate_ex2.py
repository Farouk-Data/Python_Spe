#Convert hours and rate
try :
    fh = float(input('Enter Hours: '))
except :
    print('Error, try again')
    quit()
try :
    fr = float(input('Enter Rate: '))
except :
    print('Error, try again')
    quit()
#    fh = -1
#    fr = -1

#conditions for hours
#if fh < 0 :
    #print('Error Entry')
#elif fr < 0 :
#    print('Error Entry')
if fh > 40 :
     #calculating the overpay
     reg = fh * fr
     p1=float(fh-40)*float(fr*0.5)
     xp=reg+p1
     print('the regular is=',reg)
     print('the overpay is=',p1)

else :
     xp=fh*fr

print('Pay=',xp)
