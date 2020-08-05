import pygame,sys

def ball_animation():
  global ball_speed_x,ball_speed_y
  ball.x += ball_speed_x
  ball.y += ball_speed_y

if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *=-1
if ball.left <= 0 or ball.right >= screen_width:
    ball_speed_x *=-1

    if ball.colliderect(player) or ball.colliderect(opponent):
      ball_speed_x *= -1
      
pygame.init()
clock = pygame.time.clock()
'p'
# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.rect(screen_width-20,screen_height/2-70,10,140)
oppnent = pygame.rect(10, screen_height/2-70,10,140)

bg_color= pygame.color('grey12')
light_gray = (200,200,200)

ball_spped_x = 7
ball_speed_y = 7

while True:
  #Handling input
  for event in pygame.evnt.get():
    if event.type == pygame.Quit:
      pygame.quit()
      sys.exit()

      ball.x += ball_speed_x
      ball.y += ball_speed_y

if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *=-1
if ball.left <= 0 or ball.right >= screen_width:
    ball_speed_x *=-1

    if ball.colliderect(player or ball.colliderect(opponent):
      ball_speed_x *= -1
#Visuals
screen.fill(bg.color)
pygame.draw.rect(screen,light_gray,player)
pygame.draw.rect(screen,light_gray,opponent)
pygame.darw.ellipse(screen,light_grey,ball)
pygame.draw.aaline(screen,light_gray,(screen_width/2,0),(screen_width/2,screen_height))

#Updating the window
      pygame
      clock.tick(60)