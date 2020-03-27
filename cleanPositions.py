"""
CLEAN POSITIONS FUNCTION
input: iP1 -- a list of potential positions (obtained from applying dice/cards)
This function eliminates any positions which are not allowed (e.g. non-integer, or off the board)
and also deletes any duplicates

@author: David A. Nash
"""

#import numpy as np

def cleanPositions(iP1):
    iP1.sort(axis=1)  ##make sure positions are always listed in increasing order
    iP1.view('i8,i8,i8').sort(order=['f0','f1'], axis=0)  ##sort them into increasing order (lex)
    deleteRows=np.array([]) ##keep track of things to delete
    compareRow=0 ##current row we're comparing to (for repeats)
    for i in range(iP1.shape[0]):
        if (iP1[i,0] not in Spots) or (iP1[i,1] not in Spots):
            ##mark row for deletion if off the board
            deleteRows = np.append(deleteRows, i) 
        elif (compareRow!=i) and (np.array_equal(iP1[i,:], iP1[compareRow,:])):
            ##mark duplicates for deletion
            deleteRows = np.append(deleteRows, i) 
        else:
            compareRow=i  ##reassign currentRow if we run into a different allowable position
    deleteRows = deleteRows.astype(int)
    iP1 = np.delete(iP1, deleteRows, axis=0)
    return iP1