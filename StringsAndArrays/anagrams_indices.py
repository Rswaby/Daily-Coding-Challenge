from collections import Counter

def is_anagram(s1,s2):
    return Counter(s1) == Counter(s2)

def ana_indices(word, s):
    result = []

    for i in range(len(s)):
        window = s[i:len(word)]

        if is_anagram(word, window):
            result.append(i)
    
    return result

