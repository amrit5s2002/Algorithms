from base import test_arrays
j = test_arrays()
print(j)
n = input("enter the element to be searched: ")
for i in j:
    if i==n:
        print(f"yes {n} is avalable at {i}th index")
    elif i==len(j)-1:
        print(f"no there is no element with value {n} is available")