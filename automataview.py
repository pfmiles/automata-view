# whole graph
class graph(object):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.states = set()
        self.finalStates = set()
        self.transitions = set()
        
    def add_state(self, s, final):
        self.states.add(s)
        if final:
            self.finalStates.add(s)
            
    def add_transition(self, start, end, edge):
        self.transitions.add((start, end, edge))
        
    def to_dot_string(self):
        allTemp = """
        digraph %s {
            rankdir=LR;
            size="%s,%s"
            node [shape = doublecircle]; %s;
            node [shape = circle];
            %s
        }
        """
        transitionTemp = """%s -> %s [ label = "%s" ];"""
        finals = " ".join(self.finalStates)
        trans = "\n".join([transitionTemp % trans for trans in self.transitions])
        return allTemp % (self.name, self.length, self.width, finals, trans)
        
def states_to_dot(name, length, width, states):
    """
    every 'state' instance in 'states' parameter is required to have these methods:
    is_final returns True/False indicates whether this is a final state
    get_transitions of return type {edge -> state} represents all valid transitions started from this state
    get_id returned value as the state's displaying name
    """
    g = graph(name, length, width)
    for s in states:
        g.add_state(s.get_id(), s.is_final())
        for (edge, os) in s.get_transitions().iteritems():
            g.add_transition(s.get_id(), os.get_id(), edge)
            
    return g.to_dot_string()
        
