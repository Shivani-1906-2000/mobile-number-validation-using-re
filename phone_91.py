import re
number=input("enter a mobile number")
match=re.search("[+91|91|0]?[9876]{1}\d{9}",number)
if match==None:
    print("Your mobile is not accepted")
else:
    print("mobile number accepted")