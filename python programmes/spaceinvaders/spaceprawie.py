import pygame, time, random

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

white = (255,255,255)
black = (0,0,0)
green = (0,100,0)
red = (150,0,0)
blue = (50,100,250)
light_red = (250, 0, 0)


display_width = 800
display_height = 600

smallfont = pygame.font.SysFont("castellar",25)
medfont = pygame.font.SysFont("castellar",35)
largefont = pygame.font.SysFont("magneto",60)
buttonfont = pygame.font.SysFont("algerian",25)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Space Invaders')

pygame.display.update()

wininig_sound = pygame.mixer.Sound('D:\\studia\\wdi\\spaceinvaders\\tada.wav')
shooting_sound = pygame.mixer.Sound('D:\\studia\\wdi\\spaceinvaders\\ir_end.wav')
button_sound = pygame.mixer.Sound('D:\\studia\\wdi\\spaceinvaders\\ding.wav')
enemy_sound = pygame.mixer.Sound('D:\\studia\\wdi\\spaceinvaders\\ir_begin.wav')
shot_sound = pygame.mixer.Sound('D:\\studia\\wdi\\spaceinvaders\\cr.wav')


menu = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\menu.jpg')
controls_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\controls.jpg')
background = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\bg.jpg')
img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\statekk.png')
enemy1_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\oie_transparent.png')
enemy2_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\enemy2.png')
enemy4_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\enemy3.png')
enemy3_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\enemy4.png')
boss_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\boss.png')
boom_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\boom.png')
boom1_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\boom1.png')
bonus1_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\heart.png')
bonus2_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\bonus2.png')
bonus3_img = pygame.image.load('D:\\studia\\wdi\\spaceinvaders\\bonus3.png')

clock = pygame.time.Clock()


block_size = 30
FPS = 20



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        self.enemy_x = 0
        self.enemy_y = 100
        self.enemy_width = 45
        self.enemy_height = 20
        self.enemy_speed = 5
        self.rect = pygame.Rect(self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height)

    def move_right(self):
        self.enemy_x += self.enemy_speed
        gameDisplay.blit(boss_img, [self.enemy_x,self.enemy_y, self.enemy_width, self.enemy_height])
        if self.enemy_x + self.enemy_width + 10 < display_width:
            self.rect.move(self.enemy_x,self.enemy_y)
            return 1
        if self.enemy_x + self.enemy_width + 10 == display_width:
            return 0

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, type):
        self.enemy_x = x
        self.enemy_y = y
        self.type = type
        if type == 1:
            self.enemy_width = 30
            self.enemy_height = 22
        elif type == 2:
            self.enemy_width = 30
            self.enemy_height = 22
        elif type == 3:
            self.enemy_width = 36
            self.enemy_height = 24
        elif type == 4:
            self.enemy_width = 35
            self.enemy_height = 24
        self.enemy_speed = 1
        self.rect = pygame.Rect(self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height)


    def move_right(self, rows, bonus, faster = 0):
        if self.type == 1:
            gameDisplay.blit(enemy1_img, [self.enemy_x,self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type==2:
            gameDisplay.blit(enemy2_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type == 3:
            gameDisplay.blit(enemy3_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type == 4:
            gameDisplay.blit(enemy4_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        if self.enemy_x + self.enemy_width + 10 < display_width:
            if bonus == 0:
                self.enemy_x = self.enemy_x + self.enemy_speed + faster
            self.rect.move(self.enemy_x,self.enemy_y)
            return "right"
        if self.enemy_x + self.enemy_width + 10 == display_width:
            self.move_down(rows)
            return "left"

    def move_left(self,rows, bonus, faster = 0):
        if self.type == 1:
            gameDisplay.blit(enemy1_img, [self.enemy_x,self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type==2:
            gameDisplay.blit(enemy2_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type == 3:
            gameDisplay.blit(enemy3_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        elif self.type == 4:
            gameDisplay.blit(enemy4_img, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])
        if self.enemy_x - 10 > 0:
            if bonus == 0:
                self.enemy_x = self.enemy_x - self.enemy_speed - faster
            self.rect.move(self.enemy_x, self.enemy_y)
            return "left"
        if self.enemy_x - 10 == 0:
            self.move_down(rows)
            return "right"

    def move_down(self,rows):
        for row in rows:
            for enemy in row:
                enemy.enemy_y += 30
                enemy.rect.move(enemy.enemy_x, enemy.enemy_y)

    def fire(self, enemy_fire, row_of_enemies, lead_x, block_size, level):
        for enemy in row_of_enemies:
            if self.enemy_y < enemy.enemy_y:
                return 0

        x = random.randint(0,1500)
        # levele
        if level == 1:
            if self.enemy_x < lead_x + block_size/2 and self.enemy_x + self.enemy_width > lead_x + block_size/2:
                # AI wrogow :D
                if x < 50:
                    fire = Enemy_Fire(self.enemy_x, self.enemy_y, self.enemy_width)
                    enemy_fire.append(fire)
                    enemy_sound.play()
            elif x < 5:
                fire = Enemy_Fire(self.enemy_x,self.enemy_y, self.enemy_width)
                enemy_fire.append(fire)
                enemy_sound.play()
        if level == 2:
            if self.enemy_x < lead_x + block_size/2 and self.enemy_x + self.enemy_width > lead_x + block_size/2:
                # AI wrogow :D
                if x < 75:
                    fire = Enemy_Fire(self.enemy_x, self.enemy_y, self.enemy_width)
                    enemy_fire.append(fire)
                    enemy_sound.play()
            elif x < 10:
                fire = Enemy_Fire(self.enemy_x,self.enemy_y, self.enemy_width)
                enemy_fire.append(fire)
                enemy_sound.play()
        if level == 3:
            if self.enemy_x < lead_x + block_size/2 and self.enemy_x + self.enemy_width > lead_x + block_size/2:
                # AI wrogow :D
                if x < 100:
                    fire = Enemy_Fire(self.enemy_x, self.enemy_y, self.enemy_width)
                    enemy_fire.append(fire)
                    enemy_sound.play()
            elif x < 15:
                fire = Enemy_Fire(self.enemy_x,self.enemy_y, self.enemy_width)
                enemy_fire.append(fire)
                enemy_sound.play()


class Enemy_Fire():
    def __init__(self, x, y, width):
        self.fire_x = x + width/2
        self.fire_y = y
        self.fire_size_x = 4
        self.fire_size_y = 10
        self.fire_speed = 1
        self.rect = pygame.Rect(self.fire_x, self.fire_y, self.fire_size_x, self.fire_size_y)

    def move_fire(self):
        pygame.draw.rect(gameDisplay, blue, [self.fire_x, self.fire_y, self.fire_size_x, self.fire_size_y])
        self.fire_y += 10


class Fire():

    def __init__(self, x, y):
        self.fire_x = x
        self.fire_y = y
        self.fire_size_x = 4
        self.fire_size_y = 10
        self.fire_speed = 30
        self.rect = pygame.Rect(self.fire_x, self.fire_y, self.fire_size_x, self.fire_size_y)

    def move_fire(self):
        pygame.draw.rect(gameDisplay, blue, [self.fire_x, self.fire_y, self.fire_size_x, self.fire_size_y])
        self.fire_y -= self.fire_speed

def kill(fire,enemy):
    if fire.fire_x > enemy.enemy_x and fire.fire_x < enemy.enemy_x + enemy.enemy_width and fire.fire_y < enemy.enemy_y - 20:
        return "killed"


class Bonus():

    def __init__(self, type, y):
        self.bonus_x = 10
        self.bonus_y = y
        self.bonus_width = 30
        self.bonus_height = 400
        self.type = type
        self.bonus_speed = 5
        self.rect = pygame.Rect(self.bonus_x, self.bonus_y, self.bonus_width, self.bonus_height)

    def move_right(self):
        if self.type == 1:
            gameDisplay.blit(bonus1_img, [self.bonus_x, self.bonus_y, self.bonus_width, self.bonus_height])
        elif self.type == 2:
            gameDisplay.blit(bonus2_img, [self.bonus_x, self.bonus_y, self.bonus_width, self.bonus_height])
        elif self.type == 3:
            gameDisplay.blit(bonus3_img, [self.bonus_x, self.bonus_y, self.bonus_width, self.bonus_height])
        self.bonus_x += self.bonus_speed


class Barricade():

    def __init__(self, x, y, size):
        self.bar_x = int(x)
        self.bar_y = int(y)
        self.bar_size = int(size)
        self.rect1 = pygame.Rect(self.bar_x, self.bar_y, 100, 20)
        self.rect2 = pygame.Rect(self.bar_x*2, self.bar_y*2, 100, 20)

    def draw(self):
        pygame.draw.rect(gameDisplay, blue, [self.bar_x, self.bar_y, self.bar_size, self.bar_size])



def get_bonus(fire, bonus):
    if fire.fire_x >  bonus.bonus_x and fire.fire_x < bonus.bonus_x + bonus.bonus_width and fire.fire_y < bonus.bonus_y - 20:
        return "bonus"

def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "button":
        textSurface = buttonfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def message_to_screen2(msg,color, y, size = "small", x = 0):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width-120+x), (50+y)
    gameDisplay.blit(textSurf, textRect)

def button_text(msg, x, y, width, height, size = "button"):
    textSurf, textRect = text_objects(msg, white, size)
    textRect.center = (x+(width/2), y+(height/2))
    gameDisplay.blit(textSurf, textRect)

def borders(thickness):
    pygame.draw.rect(gameDisplay, blue, [0, 0, thickness, display_height])
    pygame.draw.rect(gameDisplay, blue, [(display_width-thickness), 0, thickness, display_height])
    pygame.draw.rect(gameDisplay, blue, [0, 0, display_width, thickness])
    pygame.draw.rect(gameDisplay, blue, [0, display_height-thickness, display_width, thickness])


def buttonize(msg, x, y, width, height):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, light_red, (x, y, width, height))

        if click[0] == 1:
            if msg == "QUIT":
                button_sound.play()
                pygame.quit()
                quit()
            elif msg == "PLAY":
                button_sound.play()
                gameLoop(1)
            elif msg == "how to play":
                button_sound.play()
                game_controls()
            elif msg == "next":
                button_sound.play()
                game_controls2()
            elif msg == "back to menu":
                button_sound.play()
                game_intro()
            elif msg == "back":
                button_sound.play()
                game_controls()

    else:
        pygame.draw.rect(gameDisplay, red, (x, y, width, height))

    button_text(msg, x, y, width, height)


def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menu, [0, 0, display_width, display_height])
        message_to_screen("WELCOME TO", white, -180)
        message_to_screen("SPACE INVADERS", red, -100, "large")
        message_to_screen("THE BEST GAME YOU'VE EVER SEEN", white, -30)
        message_to_screen("SHOOT AS MANY ALIENS AS YOU CAN!", white, 10)

        buttonize("PLAY", 150, 400, 100, 50)
        buttonize("how to play", 315, 400, 180, 50)
        buttonize("QUIT", 550, 400, 100, 50)
        borders(5)
        pygame.display.update()
        clock.tick(5)

def game_controls():
    controls = True
    while controls:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(controls_img, [0, 0, display_width, display_height])
        message_to_screen("Controls", red, -200, "large")
        message_to_screen("Fire: Spacebar", white, -120)
        message_to_screen("Move Spaceship: Arrow keys", white, -80)
        message_to_screen("Points", red, -20, "large")
        message_to_screen(" 30 points", white, 50)
        message_to_screen(" 20 points", white, 95)
        message_to_screen(" 10 points", white, 140)
        message_to_screen(" ? ?  points", white, 190)
        gameDisplay.blit(enemy2_img, [280, 330, 30, 30])
        gameDisplay.blit(enemy1_img, [280, 380, 30, 30])
        gameDisplay.blit(enemy3_img, [280, 430, 30, 30])
        gameDisplay.blit(boss_img, [275, 480, 45, 20])

        buttonize("PLAY", 150, 535, 100, 50)
        buttonize("back to menu", 315, 535, 180, 50)
        buttonize("next", 550, 535, 100, 50)

        borders(5)
        pygame.display.update()
        clock.tick(5)


def game_controls2():
    controls = True
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(controls_img, [0, 0, display_width, display_height])
        # message_to_screen("WELCOME TO", white, -180)
        message_to_screen("Bonuses", red, -150, "large")
        message_to_screen("      Freezes enemies", white, -10)
        message_to_screen("Adds 1 life", white, -60)
        message_to_screen("         Faster shooting", white, 50)
        gameDisplay.blit(bonus1_img, [280, 230, 30, 30])
        gameDisplay.blit(bonus2_img, [280, 280, 30, 30])
        gameDisplay.blit(bonus3_img, [280, 330, 30, 30])

        buttonize("PLAY", 150, 535, 100, 50)
        buttonize("back to menu", 315, 535, 180, 50)
        buttonize("back", 550, 535, 100, 50)

        borders(5)
        pygame.display.update()
        clock.tick(5)




def gameLoop(level):
    gameExit = False
    gameOver = False
    winner = False
    #zmienne pomocnicze
    boom = 0
    boom1 = 0
    boss = 0

    # bonusy
    bonus_array = []
    timer_bonus2 = 0
    timer_bonus3 = 0

    #boss
    boss_timer = 200

    #batykady
    baricade_size = 10
    barricade_array = []
    for i in range(1,14):
        barricade1 = Barricade(display_width/8 + baricade_size*(i-1), display_height - 120, baricade_size)
        barricade_array.append(barricade1)
        barricade1 = Barricade(display_width / 8 + baricade_size * (i - 1), display_height - 140, baricade_size)
        barricade_array.append(barricade1)
        barricade2 = Barricade(display_width / 2 - 50 + baricade_size * (i - 1), display_height - 120, baricade_size)
        barricade_array.append(barricade2)
        barricade2 = Barricade(display_width / 2 - 50 + baricade_size * (i - 1), display_height - 140, baricade_size)
        barricade_array.append(barricade2)
        barricade3 = Barricade(display_width / 4 * 3 + baricade_size * (i - 1), display_height - 120, baricade_size)
        barricade_array.append(barricade3)
        barricade3 = Barricade(display_width / 4 * 3 + baricade_size * (i - 1), display_height - 140, baricade_size)
        barricade_array.append(barricade3)

    #player stuff
    my_speed = 10
    life = 5
    fire_array = []
    points = 0
    border_thickness = 10
    lead_x = display_width / 2
    lead_y = display_height- block_size*2
    lead_x_change = 0
    lead_y_change = 0

    # enemy stuff
    enemy_rows = []

    for t in range(1, 13):
        enemy_row = []
        for i in range(0, 5):
            if i == 0:
                enemy = Enemy(50+t*50, 150 + i * 40, 2)
            elif i == 1 or i == 2:
                enemy = Enemy(50+t*50, 150 + i * 40, 1)
            elif i == 3 or i == 4:
                enemy = Enemy(50+t*50, 150 + i*40, i)
            enemy_row.append(enemy)
        enemy_rows.append(enemy_row)
        if level == 1:
            if t == 5:
                break
        elif level == 2:
            if t == 7:
                break

    enemy_direction = "right"
    enemy_fire = []


    while not gameExit:
        pygame.mixer.music.stop()
        while gameOver == True:
            gameDisplay.fill(black)
            score = "Your score is: " + str(points)
            if winner:
                if level == 3:
                    message_to_screen("You won the game!", red, -50, "large")
                    message_to_screen(score, white, 50, "medium")
                    message_to_screen("Press Q to quit or C to play again", white, 150, "small")
                else:
                    message_to_screen("You won!",red, -50,"large")
                    message_to_screen(score, white, 50,"medium")
                    message_to_screen("Press Q to quit or C to go to the next level", white, 150,"small")
                if life != -10:
                    wininig_sound.play()
                    life = -10
            else:
                message_to_screen("Game over",red, -100,"large")
                message_to_screen(score, white, 50, "medium")
                message_to_screen("Press Q to quit or C to play again", white, 150, "small")
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_c:
                        if winner == True:
                            winner = False
                            if level == 3:
                                level == 1
                            else:
                                level += 1
                        gameLoop(level)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    lead_x_change = -my_speed
                    lead_y_change = 0
               elif event.key == pygame.K_RIGHT:
                   lead_x_change = my_speed
                   lead_y_change = 0
               #jesli chcesz sie poruszac w gore i dol to tu dodaj warunki
               elif event.key == pygame.K_SPACE:
                   if timer_bonus3 == 0:
                        if len(fire_array)==0:
                            shooting_sound.play()
                            fire = Fire(lead_x + block_size/2-2,lead_y)
                            fire_array.append(fire)
                   else:
                       shooting_sound.play()
                       fire = Fire(lead_x + block_size / 2 - 2, lead_y)
                       fire_array.append(fire)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                """
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
                """


            if lead_x >= display_width or lead_x < 0 or lead_y>=display_height or lead_y < 0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        #warunki zeby statek nie wylecial za ekran
        if lead_x < 0:
           lead_x += block_size
        if lead_x + block_size > display_width:
            lead_x -= block_size
        if lead_y - 10 < 0:
            lead_y += block_size
        if lead_y + block_size > display_height:
            lead_y -= block_size


        gameDisplay.blit(background,[0, 0, display_width, display_height])
        gameDisplay.blit(img,  [lead_x,lead_y,block_size ,block_size ])
        borders(border_thickness)

        # barykady
        for barricade in barricade_array:
            barricade.draw()

        #ruch pociskow statku
        for fire in fire_array:
            if fire.fire_y < 0:
                fire_array.remove(fire)
            else:
                # barykady
                for barricade in barricade_array:
                    if fire.fire_x >= barricade.bar_x:
                        if fire.fire_x + fire.fire_size_x <= barricade.bar_x + barricade.bar_size:
                            if fire.fire_y >= barricade.bar_y + barricade.bar_size:
                                barricade_array.remove(barricade)
                                if fire in fire_array:
                                    fire_array.remove(fire)
                fire.move_fire()
                for enemy_f in enemy_fire:
                    if fire.fire_x > enemy_f.fire_x - 10:
                        if fire.fire_x + fire.fire_size_x < enemy_f.fire_x + enemy_f.fire_size_x + 10:
                            if fire.fire_y <= enemy_f.fire_y + enemy_f.fire_size_y:
                                boom = 10
                                boom_x = fire.fire_x
                                boom_y = fire.fire_y
                                if enemy_f in enemy_fire:
                                    enemy_fire.remove(enemy_f)
                                if fire in fire_array:
                                    fire_array.remove(fire)

        if boom > 0:
            if boom >5:
                gameDisplay.blit(boom1_img, [boom_x, boom_y])
            else:
                gameDisplay.blit(boom_img, [boom_x, boom_y])

            boom -= 1


        #ruch pociskow wrogow
        for fire in enemy_fire:
            if fire.fire_y > display_height:
                enemy_fire.remove(fire)
            else:
                fire.move_fire()
                for barricade in barricade_array:
                    if fire.fire_x >= barricade.bar_x - 5:
                        if fire.fire_x + fire.fire_size_x <= barricade.bar_x + barricade.bar_size + 5:
                            if fire.fire_y == barricade.bar_y + barricade.bar_size:
                                barricade_array.remove(barricade)
                                if fire in enemy_fire:
                                    enemy_fire.remove(fire)
                #sprawdzam czy trace zycie
                if fire.fire_y + fire.fire_size_y >= lead_y and fire.fire_x >= lead_x and fire.fire_x + fire.fire_size_x <= lead_x + block_size:
                    life -= 1
                    enemy_fire.remove(fire)
                    shot_sound.play()

        # manager wrogow
        for row in enemy_rows:
            for enemy in row:
                for fire in fire_array:
                    state = kill(fire, enemy)
                    if state == "killed":
                        boom1 = 10
                        boom1_x = enemy.enemy_x
                        boom1_y = enemy.enemy_y
                        row.remove(enemy)
                        fire_array.remove(fire)
                        if enemy.type == 1:
                            points += 20
                        if enemy.type == 2:
                            points += 30
                        if enemy.type == 3 or enemy.type == 4:
                            points += 10
                        break
                if enemy_direction == "right":
                    enemy_direction = enemy.move_right(enemy_rows, timer_bonus2)
                    enemy.fire(enemy_fire, row, lead_x, block_size, level)
                elif enemy_direction == "left":
                    enemy_direction = enemy.move_left(enemy_rows, timer_bonus2)
                    enemy.fire(enemy_fire, row, lead_x, block_size, level)

        #manager bossa
        boss_timer -= 1
        if boss_timer == 0:
            boss = 1
            boss_obj = Boss()
            boss_timer = 200

        if boss == 1 and boss_obj:
            boss = boss_obj.move_right()
            for fire in fire_array:
                state2 = kill(fire, boss_obj)
                if state2 == "killed":
                    boss = 10
                    x = random.randint(1,3)
                    points_from_boss = x*110
                    points += points_from_boss
                    msg_y = boss_obj.enemy_y
                    msg_x = boss_obj.enemy_x
                    del boss_obj


        if boss > 1 and state2 == "killed":
            message_to_screen2("+ " + str(points_from_boss), white, -50 + msg_y, "small", 120 - display_width + msg_x)
            if boss == 2:
                boss = 0
            else:
                boss -= 1



        if boom1 > 0:
            if boom1 >5:
                gameDisplay.blit(boom1_img, [boom1_x, boom1_y, 25, 22])
            else:
                gameDisplay.blit(boom_img, [boom1_x, boom1_y])
            boom1 -= 1

        # manager bonusow
        x = random.randint(0,200)
        if x == 21:
            type = random.randint(1, 3)
            new_bonus = Bonus(type, 400)
            bonus_array.append(new_bonus)
        for bonus in bonus_array:
            bonus.move_right()
            for fire in fire_array:
                state = get_bonus(fire, bonus)
                if state == "bonus":
                    if bonus.type == 1:
                        life += 1
                    if bonus.type == 2:
                        timer_bonus2 = 50
                    if bonus.type == 3:
                        timer_bonus3 = 40
                    if bonus in bonus_array:
                        bonus_array.remove(bonus)

        if timer_bonus2 > 0:
            timer_bonus2 -= 1
            message_to_screen("Enemies are freezed: " + str(timer_bonus2), white, -230, "small")


        if timer_bonus3 > 0:
            timer_bonus3 -= 1
            message_to_screen("Fast shooting:  " + str(timer_bonus3), white, -270, "small")



        #wygrana
        tmp = 0
        for row in enemy_rows:
            if len(row) != 0:
                tmp+=1
                break

        if tmp == 0:
            winner = True
            gameOver = True


        #przegrana
        if life <= 0:
            gameOver = True


        # wypisuje ile mam zycia, punkty, level
        message_to_screen2("Life left: " + str(life), white, -20)
        message_to_screen2("Points: " + str(points), white, 10)
        message_to_screen2("Level: " + str(level), white, -20, "small", -550)


        pygame.display.update()

        clock.tick(FPS)

pygame.mixer.music.load('D:\\studia\\wdi\\spaceinvaders\\onestop.mid')
pygame.mixer.music.play()
game_intro()

pygame.quit()
quit()