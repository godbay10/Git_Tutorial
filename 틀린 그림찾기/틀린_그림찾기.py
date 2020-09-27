
from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene=Scene('틀린그림찾기','그림예제1.png')

problem=Object('그림예제1.png')
problem.locate(scene,100,0)
problem.show()

class Rect:
    def __init__(self,cx,cy,r):
        self.centerX=cx
        self.centerY=cy
        self.radius=r

    def checkin(self,x,y):
        return self.centerX-self.radius<x<self.centerX+self.radius and self.centerY-self.radius<y<self.centerY+self.radius

k=76
q=5
class DifferencePoint:
    def __init__(self,lcx,rcx,cy,r):
      self.left_rect=Rect(lcx,cy,r)
      self.right_rect=Rect(rcx,cy,r)
      self.left_check=Object('check.png')
      self.left_check.locate(scene,lcx+k,cy-q)
      self.right_check=Object('check.png')
      self.right_check.locate(scene,rcx+k,cy-q)
      self.found=False

    def checkin(self,x,y):
        return self.left_rect.checkin(x,y) or self.right_rect.checkin(x,y)

    def show(self):
        self.left_check.show()
        self.right_check.show()
        self.found=True

points=[
  DifferencePoint(154,695,333,9),
  DifferencePoint(80,619,199,4),
  DifferencePoint(457,996,215,20),
  DifferencePoint(468,1004,276,9),
  DifferencePoint(494,1044,470,6),
]

count=0
def problem_onMouseAction(x,y,action):
    wrong=True
    for p in points:
        if p.checkin(x,y):
            wrong=False
            if p.found==False:
              global count
              count=count+1
              p.show()
    if count==5:
      showMessage('와! 성공입니다!')
        
    if wrong:
      endGame()
problem.onMouseAction=problem_onMouseAction

showMessage('틀린 곳은 총 다섯 군데입니다. 잘 찾아보세요!')
startGame(scene)