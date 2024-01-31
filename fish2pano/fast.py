# cython: language_level=3
import time
import cython
import numpy as np

from cython.cimports.libc.math import sin, cos, M_PI
from cython.parallel import prange


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def generate_pano(img_raw: cython.uchar[:, :, ::1], radius: cython.double, center: cython.double[:], scale: cython.double):
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

    r_w: cython.Py_ssize_t = img_raw.shape[1]
    r_h: cython.Py_ssize_t = img_raw.shape[0]
    w: cython.Py_ssize_t = cython.cast(cython.Py_ssize_t, scale * 2 * M_PI * radius + 0.5)
    h: cython.Py_ssize_t = cython.cast(cython.Py_ssize_t, scale * radius + 0.5)
    img_t_result = np.zeros((h, w, 3), dtype=np.uint8)
    img_t_view: cython.uchar[:, :, ::1] = img_t_result
    x: cython.Py_ssize_t
    y: cython.Py_ssize_t
    x_: cython.double
    y_: cython.double
    theta: cython.double
    r_0: cython.double
    ix_: cython.Py_ssize_t
    iy_: cython.Py_ssize_t
    start = time.time()
    for x in prange(w, nogil=True):
        theta = (2.0 * M_PI) * x / w
        for y in range(h):
            r_0 = radius * y / h
            x_ = r_0 * cos(theta) + center[0]
            y_ = r_0 * sin(theta) + center[1]
            ix_ = cython.cast(cython.Py_ssize_t, x_ + 0.5)
            iy_ = cython.cast(cython.Py_ssize_t, y_ + 0.5)
            if x_ > 0 and ix_ < r_w and y_ > 0 and iy_ < r_h:
                img_t_view[y][x][0] = img_raw[iy_][ix_][0]
                img_t_view[y][x][1] = img_raw[iy_][ix_][1]
                img_t_view[y][x][2] = img_raw[iy_][ix_][2]
            else:
                img_t_view[y][x][0] = 0
                img_t_view[y][x][1] = 0
                img_t_view[y][x][2] = 0
    print('loop', time.time() - start)
    return img_t_result

