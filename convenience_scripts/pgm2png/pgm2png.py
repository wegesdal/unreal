import cv2
import sys
import os

directory = os.getcwd()

def main():

    if len(sys.argv) < 1:
        print('correct format is: python pgm2png.py sensitivity red green blue')
        main()
    else:
        for filename in os.listdir(directory):
            # notice: this file extension conditional is case-sensitive
            if filename.endswith(".pgm"): 
                print('converting ' + filename + ' to png')
                rgb = cv2.imread(filename)

                # export the pgm file to png format in its own subdirectory
                # if the target directory does not exist, create one
                if not os.path.exists("pngs"):
                    os.mkdir("pngs")

                # opencv uses BGA instead of RGB so we need to invert the
                # colors before saving the file
                destRGB = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
                cv2.imwrite(os.path.join(directory + "/pngs", filename + ".png"), destRGB)

            else:
                continue
main()

