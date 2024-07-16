from dataclasses import dataclass
from pathlib import Path

from utils import debugg_drawer_of_pipe_system

INPUT_FILE = "data/coding_qual_input.txt"

# Step 1: Define Pipe Connections (Dictionary)
PIPE_CONNECTIONS = {
    '═': {'right', 'left'},
    '║': {'up', 'down'},
    '╔': {'right', 'down'},
    '╗': {'down', 'left'},
    '╚': {'up', 'right'},
    '╝': {'up', 'left'},
    '╠': {'up', 'right', 'down'},
    '╣': {'down', 'up', 'left'},
    '╦': {'down', 'right', 'left'},
    '╩': {'up', 'right', 'left'},
}

OPPOSITE_DIRECTIONS = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left'
}


# PIPE_CONNECTIONS = {
#     k: {OPPOSITE_DIRECTIONS[direction] for direction in v}
#     for k, v in PIPE_CONNECTIONS.items()
# }

@dataclass(frozen=True)
class Cell:
    x: int
    y: int
    sym: str

    @staticmethod
    def from_str(s: str) -> 'Cell':
        obj, x, y = s.split()
        return Cell(int(x), int(y), obj)

    def is_sink(self) -> bool:
        return self.sym.isalpha()

    def is_source(self) -> bool:
        return self.sym == '*'

    def potential_neighbours(self) -> list[tuple[int, int]]:

        connections = (
            {'left', 'right', 'up', 'down'}
            if self.is_sink() or self.is_source()
            else PIPE_CONNECTIONS.get(self.sym, set())
        )

        res = []
        dx_dy = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
        for c in connections:
            dx, dy = dx_dy[c]
            res.append((self.x + dx, self.y + dy))

        return res


def read_file(filepath: str) -> dict[tuple[int, int], Cell]:
    res = {}
    for line in Path(filepath).read_text().splitlines():
        c = Cell.from_str(line)
        res[(c.x, c.y)] = c

    return res


def build_graph(grid: dict[tuple[int, int], Cell]) -> dict[Cell, set[Cell]]:
    pns = {
        k: v.potential_neighbours()
        for k, v in grid.items()
    }

    graph = {}
    for xy, n_xys in pns.items():
        neighbours = list(filter(lambda xy_n: xy in pns.get(xy_n, []), n_xys))

        cell = grid[xy]
        graph[cell] = {grid[xy2] for xy2 in neighbours}

    return graph


def dfs(graph: dict[Cell, set[Cell]], start: Cell) -> set[Cell]:
    visited = set()
    stack = [start]

    while stack:
        if (cell := stack.pop()) not in visited:
            visited |= {cell}
            stack += list(graph[cell] - visited)

    return {v for v in visited if v.is_sink()}


def find_start(grid: dict[tuple[int, int], Cell]) -> Cell:
    for cell in grid.values():
        if cell.is_source():
            return cell

    raise ValueError("No start found")


def calculate(path: Path) -> str:
    data = read_file(str(path))
    debugg_drawer_of_pipe_system(list(data.values()))

    graph = build_graph(data)
    start = find_start(data)

    ends = dfs(graph, start)

    return ''.join(sorted([e.sym for e in ends]))

def main() -> None:
    for f in (Path().parent.parent / "data").glob("*"):
        print(f"Calculating for {f}")
        print(f"The result string is: {calculate(f)}")


if __name__ == "__main__":
    main()
