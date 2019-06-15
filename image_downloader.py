import urllib


def downloader(image_url, index):

    full_file_name = str(index) + '.jpg'
    image = urllib.URLopener()
    image.retrieve(image_url, full_file_name)


for i in range(1, 1282):
    if i < 10:
        downloader("http://www.zimmermanphotography.com/album/kelly/000" + str(i) + ".jpg", i)
    elif i >= 10 and i < 100:
        downloader("http://www.zimmermanphotography.com/album/kelly/00" + str(i) + ".jpg", i)
    elif i >= 100 and i < 1000:
        downloader("http://www.zimmermanphotography.com/album/kelly/0" + str(i) + ".jpg", i)
    else:
        downloader("http://www.zimmermanphotography.com/album/kelly/" + str(i) + ".jpg", i)
