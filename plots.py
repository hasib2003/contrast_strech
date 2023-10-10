
import matplotlib.pyplot as plt;
import matplotlib.image as pimg;
import numpy as np

img2 = pimg.imread("./enh_wiki_by_cdf.jpg");


img1 = pimg.imread("./wiki.jpg");


def plotHistogram(title,img):

    # if(np.shape(img)[-1]>1):
    #     for i in range(np.shape(img)[-1]):

    plt.plot(x,y);
    plt.xlabel("pixel values")
    plt.ylabel("frequency")
    plt.title(title)
    plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
x1,y1 = np.unique(img1,return_counts=True)
axes[0, 0].bar(x1, y1)
axes[0, 0].set_title('Original Image Scale')

x2,y2 = np.unique(img2,return_counts=True)
axes[0, 1].bar(x2, y2)
axes[0, 1].set_title('histogram equalized')
plt.tight_layout()

# Show the plots
plt.show()
# plotHistogram("gray scale ",img1)
# plotHistogram("Intensity Sliced ",img1)
