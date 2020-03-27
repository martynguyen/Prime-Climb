"""
APPLYDIE FUNCTION
input: iP1 -- a list of positions
       die -- a single int value from 0 to 9 (n-1)
       curse -- a boolean keeping track of whether the player is currently cursed

output: iP2 -- list of all possible positions generated by applying a single die to
                the positions in iP1.

Note: (1) Due to the rules of Prime Climb, no pawns can leave position 101.
      (2) This function makes use of the function cleanPositions

@author: David A. Nash
"""

def applyDie(iP1,die,curse):
    if die==0: ##A roll of zero corresponds to the value 10
        die=10
    iP2 = np.array([]) ##initialize new array of possible positions
    if iP1[0,0]==101:  ##do not allow movement away from position 101
        print("You already won... No need to keep rolling.")  ##for debugging only
    else:
        ##when cursed, you can only subtract or divide
        iP2 = np.append(iP2, iP1-(die,0,0))
        iP2 = np.append(iP2, iP1/(die,1,1))
        ##if not cursed, you can also add or multiply
        if curse==False:  
            iP2 = np.append(iP2, iP1+(die,0,0))
            iP2 = np.append(iP2, iP1*(die,1,1))
        ##do not allow movement away from position 101 in the second position either
        if iP1[0,1]!=101: 
            ##when cursed, you can only subtract or divide
            iP2 = np.append(iP2, iP1-(0,die,0))
            iP2 = np.append(iP2, iP1/(1,die,1))
            ##if not cursed, you can also add or multiply
            if curse==False:  
                iP2 = np.append(iP2, iP1+(0,die,0))
                iP2 = np.append(iP2, iP1*(1,die,1))
        num = np.int(iP2.shape[0]/3)  ##count the number of new positions (represented as triples)
        ##reshape to a list of triples
        iP2 = iP2.reshape((num,3))
        #sort, eliminate duplicates and unallowable positions
        iP2 = cleanPositions(iP2) 
    return iP2
