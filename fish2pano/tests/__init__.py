from unittest import TestCase
import fish2pano
import fish2pano.fast
import numpy as np

our_img = np.array(np.outer(np.arange(20), np.ones(30)).reshape(20, 10, 3), dtype=np.uint8)


class TestFish2Pano(TestCase):
    def test_fish2pano_cython(self):
        b = fish2pano.fast.generate_pano(our_img, 4, np.array([5, 5], dtype=np.double), 1.0)
        self.assertTrue((b == result).all())

    def test_fish2pano_pure(self):
        b = fish2pano.generate_pano_pure(our_img, 4, [5, 5], 1.0)
        self.assertTrue((b == result).all())

    def test_fish2pano_any(self):
        b = fish2pano.fish2pano(our_img, 4, [5, 5], 1.0)
        self.assertTrue((b == result).all())


result = np.array([[[5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5]],

                   [[5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [6, 6, 6],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [5, 5, 5],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [4, 4, 4],
                    [5, 5, 5],
                    [5, 5, 5]],

                   [[5, 5, 5],
                    [5, 5, 5],
                    [6, 6, 6],
                    [6, 6, 6],
                    [7, 7, 7],
                    [7, 7, 7],
                    [7, 7, 7],
                    [7, 7, 7],
                    [7, 7, 7],
                    [7, 7, 7],
                    [6, 6, 6],
                    [6, 6, 6],
                    [5, 5, 5],
                    [5, 5, 5],
                    [4, 4, 4],
                    [4, 4, 4],
                    [3, 3, 3],
                    [3, 3, 3],
                    [3, 3, 3],
                    [3, 3, 3],
                    [3, 3, 3],
                    [3, 3, 3],
                    [4, 4, 4],
                    [4, 4, 4],
                    [5, 5, 5]],

                   [[5, 5, 5],
                    [6, 6, 6],
                    [6, 6, 6],
                    [7, 7, 7],
                    [8, 8, 8],
                    [8, 8, 8],
                    [8, 8, 8],
                    [8, 8, 8],
                    [8, 8, 8],
                    [7, 7, 7],
                    [7, 7, 7],
                    [6, 6, 6],
                    [5, 5, 5],
                    [5, 5, 5],
                    [4, 4, 4],
                    [3, 3, 3],
                    [3, 3, 3],
                    [2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2],
                    [3, 3, 3],
                    [4, 4, 4],
                    [4, 4, 4]]], dtype=np.uint8)
