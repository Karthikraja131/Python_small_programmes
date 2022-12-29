"""
import cv2
vidcap = cv2.VideoCapture('/home/baatutech/Desktop/images_for_training/images_8_6_2022/Pornography/Videos_images/bb_finished/position_video5/porn_position5_video/porn_position5_video.mp4')
success,image = vidcap.read()
count = 1
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*10))
    cv2.imwrite("frame%d.jpg" % count, image)
    print('Read a new frame: ', success)
    count += 5
"""
import cv2
import os
cam = cv2.VideoCapture("/home/baatutech/Desktop/images_for_training/images_8_6_2022/Pornography/Videos_images/bb_finished/position_video5/porn_position5_video/porn_position5_video.mp4")
currentframe = 0
while(True):
    ret,frame = cam.read()
    if ret:
      cam.set(cv2.CAP_PROP_POS_MSEC,(currentframe*100000))
      name = 'Video to Images\Frame(' + str(currentframe) + ').jpg'
      cv2.imwrite(name, frame)
      print('Read a new frame: ',ret)
      currentframe += 1
    else:
        break
#cam.release()
#cv2.destroyAllWindows()   
    
