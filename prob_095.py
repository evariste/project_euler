"""The proper divisors of a number are all the divisors excluding the
number itself. For example, the proper divisors of 28 are 1, 2, 4, 7,
and 14. As the sum of these divisors is equal to 28, we call it a
perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum
of the proper divisors of 284 is 220, forming a chain of two
numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an
amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.

Ans: 14316

Part of a chain of length 28 (!)

[14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786,
294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736,
381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744,
19916, 17716]

Implementation below is probably not very efficient, takes about 1
minute on a macbook.

"""

from abcdPrimeUtils import allFactors
import numpy


N = 1000000
visited = numpy.zeros( (N+1,1), dtype=numpy.bool)

longestChain = [1]
for start in range(2,N+1):
    if visited[start]:
        continue
        
    currChain = []
    currVal = start

    while currVal <= N and not currVal in currChain:
        if visited[currVal]:
            # Joined in with an earlier chain
            break
        currChain = currChain + [currVal]
        visited[currVal] = True
        currVal = sum(list(allFactors(currVal))) - currVal

    if currVal in currChain:
        # Identify where the chain starts, there may well be a
        # sequence of numbers before the cyclic part.
        i = 0
        while not currChain[i] == currVal:
            i = i + 1
        currChain = currChain[i::]

        if len(currChain) > len(longestChain):
            longestChain = currChain

print longestChain
print min(longestChain)


"""
Chains not exceeding 1000000

    [1]
    [6]
    [28]
    [220, 284]
    [496]
    [1184, 1210]
    [2924, 2620]
    [5020, 5564]
    [14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716]
    [6232, 6368]
    [8128]
    [12496, 14288, 15472, 14536, 14264]
    [10744, 10856]
    [12285, 14595]
    [17296, 18416]
    [76084, 63020]
    [185368, 203432]
    [66928, 66992]
    [67095, 71145]
    [69615, 87633]
    [79750, 88730]
    [100485, 124155]
    [122265, 139815]
    [122368, 123152]
    [141664, 153176]
    [142310, 168730]
    [280540, 365084]
    [171856, 176336]
    [176272, 180848]
    [196724, 202444]
    [635624, 712216]
    [455344, 437456]
    [901424, 879712]
    [308620, 389924]
    [319550, 430402]
    [624184, 691256]
    [356408, 399592]
    [503056, 514736]
    [469028, 486178]
    [898216, 980984]
    [609928, 686072]
    [522405, 525915]
    [600392, 669688]
    [643336, 652664]
    [667964, 783556]
    [726104, 796696]
    [802725, 863835]

"""
