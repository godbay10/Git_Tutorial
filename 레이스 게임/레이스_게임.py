
from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene=Scene('레이스', 'SantaRace/background.png')

PlayButton=Object('SantaRace/play.png')
PlayButton.locate(scene,500,30)

PlayButton2=Object('SantaRace/play-90.png')
PlayButton2.locate(scene,700,20)
PlayButton2.setScale(1.3)

StartButton=Object('SantaRace/start.png')
StartButton.locate(scene,590,70)
StartButton.show()

EndButton=Object('SantaRace/end.png')
EndButton.locate(scene,590,20)
EndButton.show()

santa=Object('SantaRace/santa.png')
santa.x=0
santa.y=100
santa.locate(scene,santa.x,santa.y)
santa.show()

timer=Timer(15.0)
showTimer(timer)

showMessage('자고로 산타는 하늘도 날 줄 알아야지. 미션을 마치려면 위로도 날라가야해!')

def PlayButton2_onMouseAction(x,y,action):
    santa.y=santa.y+30
    santa.locate(scene,santa.x,santa.y)
PlayButton2.onMouseAction=PlayButton2_onMouseAction

def PlayButton_onMouseAction(x,y,action):
    santa.x=santa.x+30
    santa.locate(scene,santa.x,santa.y)
    if santa.x>1280:
      a=True
    if santa.x>1280 and santa.y>600:
      showMessage('미션 성공')
      PlayButton.hide()
      PlayButton2.hide()
      StartButton.setImage('SantaRace/restart.png')
      StartButton.show()
      EndButton.show()
      timer.stop()
PlayButton.onMouseAction=PlayButton_onMouseAction


def EndButton_onMouseAction(x,y,action):
    endGame()
EndButton.onMouseAction=EndButton_onMouseAction

def StartButton_onMouseAction(x,y,action):
    StartButton.hide()
    EndButton.hide()
    PlayButton.show()
    PlayButton2.show()

    timer.set(15.0)
    timer.start()

    santa.x=0
    santa.y=100
    santa.locate(scene,santa.x,santa.y)
StartButton.onMouseAction=StartButton_onMouseAction

def timer_On():
    showMessage('미션 실패')
timer.onTimeout=timer_On

startGame(scene)