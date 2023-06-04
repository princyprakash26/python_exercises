#string edit distance

def edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    cost = 0
    if str1[-1] != str2[-1]:
        cost += 1

    d1 = edit_distance(str1[:-1], str2) + 1
    d2 = edit_distance(str1, str2[:-1]) + 1
    d3 = edit_distance(str1[:-1], str2[:-1]) + cost

    return min(d1, d2, d3)

string1 = "kitten"
string2 = "sitting"
distance = edit_distance(string1, string2)
print( distance)


