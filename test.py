from automataview import states_to_dot
# for test
class state(object):
    # n: state num
    # transitMap: edge -> nextState mapping
    
    def __init__(self, n, trans=[], final=False):
        self.n = n
        self.trans = trans
        self.final = final
        
    def is_final(self):
        return self.final
    
    def get_id(self):
        return self.n
    
    def get_transitions(self):
        return self.trans
        
s3 = state('s3', [], True)
        
trans3 = []
s2 = state('s2', trans3, True)

trans2 = [('{EOF, A}', s3), ('B', s2)]
s1 = state('s1', trans2)

trans1 = [('A', s1), ('B', s2)]
s0 = state('s0', trans1)

print states_to_dot('testDot', 15, 15, [s0, s1, s2, s3])
