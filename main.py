import cv2
import numpy as np
import os
import sys

# adjust_color is a function that will extract the RGB number from the input image with range 0 to 255.
# to make easier to calculate for RGB number, all number will be divided by the maximum of color number (255) so the range will be 0 to 1.
# after that we will use sigmoid tanh to have boundary the value between [-19 ... 0 ... 19].
# Why we used tanh sigmod because the value from only be range -1 , 0 and 1 to have lower and upper boundary.
# and of course -1 will be the max lower boundary for coolest, 0 as a default, 1 the max upper boundary for warmest.
# after we have scale number, we multiple by 15% to make more temperature range.
# if temparature >= 0 that mean Red spectrum will be higher [max 1] that Blue spectrum [less < 1], otherwise blue will have higher spectrum than red.
# the output image will be created.
def adjust_color(image_path, output_path, temperature):
    # Red input image
    img = cv2.imread(image_path)
    #make it as range 0 to 1
    img_float = img.astype(np.float32) / 255.0
    # tanh for range temperature and only used 15%
    scale = np.tanh(np.abs(temperature)) * 0.15

    # modify the R and B number.
    if temperature >= 0:
        img_float[:, :, 0] -= scale  # Blue channel
        img_float[:, :, 2] += scale   # Red channel
    else:
        img_float[:, :, 0] += scale  # Blue channel
        img_float[:, :, 2] -= scale # Red channel

    # make standard value with default range 0 and 1, if X < 0 , then make it 0, and if X > 1 then make it 1.
    img_float = np.clip(img_float, 0, 1)
    # return back the value on range 0 to 255.
    img_uint8 = (img_float * 255).astype(np.uint8)
    # create the outputs image.
    cv2.imwrite(output_path, img_uint8)


if __name__ == "__main__":
    # checking overall length of argv that python will be parse as array.
    # The required paramaters are (1) script_name.py, (2) input_image.jpg and (3) output_image..jpg
    # The optionnal parameters only temperature and default value is 0.
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_image.jpg output_image.jpg [--temperature[-19...0...19]]")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Validate is input image path exist or nots
    if not os.path.isfile(input_image_path):
        print('Input file not found - please make sure file is exist.')
        sys.exit(1)

    # Validate input image must be have extension jpg or jpeg.
    if not input_image_path.lower().endswith(('.jpg', '.jpeg')):
        print('Input file must be a JPEG image.')
        sys.exit(1)
    
    # Validate input image must be have extension jpg or jpeg.
    if not output_image_path.lower().endswith(('.jpg', '.jpeg')):
        print('Output file must be have extention (*.jpg, *.jpeg).')
        sys.exit(1)
    
    # parse optional paramater temperature
    temperature = 0.0
    if len(sys.argv) > 3 and sys.argv[3] == "--temperature":
        if len(sys.argv) < 5:
            print("Temperature value missing.")
            sys.exit(1)
        try:
            temperature = int(sys.argv[4])
            if temperature < -19 and temperature > 19:
                print("Invalid temperature range should be [-19s..0...19].")
                sys.exit(1)
        except ValueError:
            print("Invalid temperature value should be integer number.")
            sys.exit(1)

    adjust_color(input_image_path, output_image_path, temperature)

