class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol)


class MooreMachine:
    def __init__(self, initial_state=None):
        self.current_state = initial_state
        self.states = {}

    def add_state(self, state):
        self.states[state.name] = state
        if self.current_state is None:
            self.current_state = state

    def set_initial_state(self, state_name):
        self.current_state = self.states.get(state_name)

    def process_input(self, input_symbols):
        outputs = [self.current_state.output]

        for symbol in input_symbols:
            next_state = self.current_state.get_next_state(symbol)
            if next_state is None:
                raise ValueError(f"Nieprawidłowe wejście: {symbol}")
            self.current_state = next_state
            outputs.append(self.current_state.output)

        return outputs


if __name__ == "__main__":
    s0 = State("S0", "A")
    s1 = State("S1", "B")
    s2 = State("S2", "C")

    s0.add_transition("0", s0)
    s0.add_transition("1", s1)

    s1.add_transition("0", s2)
    s1.add_transition("1", s0)

    s2.add_transition("0", s1)
    s2.add_transition("1", s2)

    moore_machine = MooreMachine()
    moore_machine.add_state(s0)
    moore_machine.add_state(s1)
    moore_machine.add_state(s2)
    moore_machine.set_initial_state("S0")

    input_sequence = "101100"
    print(f"Ciąg wejściowy: {input_sequence}")
    output_sequence = moore_machine.process_input(input_sequence)
    print(f"Ciąg wyjściowy: {''.join(output_sequence)}")
