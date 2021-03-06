# -*- coding: utf-8 -*-
"""
Boris Taratutin
Wed Nov 17 11:06:35 2010

A collection of dictionary manipulator functions
"""

def sortDict(d):   
    """ Sorts dictionary d and returns a tuple of (key arr, value_arr) """
    keys = [key for key in sorted(d, key=d.get, reverse=True)]
    vals = [d[key] for key in sorted(d, key=d.get, reverse=True)]
    return (keys, vals)
    
def getTopN(d, N=10):
    """ Gets the top N dictionary values (assuming dict has int values) """
    (keys, vals) = sortDict(d)
    return [(key, d[key]) for key in keys[:N]]
    
    
from operator import itemgetter
def sortDictGetItems(d, key=0, reverse=False):
    """ Returns a sorted version of a dictionary
    
    Args:       d:      dictionary to be sorted
                key:    whether to sort by first (0) or second (1) tuple val
                reverse:whether to reverse the sort of the results (desc.)
    Returns:    sorted: a sorted list of tuple pairs (key, val) from the dict.
    """
    # Key: a function of one argument that is used to extract a comparison key 
    #      from each list element (ie. key=str.lower)
    # Itemgetter: returns a <callable object> 
    # Alt: key=lambda x: x[key]     # 10x slower, but more elegant (no imports)
    return sorted(d.iteritems(), key=itemgetter(key), reverse=reverse) 
    
    
def _sortDictGetValues(d, reverse=False):
    """ Returns a sorted version of a dictionary
    
    Args:       d: dictionary to be sorted
    Returns:    a list of the values (no keys), in ascending order
    """
    items = d.items()
    items.sort(reverse=reverse)
    return [val for key,val in items]
    