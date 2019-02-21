def LD(s1, s2):
    m = []
    for i in range(0, len(s1)):
        m[i][0] = i
    
    for j in range(0, len(s2)):
        m[0][j] = j
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            
            if(s1[i] == s2[j]):
                m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1])
            
            else:
                m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1]+!)

    return m[len(s1)][len(s2)]


    if __name__ == "__main__":
        s1 = "Snow"
        s2 = "Slow"

        print(LD(s1, s2))

        

