def tower(n , a, b, c):
    if n == 1:
        print ("Move disk 1 from source",a,"to destination",c)
    else:
        tower(n-1, a, c, b)
        print ("Move disk",n,"from source",a,"to destination",c)
        tower(n-1, b, a, c)
n = int(input("Write the number of disks:"))
tower(n,'A','B','C')