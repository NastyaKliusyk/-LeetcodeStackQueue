class FreqStack:

    def __init__(self):
        self.freq_map = {}
        self.group_map = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = freq

        self.max_freq = max(self.max_freq, freq)

        if freq not in self.group_map:
            self.group_map[freq] = []
        self.group_map[freq].append(val)

    def pop(self) -> int:

        most_frequent = self.group_map[self.max_freq].pop()
        self.freq_map[most_frequent] -= 1

        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
        
        return most_frequent
