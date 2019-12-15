"""
Given a list of (website, user) pairs that represent users visiting websites. 
come up with a program that identifies the top k pairs of websites with the 
greatest similarity 
"""
from collections import defaultdict
import heapq
def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])


def top_pairs(log, k):
    visitors = defaultdict(set) #this is a dictionsionary where the key is a imutable object and the value is a set

    for site, user in log:
        visitors[site].add(user)
    pairs = []
    sites = list(visitors.keys())

    for  _ in range(k):
        heapq.heappush(pairs,(0,('','')))
    for i in range(len(sites)-1):
        for j in range(i+1, len(sites)):
            score = compute_similarity(sites[i],sites[j],visitors)
            heapq.heappushpop(pairs,(score, (sites[i],sites[j])))
    return [pair[1] for pair in pairs]