def Recursion(n):  # defining the function
    if n < 1:
        print("n is lesser than value 1")
    else:
        Recursion(n-1)
        print(n)


Recursion(5)

# As n = 5 , It would go through else , then Recusrion parameter is reduced by 1 ,
# it would print print if statement first at it would go thrugh else

# The output of Recursion :

# n is lesser than value 1
# 1
# 2
# 3
# 4
# 5
