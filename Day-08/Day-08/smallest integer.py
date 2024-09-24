# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

def A(a):
    p=set()
    for i in a:
         if i > 0:
             p.add(i)
    s=1
    while s in p:
        s += 1
    return s

a=[1,3,6,4,1,2]

print(A(a))