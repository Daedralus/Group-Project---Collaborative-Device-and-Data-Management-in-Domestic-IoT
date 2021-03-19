from picamera import PiCamera
from time import sleep

i=0
camera = PiCamera()

while (i<10):
    
    camera.start_preview(alpha=200)
    sleep(5)
    camera.capture('/home/pi/Desktop/image'+str(i)+'.jpg')
    camera.stop_preview()
    i=(i+1)%3
    
