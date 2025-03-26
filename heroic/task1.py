
name=input("enter your name")
age=int(input("enter your age"))
def check(Name,Age):
    if Age>=20 :
        print(Name, "is adult" )
    elif Age>=10 and Age<=20 :
        print(Name,"is tenager") 
    else:
        print(Name,"is child")      