# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## Task 1
minutes_in_week = 7*24*60

## Task 2
remainder_without_mod = (2304811/47 - 2304811//47) *47

## Task 3
divisible_by_3 = (673+909)%3 == 0

## Task 4
x = -9
y = 1/2
statement_val = 1.0

## Task 5
first_five_squares = {x*x for x in {1,2,3,4,5}}

## Task 6
first_five_pows_two = {2**x for x in {0,1,2,3,4}}

## Task 7: enter in the two new sets
X1 = {2,7,11}
Y1 = {1,3,5}

## Task 8: enter in the two new sets
X2 = {0,2,1}
Y2 = {5,10,20}

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {x+1 for x in range(-1,len(digits)**3-1)}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {x for x in S for y in T if x==y}

## Task 11
L_average = sum([20,10,15,75])/len([20,10,15,75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum({sum(LofL[x]) for x in range(len(LofL))})

## Task 13
cartesian_product =[[x,y] for x in ["A", "B", "C"] for y in [1,2,3]]
# use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) !=(0,0,0)]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 and (i,j,k) !=(0,0,0)][0]

<<<<<<< HEAD
## Task 17
L1 = [1,1,2,3] # <-- want len(L1) != len(list(set(L1)))
L2 = [3,1,2] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))
=======
## 14: (Task 14) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 and not i==j==k==0]



## 15: (Task 15) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 and not i==j==k==0]



## 16: (Task 16) List and set differ
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))
example_L = [1,1,2,2]



## 17: (Task 17) Odd numbers
# Replace {...} with a one-line set comprehension over a range of the form range(n)
odd_num_list_range = {x for x in range(100) if x % 2 == 1}

>>>>>>> origin/master

## Task 18
odd_num_list_range = set(x for x in range(1,100,2))

<<<<<<< HEAD
## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))
=======
## 18: (Task 18) Using range and zip
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
L = ['A','B','C','D','E']
range_and_zip = list(zip([x for x in range(5)],L))
>>>>>>> origin/master

## Task 20
list_sum_zip = [x+y for x,y in zip([10,25,40],[1,15,20])]

<<<<<<< HEAD
## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dlist[i][k] for i in range(len(dlist))]
=======

## 19: (Task 19) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
list_sum_zip = [x+y for (x,y) in zip([10,25,40],[1,15,20])]



## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']
value_list = [x[k] for x in dlist]
>>>>>>> origin/master

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
<<<<<<< HEAD
value_list_modified_1 = [dlist[i][k] if k in dlist[i] else 'NOT PRESENT' for i in range(len(dlist))]# <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [dlist[i][k] if k in dlist[i] else 'NOT PRESENT' for i in range(len(dlist))] # <-- as you do here
=======
#Replace [...] with a one-line comprehension 
value_list_modified_1 = [ks[k] if k in ks else 'NOT PRESENT' for ks in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [ks[k] if k in ks else 'NOT PRESENT' for ks in dlist] # <-- as you do here

>>>>>>> origin/master

## Task 23
square_dict = {k:k*k for k in range(100)}

<<<<<<< HEAD
## Task 24
D = {'red','white','blue'}
identity_dict = {list(D)[i]:list(D)[i] for i in range(len(D))}
=======
## 22: (Task 22) A dictionary mapping integers to their squares
# Replace {...} with a one-line dictionary comprehension
square_dict = {k:k**2 for k in list(range(100)) }



## 23: (Task 23) Making the identity function
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension
identity_dict = {list(D)[i]:list(D)[i] for i in range(len(D))}

>>>>>>> origin/master

## Task 25
base = 10
<<<<<<< HEAD
digits = set(range(10))
representation_dict = {(x+1):[((((x+1)//base)//base)%base),(((x+1)//base)%base), ((x+1)%base)] for x in range(-1,len(digits)**3-1)}
=======
digits = set(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variables 'base' and 'digits' so it will work correctly if these
# are assigned different values (e.g. base = 2 and digits = {0,1})
representation_dict = { x:(x//base**2,x%(base**2)//base,x%(base**2)%base) for x in range(1000)}

>>>>>>> origin/master

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
<<<<<<< HEAD
listdict2dict = {k:v for (k,v) in zip(list(filter(None, names)), d.values())}

## Task 27
def nextInts(L): return [l+1 for l in L]
=======
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
listdict2dict = {k:v for (k,v) in zip(list(filter(None, names)), id2salary.values())}



## 26: (Task 26) Procedure nextInts
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def nextInts(L): return [l+1 for l in L]



## 27: (Task 27) Procedure cubes
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def cubes(L): return [l**3 for l in L]



## 28: (Task 28) Procedure dict2list
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def dict2list(dct, keylist): return  [dct[k] for k in keylist]
>>>>>>> origin/master

## Task 28
def cubes(L): return [l**3 for l in L]

## Task 29
def dict2list(dct, keylist): return  [dct[k] for k in keylist]

<<<<<<< HEAD
## Task 30 
=======
## 29: (Task 29) Procedure list2dict
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
>>>>>>> origin/master
def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist, L)} 

