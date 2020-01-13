gJump=0
gY=0

def setup():
    size (800,600)
    background(49, 204, 196)
    # frameRate (10)
    
def bird():
    bird=createShape(GROUP)
    head=createShape (ELLIPSE, 425,285,25,25)
    body= createShape(ELLIPSE, 400,300, 50,40)
    wing=createShape (TRIANGLE, 415, 300, 410, 315, 400, 290)
    fill(255, 240, 25)
    bird.addChild(body)
    bird.addChild(head)
    bird.addChild(wing)
    #shape(bird)
    #translate(-200, 100)
    shape(bird)
    
def keyPressed():
    if keyCode==32:
        global gJump
        gJump+=1
    
    
def draw():
    global gY
    global gJump
         
    background(49, 204, 196)
    
    lNewY=-(gJump*50)+gY
            
    translate (-200,lNewY)
    if lNewY<250:
        gY+=1
    bird()
