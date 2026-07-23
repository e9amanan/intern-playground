def min_window(s:str,t:str)->str:
    """from collections import counter
        target_counts=counter(t)
        min_sub=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                sub_counts=counter(sub)
                if all(sub_counts[c]>=target_counts[c] for c in target_counts):
                    if min_sub=="" or len(sub)<len(min_sub):
                        min_sub=sub
            return min_sub"""
    
    if not t or not s:
        return""
    
    target_counts={}
    for char in t:
        target_counts[char]=target_counts.get(char,0)+1

    window_counts={}
    have=0
    need=len(target_counts)

    res= (float("inf"),-1,-1)
    left=0

    for right in range(len(s)):
        char=s[right]
        window_counts[char]=window_counts.get(char,0)+1

        if char in target_counts and window_counts[char]==target_counts[char]:
            have +=1

        while have == need:
            if(right-left+1)< res[0]:
                res=(right-left+1,left,right)


            left_char=s[left]
            window_counts[left_char]-=1

            if left_char in target_counts and window_counts[left_char]<target_counts[left_char]:
                have -=1

            left +=1

    window_length,start,end=res
    if window_length!= float("inf"):
        return s[start:end+1]
    return""