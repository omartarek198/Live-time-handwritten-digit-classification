import  pandas as pd
import pygame
import numpy
import tensorflow
from tensorflow import keras


model = keras.models.load_model('model.h5')

from PIL import Image

def recognize( ):
    # open method used to open different extension image file
    print ([11] * 1000)
    # im = Image.open(r"8small.png")
    im = Image.open(r"screenshot.png")

    im = im.resize((28, 28))

    im = im.convert('L')
    im = numpy.asarray(im)
    im = numpy.expand_dims(im, 0)
    im = im.astype("float32") / 255
    print(im.shape)

    # print(im)

    y_pred = model.predict(im)

    max = -1
    index = 0

    for i in range(len(y_pred[0])):
        if (y_pred[0][i] > max):
            max = y_pred[0][i]
            index = i

    print(y_pred)

    return index,max


#DrawingArea x,y,w,h
drawingArea = [299,199,280,280]
outputArea = [899,199,280,280]

def CursorInDrawArea(x,y):
    if x >= drawingArea[0] and x <= drawingArea[0] + drawingArea[2]:
        if y > drawingArea[1] and y <= drawingArea[1] + drawingArea[3]:
            return True
    return False



def DrawStrings():
    text_surface = my_font.render('Draw', False, (255, 255, 255))

    screen.blit(text_surface, (drawingArea[0] + drawingArea[2] * 1 / 3, drawingArea[1] - 50))
    text_surface = my_font.render('Enter to Clear', False, (255, 255, 255))
    screen.blit(text_surface, (100, 100))
    text_surface = my_font.render('Space to submit', False, (255, 255, 255))
    screen.blit(text_surface, (100, 150))

    text_surface2 = my_font.render('Output', False, (255, 255, 255))
    screen.blit(text_surface2, (outputArea[0] + outputArea[2] * 1 / 3, outputArea[1] - 50))

def DrawScene():
    MouseDown = False

    DrawStrings()
    while True:
        pygame.draw.rect(screen, [255,255,255], drawingArea,2)
        pygame.draw.rect(screen, [255,255,255],outputArea,2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION and MouseDown:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                pygame.draw.circle(screen, (255, 255, 255),
                                   [x, y], 5, 5)
                if not CursorInDrawArea(x, y):
                    pygame.draw.circle(screen, (0, 0, 0),
                                       [x, y], 5, 5)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                        sub = screen.subsurface(drawingArea)
                        pygame.image.save(sub, "screenshot.png")
                        result, conf = recognize()
                        print(result)
                        text_surface3 = my_fontBIG.render(str(result), False, (255, 255, 255))
                        screen.blit(text_surface3, (outputArea[0] + outputArea[2] * 1 / 4, outputArea[1] - 30))
                if event.key == pygame.K_RETURN:
                            # clear
                            screen.fill((0, 0, 0))
                            pygame.draw.rect(screen, [0, 0, 0], drawingArea, 2)
                            pygame.draw.rect(screen, [0, 255, 0], outputArea, 2)

                            pygame.draw.rect(screen, [255, 255, 255], drawingArea, 2)
                            pygame.draw.rect(screen, [255, 255, 255], outputArea, 2)
                            DrawStrings()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # MakeBall(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                MouseDown= True
            if event.type == pygame.MOUSEBUTTONUP:

                MouseDown = False


            pygame.display.flip()
            fpsClock.tick(fps)


# recognize( Image.open(r"1.png"))



# Configuration

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 640
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 0))
my_font = pygame.font.SysFont('arial', 30)
my_fontBIG = pygame.font.SysFont('arial', 290)

DrawScene()