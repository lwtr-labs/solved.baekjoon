def solution(myString, pat):

    
    len_pat = len(pat)
    len_myString = len(myString)
    
    if len_pat > len_myString:
        return 0
    
    myString = myString.lower()
    pat = pat.lower()    
    
    for i in range(len_myString - len_pat + 1):
        if myString[i:i+len_pat] == pat:
            return 1
        
    return 0