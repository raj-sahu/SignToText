import numpy as np
import cv2
import os


def SegmentHand(frame, display=0):
    """
    Segment Hand From An Given Frame

    Args:
        frame ([type]): [description]

    Returns:
        [type]: [description]
    """

    image = frame
    output = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([41, 156, 49])
    upper = np.array([179, 255, 255])

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(output, output, mask=mask)

    output = cv2.resize(output, (256, 256))

    if display == 1:
        while True:
            cv2.imshow("Output", output)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
            if key % 256 == 32:
                repeat = True
                break
    return output


def genrateFrames(vid_dir, frame_limit, No_Class):
    """
    Genrate frames by Splitting The Video in Different Frames and Segmenting 
    Hands in Each Frame 

        PARAMETERS:
        vid_dir (str): Directory of videos

        frame_limit (int): Maximum number of frames per video

        No_Class (int): Enables To Perform This Operation On The Data Srt Partially       
        RETURN:
        X_train: Training Frames

        Y_train: Labels of each frame

    """

    data = []
    signs = os.listdir(vid_dir)

    for sign in signs:
        print("PROCESS >>> ", sign)
        videos = os.listdir(os.path.join(vid_dir, sign))
        for vid in videos:

            i = 0
            cap = cv2.VideoCapture(os.path.join(vid_dir, sign, vid))
            while(cap.isOpened() and i < frame_limit):

                ret, frame = cap.read()
                if ret == False:
                    break
                output = SegmentHand(frame)
                data.append([output, sign])
                i += 1

    cap.release()
    X_train = []
    Y_train = []
    for result, label in data:
        X_train.append(result)
        Y_train.append(label)

    return(X_train, Y_train)


if __name__ == '__main__':
    frame = cv2.imread("hand.png")
    SegmentHand(frame, 1)
    cv2.destroyAllWindows()
