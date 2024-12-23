"""
Implementation of Logic Gates to demonstrate how inheritance works in Python.
A logic gate takes in boolean inputs, and outputs a boolean value based on simple logical operations (e.g AND, OR, NOT, etc. ).
Each logical operation is based on a truth table which we will use to simplify calculating the output.
"""

import itertools

class LogicGate:
    def __init__(self, label) -> None:
        """
        Args: 
            label (str): identifies the gate
            output (bool): evaluation of the the inputs according to gate logic
        """
        self.label = label
        self.output = None
        self.truth_table = None

    def get_label(self) -> str:
        return self.label
    
    def get_output(self) -> bool:
        self.output = self.perform_gate_logic()
        return self.output
    
    def perform_gate_logic(self) -> bool:
        """
        Perform logical operations according to type of LogicalGate.
        To be implemented in the child classes

        Returns: 
            (bool): product of the logical operation given the inputs
        """
        pass

    def set_next_pin(self, input):
        """
        Sets the next empty pin on the LogicalGate to the input, if there is an empty pin.
        To be implemented in the child classes
        Args:
            input: possible value of the next empty pin
        Returns:
            None
        """
        pass
    

class BinaryGate(LogicGate):
    """
    Class to define a type of logic gate that takes 2 inputs
    """

    def __init__(self, label, pin_a = None, pin_b = None) -> None:
        """
        Args:
            pin_a (bool): first input
            pin_b (bool): second input
        """
        super().__init__(label)
        self.pin_a = pin_a
        self.pin_b = pin_b

    def get_pin_a(self):
        return self.pin_a
    
    def set_pin_a(self, pin_a):
        self.pin_a = pin_a
    
    def get_pin_b(self):
        return self.pin_b
    
    def set_pin_b(self, pin_b):
        self.pin_b = pin_b

    def set_next_pin(self, input):
        if self.pin_a == None:
            self.pin_a = input
        elif self.pin_b == None:
            self.pin_b = input
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")    

    def perform_gate_logic(self):
        if not self.truth_table:
            return None
        row = int(self.pin_a)
        col = int(self.pin_b)
        return self.truth_table[row][col]
    
class UnaryGate(LogicGate):
    """
    Class to define a type of logic gate that takes 1 input
    """

    def __init__(self, label, pin_a=None) -> None:
        """
        Args:
            pin_a (bool): input
        """
        super().__init__(label)
        self.pin_a = pin_a

    def get_pin_a(self):
        return self.pin_a
    
    def set_pin_a(self, pin_a=None):
        self.pin_a = pin_a

    def set_next_pin(self,input):
        if self.pin_a == None:
            self.pin_a = input
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
    
    def perform_gate_logic(self):
        if not self.truth_table:
            return None
        col = int(self.pin_a)
        return self.truth_table[col]


class ANDGate(BinaryGate):
    """
    The AND Logical Gate only outputs True if both inputs are true
    """

    def __init__(self, label, pin_a=None, pin_b=None) -> None:
        super().__init__(label, pin_a, pin_b)
        self.truth_table = [[0,0],
                            [0,1]]


class NANDGate(BinaryGate):
    def __init__(self, label, pin_a=None, pin_b=None) -> None:
        super().__init__(label, pin_a, pin_b)
        self.truth_table = [[1,1],
                            [1,0]]
        

class ORGate(BinaryGate):
    """
    The OR Logical Gate only outputs True if one of inputs is true
    """
    def __init__(self, label, pin_a=None, pin_b=None) -> None:
        super().__init__(label, pin_a=None, pin_b=None)
        self.truth_table = [[0,1],
                            [1,1]]
        
class NORGate(BinaryGate):
    def __init__(self, label, pin_a=None, pin_b=None) -> None:
        super().__init__(label, pin_a, pin_b)
        self.truth_table = [[1,0],
                            [0,0]]

class NOTGate(UnaryGate):
    def __init__(self, label, pin_a=None) -> None:
        super().__init__(label, pin_a)
        self.truth_table = [1,0]


class Connector:
    """
    The class object serves to connect two logical gates together
    """
    def __init__(self, from_gate: LogicGate, to_gate: LogicGate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.set_next_pin(from_gate.get_output())
    
    def get_from_gate(self):
        return self.from_gate
    
    def get_to_gate(self):
        return self.get_to_gate
    
        


if __name__ == "__main__":
    #Prove NOT(( A and B) or (C and D)) == NOT( A and B ) and NOT (C and D)

    inputs = list(itertools.product([0,1], repeat=4))

    for input in inputs:
        AB = ANDGate("(A and B)", input[0],input[1])
        CD = ANDGate("(C and D)", input[2], input[3])
        ABorCD = ORGate("( A and B) or (C and D)")
        c1 = Connector(from_gate=AB, to_gate=ABorCD)
        c2 = Connector(from_gate=CD, to_gate=ABorCD)
        nABorCD = NOTGate("NOT(( A and B) or (C and D))")
        c3 = Connector(from_gate=ABorCD, to_gate=nABorCD)

        nAB = NOTGate("NOT( A and B )")
        c4 = Connector(from_gate=AB, to_gate=nAB)

        nCD = NOTGate("NOT (C and D)")
        c5 = Connector(from_gate=CD, to_gate=nCD)

        nABnCD = ANDGate("NOT( A and B ) and NOT (C and D)")
        c6 = Connector(from_gate = nAB, to_gate=nABnCD)
        c7 = Connector(from_gate= nCD, to_gate= nABnCD)


        print(input, nABorCD.get_output() == nABnCD.get_output())

    


    