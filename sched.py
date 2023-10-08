# Written By Mohaned Sherhan..


from DataBase.src import download_src
from DataBase.src import upload_src
from datetime import datetime
import schedule 
import time 
import json
import os

main_path = os.getcwd()
timer_path = f"{main_path}\\DataBase\\Time\\main_json_timer.json"
message_txt = f"{main_path}\\DataBase\\the_messages\\messages.txt"
videos_file_path = f"{main_path}\\DataBase\\videos_file"
APIs_path = f"{main_path}\\DataBase\\APIs_file\\upload_video.py-oauth2.json"

def jop() :
    try :
        with open (timer_path,"r" ,encoding="utf-8") as info_video_file_json :
            info_video_file:dict = json.load(info_video_file_json) 
            info_video_file_json.close()
        keys:list = list(info_video_file.keys())
        video = info_video_file[keys[0]]
        # to download the video :
        URL:str = video['url'].replace(" " , "")
        respons:bool = download_src.download(url=URL, main_path=main_path)
        if respons :
            # Upload the video :
            TITLE:str = video['title']
            DES:str = video['description']
            TAGS:list = video['tags']
            stat , message= respons = upload_src.upload(
                py_oauth2_path=APIs_path,
                video_title=TITLE,
                video_description=DES,
                video_tags=TAGS,
                videos_path=videos_file_path
            )
            if stat == False and message == "client_secret" :
                with open(message_txt,"a") as message_file :
                    message_file.writelines(f"ERROR: client_secret < {datetime.now().strftime('%Y-%m-%d -> %H:%M')} > ")
                    message_file.close()
        del info_video_file[keys[0]]
        with open(timer_path , "w" , encoding='utf-8') as new_video_file_info :
            json.dump(info_video_file,new_video_file_info)
            new_video_file_info.close()
        print ("the downloaded is doen.")
        if info_video_file == {} :
            open(timer_path,'w').close()
    except :
        with open(message_txt,"a") as message_file :
            message_file.writelines(f"The Data Base in ( {datetime.now().strftime('%Y-%m-%d -> %H:%M')} ) is NULL... For That There is No Video Has been Uploaded.\n")
            message_file.close()


schedule.every(2).minutes.do(jop)

while True :
    schedule.run_pending()
    time.sleep(1)
