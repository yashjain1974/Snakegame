import pygame
import random
import os
pygame.init()
pygame.mixer.init()            #To play music



#colors
yellow=(255,255,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

#declaring variables

game_height = 500
game_width = 800
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,20)
font1=pygame.font.SysFont(None,40)

#game display
game_window=pygame.display.set_mode((game_width,game_height))
pygame.display.update()
#background image

bgimg1=pygame.image.load("welcome.png")
bgimg2=pygame.image.load("pic.jpg")
bgimg3=pygame.image.load("background 1.png")
bgimg4=pygame.image.load("background 2.png")
bgimg5=pygame.image.load("background.png")
bgimg6=pygame.image.load("space.png")
bgimg7=pygame.image.load("game_over.jpg")

bgimg1=pygame.transform.scale(bgimg1,(game_width,game_height)).convert_alpha()
bgimg2=pygame.transform.scale(bgimg2,(game_width,game_height)).convert_alpha()
bgimg3=pygame.transform.scale(bgimg3,(game_width,game_height)).convert_alpha()
bgimg4=pygame.transform.scale(bgimg4,(game_width,game_height)).convert_alpha()
bgimg5=pygame.transform.scale(bgimg5,(game_width,game_height)).convert_alpha()
bgimg6=pygame.transform.scale(bgimg6,(game_width,game_height)).convert_alpha()




def plot_snake(game_window,color,snake_size_x,snake_size_y,snk_list):
    for x,y in snk_list:
       pygame.draw.ellipse(game_window, color, [x,y,snake_size_x,snake_size_y])

def screen_text(text,color,x,y):
    text_screen=font.render(text,True,color)
    game_window.blit(text_screen,[int(x),int(y)])

def welcome_text(text,color,x,y):
    text_screen=font1.render(text,True,color)
    game_window.blit(text_screen,[int(x),int(y)])

def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill((234,200,206))
        game_window.blit(bgimg1, (0, 0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:

                    background()
        pygame.display.update()
        clock.tick(60)


#game title
pygame.display.set_caption("Snake Game")
def background():
    exit_game = False
    while not exit_game:
        game_window.fill((234, 200, 206))
        game_window.blit(bgimg2, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
             if event.key == pygame.K_1:
              game_loop1()
             if event.key==pygame.K_2:
              game_loop2()
             if event.key==pygame.K_3:
              game_loop3()
             if event.key==pygame.K_4:
              game_loop4()
        pygame.display.update()
        clock.tick(60)


#Creating loop
def game_loop1():
    # declaring variables
    exit_game = False
    game_over=False
    x_pos = 45
    y_pos = 45
    x_velocity = 0
    y_velocity = 0
    init_velocity = 2
    snake_size_x = 15
    snake_size_y = 15
    fps = 100
    food_size = 10
    score = 0
    snk_list = []
    snk_len = 1
    food_x = random.randint(20, game_width - 50)
    food_y = random.randint(20, game_height - 50)

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:   #creating loop
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg3, (0, 0))

            screen_text("Game over! Press enter key to continue",red,game_width/2-120,game_height/2-20)
            screen_text(f"Your score :-{score}", red, game_width / 2 - 120, game_height / 2 + 20)

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:

                    exit_game=True


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:     #creating keys actions
                    if event.key==pygame.K_RIGHT:
                        x_velocity=init_velocity
                        y_velocity=0
                    if event.key==pygame.K_DOWN:
                        y_velocity=init_velocity
                        x_velocity =0
                    if event.key==pygame.K_LEFT:
                        x_velocity = -init_velocity
                        y_velocity = 0
                    if event.key==pygame.K_UP:
                        y_velocity=-init_velocity
                        x_velocity = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_r:
                        highscore=0

                         #filling game window color
            x_pos=x_pos+x_velocity               #creating motion in snake
            y_pos=y_pos+y_velocity
            if abs(x_pos-food_x)<10 and abs(y_pos-food_y)<10:
                score+=10

                food_x = random.randint(20, game_width - 50)
                food_y = random.randint(20, game_height - 50)
                snk_len+=6
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                if score>int(highscore):

                    highscore=score


                 #drawing snake head       #creating snake head
            if snk_len>200:
                init_velocity=3
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg3, (0, 0))
            screen_text(f"Score:-{score}                                                  High Score:-{highscore}", blue, 5, 5)
            screen_text("Created by :-Yash jain",black,600,470)

            pygame.draw.rect(game_window, black, [food_x, food_y, food_size, food_size])
            head=[]
            head.append(x_pos)
            head.append(y_pos)
            snk_list.append(head)
            if len(snk_list) > snk_len:

                del snk_list[0]
            if x_pos<0 or x_pos>game_width or y_pos<0 or y_pos>game_height:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window,red, snake_size_x,snake_size_y, snk_list)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def game_loop2():
    # declaring variables
    exit_game = False
    game_over=False
    x_pos = 45
    y_pos = 45
    x_velocity = 0
    y_velocity = 0
    init_velocity = 2
    snake_size_x = 15
    snake_size_y = 15
    fps = 100
    food_size = 10
    score = 0
    snk_list = []
    snk_len = 1
    food_x = random.randint(20, game_width - 50)
    food_y = random.randint(20, game_height - 50)

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:   #creating loop
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg4, (0, 0))

            screen_text("Game over! Press enter key to continue",red,game_width/2-120,game_height/2-20)
            screen_text(f"Your score :-{score}", red, game_width / 2 - 120, game_height / 2 + 20)

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:

                    exit_game=True


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:     #creating keys actions
                    if event.key==pygame.K_RIGHT:
                        x_velocity=init_velocity
                        y_velocity=0
                    if event.key==pygame.K_DOWN:
                        y_velocity=init_velocity
                        x_velocity =0
                    if event.key==pygame.K_LEFT:
                        x_velocity = -init_velocity
                        y_velocity = 0
                    if event.key==pygame.K_UP:
                        y_velocity=-init_velocity
                        x_velocity = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_r:
                        highscore=0

                         #filling game window color
            x_pos=x_pos+x_velocity               #creating motion in snake
            y_pos=y_pos+y_velocity
            if abs(x_pos-food_x)<10 and abs(y_pos-food_y)<10:
                score+=10

                food_x = random.randint(20, game_width - 50)
                food_y = random.randint(20, game_height - 50)
                snk_len+=6
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                if score>int(highscore):

                    highscore=score


                 #drawing snake head       #creating snake head
            if snk_len>200:
                init_velocity=3
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg4, (0, 0))
            screen_text(f"Score:-{score}                                                  High Score:-{highscore}", blue, 5, 5)
            screen_text("Created by :-Yash jain",black,600,470)

            pygame.draw.rect(game_window, black, [food_x, food_y, food_size, food_size])
            head=[]
            head.append(x_pos)
            head.append(y_pos)
            snk_list.append(head)
            if len(snk_list) > snk_len:

                del snk_list[0]
            if x_pos<0 or x_pos>game_width or y_pos<0 or y_pos>game_height:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window,red, snake_size_x,snake_size_y, snk_list)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def game_loop3():
    # declaring variables
    exit_game = False
    game_over=False
    x_pos = 45
    y_pos = 45
    x_velocity = 0
    y_velocity = 0
    init_velocity = 2
    snake_size_x = 15
    snake_size_y = 15
    fps = 100
    food_size = 10
    score = 0
    snk_list = []
    snk_len = 1
    food_x = random.randint(20, game_width - 50)
    food_y = random.randint(20, game_height - 50)

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:   #creating loop
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg5, (0, 0))

            screen_text("Game over! Press enter key to continue",red,game_width/2-120,game_height/2-20)
            screen_text(f"Your score :-{score}", red, game_width / 2 - 120, game_height / 2 + 20)

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:

                    exit_game=True


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:     #creating keys actions
                    if event.key==pygame.K_RIGHT:
                        x_velocity=init_velocity
                        y_velocity=0
                    if event.key==pygame.K_DOWN:
                        y_velocity=init_velocity
                        x_velocity =0
                    if event.key==pygame.K_LEFT:
                        x_velocity = -init_velocity
                        y_velocity = 0
                    if event.key==pygame.K_UP:
                        y_velocity=-init_velocity
                        x_velocity = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_r:
                        highscore=0

                         #filling game window color
            x_pos=x_pos+x_velocity               #creating motion in snake
            y_pos=y_pos+y_velocity
            if abs(x_pos-food_x)<10 and abs(y_pos-food_y)<10:
                score+=10

                food_x = random.randint(20, game_width - 50)
                food_y = random.randint(20, game_height - 50)
                snk_len+=6
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                if score>int(highscore):

                    highscore=score


                 #drawing snake head       #creating snake head
            if snk_len>200:
                init_velocity=3
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg5, (0, 0))
            screen_text(f"Score:-{score}                                                  High Score:-{highscore}", blue, 5, 5)
            screen_text("Created by :-Yash jain",black,600,470)

            pygame.draw.rect(game_window, black, [food_x, food_y, food_size, food_size])
            head=[]
            head.append(x_pos)
            head.append(y_pos)
            snk_list.append(head)
            if len(snk_list) > snk_len:

                del snk_list[0]
            if x_pos<0 or x_pos>game_width or y_pos<0 or y_pos>game_height:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window,red, snake_size_x,snake_size_y, snk_list)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
def game_loop4():
    # declaring variables
    exit_game = False
    game_over=False
    x_pos = 45
    y_pos = 45
    x_velocity = 0
    y_velocity = 0
    init_velocity = 2
    snake_size_x = 15
    snake_size_y = 15
    fps = 100
    food_size = 10
    score = 0
    snk_list = []
    snk_len = 1
    food_x = random.randint(20, game_width - 50)
    food_y = random.randint(20, game_height - 50)

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:   #creating loop
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill((234, 200, 206))
            game_window.blit(bgimg6, (0, 0))

            screen_text("Game over! Press enter key to continue",red,game_width/2-120,game_height/2-20)
            screen_text(f"Your score :-{score}", red, game_width / 2 - 120, game_height / 2 + 20)

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:

                    exit_game=True


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():       #creating event handler
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:     #creating keys actions
                    if event.key==pygame.K_RIGHT:
                        x_velocity=init_velocity
                        y_velocity=0
                    if event.key==pygame.K_DOWN:
                        y_velocity=init_velocity
                        x_velocity =0
                    if event.key==pygame.K_LEFT:
                        x_velocity = -init_velocity
                        y_velocity = 0
                    if event.key==pygame.K_UP:
                        y_velocity=-init_velocity
                        x_velocity = 0
                    if event.key==pygame.K_q:
                        score+=10
                    if event.key==pygame.K_r:
                        highscore=0

                         #filling game window color
            x_pos=x_pos+x_velocity               #creating motion in snake
            y_pos=y_pos+y_velocity
            if abs(x_pos-food_x)<10 and abs(y_pos-food_y)<10:
                score+=10
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(20, game_width - 50)
                food_y = random.randint(20, game_height - 50)
                snk_len+=6

                if score>int(highscore):

                    highscore=score


                 #drawing snake head       #creating snake head
            if snk_len>200:
                init_velocity=3
            game_window.fill((234,200,206))
            game_window.blit(bgimg6, (0, 0))
            screen_text(f"Score:-{score}                                                  High Score:-{highscore}", white, 25, 10)
            screen_text("Created by :-Yash jain",white,600,470)

            pygame.draw.rect(game_window, green, [food_x, food_y, food_size, food_size])
            head=[]
            head.append(x_pos)
            head.append(y_pos)
            snk_list.append(head)
            if len(snk_list) > snk_len:

                del snk_list[0]
            if x_pos<0 or x_pos>game_width or y_pos<0 or y_pos>game_height:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("game_over1.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window,red, snake_size_x,snake_size_y, snk_list)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
