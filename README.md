# Install deps
```
poetry install
poetry shell
```

Make sure to compile optimized version of generate_pano, will probably be over 400 times faster.

```
python setup.py build_ext --inplace
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
