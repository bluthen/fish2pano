import sys
import cv2
import math
import numpy as np


def generate_pano(img_raw, radius, center, scale):
    """
    Generate panoramic image.
    :param img_raw:
    :param radius: Radius of image circle in pixels
    :param center: Center of image circle in pixels
    :param scale: Scale image, end result image size is:
          width = int(scale * 2 * math.pi * radius + 0.5)
          height = int(scale * radius + 0.5)
        if you have a desired width or height size to find sacle:
          scale = width/(2*math.pi*radius)
          OR
          scale = height/radius
    :return:
    """
    # w = int(2*math.pi*r+0.5)
    # h = int(r)
    img_rs = img_raw.shape
    # print(img_rs)
    w = int(scale * 2 * math.pi * radius + 0.5)
    h = int(scale * radius + 0.5)
    img_t = np.zeros((h, w, 3), dtype=np.uint8)
    for x in range(w):
        theta = (2.0 * math.pi) * x / w
        for y in range(h):
            r_0 = radius * y / h
            x_ = r_0 * math.cos(theta) + center[0]
            y_ = r_0 * math.sin(theta) + center[1]
            ix_ = int(x_ + 0.5)
            iy_ = int(y_ + 0.5)
            if x_ > 0 and ix_ < img_rs[1] and y_ > 0 and iy_ < img_rs[0]:
                img_t[y][x] = img_raw[iy_][ix_]
            else:
                img_t[y][x] = [0, 0, 0]
    # print('raw', img_raw.shape, img_raw.dtype)
    # print('t', img_t.shape, img_t.dtype)
    return img_t


def main():
    # TODO: Interpolation
    if len(sys.argv) < 6:
        print("Usage: %s [image] [radius] [centerx,centery] [scale_factor] [outfile_name]" % (sys.argv[0],))
        sys.exit(1)
    imgfile = sys.argv[1]
    radius = float(sys.argv[2])
    center = [float(x) for x in sys.argv[3].split(',')]
    scale = float(sys.argv[4])
    outfile = sys.argv[5]
    img_raw = cv2.imread(imgfile)
    img_t = generate_pano(img_raw, radius, center, scale)
    cv2.imshow('transformed', img_t)
    cv2.waitKey()
    cv2.imwrite(outfile, img_t)


if __name__ == '__main__':
    main()
