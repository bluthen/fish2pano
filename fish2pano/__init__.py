import sys
import math
import traceback

import numpy as np
import time


def generate_pano_pure(img_raw, radius, center, scale):
    """
    Generate panoramic image.
    :param img_raw: image to make pano from, uint8 numpy array with shape (w, h, 3)
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
    img_rs = img_raw.shape
    w = int(scale * 2 * math.pi * radius + 0.5)
    h = int(scale * radius + 0.5)
    img_t = np.zeros((h, w, 3), dtype=np.uint8)
    start = time.time()

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
    print('Loop', time.time() - start)
    return img_t


def fish2pano(img_raw: np.ndarray, radius: float, center: list[int, int], scale: float):
    """
    Generate panoramic image.
    :param img_raw: image to make pano from, uint8 numpy array with shape (w, h, 3)
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
    try:
        import fish2pano.fast
        img_t = fish2pano.fast.generate_pano(img_raw, radius, np.array(center, dtype=np.double), scale)
    except:
        traceback.print_exc()
        print("WARNING: Falling back to non-optimized slow version", file=sys.stderr)
        img_t = generate_pano_pure(img_raw, radius, center, scale)
    return img_t

