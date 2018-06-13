visited=["NYC", "Miami", "Mumbai", "Los Angeles", "Dubai", "Alexandria"]
print("visited: ",visited)
wish=["Moscow", "Beijing", "Las Vegas"]
print("wish: ",wish)
all=visited+wish
print("All: ",all)
visited.extend(wish)
print("Using .extend(): ",visited)
A=[1,2,31,3,4]
B=[2,5,3,52,1]
print("A,B: ",A,B)
print("A+B: ",A+B)
A.extend(B)
print("Using .extend(): ",A)
