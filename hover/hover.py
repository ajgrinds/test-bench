import cv2
from time import sleep

IP_ADDRESS = 0
CROP_PERCENTAGE = 0.025  # 2.5% to start NOTE: This is 2.5% on 4 sides or 5% of the height and 5% of the width


cap = cv2.VideoCapture(IP_ADDRESS)


def compare_frames(first_frame, last_frame):  # pass in a CV2 image (second output from cv2.read)
    height, width, channels = first_frame.shape()
    # crop the image by 2.5% (0.025) on each side, this allows the image to be compared, this value could easily be
    # played with in the variable above

    first_cropped = first_frame[height * CROP_PERCENTAGE:height * (1 - CROP_PERCENTAGE),
                                width * CROP_PERCENTAGE:width * (1 - CROP_PERCENTAGE)]

    # cropping order: center, left, up-left, up, up-right, right, down-right, down, down-left
    # tilting has yet to be implemented
    # THERE MIGHT BE A BETTER WAY TO DO THIS, PLEASE LET ME KNOW
    last_cropped = {
        'center': last_frame[height * CROP_PERCENTAGE:height * (1 - CROP_PERCENTAGE),
                             width * CROP_PERCENTAGE:width * (1 - CROP_PERCENTAGE)], # crop center

        'left': last_frame[height * CROP_PERCENTAGE:height * (1 - CROP_PERCENTAGE),
                           0:width * (1 - (CROP_PERCENTAGE * 2))],  # crop left

        'up-left': last_frame[0:height * (1 - (CROP_PERCENTAGE * 2)),
                              0:width * (1 - (CROP_PERCENTAGE * 2))],  # crop up-left

        'up': last_frame[0:height * (1 - (CROP_PERCENTAGE * 2)),
                         width * CROP_PERCENTAGE:width * (1 - CROP_PERCENTAGE)],  # crop up

        'up-right': last_frame[0:height * (1 - (CROP_PERCENTAGE * 2)),
                               width * (CROP_PERCENTAGE * 2): width],  # crop up-right

        'right': last_frame[height * CROP_PERCENTAGE:height * (1 - CROP_PERCENTAGE),
                            width * (CROP_PERCENTAGE * 2): width],  # crop right

        'down-right': last_frame[height * (CROP_PERCENTAGE * 2):height,
                                 width * (CROP_PERCENTAGE * 2): width],  # crop down-right

        'down': last_frame[height * (CROP_PERCENTAGE * 2):height,
                           width * CROP_PERCENTAGE:width * (1 - CROP_PERCENTAGE)],  # crop down

        'down-left': last_frame[height * (CROP_PERCENTAGE * 2):height,
                                0:width * (1 - (CROP_PERCENTAGE * 2))]}  # crop down-left

    compare_value = 0
    best_image = 0
    for key in last_cropped:
        img_compare_value = -0
        if img_compare_value < compare_value:  # COMPARE IMAGES *IDK how to get IMG_COMPARE_VALUE*
            compare_value = img_compare_value
            best_image = key

    if best_image == 'center':
        print("Ha you thought")

    if 'left' in best_image:
        print("Move right")

    elif 'right' in best_image:
        print("Move left")

    if 'up' in best_image:
        print("Move down")

    elif 'down' in best_image:
        print("Move up")


def listener():
    global CROP_PERCENTAGE
    if CROP_PERCENTAGE >= 1:
        print("WARNING: ROV hover cannot do anything as the CROP_PERCENTAGE has been set to a number greater than 1, it"
              "has been set back to the default of 2.5%")
        CROP_PERCENTAGE = 0.025
    while True:
        ret, first_frame = cap.read()  # get first frame
        sleep(0.1)
        ret, last_frame = cap.read()  # if we can't get 10 FPS there's a problem

        compare_frames(first_frame, last_frame)


if __name__ == '__main__':
    listener()