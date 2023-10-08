# Written By Mohaned Sherhan..

import pytube
import os

def get_new_name_video(videos_path:str) :
    videsos_name:list = os.listdir(videos_path)
    if videsos_name != [] :
        return ( int(videsos_name[-1].split(".")[0]) + 1 )
    else :
        return 1
def delete_old_video(videos_path:str) :
    os.remove(videos_path)

# def to search about the resolutions :
def resolutions(streams) :
    the_p = {}
    if streams.filter(res="4320p") :
        the_p["4320"] = streams.filter(res="4320p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="2160p") :
        the_p["2160"] = streams.filter(res="2160p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="1080p") :
        the_p["1080"] = streams.filter(res="1080p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="720p") :
        the_p["720"] = streams.filter(res="720p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="480p") :
        the_p["480"] = streams.filter(res="480p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="360p") :
        the_p["360"] = streams.filter(res="360p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="240p") :
        the_p["240"] = streams.filter(res="240p" ,  mime_type="video/mp4" ).first()
    if streams.filter(res="144p") :
        the_p["144"] = streams.filter(res="144p" ,  mime_type="video/mp4" ).first()
    return the_p

# to download the video from YouTube : 
def download( url:str ,main_path:str ) :
    try :
        streams = pytube.YouTube(url).streams
        video_res_urls = resolutions(streams)
        ver = 0
        for highest in list(video_res_urls.keys()) :
            ver = int(highest) if int(highest) > ver else ver
        else :
            new_name = get_new_name_video(f"{main_path}\\DataBase\\videos_file")
            video = video_res_urls[f'{ver}'].download(f"{main_path}\\DataBase\\videos_file")
            named = f"{main_path}\\DataBase\\videos_file\\{new_name}.mp4"
            os.rename(video, named)
            if new_name != 1 :
                delete_old_video(f"{main_path}\\DataBase\\videos_file\\{new_name-1}.mp4")
            return True
    except :
        return False