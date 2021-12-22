class Bingo:
    def __init__(self, data):
        self.data = [line.split() for line in data]
        assert len(self.data[0]) == len(self.data)

    def get_column(self, column):
        value = []
        for line in self.data:
            value.append(line[column])
        return value

    def __setitem__(self, index, value):
        self.data[index[1]][index[0]] = value

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index]
        return self.data[index[1]][index[0]]
    
    def index(self, value):
        for i, line in enumerate(self.data):
            try:
                return (line.index(value), i)
            except ValueError:
                pass

    def __len__(self):
        return len(self[0])
    
    def victory(self):
        """returns True if it wins, else False"""
        for i, line in enumerate(self.data):
            if all([value == "x" for value in line]):
                return True
            if all([value == "x" for value in self.get_column(i)]):
                return True
        if all([self[i,i] == "x" for i in range(len(self))]):
            return True
        if all([self[i] == "x" for i in range(len(self))]):
            return True
        return False

    def playtest(self, draws):
        """returns a tuple: 
        (the amount of turns the table has to play in order to win,
        the last draw)"""
        turns = 0
        for draw in draws:
            index = self.index(draw)
            if index is not None:
                self[index] = "x"
            if self.victory():
                return turns, self.score()*int(draw)
            turns += 1
        return (999, 0)
    
    def __str__(self):
        return "\n".join([" ".join(data) for data in self.data])
    
    def score(self):
        total = 0
        for row in self.data:
            for value in row:
                if value != "x":
                    total += int(value)
        return total




with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    file_draws = lines[0].split(",")
    scores = []

    # bingo = Bingo(lines[2:7])
    # print(bingo.playtest(file_draws))
    for i in range((len(lines)-2)//6):
        current = Bingo(lines[2+i*6:i*6+7])
        scores.append(current.playtest(file_draws))
    # Part 1
    print(min(scores, key=lambda element:element[0])[1])
    # Part 2
    print(max(scores, key=lambda element:element[0])[1])