# DEPRECATED

You should just use [OpenCV wrapPolar](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga49481ab24fdaa0ffa4d3e63d14c0d5e4) directly.

See [issue #4](https://github.com/bluthen/fish2pano/issues/4)

# Install
```
pip install fish2pano
```

## Inplace 

If you are running in place from source from the repository, make sure to compile optimized version of fish2pano.fast, it will probably be over 200 times faster. If you installed with pip then yous hould be good.

```
python setup.py build --inplace
```

# Usage
```
> import fish2pano
> myimg = ... # Load numpy of shape (W, H, 3) representing the image
> radius = 481 # How big a circle your fisheye image is in pixels
> center = [618, 538] # Center of your fisheye image
> scale = 0.5 # How big the resulting pano is compared to the original
> mypano = fish2pano.fish2pano(myimg, radius, center, scale) # numpy array of your new pano image
```

# Command Line and Graphical tools

See [fish2panoui](https://github.com/bluthen/fish2panoui) repo for command line and graphical tools to turn fisheye image to panoramic.

It also has a tool "findcircle.py" that helps you find the radius and center of the fisheye in your image.

## Example

![Image of sky from a fisheye lens](./large2.jpg "Fisheye")

```
python fish2panoui.py large2.jpg 481 618,538 0.5 large2_pano.jpg
```


![Image of sky in panoramic form](./large2_pano.jpg "Pano")
