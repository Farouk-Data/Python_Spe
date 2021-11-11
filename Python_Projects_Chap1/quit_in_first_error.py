hours = input('Enter Hours:')
try :
    fh=float(hours)
    rate = input('Enter Rate:')
    fr=float(rate)
except :
    print('Error , Try Valide Numbers.')
    quit()
if fh > 40 :
    reg_pay=fh*fr
    ad_pay=(fh-40)*(fr*0.5)
    pay= reg_pay + ad_pay
else :
    pay=fh*fr

print('Pay=',pay)
