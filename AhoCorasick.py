from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = {}
        self.output = defaultdict(list)
        self.fail = {}
        self.state_count = 0

    def add_pattern(self, pattern):
        current_state = 0

        for char in pattern:
            if char not in self.trie.get(current_state, {}):
                self.state_count += 1
                if current_state not in self.trie:
                    self.trie[current_state] = {}
                self.trie[current_state][char] = self.state_count

            current_state = self.trie[current_state][char]

        self.output[current_state].append(pattern)

    def build(self):
        queue = deque()
        for char, next_state in self.trie.get(0, {}).items():
            self.fail[next_state] = 0
            queue.append(next_state)
        while queue:
            state = queue.popleft()
            for char, next_state in self.trie.get(state, {}).items():
                queue.append(next_state)
                fail_state = self.fail.get(state, 0)
                while fail_state and char not in self.trie.get(fail_state, {}):
                    fail_state = self.fail.get(fail_state, 0)
                self.fail[next_state] = self.trie.get(fail_state, {}).get(char, 0)
                self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, text):
        state = 0
        results = []

        for i, char in enumerate(text):
            while state and char not in self.trie.get(state, {}):
                state = self.fail[state]
            state = self.trie.get(state, {}).get(char, 0)

            if self.output[state]:
                for pattern in self.output[state]:
                    results.append((i - len(pattern) + 1, pattern))

        return results

if __name__ == "__main__":
    aho = AhoCorasick()
    words = ["valuation", "hit", "secondary", "CNBC"]

    for word in words:
        aho.add_pattern(word)

    aho.build()
    text = "The valuation of Elon Musk’s SpaceX hit $350 billion based on a secondary share sale, CNBC confirmed Wednesday."
    matches = aho.search(text)

    print(matches)