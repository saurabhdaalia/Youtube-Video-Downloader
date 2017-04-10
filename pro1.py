import pafy
from pprint import pprint 
import os
 

print "Welcome to Video to audio converter+Downloader"
print "************************************************"

url=raw_input("Enter playlist url: ")
print "Retrieving the Url...."

playlist=pafy.get_playlist(url)
print "Total songs in playlist:",len(playlist['items'])




newpath='f:/saurabh/videos/youtube'  #making directory
if not os.path.exists(newpath):
    os.makedirs(newpath)
        

	
	
for item in playlist['items']:
    video=item['pafy']
    vid=video.getbest()
    try :
	
        print "Downloading "+str(video.title)+"...."
    except :
        print "downloading" 	
	
    filename=vid.download(filepath=newpath)
			
	
