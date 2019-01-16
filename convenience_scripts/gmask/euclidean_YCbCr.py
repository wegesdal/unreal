import cv2
import numpy
import sys
import os
import rawpy
import math

directory = os.getcwd()

def main():

    if len(sys.argv) < 1:
        print('correct format is: python process.py sensitivity red green blue')
        main()
    else:
        for filename in os.listdir(directory):
            key = (sys.argv[2], sys.argv[3], sys.argv[4])
            # CR2 is for Canon cameras, other cameras may need to be added to
            # this conditional
            # notice: this file extension conditional is case-sensitive
            if filename.endswith(".CR2"): 
                raw_image = filename
                raw = rawpy.imread(raw_image)
                rgb = raw.postprocess()

                # construct a 1x1 pixel image of our key color to convert from
                # RGB to YCrCb colorspace
                key_pixelRGB = numpy.zeros((1,1,3), numpy.uint8)
                key_pixelRGB[0,0] = key
                key_pixel_YCrCb = cv2.cvtColor(key_pixelRGB, cv2.COLOR_BGR2YCR_CB)

                # export the RAW file to tiff format in its own subdirectory
                # if the target directory does not exist, create one
                if not os.path.exists("tiffs"):
                    os.mkdir("tiffs")

                # opencv uses BGA instead of RGB so we need to invert the
                # colors before saving the file
                destRGB = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
                cv2.imwrite(os.path.join(directory + "/tiffs", filename + ".tiff"), destRGB)

                # convert BGA data to YCrCb, this is a little confusing because
                # although rgb contain
                destCR_CB = cv2.cvtColor(rgb, cv2.COLOR_BGR2YCR_CB)

                # only one sensitivity parameter for now
                # TODO: use a dual sensitivity (one for each channel, Cr vs.
                # euclidean distance and Cb vs euclidean distance)
                sensitivity = sys.argv[1]
                empty_img = numpy.zeros_like(rgb)

                # the second page of 3 dimensional array destCR_CB, which
                # contains the Cb data of the image
                Cr_p = destCR_CB[:, :, 1]

                # the third page of 3 dimensional array destCR_CB, which
                # contains the Cr data of the image
                Cb_p = destCR_CB[:, :, 2]

                # create an array of ones and multiply by the key_pixel value
                # in YCR_CB color space

                Cr_key = numpy.ones_like(Cr_p) * int(key_pixel_YCrCb[0,0][1])
                Cb_key = numpy.ones_like(Cb_p) * int(key_pixel_YCrCb[0,0][2])

                # calculate the sum of euclidean distances between the the Cr and Cb values respectively
                eucDis = numpy.sqrt((Cr_p - Cr_key.astype(float)) ** 2 + (Cb_p - Cb_key.astype(float)) ** 2)
                mask = eucDis.astype(int) < int(sensitivity)
                
                # result is true if that pixel's euclidean distance is less
                # than the given sensitivity parameter
                # TODO: allow different sensitivities for Cb and Cr values
                
                result = numpy.where(mask, 255, 0)
                if not os.path.exists("ycrcb"):
                    os.mkdir("ycrcb")
                cv2.imwrite(os.path.join(directory + "/ycrcb", filename + "_ycrcb.tiff"), destCR_CB)

                if not os.path.exists("masks"):
                    os.mkdir("masks")
                cv2.imwrite(os.path.join(directory + "/masks", filename + "_mask.tiff"), result)

            else:
                continue
main()
