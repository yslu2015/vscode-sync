import pygame
import random
import time

# 初始化 pygame
pygame.init()

# 设置屏幕大小
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("小球碰撞游戏")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 定义小球类
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # 边界检测
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def collide(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance <= self.radius + other.radius

# 初始化小球
player_ball = Ball(300, 300, 20, BLUE, 0, 0)
auto_ball = Ball(100, 100, 20, RED, 3, 3)

# 游戏变量
collision_count = 0
running = True
clock = pygame.time.Clock()

# 游戏主循环
while running:
    screen.fill(WHITE)  # 清屏

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_ball.y -= 5
    if keys[pygame.K_DOWN]:
        player_ball.y += 5
    if keys[pygame.K_LEFT]:
        player_ball.x -= 5
    if keys[pygame.K_RIGHT]:
        player_ball.x += 5

    # 移动自动小球
    auto_ball.move()

    # 检测碰撞
    if player_ball.collide(auto_ball):
        collision_count += 1
        print(f"碰撞次数: {collision_count}")
        auto_ball = None  # 移除自动小球
        time.sleep(1)  # 等待 1 秒
        # 生成新的自动小球，速度加快
        new_speed_x = random.choice([-5, 5]) + (collision_count * 0.5)
        new_speed_y = random.choice([-5, 5]) + (collision_count * 0.5)
        auto_ball = Ball(random.randint(50, 550), random.randint(50, 550), 20, RED, new_speed_x, new_speed_y)

    # 绘制小球
    player_ball.draw()
    if auto_ball:
        auto_ball.draw()

    # 显示碰撞次数
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"碰撞次数: {collision_count}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # 更新屏幕
    pygame.display.flip()
    clock.tick(60)  # 控制帧率

    # 游戏结束条件
    if collision_count >= 10:
        print("游戏结束！")
        running = False

# 退出游戏
pygame.quit()