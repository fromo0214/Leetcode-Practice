import math
# https://leetcode.com/problems/koko-eating-bananas/
def minEatingBananas(piles, h):

   
    """""
    Notes:
    Coco can only eat at most 1 entire pile at a given hour
    h must be >= len(piles), because if we have 5 piles
                              [1,1,2,2,3]    h = 4
                              k = 3  she can eat[1,1,2,2] because she has 4 hours k < 1 and 2
    Example:
    [3, 6, 7, 11] h = 8, k = 1
     ^ Coco has 3 hours to eat this pile k = 3/1 = 3
     [3, 6, 7, 11]
                ^
     If k = 11, coco would be able to finish the max pile in 1 hour, meaning coco can finish every
     other pile in 1 hour, therefore the output will be 4
    
    """

    # k = bananas per hour speed, gonna be our mid for binary search algo
    
        
    l, r = 0, max(piles)

    # the result is set to r because as stated as bove if the value is high, coco
    # will be able to eat the rest of piles of bananas 
    res = r

    while l <= r:
        hrs = 0
        k = (l + r) // 2

        for pile in piles:
            hrs += math.ceil(pile / k) #here we are rounding up to divide piles to get how many hours
                                        # if there are 7/3 then it would take coco 2 hours to eat that pile 
        
        if hrs > h:
            l = k + 1
        else:
            res = min(res, k)
            r = k - 1



    return res

piles = [3,6,7,11]
h = 8
print(minEatingBananas(piles,h))




def kokoeatingbananas(piles, h):

    l, r = 1, max(piles)

    res = r
    while l <= r:
        hrs = 0
        k = (l + r) // 2
        for pile in piles:
            hrs += math.ceil(piles / k)

        if hrs > h:
            l = k + 1

        else:
            res = k
            r = k - 1

    
    return res
