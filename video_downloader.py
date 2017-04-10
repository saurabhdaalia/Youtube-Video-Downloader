import pafy  #module to download youtube videos
import os

print "Welcome to Video downloader"
print "###################################"

choice=0
choice=int(raw_input("Press 1 to download playlist or 2 to download coustom videos  "))

newpath=raw_input("Enter the path : ")

if not os.path.exists(newpath):
    os.makedirs(newpath)



if choice==1:
    playlist_url=raw_input("Enter playlist URL : ")
    print "Retrieving the playlist...."
    playlist=pafy.get_playlist(playlist_url)  #making the pafy object i.e a dictionary
    print "Total videos in playist",len(playlist['items']) 
    mode=0
    mode=int(raw_input("Press 1 to download video or 2 to download audio only "))
    if mode==1:
        for item in playlist['items']: #the "items" key in dictonary further contain a list of all the videos of playlist
            vid=item['pafy']              #the further list contain dictioanry in it having all the information about the video
            video=vid.getbest()           #best resoltuion availaible 
            print "Preparing to Download..."
            try:
			    print "Downloading "+str(vid.title)
            except :
                print "Downloaind Video..."
				
            file=video.download(quiet=False, filepath=newpath)      #download process	 
        print "DOWNLOAD COMPLETE "	
    elif mode==2:
        for item in playlist['items']:
            vid=item['pafy']
            audio=vid.getbestaudio()      # converting into audio
            try :
			    print "Downloading "+str(vid.title)+"(audio)"
            except:
                print "Downloading audio"			
            
            audio_file=audio.download(quiet=False, filepath=newpath)		
        print "DOWNLOAD COMPLETE"		

elif choice==2:
    url_list=list()
    i=int(raw_input("Enter the amount of Videos "))
    for count in range(0,i): 
        url=raw_input("Enter the URL")
        url_list.append(url)              #making the list of URLS
    print "Preparing to Download..."
    mode1=int(raw_input("Press 1 to download video or Press 2 to download audio only"))
    if mode1==1:
        for link in url_list:
            obj=pafy.new(link)
            video=obj.getbest()
            try:
			    print "Downloading "+str(obj.title)    
            except:
			    print "Downloading Video"
            file=video.download(quiet=False, filepath=newpath)	
	    print "DOWNLOAD COMPLETE" 
	
    elif mode1==2:
	    for link in url_list:
		    obj=pafy.new(link)
            audio=obj.getbestaudio()
            try :
			    print "downloading "+str(obj.title)+" (audio)"
            except :
                print "downloading audio"	
            audio_file=audio.download(quiet=False, filepath=newpath)
	    print "Download Complete"	