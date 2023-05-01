Name = input("Enter name : ")
Family = input("Enter family : ")

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
Average=(sub1+sub2+sub3)/3

if Average>=86 and Average<=100:
    print(Name, Family, Average, "Your Grade is A")
elif Average>=71 and Average<86:
    print(Name, Family, Average, "Your Grade is B")
elif Average>=51 and Average<71:
    print(Name, Family, Average, "Your Grade is C")
