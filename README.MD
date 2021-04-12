# Histogram Equalization vs Contrast Stretching

## Histogram Equalization
Histogram Equalization increases the global contrast of many images, especially when the usable data of the image is represented by close contrast values. Through this adjustment, the intensities can be better distributed on the histogram. This allows for areas of lower local contrast to gain a higher contrast.
Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values.(source)[https://en.wikipedia.org/wiki/Histogram_equalization]

## Contrast Stretching

Contrast is a measure of the “range” of an image; i.e. how spread its intensities are. It has many formal definitions one famous is Michelson’s:
He says `contrast =  ( Imax - Imin )/( Imax + I min )` (source)[https://stackoverflow.com/questions/41118808/difference-between-contrast-stretching-and-histogram-equalization]
Contrast Stretching and Histogram Equalisation have the same goal: making the images to use entire range of values available to them.


## Visual Results
#### Input Image

img

### Histogram Equalization
img2-5
### Contrast Stretching
img6