
from bangtal import *

import random

x1=random.randrange(10,20)
x2=random.randrange(10,20)

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene1=Scene('농장 게임','Images/농가.jpg')

scene2=Scene('농장 게임','Images/벼.jpg')

Question=Object('Images/의문.jpg')
Question.locate(scene1,1125,580)
Question.setScale(0.08)
Question.show()

scene2a=Object('Images/벼.jpg')
scene2a.locate(scene2,0,0)
scene2a.show()

scene3=Scene('농장 게임','Images/보리.jpg')

scene3a=Object('Images/보리.jpg')
scene3a.locate(scene3,0,0)
scene3a.show()

scene4=Scene('농장 게임','Images/배경-2.png')

door1=Object('Images/문-왼쪽-닫힘.png')
door1.locate(scene4,320,270)
door1.hide()

door2=Object('Images/문-오른쪽-닫힘.png')
door2.locate(scene4,830,280)
door2.hide()

start=Object('Images/start.png')
start.locate(scene1,520,90)
start.setScale(0.2)
start.show()

back1=Object('Images/뒤로가기.png')
back1.locate(scene2,80,40)
back1.setScale(2)

back2=Object('Images/뒤로가기.png')
back2.locate(scene3,80,40)
back2.setScale(2)

basket=Object('Images/바구니.png')
basket.locate(scene4,50,30)
basket.setScale(0.1)
basket.hide()

writing1=Object('Images/벼-글씨.png')
writing1.locate(scene4,310,560)
writing1.setScale(2)
writing1.hide()

writing2=Object('Images/보리-글씨.png')
writing2.locate(scene4,840,570)
writing2.setScale(2)
writing2.hide()

timer1=Timer(20.0)
showTimer(timer1)

def Question_onMouseAction(x,y,action):
    showMessage('벼와 보리를 해당 개수만큼만 바구니에 모아야돼. 벼와 보리 합쳐서 다섯개 이상 들 수 없어. 더 모으려면 바구니에다 저장해야해.')
Question.onMouseAction=Question_onMouseAction

def door1_onMouseAction(x,y,action):
    scene2.enter()
    back1.show()
door1.onMouseAction=door1_onMouseAction

def door2_onMouseAction(x,y,action):
    scene3.enter()
    back2.show()
door2.onMouseAction=door2_onMouseAction

def back1_onMouseAction(x,y,action):
    scene4.enter()
    back1.hide()
back1.onMouseAction=back1_onMouseAction

def back2_onMouseAction(x,y,action):
   scene4.enter()
   back2.hide()
back2.onMouseAction=back2_onMouseAction

a=0
def scene2a_onMouseAction(x,y,action):
    global a,b
    a=a+1
    if a+b>5:
        showMessage('더이상 담을 수 없어. 우선 짐을 비워야해')
        a=a-1
scene2a.onMouseAction=scene2a_onMouseAction

b=0
def scene3a_onMouseAction(x,y,action):   
      global a,b
      b=b+1
      if a+b>5:
          showMessage('더이상 담을 수 없어. 우선 짐을 비워야해')
          b=b-1
scene3a.onMouseAction=scene3a_onMouseAction

a1=0
b1=0
def basket_onMouseAction(x,y,action):
    global a,b
    global a1,b1
    a1=a+a1
    a=a-a
    b1=b+b1
    b=b-b
    if a1==x1 and b1==x2:
        showMessage('성공!')
        timer1.stop()
basket.onMouseAction=basket_onMouseAction

def start_onMouseAction(x,y,action):
    start.hide()
    door1.show()
    door2.show()
    basket.show()
    writing1.show()
    writing2.show()

    timer1.set(20.0)
    timer1.start()

    scene4.enter()

    global x1,x2
    showMessage('벼는'+str(x1)+'개, 보리는'+str(x2)+'개 필요합니다')
start.onMouseAction=start_onMouseAction

def timer1_On():
    showMessage('미션 실패')
timer1.onTimeout=timer1_On

startGame(scene1)


