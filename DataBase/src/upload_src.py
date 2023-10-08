# Written By Mohaned Sherhan..

from googleapiclient.discovery import build
from oauth2client.file import Storage
import httplib2
import os

def upload( py_oauth2_path:str , video_title:str , video_description:str , video_tags:list , videos_path:str ) :
    try :
        storage = Storage( py_oauth2_path )
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            return False , "client_secret"
        # Set info for the YouTube AIP :
        youtube = build("youtube", "v3", http=credentials.authorize(httplib2.Http()))
        video = str(os.listdir(videos_path)[0])
        video_file = open( f"{videos_path}\\{video}" , "rb" )
        # ubload the video to YouTube : 
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": video_title,
                    "description": video_description,
                    "tags": video_tags
                },
                "status": {
                    "privacyStatus": "public"
                }
            },
            media_body=video_file.name
        )
        # loding uploading the video ... 
        response = request.execute()
        # the video has been uploaded ...
        return True , "Yes" 
    except :
        return False , "No"
