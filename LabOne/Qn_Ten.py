'''
10. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

t1 = float(input("enter time in seconds: "))
t2 = float(t1 / 60)
t3 = float(t1 / 3600)
t4 = float(t1 / 86400)
print(f"{t1} is equivalent to {t4} days.")
print(f"{t1} is equivalent to {t3} hours.")
print(f"{t1} is equivalent to {t2} minutes.")
