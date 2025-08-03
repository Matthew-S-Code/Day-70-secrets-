import os

normU = my_secret = os.environ['normal_user']
normP = os.environ['Normal_pass']

adminU = my_secret = os.environ['admin_user']
adminP = os.environ['Admin_pass']

user = input("Enter your username:\t")
password = input("Enter your password:\t")

if password == normP and user == normU:
  print("Hello normie")
elif password == adminP and user == adminU:
  print("Hello admin")
else:
  print("incorrect ")
