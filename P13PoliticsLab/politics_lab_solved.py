# version code d357d7b38bcc+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.

voting_data = list(open("voting_record_dump109.txt"))



## 1: (Task 1) Create Voting Dict
def create_voting_dict():
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    l=[]
    mylist= []
    d = {}
    for e in voting_data:
        splitted = e.split(" ")crat
        l.append(splitted)
    for e in l:
        spl = e[3:]
        spl = list(map(int, spl))
        d[e[0]]=spl
    return d



## 2: (Task 2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum([a*b for (a,b) in zip(voting_dict[sen_a], voting_dict[sen_b])])



## 3: (Task 3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    
    result = -1000000
    most_s = set()
    for k in voting_dict.keys():
        if k != sen:
            new_result = policy_compare(sen, k, voting_dict)
            if new_result > result:
                result = new_result
                most_s = (k, result)
    return most_s[0]



## 4: (Task 4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
    """
    result = 1000000
    least_s = set()
    for k in voting_dict.keys():
        if k != sen:
            new_result = policy_compare(sen, k, voting_dict)
            if new_result < result:
                result = new_result
                least_s = (k, result)
    return least_s[0]



## 5: (Task 5) Chafee, Santorum
most_like_chafee    = most_similar('Chafee', create_voting_dict())
least_like_santorum = least_similar('Santorum', create_voting_dict())  



## 6: (Task 6) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    result = 0
    for n in sen_set:
        new_result = policy_compare(sen, n, voting_dict)
        result += new_result
    return result / len(sen_set)


def dems(voting_dict):
    l=[]
    dems = []
    for e in voting_data:
        splitted = e.split(" ")
        l.append(splitted)
    for e in l:
        if e[1]=='D':
            dems.append(e)
    return dems

def create_voting_dict_dems():
    l=[]
    mylist= []
    d = {}
    for e in dems(voting_data):
        spl = e[3:]
        spl = list(map(int, spl))
        d[e[0]]=spl
    return d

def sen_set_dems(voting_dict):
    dem_set = set()
    for key in voting_dict:
        dem_set.add(key)
    return dem_set

def most_average(sen_set, voting_dict):
    most_avg = -1000000
    for e in sen_set:
        new_avg = find_average_similarity(e, sen_set, voting_dict)
        if most_avg < new_avg:
            most_avg = new_avg
    return (most_avg, e)
        

most_average_Democrat = 'Kerry' # give the last name (or code that computes the last name)



## 7: (Task 7) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    l=[]
    for e in sen_set:
        voting_recs = voting_dict[e]
        l.extend([voting_recs])
    return [sum([el[i] for el in l])/len(sen_set) for i in range(len(l[0]))]

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814,
                           0.9767441860465116, -0.13953488372093023, -0.9534883720930233,
                           0.813953488372093, 0.9767441860465116, 0.9767441860465116,
                           0.9069767441860465, 0.7674418604651163, 0.6744186046511628,
                           0.9767441860465116, -0.5116279069767442, 0.9302325581395349,
                           0.9534883720930233, 0.9767441860465116, -0.3953488372093023,
                           0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233,
                           -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512,
                           0.9767441860465116, 0.8604651162790697, 0.9767441860465116,
                           0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256,
                           0.9767441860465116, -0.4883720930232558, 0.23255813953488372,
                           0.8837209302325582, 0.4418604651162791, 0.9069767441860465,
                           -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]



## 8: (Task 8) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
        True
    """
    result = 1000000
    most_s = set()
    for key in voting_dict:
        for n in voting_dict:
            new_result = policy_compare(key, n, voting_dict)
            if new_result < result:
                result = new_result
                most_s = (key, n)
    return most_s

