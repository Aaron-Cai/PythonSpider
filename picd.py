import urllib,urllib2

url = 'http://a.hiphotos.baidu.com/image/w%3D230/sign=494c2900a344ad342ebf8084e0a30c08/f11f3a292df5e0fe414a02ec5e6034a85fdf7289.jpg'

img = urllib2.urlopen(url).read()

# print img

open('test.jpg','wb').write(img)