# snake.py
import pygame, sys, random

# ---------- Settings ----------
CELL = 25
GRID_W, GRID_H = 24, 24
W, H = GRID_W * CELL, GRID_H * CELL
FPS_BASE = 8               # starting speed
SPEED_STEP_EVERY = 5       # increase speed every N apples
BORDER_COLOR = (40, 40, 40)
BG1, BG2 = (18, 18, 18), (24, 24, 24)
SNAKE_HEAD, SNAKE_BODY = (70, 220, 100), (60, 190, 90)
FOOD_COLOR = (220, 60, 80)
TEXT = (230, 230, 230)
SHADOW = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22, bold=True)
big  = pygame.font.SysFont("consolas", 42, bold=True)

# ---------- Helpers ----------
def grid_rand(exclude):
    """Return a random grid cell not inside 'exclude' set of (x,y)."""
    while True:
        p = (random.randrange(0, GRID_W), random.randrange(0, GRID_H))
        if p not in exclude: return p

def draw_cell(pos, color):
    x, y = pos
    r = pygame.Rect(x*CELL, y*CELL, CELL, CELL)
    pygame.draw.rect(screen, color, r, border_radius=6)

def draw_board():
    screen.fill(BG1)
    # subtle checkerboard
    for x in range(GRID_W):
        for y in range(GRID_H):
            if (x + y) % 2 == 0:
                pygame.draw.rect(
                    screen, BG2, (x*CELL, y*CELL, CELL, CELL), border_radius=8
                )
    # border
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, W, H), 2, border_radius=8)

# def text(surface, s, f, pos, c=TEXT, center=False, shadow=True):
#     img = f.render(s, True, c)
#     if shadow:
#         sh = f.render(s, True, SHADOW)
#         rect = sh.get_rect(center=pos if center else None)
#         if not center:
#             rect.topleft = (pos[0]+1, pos[1]+1)
#         else:
#             rect.center = (pos[0]+1, pos[1]+1)
#         surface.blit(sh, rect)
#     rect = img.get_rect(center=pos if center else None)
#     if not center: rect.topleft = pos
#     surface.blit(img, rect)
def text(surface, s, f, pos, c=TEXT, center=False, shadow=True):
    img = f.render(s, True, c)
    if shadow:
        sh = f.render(s, True, SHADOW)
        if center:
            rect = sh.get_rect(center=pos)
        else:
            rect = sh.get_rect()
            rect.topleft = (pos[0]+1, pos[1]+1)
        surface.blit(sh, rect)

    if center:
        rect = img.get_rect(center=pos)
    else:
        rect = img.get_rect()
        rect.topleft = pos
    surface.blit(img, rect)


# ---------- Game State ----------
def new_game():
    start = (GRID_W//2, GRID_H//2)
    snake = [start, (start[0]-1, start[1]), (start[0]-2, start[1])]
    direction = (1, 0)  # moving right
    food = grid_rand(set(snake))
    score = 0
    alive = True
    paused = False
    return snake, direction, food, score, alive, paused

snake, direction, food, score, alive, paused = new_game()

def change_dir(key, direction):
    # prevent reversing directly
    mapping = {
        pygame.K_LEFT:  (-1, 0),
        pygame.K_a:     (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_d:     (1, 0),
        pygame.K_UP:    (0, -1),
        pygame.K_w:     (0, -1),
        pygame.K_DOWN:  (0, 1),
        pygame.K_s:     (0, 1),
    }
    if key in mapping:
        nd = mapping[key]
        if (nd[0] == -direction[0] and nd[1] == -direction[1]):
            return direction
        return nd
    return direction

def step(snake, direction, food, score):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # wall collision
    if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
        return snake, food, score, False, True  # dead

    # self collision
    if new_head in snake:
        return snake, food, score, False, True

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = grid_rand(set(snake))
    else:
        snake.pop()  # move forward

    return snake, food, score, True, False

# ---------- Main Loop ----------
frame = 0
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if alive and not paused:
                direction = change_dir(e.key, direction)
            if e.key == pygame.K_p and alive:
                paused = not paused
            if not alive and e.key == pygame.K_r:
                snake, direction, food, score, alive, paused = new_game()

    draw_board()

    # speed scales with score
    fps = FPS_BASE + (score // SPEED_STEP_EVERY)
    if alive and not paused:
        frame += 1
        # move every frame (since FPS controls pace)
        snake, food, score, cont, dead = step(snake, direction, food, score)
        alive = cont and not dead

    # draw food & snake
    draw_cell(food, FOOD_COLOR)
    for i, p in enumerate(snake):
        draw_cell(p, SNAKE_HEAD if i == 0 else SNAKE_BODY)

    # HUD
    text(screen, f"Score: {score}", font, (10, 8))
    text(screen, "P: Pause  R: Restart  ESC: Quit", font, (10, H-28))

    if paused:
        text(screen, "PAUSED", big, (W//2, H//2-10), center=True)
        text(screen, "Press P to resume", font, (W//2, H//2+26), center=True)

    if not alive:
        text(screen, "GAME OVER", big, (W//2, H//2-14), center=True)
        text(screen, f"Final Score: {score}", font, (W//2, H//2+24), center=True)
        text(screen, "Press R to restart", font, (W//2, H//2+52), center=True)

    pygame.display.flip()
    clock.tick(fps)
