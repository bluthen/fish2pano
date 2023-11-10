import sys
import cv2
import numpy as np
from scipy import optimize
import json


def calc_r(contour_t, xc, yc):
    """ calculate the distance of each 2D points from the center (xc, yc) """
    return np.sqrt((contour_t[0] - xc) ** 2 + (contour_t[1] - yc) ** 2)


def gen_f2(contour_t):
    """
    Function generator for arc lease squares.
    :param contour_t:
    :return:
    """

    def f2(c):
        """ calculate the algebraic distance between the data points and the mean circle centered at c=(xc, yc) """
        r_i = calc_r(contour_t, *c)
        return r_i - r_i.mean()

    return f2


def circle_least_squares(contour):
    """
    Does least squares on array of [x,y] points to find circle function.
    :param contour: The array of [x,y] points to get circle function for.
    :return: (radius, center) The radius and center of the circle
    """
    # http://scipy-cookbook.readthedocs.io/items/Least_Squares_Circle.html

    # If concave
    contour_shape = contour.shape
    contour_r = contour.T
    # contour_r = np.reshape(contour, [contour_shape[0], contour_shape[2]]).T
    center, ier = optimize.leastsq(gen_f2(contour_r), (3888, 3888))
    r_i2 = calc_r(contour_r, center[0], center[1])
    r_2 = np.mean(r_i2)
    r_residu2 = np.sum((r_i2 - r_2) ** 2.0)

    # If convex
    contour_shape = contour.shape
    contour_r = contour.T
    # contour_r = np.reshape(contour, [contour_shape[0], contour_shape[2]]).T
    center_b, ier = optimize.leastsq(gen_f2(contour_r), (0, 0))
    r_i2 = calc_r(contour_r, center_b[0], center_b[1])
    r_2_b = np.mean(r_i2)
    r_residu2 = np.sum((r_i2 - r_2) ** 2.0)

    if r_2_b < r_2:
        return r_2_b, center_b
    else:
        return r_2, center


def main():
    if len(sys.argv) != 2:
        print("Usage: %s [image]" % (sys.argv[0]))
        print("After clicking points on the circle perimeter hit escape.")
        sys.exit(1)
    imgfile = sys.argv[1]

    points = []
    img_raw = None
    nomore = False

    def mouse_cb(event, x, y, flags, param):
        if not nomore and event == cv2.EVENT_LBUTTONDOWN:
            print('point', x, y)
            points.append((x, y))
            cv2.circle(img_raw, (x, y), 3, (0, 0, 255), -1)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_cb)

    img_raw = cv2.imread(imgfile)
    while True:
        cv2.imshow('image', img_raw)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
    nomore = True
    points = np.array(list(map(np.array, points)))
    # print(points)
    r, center = circle_least_squares(points)
    print(json.dumps({"radius": r, "center": list(center)}))
    center = list(map(lambda x: int(x + 0.5), center))
    r = int(r + 0.5)
    cv2.circle(img_raw, center, r, (0, 255, 0), 1)
    cv2.circle(img_raw, center, 3, (0, 255, 0), -1)
    cv2.imshow('image', img_raw)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
