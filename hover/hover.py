import cv2
from time import sleep
from skimage.measure import compare_ssim

IP_ADDRESS = "moveRight.mp4"
CROP_PERCENTAGE = 0.0005  # .05% to start NOTE: This is .05% on 4 sides or .1% of the height and .1% of the width
# if this is too high, it leads to not moving and just staying at the center


cap = cv2.VideoCapture(IP_ADDRESS)


def compare_frames(first_frame, last_frame):  # pass in a CV2 image (second output from cv2.read)
    height, width, channels = first_frame.shape
    # crop the image by 2.5% (0.025) on each side, this allows the image to be compared, this value could easily be
    # played with in the variable above
    # Then convert it to grayscale for comparision

    first_cropped_gray = cv2.cvtColor(first_frame[round(height * CROP_PERCENTAGE):round(height * (1 - CROP_PERCENTAGE)),
                                                  round(width * CROP_PERCENTAGE):round(width * (1 - CROP_PERCENTAGE))],
                                      cv2.COLOR_BGR2GRAY)

    # cropping order: center, left, up-left, up, up-right, right, down-right, down, down-left
    # tilting has yet to be implemented
    # THERE MIGHT BE A BETTER WAY TO DO THIS, PLEASE LET ME KNOW
    last_cropped = {
        'center': last_frame[round(height * CROP_PERCENTAGE):round(height * (1 - CROP_PERCENTAGE)),
                             round(width * CROP_PERCENTAGE):round(width * (1 - CROP_PERCENTAGE))],  # crop center

        'left': last_frame[round(height * CROP_PERCENTAGE):round(height * (1 - CROP_PERCENTAGE)),
                           0:round(width * (1 - (CROP_PERCENTAGE * 2)))],  # crop left

        'up-left': last_frame[0:round(height * (1 - (CROP_PERCENTAGE * 2))),
                              0:round(width * (1 - (CROP_PERCENTAGE * 2)))],  # crop up-left

        'up': last_frame[0:round(height * (1 - (CROP_PERCENTAGE * 2))),
                         round(width * CROP_PERCENTAGE):round(width * (1 - CROP_PERCENTAGE))],  # crop up

        'up-right': last_frame[0:round(height * (1 - (CROP_PERCENTAGE * 2))),
                               round(width * (CROP_PERCENTAGE * 2)): width],  # crop up-right

        'right': last_frame[round(height * CROP_PERCENTAGE):round(height * (1 - CROP_PERCENTAGE)),
                            round(width * (CROP_PERCENTAGE * 2)): width],  # crop right

        'down-right': last_frame[round(height * (CROP_PERCENTAGE * 2)):height,
                                 round(width * (CROP_PERCENTAGE * 2)): width],  # crop down-right

        'down': last_frame[round(height * (CROP_PERCENTAGE * 2)):height,
                           round(width * CROP_PERCENTAGE):round(width * (1 - CROP_PERCENTAGE))],  # crop down

        'down-left': last_frame[round(height * (CROP_PERCENTAGE * 2)):height,
                                0:round(width * (1 - (CROP_PERCENTAGE * 2)))]}  # crop down-left

    compare_value = 0
    best_image = 0
    for key in last_cropped:
        compare_img = cv2.cvtColor(last_cropped[key], cv2.COLOR_BGR2GRAY)  # convert image to gray scale
        height = min(compare_img.shape[0], first_cropped_gray.shape[0])
        width = min(compare_img.shape[1], first_cropped_gray.shape[1])
        (img_compare_value, diff) = compare_ssim(first_cropped_gray[0:height, 0:width], compare_img[0:height, 0:width],
                                                 full=True)  # crop them to the same size then compare them. Diff is the
        # actual image with differences highlighted
        if img_compare_value > compare_value:  # COMPARE IMAGES, higher number means more similar
            compare_value = img_compare_value
            best_image = key
        elif img_compare_value == compare_value:  # if they're equal add it to the end
            best_image += "-{0}".format(key)

    if best_image == 'center':
        print("Ha you thought")

    if 'left' in best_image:
        print("Move left")

    elif 'right' in best_image:
        print("Move right")

    if 'up' in best_image:
        print("Move up")

    elif 'down' in best_image:
        print("Move down")

    print("\n")


def listener():
    global CROP_PERCENTAGE
    if CROP_PERCENTAGE >= 0.5:
        print("WARNING: ROV hover cannot do anything as the CROP_PERCENTAGE has been set to a number greater than 1, it"
              "has been set back to the default of .05%")
        CROP_PERCENTAGE = 0.0005
    while True:
        ret, first_frame = cap.read()  # get first frame
        sleep(0.1)
        ret, last_frame = cap.read()  # if we can't get 10 FPS there's a problem

        compare_frames(first_frame, last_frame)


if __name__ == '__main__':
    listener()