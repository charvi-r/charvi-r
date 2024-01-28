print('two numbers below:')
a=int(input('enter first number:'))
b=int(input('enter seecond number:'))
ch=0
while ch<5:
    print('calculator menu')
    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.divde')
    print('5.exit')
    ch=int(input('enter your choice:'))
    if ch==1:
         c=a+b
          print('sum:',c)
    elif ch==2:
          c=a-b
          print('diffrence:',c)
    elif ch==3:
          c=a*b
          print('product:',c)
    elif ch==4:
         try:
          c=a/b
          print('quotient:',c)
         except: 
          print('Error occured while dividing the given number')
             
          
    elif ch==5:
         exit
    else:
        print('INVALID CHOICE') 

        
