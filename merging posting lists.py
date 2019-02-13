

def intersect(p1, p2):

    answer = []
    i = 0
    j = 0

    while (i<(len(p1)) and j < (len(p2))):

        if(p1[i] == p2[j]):
            answer.append(p1[i])
            i = i+1
            j = j+1
        
        elif (p1[i] < p2[j]):
            i = i+1
        
        else:
            j = j + 1

    return answer


if __name__ == "__main__":

    p1 = [1,2,4,11,31,45,173,174]
    p2 = [2,31,54,101]

    merged = intersect(p1, p2)

    print(merged)

    

