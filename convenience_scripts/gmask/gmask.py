import cv2, numpy, sys, os

directory = os.getcwd()

def main():

    if len(sys.argv) < 1:
        print('input a sensitivity value as cl argument')
        main()
    else:
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".tif"): 
                img = cv2.imread(filename)

                sensitivity = sys.argv[1]
                empty_img = numpy.zeros_like(img)
                RED, GREEN, BLUE = (2, 1, 0)
                reds = img[:, :, RED]
                greens = img[:, :, GREEN]
                blues = img[:, :, BLUE]
                mask = (greens < int(sensitivity)) | (numpy.amax(img, axis=2) != greens)
                result = numpy.where(mask, 255, 0)
                os.mkdir("masks")
                cv2.imwrite(os.path.join(directory + "/masks", filename + "_mask.jpg"), result)
                continue
            else:
                continue

main()