# rodar no adesso
import glob
import urllib
import Image
mmfreedom(2)

fileglob = 'hirata/images*/*'

media_root = config.media_root.replace('\\', '/').rstrip('/')
media_url = config.media_url.replace('\\', '/').rstrip('/')
fileglob = os.path.join(media_root, fileglob)
files = glob.glob(fileglob)
files.sort()

for img in files:
   img = img.replace('\\', '/')
   url = urllib.quote(img.replace(media_root, media_url))
   print "http://adessowiki.fee.unicamp.br" + url


# wget -x --random-wait -i images.filelist
