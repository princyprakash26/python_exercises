# does a string contain a sublist:

def isSublist(larger,smaller):

    for i in range(len(larger)+1):
        if smaller[i] in larger:
            return True
        elif smaller[i] is not larger:
            return False

largerlist=[1,2,3,4,5,6,7]
smallerlist=[5]

print(isSublist(largerlist,smallerlist))
smallerlist=[8]

print(isSublist(largerlist,smallerlist))
