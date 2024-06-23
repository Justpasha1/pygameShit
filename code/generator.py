import random

def generate_level(width, height):

  level = [[1 for _ in range(width)] for _ in range(height)]

  # Создать список свободных клеток
  free_cells = []
  for y in range(1, height - 1):
    for x in range(1, width - 1):
      if random.random() < 0.5:
        free_cells.append((y, x))

  random.shuffle(free_cells)
  for i in range(len(free_cells) - 1):
    y1, x1 = free_cells[i]
    y2, x2 = free_cells[i + 1]

    # Проложить путь между двумя клетками
    dig_path(level, y1, x1, y2, x2)

  # Добавить начальную позицию игрока
  level[0][0] = 2

  # Добавить выход
  level[height - 1][width - 1] = 3

  return level

def dig_path(level, y1, x1, y2, x2):

  if y1 == y2 and x1 == x2:
    return

  if abs(y1 - y2) > 1 or abs(x1 - x2) > 1:
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2

    dig_path(level, y1, x1, mid_y, mid_x)
    dig_path(level, mid_y, mid_x, y2, x2)
    return


  if y1 != y2:
    level[y1][x1] = 0
    for y in range(y1 + 1, y2):
      level[y][x1] = 0
  else:
    level[y1][x1] = 0
    for x in range(x1 + 1, x2):
      level[y1][x] = 0

def print_level(level):

  symbols = {
      0: " ",  # Коридор
      1: "#",  # Стена
      2: "@",  # Игрок
      3: "!",  # Выход
  }

  for row in level:
    print("".join([symbols[cell] for cell in row]))

level = generate_level(10, 10)
print_level(level)