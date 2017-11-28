height=float(input("your height"))
weight=float(input("your weight"))
bmi=weight/(height*height)
if bmi<=18.5:
    print("体重过轻")
elif bmi<=25:
    print("体重正常")
elif bmi<=28:
    print("体重过重")
elif bmi<=32:
    print("体重肥胖")
else:
    print("严重肥胖")