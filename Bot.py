# Written By Mohaned Sherhan..


from telegram.ext import Application , CommandHandler , MessageHandler , filters , ContextTypes
from telegram import Update
from pytube import YouTube
import json
import os 

# Telegram Bot Key: 
TOKEN = "{YOUR_BOT_TOKEN}"

main_path = os.getcwd()

# Start 
async def start_command(update : Update , context: ContextTypes.DEFAULT_TYPE) :
    text = """
This Bot Created By Mohaned Sherhan ....
To Get The Commend Plase Enter /help.
"""
    await update.message.reply_text(text)

# help the user :
async def help_command(update : Update , context: ContextTypes.DEFAULT_TYPE) :
    text = """
Welcome To Help Commend :
I am going to show you how to use this bot.
/new to make new post and this data :
<url>&<video_title>&<video_description>&<video_tags>
"""
    await update.message.reply_text(text)

# getting the info of video : 
async def new_command(update : Update , context: ContextTypes.DEFAULT_TYPE) :
    message:list = update.message.text.replace('/new' , '').split("&")
    # the list message it included with = [ url , title , description , tags , privacyStatus]
    cheak_url:str = "https://youtube.com/"
    if cheak_url in message[0] :
        try :
            YouTube(message[0].replace(" ",""))
            with open (f"{main_path}\\DataBase\\Time\\main_json_timer.json" , "r" ) as timer_file :
                try :
                    timer_data:dict = json.load(timer_file)
                    key:int = int( list (timer_data.keys())[-1] )
                    timer_data[f"{key+1}"] = {
                        "url" : message[0].replace(' ',''),
                        "title" : message[1],
                        "description" : message[2],
                        "tags" : message[3].split(',')
                    }
                    with open(f"{main_path}\\DataBase\\Time\\main_json_timer.json" , "w" , encoding='utf-8') as new_file :
                        json.dump(timer_data, new_file)
                        new_file.close()
                    await update.message.reply_text(f"The number of videos in the data base is {key+1}.")

                except json.decoder.JSONDecodeError : # the file is NULL 
                    timer_data = {'1':{
                            "url" : message[0],
                            "title" : message[1],
                            "description" : message[2],
                            "tags" : message[3].split(',')
                        }
                    }
                    with open(f"{main_path}\\DataBase\\Time\\main_json_timer.json" , "w" , encoding='utf-8') as new_file :
                        json.dump(timer_data, new_file)
                        new_file.close()
                    await update.message.reply_text("The number of videos in the data base is 1.")
                timer_file.close()
        except :
            await update.message.reply_text("I can't Download this Video... ")
    else :
        await update.message.reply_text("the URL is not YouTube URL >> https://youtube.com/")

# read the news from the message file :
async def news_command(update : Update , context: ContextTypes.DEFAULT_TYPE) :
    with open(f"{main_path}\\DataBase\\the_messages\\messages.txt","r") as message_file:
        message_data = message_file.readlines()
        message_file.close()
        if message_data :
            for message in message_data :
                await update.message.reply_text(message)
            else :
                open(f"{main_path}\\DataBase\\the_messages\\messages.txt","w").close()
        else :
            await update.message.reply_text("there is no news 0_0 .")



if __name__ == "__main__" :
    app = Application.builder().token(TOKEN).build()

    # command 
    app.add_handler( CommandHandler('start',start_command) )
    app.add_handler( CommandHandler('help',help_command) )
    app.add_handler( CommandHandler( 'new' , new_command)  )
    app.add_handler( CommandHandler( 'news' , news_command)  )


    print ("Polling ... ")
    app.run_polling(poll_interval=3)