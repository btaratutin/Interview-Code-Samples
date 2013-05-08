# -*- coding: utf-8 -*-
"""
Boris Taratutin
Sep. 25, 2011

An implementation of a FIFO using a dictionary
"""


class Fifo:
    """ Implements a FIFO: "first-in, first-out" data structure """
    
    def __init__(self, items=[]):
        """ Initialize FIFO attributes """
        self.fifo = {}
        self.next_in = 0
        self.next_out = 0
        
        [self.add(item) for item in items]
        
    
    def add(self, item):
        """ Add a value to the FIFO """
        self.fifo[self.next_in] = item
        self.next_in += 1
        
    def pop(self):
        """ Get the next value out of the fifo """
        if not self.fifo: return None           # Empty fifo case

        popped = self.fifo.pop(self.next_out)
        self.next_out += 1
        
        return popped
        
    def last_in(self):
        """ Returns the last value inserted into the fifo - doesn't pop """
        if not self.fifo: return None
        
        return self.fifo[self.next_in-1]
        
    def all_values(self):
        """ Returns the values of the fifo """
        if not self.fifo: return None

        return self.fifo.values()
        
    def __iter__(self):
        """ Create a generator that enumerates all of the values in the fifo,
            in the order they would be popped (without actually popping them) """
        n_out = self.next_out
        
        while n_out < self.next_in:
            yield self.fifo[n_out]
            n_out += 1

    def __str__(self):
        """ Use the overriden iter method we defined to iterate through the
            fifo, and return each item as a string """
        return ", ".join( [str(val) for val in iter(self)] )
        
    def __nonzero__(self):
        """ Returns a boolean that says whether it's empty or not.
            Empty = False. If next_in == next_out, it's empty! """
        return not (self.next_in == self.next_out)
        
    
    def __len__(self):
        """ Returns the number of items in the fifo right now """
        return len(self.fifo.keys())
    

        
            
        
# If run from command line, will call this
if __name__ == "__main__":

	print "Running Fifo Example\n"

	to_add = [1,7,5,5,3]
	fifo =  Fifo(to_add)

	print "added ", to_add, " to FIFO"

	print "FIFO length: ", len(fifo) # Demonstrates the FIFO __len__ method
	print "FIFO last in: ", fifo.last_in()
	print "FIFO repr: ", fifo # Uses the FIFO __str__ method

	print "\niterating over vals (popping):"
	for i in iter(fifo):
		print fifo.pop()

	print "\nnew FIFO length: ", len(fifo)
	print "new FIFO last in: ", fifo.last_in()
	print "new FIFO repr: ", fifo

	print "\nFinished."
    
    
    
    
