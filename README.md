automata-view
=============

Scripts to convert automatons to visible png images.

Example: test.py:  

	from automataview import states_to_dot
	# for test
	class state(object):
	    # n: state num
	    # transitMap: edge -> nextState mapping
	    
	    def __init__(self, n, transitMap={}, final=False):
	        self.n = n
	        self.transitMap = transitMap
	        self.final = final
	        
	    def is_final(self):
	        return self.final
	    
	    def get_id(self):
	        return self.n
	    
	    def get_transitions(self):
	        return self.transitMap
	        
	s3 = state('s3', {}, True)
	        
	trans3 = {}
	s2 = state('s2', trans3, True)
	
	trans2 = {'{EOF, A}': s3, 'B': s2}
	s1 = state('s1', trans2)
	
	trans1 = {'A': s1, 'B': s2}
	s0 = state('s0', trans1)
	
	print states_to_dot('testDot', 15, 15, [s0, s1, s2, s3])
	
In command line, run: 
	
	$ python test.py > test.dot
	
	$ dot -Tpng test.dot > test.png
	
and open the resulting png file to view your automaton, have fun...