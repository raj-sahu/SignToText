import argparse
from keras.models import Model, load_model
import pickle
import cv2
import os
import numpy as np
from hand_tracker import handtracking


model = load_model('SignToText5.h5')


def predict_video():
    # model = load_model('SignToText4.h5')
    repeat = True

    while repeat:
        repeat = False
        handtracking()

        textscreen = np.zeros((512, 512, 3))
        cap = cv2.VideoCapture('outputWebCan.mp4')

        i = 0
        testdata = []
        predictions = []
        imgdata = []

        while(cap.isOpened() and i <= 100):

            ret, frame = cap.read()

            if ret == None:
                break

            image = frame
            try:
                result = image.copy()
            except:
                break

            result = cv2.resize(result, (256, 256))

            imgdata.append(result)

            if len(imgdata) == 16:
                testdata.append(imgdata)
                imgdata = []

            i += 1

        testdata = np.array(testdata)

        for data in testdata:
            predictions.append((np.argmax(model.predict(data), axis=-1)))
        print("PREDICTED:>>>", predictions)

        # cv2.putText(textscreen, "Press Space to Restart or Esc to Quit",
        #             (0, 500), 0, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(textscreen, "Press Space to Restart or Esc to Quit",
                    (0, 500), cv2.FONT_ITALIC, 1, (255, 255, 255))

        for j in range(len(predictions)):
            result = np.bincount((predictions[j])).argmax()
            labels = ["Bright", "Green", "Light-Blue",
                      "Opaque", "Red", "Yellow"]

            print("       TEXT            ", labels[result])
            cv2.putText(textscreen, labels[result], ((70), 40+200*j),
                        0, 1, (255, 255, 255), 2, cv2.LINE_AA)

        while True:
            cv2.imshow("Sign->Text", textscreen)
            key = cv2.waitKey(1)
            if key & 0xFF == 27:
                break
            if key % 256 == 32:
                repeat = True
                break


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("model", help="model to be executed")
    # args = parser.parse_args()
    # model_file = args.graph

    # pickle_in = open("models/EncodedLabels.sav", "rb")
    # EncodedLabels = pickle.load(pickle_in)

    predict_video()
