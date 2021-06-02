# Music Recommendation System based on Facial Emotions Recognition

### About Project 

Face recognition technology has widely attracted attention due to its enormous application value and market potential. It is being implemented in various fields like security system, digital video processing, and many such technological advances. Additionally, music is the form of art, which is known to have a greater connection with a person’s emotions.
It has got a unique ability to lift up one’s mood. Relatively, this project focuses on building an efficient music recommendation system which determines the emotion of user using Facial Recognition techniques. The algorithm implemented would prove to be more proficient than the existing systems.
The overall concept of the system is to recognize facial emotions and recommend songs efficiently. The proposed system will be both time and cost efficient.
 
### Workflow

The first step is to import the necessary libraries by installing them into your system. The main libraries required for this project are the following:
1. TensorFlow
2. Numpy
3. Song Dataset
4. Haarcascade files
5. Dlib
6. OpenCV
7. GUI (Tkinter)


#### Installation
##### > For windows users:
(run those in command prompt/cmd/terminal)

1. `pip install tensorflow`

2. `pip install numpy`

3. `pip install opencv-python`

4. Dlib and Haarcascade files to be downloaded as external zip files and extract it to the main project directory/folder where your project files are stored.
OR If you are using PyCharm IDE, you can directly install the dlib library in the project settings ---> Configure Interpreter, and add your required libraries from there.

5. Song dataset can be downloaded from any online sites which allows .mp3, .mp4, .avi, .wav, .mpeg and other music extension files for free download.
Also, you  can make your own Expression dataset (NOTE: You can downlaod expression images from google, or you can record your video and make diffrent facial expressions, and convert them into Grayscale images(For more accurate prediction)).

### What steps you have to follow??
- Download this repository.
- Make 'Images' folder in your project, make subfolder for emotions like Happy, Sad, Fear, Angry etc.
- Use `Frames.py` file to convert your own or any live video into frames of images to get a large dataset. 
- Put `Face_crop.py` & `haarcascade_frontalface_alt.xml` in every type of image folder, ex: put this program in "happy" image folder and run this program. It will detect faces from images and convert it into grayscale and makes new images in the same folder.
- Make 'Songs' folder and make subfolders for emotions and put Songs like Happy songs in "Happy" folder.
- After that you have to create the model, for that you can copy the code from code.txt file and open terminal in your project folder and paste it & hit enter.
- It will take aaround 20-25 minutes to train the model completely, use large number of datasets for getting best accuracy. Our model after training achieved 95.8% accuracy.
- After training it will create two files called as `retrained_graph.pb` & `retrained_labels.txt`.
- Now run `music_player_webcam.py` (give proper path of songs and Mediaplayer according to your location inside the program/code).
- You can also interface this with the `music.py` file which is a GUI based music app that plays songs based on facial emotions. This work was not able to complete by us in this project, but we have provided the GUI code for music app as well separately and we'll combine it soon and update it in our GitHub repositories.
- That's all..!!
