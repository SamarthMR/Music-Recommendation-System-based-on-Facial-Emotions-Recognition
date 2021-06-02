import cv2
import os
#import pafy
# for youtube
#url = 'https://youtu.be/VwtuKykuTXs'
#vPafy = pafy.new(url)
#play = vPafy.getbest(preftype="mp4") #webm
#cap = cv2.VideoCapture("C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/images/Angry/My face emotions.mp4")
#cap = cv2.VideoCapture(play.url)

video_path = 'C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/videos/Smile-1.mp4' # video name
output_path = 'C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/images/Smile' # location on ur pc

if not os.path.exists(output_path):
     os.makedirs(output_path)


cap = cv2.VideoCapture(video_path)
#cap = cv2.VideoCapture(play.url)
index = 0

while cap.isOpened() :
     Ret, Mat = cap.read()
     
     if Ret :
          index += 1
          if index % 9 != 0 :
               continue
          
          cv2.imwrite(output_path + '/' + str(index) + '.png', Mat)
     
     else:
          break

cap.release()