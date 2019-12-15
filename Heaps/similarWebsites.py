"""
Given a list of (website, user) pairs that represent users visiting websites. 
come up with a program that identifies the top k pairs of websites with the 
greatest similarity 
"""
from collections import defaultdict
def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])


def top_pairs(log, k):
    visitors = defaultdict(set) #this is a dictionsionary where the key is a imutable object and the value is a set

    for site, user in log:
        visitors[site].add(user)