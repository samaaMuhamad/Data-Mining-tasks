import pandas as pd
import itertools

data = pd.read_csv('retail_dataset.csv')

minimum_support_ = float(input ("Enter minimum_support :"))*315
minimum_confidence_decimal = float(input ("Enter minimum_confi :"))*100

records = []
for row in range(0, 315):  #hanakhod el data n7otaha fel records
    records.append([str(data.values[row,col]) for col in range(1, 8)] )

print(records)
items = sorted([item for sublist in records for item in sublist if item != 'nan'])
#print(items)  items de feha kol el data wara b3d w bel trteeb w shelt ay nan


def sublist(list1, list2):   #de bttcheck lw el list1 de gwa list2
    return set(list1) <= set(list2)
    
def check_if_subset_is_frequent (itemset, l, n):  #de btshof lw el subset kolhom frequent 
    if n>1:    
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
        
        
    for i in subsets:  #lw kol combination tl3naha kanet frequent hatrg3 true lw laa hatrg3 false
        if not i in l:
            return False
    return True


def getList_1 (items, minimum_support_): #de b2a hanakhod kol item w n3eddo w n7oto fe c1 
    c1 = {i:items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_:
           l1[key] = value 
    
    return c1, l1

def getList_2(l1, records, minimum_support_):
    l1 = sorted(list(l1.keys()))  #hena bageeb el l1 keys bas
    List1 = list(itertools.combinations(l1, 2))   #de btgeeb kol el combinations el etnenat m3 b3d
    c2 = {}
    l2 = {}
    for i in List1: #ha3dy 3la kol wa7ed gwa List1 w a7seb el count bta3o lw hoa gwa records
        count = 0
        for j in records:
            if sublist(i, j):
                count+=1
        c2[i] = count #b3d ma a7sebo a7oto fel c2
    for key, value in c2.items():
        if value >= minimum_support_:
            if check_if_subset_is_frequent (key, l1, 1):  #de b2a by3mel check lw heya 
                l2[key] = value  #asln el subset bt3ha gwa el list ely ablaha
    
    return c2, l2
    
def getList_3(l2, records, minimum_support_):
    l2 = list(l2.keys())
    List2 = sorted(list(set([item for t in l2 for item in t])))
    List2 = list(itertools.combinations(List2, 3))
    c3 = {}
    l3 = {}
    for i in List2:
        count = 0
        for j in records:
            if sublist(i,j):
                count+=1
        c3[i] = count
    for key, value in c3.items():
        if value >= minimum_support_:
            if check_if_subset_is_frequent (key, l2, 2):
                l3[key] = value 
        
    return c3, l3

def getList_4 (l3, records, minimum_support_):
    l3 = list(l3.keys())
    List3 = sorted(list(set([item for t in l3 for item in t])))
    List3 = list(itertools.combinations(List3, 4))
    c4 = {}
    l4 = {}
    for i in List3:
        count = 0
        for j in records:
            if sublist(i, j):
                count+=1
        c4[i] = count
    for key, value in c4.items():
        if value >= minimum_support_:
            if check_if_subset_is_frequent (key, l3, 3):
                l4[key] = value 
        
    return c4, l4

def getList_5(l4, records, minimum_support_):
    l4 = list(l4.keys())
    List4 = sorted(list(set([item for t in l4 for item in t])))
    List4 = list(itertools.combinations(List4, 5))
    c5 = {}
    l5 = {}
    for i in List4:
        count = 0
        for j in records:
            if sublist(i, j):
                count+=1
        c5[i] = count
    for key, value in c5.items():
        if value >= minimum_support_:
            if check_if_subset_is_frequent (key, l4, 4):
                l5[key] = value 
        
    return c5, l5

c1, l1 = getList_1 (items, minimum_support_)
c2, l2 = getList_2(l1, records, minimum_support_)
c3, l3 = getList_3(l2, records, minimum_support_)
c4, l4 = getList_4 (l3, records, minimum_support_)
c5, l5 = getList_5(l4, records, minimum_support_)
print("L1 ===> ", l1)
print("L2 ===> ", l2)
print("L3 ===> ", l3)
print("L4 ===> ", l4)
print("L5 ===> ", l5)

itemlist = {**l1, **l2, **l3, **l4, **l5}

def support_count(itemset, itemlist):
    if len(itemset)==1:   # ('milk',) fa han7welha tb2a item wa7ed bas 
        itemset=itemset[0]
    return itemlist[itemset]


#####################################################
sets = []
for i1 in list(l2.keys()):
    subsets = list(itertools.combinations(i1, 1))
    #print(subsets)
    sets.append(subsets)
#print(sets)

list_l2 = list(l2.keys())
print("\n\n\n-------Strong association Rules are:------\n")
for i in range(0, len(list_l2)):
    for j in sets[i]:
        a = j
        b = set(list_l2[i]) - set(j)   #msln listl2[i] de feha (bagel w bread) enama set(j) feha bagel bas, fa bytr7 de mn el so3'yr
        #print(set(list_l2[i]),set(j) )
        confidence = (support_count(list_l2[i], itemlist)/support_count(j, itemlist))*100
        support=(support_count(list_l2[i], itemlist)/315)*100
        if confidence>= minimum_confidence_decimal:
            print("\n Rule:{}->{} ".format(a,b))
            print("    Support{}->{} = ".format(a,b), support)
            print("    Confidence{}->{} = ".format(a,b), confidence)
        
        
##################################################################

sets = []
for i1 in list(l3.keys()):
    subsets = list(itertools.combinations(i1, 2))
    subsets += list(itertools.combinations(i1, 1))
    sets.append(subsets)

list_l3 = list(l3.keys())
for i in range(0, len(list_l3)):
    for j in sets[i]:
        a = j
        b = set(list_l3[i]) - set(j)  #hena listl3[i] heya {'Cheese', 'Meat', 'Eggs'} wel set(j) da {'Cheese'} 
        #print(set(list_l3[i]),set(j) )  haytr7 el etnen mn b3d
        confidence = (support_count(list_l3[i], itemlist)/support_count(j, itemlist))*100
        support=(support_count(list_l3[i], itemlist)/315)*100
        if confidence>= minimum_confidence_decimal:
            print("\n Rule:{}->{} ".format(a,b))
            print("    Support{}->{} = ".format(a,b), support)
            print("    Confidence{}->{} = ".format(a,b), confidence)
            
#######################################################################
sets=[]
for i1 in list(l4.keys()):
    subsets = list(itertools.combinations(i1, 3))
    subsets += list(itertools.combinations(i1, 2))
    subsets += list(itertools.combinations(i1, 1))
    sets.append(subsets)
    
list_l4 = list(l4.keys())

for i in range(0, len(list_l4)):
    for iter1 in sets[i]:
        a = j
        b = set(list_l4[i]) - set(j)
        confidence = (support_count(list_l4[i], itemlist)/support_count(j, itemlist))*100
        support=(support_count(list_l4[i], itemlist)/315)*100
        if confidence>= minimum_confidence_decimal:
            print("\n Rule:{}->{} ".format(a,b))
            print("    Support{}->{} = ".format(a,b), support)
            print("    Confidence{}->{} = ".format(a,b), confidence)
            

####################################################################
sets = []
for i1 in list(l5.keys()):
    subsets = list(itertools.combinations(i1, 4))
    subsets = list(itertools.combinations(i1, 3))
    subsets += list(itertools.combinations(i1, 2))
    subsets += list(itertools.combinations(i1, 1))
    sets.append(subsets)

list_l5 = list(l5.keys())
for i in range(0, len(list_l5)):
    for iter1 in sets[i]:
        a = j
        b = set(list_l5[i]) - set(j)
        confidence = (support_count(list_l5[i], itemlist)/support_count(j, itemlist))*100
        support=(support_count(list_l5[i], itemlist)/315)*100
        if confidence>= minimum_confidence_decimal:
            print("\n Rule:{}->{} ".format(a,b))
            print("    Support{}->{} = ".format(a,b), support)
            print("    Confidence{}->{} = ".format(a,b), confidence)
