import time
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 4
# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
global text
webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.
now = time.time()  ###For calculate seconds of video
future = now + 60  ####here is second of time which taken by emotion recognition system ,you can change it
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test_sam.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Smile':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)

        if text == 'Fear':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == 'Sad':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)

    # Show the image/
    cv2.imshow('Music Recommendation based on Facial Expressions', im)
    key = cv2.waitKey(30)& 0xff
    if time.time() > future:##after 20second music will play
        try:
            cv2.destroyAllWindows()
            mp = 'C:/Program Files/Windows Media Player/wmplayer.exe'
            if text == 'Angry':
                randomfile = random.choice(os.listdir("C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Angry/"))
                print('You are angry !!!! Please calm down :) , I will play a song for you to calm down:' + randomfile)
                file = ('C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Angry/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Smile':
                randomfile = random.choice(os.listdir("C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Smile/"))
                print('You are smiling :) , I will play a special song for you: ' + randomfile)
                file = ('C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Smile/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Fear':
                randomfile = random.choice(os.listdir("C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Fear/"))
                print('You have fear of something :( , I will play this song for you to make you feel better: ' + randomfile)
                file = ('C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Fear/' + randomfile)
                subprocess.call([mp, file])

            if text == 'Sad':
                randomfile = random.choice(os.listdir("C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Sad/"))
                print('You are sad, dont worry :) ,I am playing a good song for you: ' + randomfile)
                file = ('C:/Users/mrsam/PycharmProjects/Music-Recommendation-based-on-Facial-Expressions/Songs/Sad/' + randomfile)
                subprocess.call([mp, file])
            break

        except :
            print('Please stay focus in Camera frame atleast 15 seconds & run this program again :)')
            break

    if key == 27:  # The Esc key
        break