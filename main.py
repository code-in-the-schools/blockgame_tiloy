import pygame
import paddle
import block

ScreenW, ScreenH = 1280,720
backgroundColor = [123,126,130]

offset = 30
PaddleW = 200
PaddleH = 25
Paddlex = ScreenW / 2 - PaddleW / 2
Paddley = ScreenH - PaddleH - offset

n = 10
BlockW = ScreenW / n
BlockH = BlockW / 2
print
pygame.init()

pygame.display.set_caption("Breakout game")
Display = pygame.display.set_mode([ScreenW, ScreenH])

Display.fill(backgroundColor)

player = paddle.paddle(Paddlex, Paddley, PaddleW, PaddleH )

block = []

for x in range(0,int(ScreenW),int(BlockW)):
      blocks.append(block.Block(x,50,BlockW,BlockH))

    

FPSClock = pygame.time.Clock()
FPS = 60
    
Gameover = False
print
    
while not Gameover:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
             Gameover = True
          Display.fill(backgroundColor)
          mousex = pygame.mouse.get_pos()[0]
          player.draw(Display)
          player.move(mousex)
          for i in range(len(blocks)):
            block[i].draw(display)
           pygame.display.flip()
         pygame.display.update()
           FPSClock.tick(FPS)
           print
         
pygame.quit()
          