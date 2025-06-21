import random

FIELD_SIZE = 10
WHALE = "🐳"
FISH = "🐟"
EMPTY = "🌊"
DIRECTIONS = {"⬅️": (-1, 0), "➡️": (1, 0), "⬆️": (0, -1), "⬇️": (0, 1)}

class WhaleGame:
    def __init__(self):
        self.whale = [FIELD_SIZE // 2, FIELD_SIZE // 2]
        self.score = 0
        self.spawn_fish()

    def spawn_fish(self):
        while True:
            self.fish = [random.randint(0, FIELD_SIZE - 1),
                         random.randint(0, FIELD_SIZE - 1)]
            if self.fish != self.whale:
                break

    def move(self, direction):
        dx, dy = DIRECTIONS.get(direction, (0, 0))
        self.whale[0] = max(0, min(FIELD_SIZE - 1, self.whale[0] + dx))
        self.whale[1] = max(0, min(FIELD_SIZE - 1, self.whale[1] + dy))
        if self.whale == self.fish:
            self.score += 1
            self.spawn_fish()

    def render(self):
        rows = []
        for y in range(FIELD_SIZE):
            row = "".join(
                WHALE if [x, y] == self.whale else
                FISH if [x, y] == self.fish else
                EMPTY
                for x in range(FIELD_SIZE)
            )
            rows.append(row)
        rows.append(f"\n🎯 Рыбок поймано: {self.score}")
        return "\n".join(rows)
