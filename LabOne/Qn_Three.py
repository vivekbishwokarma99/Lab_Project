'''
3. N students take K apples and distribute them among each other evenly. The remaining (the undivisible)
   part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
   The program reads the number N and K. It should print the two answers for the questions above.
'''
N = int(input("Enter the total number of students:"))
K = int(input("Enter the total number of apples in a basket"))
app = K // N
rem = K % N
print(f"Number of apples each student will get: {app}")
print(f"Number of remaining apples in a basket: {rem} ")

