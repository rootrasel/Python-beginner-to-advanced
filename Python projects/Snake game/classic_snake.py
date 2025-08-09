import pygame, sys, random, numpy as np

# ---------------- Config ----------------
CELL = 16
GRID_W, GRID_H = 24, 24
W, H = GRID_W*CELL, GRID_H*CELL

# classic colors
BG   = (0, 0, 0)
SNAKE_CLASSIC = (255, 255, 255)
FOOD_CLASSIC  = (255, 255, 255)
HUD  = (255, 255, 255)

# speed (ms per move)
STEP_MS_START = 180
STEP_MS_MIN   = 70
SPEEDUP_EVERY = 5
BORDER_WALLS  = True

# === Baby Snake style config ===
BABY_MODE    = True        # toggle baby look
BABY_SCALE   = 0.62        # 0.5–0.75: lower => smaller look
SNAKE_BODY   = (140, 255, 140)
SNAKE_OUTLINE= (30, 120, 30)
SNAKE_HEAD   = (180, 255, 180)
FOOD_BABY    = (255, 90, 90)

# --------------- init -------------------
pygame.init()
pygame.display.set_caption("Nokia Snake")
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("monospace", 18, bold=True)

# tiny beep using generated sine — keeps it file-free
pygame.mixer.init(frequency=22050, size=-16, channels=1)
def tone(freq=880, ms=60, vol=0.25):
    t = np.linspace(0, ms/1000.0, int(22050*ms/1000.0), False)
    wav = (np.sin(2*np.pi*freq*t) * 32767 * vol).astype(np.int16)
    return pygame.mixer.Sound(wav)

beep_eat = tone(900, 60, 0.3)
beep_die = tone(220, 180, 0.35)

# --------------- helpers ----------------
def rand_cell(exclude):
    while True:
        p = (random.randrange(GRID_W), random.randrange(GRID_H))
        if p not in exclude: return p

def new_game():
    mid = (GRID_W//2, GRID_H//2)
    snake = [mid, (mid[0]-1, mid[1]), (mid[0]-2, mid[1])]
    direc = (1, 0)
    food  = rand_cell(set(snake))
    score = 0
    step_ms = STEP_MS_START
    return snake, direc, food, score, True, step_ms

snake, direc, food, score, alive, step_ms = new_game()
elapsed = 0  # ms accumulator

def change_dir(key, d):
    m = {
        pygame.K_LEFT:(-1,0), pygame.K_a:(-1,0),
        pygame.K_RIGHT:(1,0), pygame.K_d:(1,0),
        pygame.K_UP:(0,-1), pygame.K_w:(0,-1),
        pygame.K_DOWN:(0,1), pygame.K_s:(0,1),
    }
    if key in m:
        nd = m[key]
        if nd[0]==-d[0] and nd[1]==-d[1]: return d
        return nd
    return d

def step_once(snake, d, food, score, step_ms):
    hx, hy = snake[0]
    nx, ny = hx + d[0], hy + d[1]

    if BORDER_WALLS:
        if not (0 <= nx < GRID_W and 0 <= ny < GRID_H):
            return snake, food, score, step_ms, False
    else:
        nx %= GRID_W; ny %= GRID_H

    head = (nx, ny)
    if head in snake:
        return snake, food, score, step_ms, False

    snake.insert(0, head)
    if head == food:
        score += 1
        beep_eat.play()
        food = rand_cell(set(snake))
        if score % SPEEDUP_EVERY == 0:
            step_ms = max(STEP_MS_MIN, step_ms - 15)
    else:
        snake.pop()

    return snake, food, score, step_ms, True

# --------- Baby look helpers ----------
def baby_rect(x, y):
    margin = int((1 - BABY_SCALE) * CELL / 2)
    size = CELL - margin*2
    return pygame.Rect(x*CELL + margin, y*CELL + margin, size, size)

def draw_segment(i, x, y):
    r = baby_rect(x, y)
    pygame.draw.rect(screen, SNAKE_HEAD if i == 0 else SNAKE_BODY, r, border_radius=6)
    pygame.draw.rect(screen, SNAKE_OUTLINE, r, width=2, border_radius=6)

def draw_head_eyes(head, direc):
    eye = max(2, CELL//8)
    off = max(2, CELL//6)
    x, y = head
    r = baby_rect(x, y)
    cx, cy = r.center
    if direc == (1,0):
        e1 = (cx+off, cy-eye); e2 = (cx+off, cy+eye)
    elif direc == (-1,0):
        e1 = (cx-off, cy-eye); e2 = (cx-off, cy+eye)
    elif direc == (0,-1):
        e1 = (cx-eye, cy-off); e2 = (cx+eye, cy-off)
    else:
        e1 = (cx-eye, cy+off); e2 = (cx+eye, cy+off)
    for ex, ey in (e1, e2):
        pygame.draw.rect(screen, (20,20,20),
                         pygame.Rect(ex-eye//2, ey-eye//2, eye, eye), border_radius=2)

# --------------- drawing ----------------
def draw():
    screen.fill(BG)

    if BABY_MODE:
        # food (round)
        pygame.draw.ellipse(screen, FOOD_BABY, baby_rect(food[0], food[1]))
        # snake
        for i, (x, y) in enumerate(snake):
            draw_segment(i, x, y)
        draw_head_eyes(snake[0], direc)
    else:
        # classic look
        for (x, y) in snake:
            pygame.draw.rect(screen, SNAKE_CLASSIC, (x*CELL, y*CELL, CELL, CELL))
        pygame.draw.rect(screen, FOOD_CLASSIC, (food[0]*CELL, food[1]*CELL, CELL, CELL))

    img = font.render(f"Score: {score}", True, HUD)
    screen.blit(img, (6, 6))

# --------------- main loop --------------
while True:
    dt = clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if alive:
                direc = change_dir(e.key, direc)
            else:
                if e.key == pygame.K_r:
                    snake, direc, food, score, alive, step_ms = new_game()
                    elapsed = 0

    if alive:
        elapsed += dt
        while elapsed >= step_ms:
            elapsed -= step_ms
            snake, food, score, step_ms, alive = step_once(
                snake, direc, food, score, step_ms
            )
            if not alive:
                beep_die.play()
                break

    draw()
    if not alive:
        over = font.render("GAME OVER  (R to restart)", True, HUD)
        rect = over.get_rect(center=(W//2, H//2))
        screen.blit(over, rect)

    pygame.display.flip()
