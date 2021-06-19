# How to load a Tensorflow model using OpenCV
# Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/

#ref links
#https://jeanvitor.com/tensorflow-object-detecion-opencv/
#https://ashwin-phadke.github.io/post/load-tensorflow-models-using-opencv/
#https://thedatafrog.com/en/articles/human-detection-video/

import cv2
import mailing
# Load a model imported from Tensorflow
#currently using Mobilenet_v1_2017
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')

#specify the object you want to detect (otherwise too many boxes)
detection_class = 1 #look it up from the coco_labels.txt file (its for person)

# open webcam video stream by first starting the window
cv2.startWindowThread()
cap = cv2.VideoCapture(0)

#while ctrl+c is not pressed
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # resizing for faster detection
    img = cv2.resize(frame, (300, 300))
    rows, cols, channels = img.shape
     
    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # breaking the loop if the user types q
        # note that the video window must be highlighted!
        break
    # Loop on the outputs

    for detection in networkOutput[0,0]:
        score = float(detection[2])
        #https://heartbeat.fritz.ai/real-time-object-detection-on-raspberry-pi-using-opencv-dnn-98827255fa60
        detected_class = int(detection[1])
        #print("classid ",detection[1]) 
        if score > 0.2 and detected_class==detection_class:
         
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
     
            #draw a red rectangle around detected objects
            cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
            cv2.imwrite('person.png', img)
            mailing.send_warning()
            # Show the image with a rectagle surrounding the detected objects 
        cv2.imshow('Image', img)
        cv2.waitKey(1)
            


cap.release()
cv2.destroyAllWindows()
# the following is necessary on the mac,
# maybe not on other platforms:
cv2.waitKey(1)

