import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
#DO NOT TOUCH ABOVE THIS LINE
#Do your work Below
red=random.randint(0, 255)
green=random.randint(0, 255)
blue=random.randint(0, 255)
rg=(red+green)//3
bg=(blue+green)//3
rb=(red+blue)//3

class cube(object):
  
  snakeColor=(bg,green,red)
  
  rows=20
  pixelWidth= 500
  
  def __init__(self,start, directionX=1,directionY=0, color=snakeColor):
    self.pos=start
    self.directionX=1
    self.directionY=0
    self.color=color
  
  def move(self, directionX, directionY):
    self.directionX = directionX
    self.directionY = directionY
    
    self.pos = (self.pos[0] + self.directionX, self.pos[1] + self.directionY)
    
  def draw(self,surface, eyes = False):
    dis = self.pixelWidth // self.rows
    rowPos = self.pos[0] #row
    columnPos = self.pos[1] #column
    
    pygame.draw.rect(surface, self.color, (rowPos*dis+1,columnPos*dis+1, dis-2, dis-2)) #just give. done to draw INSIDE of the grid lines
    if eyes == True:
      centre = dis//2
      radius = 3
      circleMiddle = (rowPos*dis+centre-radius,columnPos*dis+8)
      circleMiddle2 = (rowPos*dis + dis -radius*2, columnPos*dis+8)
      pygame.draw.circle(surface, (225,225,225), circleMiddle, radius)
      pygame.draw.circle(surface, (225,225,225), circleMiddle2, radius)


class snake(object):
  body=[]
  turns={}
  red=random.randint(0, 255)
  green=random.randint(0, 255)
  blue=random.randint(0, 255)
  
  
  
  def __init__(self, color, pos):
    self.color=color
    self.head=cube(pos)
    self.body.append(self.head)
    self.directionX = 0
    self.directionY = 1
    
  def draw(self, surface):
    for i, c in enumerate(self.body):
      if i == 0: #checking if first spawn, used to add eyes. 
        c.draw(surface, True)
      else:
        c.draw(surface)
        
  def reset(self,color,pos):
    
    self.head = cube(pos)
    self.body = []
    self.body.append(self.head)
    self.turns = {}
    self.directionX = 0
    self.directionY = 1
    Red=random.randint(0, 255)
    Green=random.randint(0, 255)
    Blue=random.randint(0, 255)
    
        
  def addCube(self, color):
   
    tail=self.body[-1]
    dx = tail.directionX
    dy = tail.directionY
    
    
    if dx == 1 and dy == 0:
      self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
    elif dx == -1 and dy == 0:
      self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
    elif dx == 0 and dy == 1:
      self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
    elif dx == 0 and dy == -1:
      self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
      
    self.body[-1].directionX =dx
    self.body[-1].directionY =dy

    
    
    
  def move(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        
      keys = pygame.key.get_pressed() #gets a list of all key values if they are pressed. can key each key if you want
      
      for key in keys: #loop
        if keys[pygame.K_a]: #conditionals
          self.directionX = -1
          self.directionY = 0
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
        elif keys[pygame.K_LEFT]: #conditionals
          self.directionX = -1
          self.directionY = 0
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY] #the : in pos[:] is to make a COPY
          #the : in pos[:] is to make a COPY
          
        elif keys[pygame.K_d]: #use elif to prevent multiple keys being registered
          self.directionX = 1
          self.directionY = 0
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
        elif keys[pygame.K_RIGHT]: #use elif to prevent multiple keys being registered
          self.directionX = 1
          self.directionY = 0
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
          
        elif keys[pygame.K_w]:
          self.directionX = 0
          self.directionY = -1
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
        elif keys[pygame.K_UP]:
          self.directionX = 0
          self.directionY = -1
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
          
        elif keys[pygame.K_s]:
          self.directionX = 0
          self.directionY = 1
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
        elif keys[pygame.K_DOWN]:
          self.directionX = 0
          self.directionY = 1
          self.turns[self.head.pos[:]] = [self.directionX, self.directionY]
     
          
    for i, c in enumerate(self.body): #pull for list. Just give to students or rewrite
      p = c.pos[:]
      if p in self.turns:
        turn = self.turns[p]
        c.move(turn[0], turn[1])
        if i == len(self.body)-1:
          self.turns.pop(p)#remove the position from the list so it doesn't automatically turn when you go there
          
      else: #checks to see if we are at the end of the string, used to make it so you move to otherside of screen
        if c.directionX == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
        elif c.directionX == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
        elif c.directionY == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
        elif c.directionY == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
        else: c.move(c.directionX,c.directionY)
    
def drawGrid(w, rows, surface):
  sizeBetween= w//rows
  x=0
  y=0
  
  for l in range(rows):
    x= x + sizeBetween
    y = y + sizeBetween
    
    pygame.draw.line(surface,(rb,rg, bg), (x,0), (x,w)) 
    pygame.draw.line(surface,(rb, rg, bg), (0,y), (w,y)) 

def redrawWindow(surface):
  global rows, width, box, theSnake
  surface.fill((red, green, blue))
  box.draw(surface)
  theSnake.draw(surface)
  drawGrid(width, rows, surface)
  pygame.display.update()
  
def randomBox(rows,item,):
  positions = item.body
  
  while True:
    x = random.randrange(rows)
    y = random.randrange(rows)
    
    #checks to make sure a apple isn't on top of the snake
    if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: #give to students. 
      continue
    else:
      break
    
  return (x, y)
def messageBox(subject, content):
  root = tk.Tk()
  root.attributes("-topmost", True)
  root.withdraw()
  messagebox.showinfo(subject, content)
  try:
    root.destroy()
  except:
    pass

def main():
  boxColor=(blue,red,green)
  global rows, width, box,theSnake
  width= 500
  rows= 20
  
  window= pygame.display.set_mode((width,width))
  theSnake=snake((blue, red, green),(10,10))
  box=cube((15,15),color=boxColor)
  
  flag = True #if true keep game running
  
  clock=pygame.time.Clock()
  
  while flag:
    
    posX=random.randint(0, 20)
    posY=random.randint(0, 20)
    pygame.time.delay(10)
    clock.tick(10)
    theSnake.move()
    
    if theSnake.body[0].pos==box.pos:
      theSnake.addCube(color=(green,red,blue))
      box = cube(randomBox(rows,theSnake),color=(green,red,blue))
    
    for x in range(len(theSnake.body)):
      if theSnake.body[x].pos in list(map(lambda z:z.pos,theSnake.body[x+1:])):
        print("Score: ", len(theSnake.body))
        messageBox("You Lost Try Again", "Play Again")
        theSnake.reset((blue, red, green),(10,10))
        break
    
    redrawWindow(window)
  pass
  

  #do not go below this line
  
main()


