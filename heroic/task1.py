
name=input("enter your name : ")
age=int(input("enter your age   :"))
def check(Name,Age):
    if Age>=20 :
        print(Name, "is adult" )
        print(Age, "years old" )
        
    elif Age>=10 and Age<=20 :
        print(Name,"is tenager") 
        print(Age, "years old" )
    else:
        print(Name,"is child")  
        print(Age, "years old" )    
check(name,age)       