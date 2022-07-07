import pygame as pg
import time
import random

pg.init()


white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

dis_wid = 400
dis_len = 400


dis = pg.display.set_mode((dis_wid, dis_len))
pg.display.set_caption('My Snake Game')

clock = pg.time.Clock()

snake_speed = 15
snake_block = 10

font_style = pg.font.SysFont('arial', 20)
score_font = pg.font.SysFont('comicsansms', 25)



def our_snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def score_msg(msg, color):
    mesg = score_font.render("Your Score:"+msg, True, color)
    dis.blit(mesg, [5, 2])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_wid/4, dis_len/3])

def generate_food():
    foodx = round(random.randrange(0, dis_wid - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_wid - snake_block) / 10.0) * 10.0
    return foodx, foody

def game_loop():
    game_over = False
    game_close = False

    x1 = dis_wid / 2
    y1 = dis_len / 2

    x1_change = 0
    y1_change = 0
    score = 1
    snake_list = []
    
    foodx , foody = generate_food()

    while not game_over:
        
        while game_close == True:
            dis.fill(white)
            message("You Lost! q: quit c: cont", red)
            pg.display.update()
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        game_loop()    
                          
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pg.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pg.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        
        if x1 >= dis_wid or x1 <= 0 or y1 >= dis_len or y1 <= 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        
        pg.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])       
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > score:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        our_snake(snake_block, snake_list)
        score_msg(str(score-1), green)
        pg.display.update()
        
        
        if x1 == foodx and y1 == foody:
            print("yummy")
            foodx, foody = generate_food()
            score+=1
            score_msg(str(score-1), green)
            pg.display.update()
        
            
        clock.tick(snake_speed)
    pg.quit()
    quit()
        
game_loop()
