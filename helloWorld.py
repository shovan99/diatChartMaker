print("Press 1 for you , Press 2 for mom and Press 3 for dad")
def getDate():
    import datetime
    return datetime.datetime.now()
try:
        firstInput=int(input())
        if firstInput==1:
            print("Write here about your diat plans!!")
            f=open('you.txt','a')
            shovanInput=input()
            f.write(shovanInput)
            f.close()
            f1 = open('you.TXT')
            for lines in f1:
                print(lines , end="")
            time=getDate()
            print("\n",time)
        if firstInput==2:
            print("Write here about your mom's diat plans!!")
            f=open('mom.txt','a')
            momInput=input()
            f.write(momInput)
            f.close()
            f1 = open('mom.TXT')
            for lines in f1:
                print(lines , end="")
            time=getDate()
            print("\n",time)
        if firstInput==3:
            print("Write here about your dad's diat plans!!")
            f=open('dad.txt','a')
            dadInput=input()
            f.write(dadInput)
            f.close()
            f1 = open('dad.TXT')
            for lines in f1:
                print(lines , end="")
            time=getDate()
            print("\n",time)

except Exception as e:
  print(e,"\ncheck the process carefully.")