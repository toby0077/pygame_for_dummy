# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:56:24 2019

Python菜鸟快乐游戏编程_pygame（博主录制，2K分辨率）：http://dwz.date/cfGs
作者邮件：231469242@qq.com
作者微信公众号：PythonEducation
"""
import time,random
import pygame


pygame.init()
display_width=1200
display_height=1000
gameDisplay=pygame.display.set_mode((display_width,display_height))
#设置pygame游戏界面的文字标题和图片
pygame.display.set_caption('肥猫和大熊熊')
gameIcon = pygame.image.load('logo.png')
pygame.display.set_icon(gameIcon)
pygame.display.update()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)

#赋予时间对象
clock=pygame.time.Clock()
block_size=10
fps=30
#暂停键
pause = False

#create a Font object from the system fonts从电脑操作系统里创造一个字体对象
font=pygame.font.SysFont(None,25)
#添加背景音乐Create a new Sound object from a file or buffer object
sound = pygame.mixer.Sound("SevenAttesa.wav")
sound_gameOver = pygame.mixer.Sound("gameover.wav")
#生成蛇
def snake(block_size,snake_list):
    for XnY in snake_list:
        #绘制贪吃蛇的一个方形
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

#绘制字体
def message_to_screen(msg,color):
    #draw text on a new Surface绘制文字到界面上了
    #msg是文字内容
    #TRUE为使用抗锯齿
    #color是颜色参数
    screen_text=font.render(msg,True,color)
    #draw one image onto another在一个图像上绘制一个图像
    #screen_text为文本内容
    #[display_width/2,display_height/2]绘制的位置
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])
 
def gameloop():
    global pause
    #播放音乐
    pygame.mixer.Sound.play(sound,loops=-1)
    gameExit=False
    gameOver=False
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=0
    lead_y_change=0
    #蛇图形列表
    snake_list=[]
    #蛇身长度
    snakeLength=1
    
    randAppleX=round(random.randrange(0+block_size,display_width-block_size)/10)*10
    randAppleY=round(random.randrange(0+block_size,display_height-block_size)/10)*10
    
    while not gameExit:
        while gameOver==True:
            pygame.mixer.Sound.stop(sound)
            pygame.mixer.Sound.play(sound_gameOver,loops=0)
            gameDisplay.fill(black)
            message_to_screen("Game Over,press Q to quit or C to continue",red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key == pygame.K_p:
                    pause = True
                    #paused()
            
        if lead_x>=display_width or lead_x<10 or lead_y>=display_height or lead_y<0:
            gameOver=True
        
        
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(black)
        #绘制一个随机苹果
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snake_list.append(snakeHead)
        
        #如果蛇没有吃掉苹果，那么蛇移动新的位置不会放入snake_list（绘制到屏幕上）
        if len(snake_list)>snakeLength:
            print("snake_list before",snake_list)
            del snake_list[0]
            print("snake_list after",snake_list)
        #生成蛇
        snake(block_size,snake_list)
        pygame.display.update()
        
        #当苹果碰触到蛇后
        if lead_x==randAppleX and lead_y==randAppleY:
            #随机生成一个新的苹果
            randAppleX=round(random.randrange(0+block_size,display_width-block_size)/10)*10
            randAppleY=round(random.randrange(0+block_size,display_height-block_size)/10)*10
            snakeLength+=1
        #控制显示速度快慢
        clock.tick(fps)
    
        
    pygame.quit()
    quit()
    
gameloop()






















