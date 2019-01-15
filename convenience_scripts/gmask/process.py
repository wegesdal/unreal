
import cv2, numpy, sys, os, rawpy, math

directory = os.getcwd()

def main():

    if len(sys.argv) < 1:
        print('correct format is: python process.py sensitivity red green blue')
        main()
    else:
        for filename in os.listdir(directory):
            key = (sys.argv[2], sys.argv[3], sys.argv[4])
            #cr2 is for Canon cameras, other cameras may need to be added to this conditional
            if filename.endswith(".CR2"): 
                raw_image = filename
                raw = rawpy.imread(raw_image)
                rgb = raw.postprocess()
                if not os.path.exists("tiffs"):
                    os.mkdir("tiffs")
                #opencv uses bga instead of rgb so we need to invert the colors before saving the file
                destRGB = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
                cv2.imwrite(os.path.join(directory + "/tiffs", filename + ".tiff"), destRGB)
                sensitivity = sys.argv[1]
                empty_img = numpy.zeros_like(rgb)
                RED, GREEN, BLUE = (2, 1, 0)
                reds = rgb[:, :, RED]
                greens = rgb[:, :, GREEN]
                blues = rgb[:, :, BLUE]
                rkey = numpy.ones_like(reds)*int(key[0])
                gkey = numpy.ones_like(greens)*int(key[1])
                bkey = numpy.ones_like(blues)*int(key[2])
                rkey -= reds
                gkey -= greens
                bkey -= blues
                mask = (rkey + bkey + gkey < int(sensitivity)) #| (numpy.amax(rgb, axis=2) != greens)
                result = numpy.where(mask, 255, 0)
                if not os.path.exists("masks"):
                    os.mkdir("masks")
                cv2.imwrite(os.path.join(directory + "/masks", filename + "_mask.tiff"), result)
                continue
            else:
                continue

main()