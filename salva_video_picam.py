import picamera
from time import sleep

camera = picamera.PiCamera()
camera.capture('image_mia1.jpg')

camera.start_preview()
camera.vflip = True
camera.hflip = True
camera.brightness = 60

camera.start_recording('video_mio1.h264')
sleep(5)
camera.stop_recording()



#raspistill -k

#You should see a preview appear on the screen. 
#It doesn’t matter if the picture is upside-down; 
#you can configure this later. Press Ctrl + C 
#to exit the preview.

#Some Power Details

#The Guide 10 Recharger Pack is rated for 2300mAh at 4.8V. 
#The Raspberry Pi with the LCD and Wi-Fi will probably 
#draw between 500–1000mA per hour, so a 2300mAh battery 
#pack should last around 2 hours. I would recommend 
#against pushing this limit. 
#If the battery can’t supply enough power 
#you may end up losing the contents 
#of your SD card, or worse.