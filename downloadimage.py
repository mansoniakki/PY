import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("http://imshopping.rediff.com/imgshop/800-1280/shopping/pixs/25886/m/mg089._mariyam-wooden-elephant-stool-for-decoratives-showpiece.jpg")