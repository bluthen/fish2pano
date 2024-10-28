# DEPRECATED

You should just use [OpenCV wrapPolar](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga49481ab24fdaa0ffa4d3e63d14c0d5e4) directly.

See [issue #4](https://github.com/bluthen/fish2pano/issues/4)



# Install deps
```
poetry install
poetry shell
```

# findcircle.py

This users opencv UI to let you click the perimeter of the fish eye circle. Using the points it will find the radius and center.


# fish2pano.py

Turns a fisheye image into a panoramic image.


# Example

![Image of sky from a fisheye lens](./large2.jpg "Fisheye")

```
python fish2pano.py large2.jpg 481 618,538 0.5 large2_pano.jpg
```


![Image of sky in panoramic form](./large2_pano.jpg "Pano")
