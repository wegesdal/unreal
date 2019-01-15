
            


import cv2, numpy, sys, os, rawpy

directory = os.getcwd()

def main():

    if len(sys.argv) < 1:
        print('input a sensitivity value as cl argument')
        main()
    else:
        for filename in os.listdir(directory):
            #cr2 is for Canon cameras, other cameras may need to be added to this conditional
            if filename.endswith(".cr2"):
                raw_image = filename
                raw = rawpy.imread(raw_image)
                rgb = raw.postprocess()
                os.mkdir("tiffs")
                cv2.imwrite(os.path.join(directory + "/tiffs", filename + ".tiff"), rgb)
                sensitivity = sys.argv[1]
                empty_img = numpy.zeros_like(rgb)
                RED, GREEN, BLUE = (2, 1, 0)
                reds = img[:, :, RED]
                greens = img[:, :, GREEN]
                blues = img[:, :, BLUE]
                mask = (greens < int(sensitivity)) | (numpy.amax(rgb, axis=2) != greens)
                result = numpy.where(mask, 255, 0)
                os.mkdir("masks")
                cv2.imwrite(os.path.join(directory + "/masks", filename + "_mask.jpg"), result)
                continue
            else:
                continue

main()