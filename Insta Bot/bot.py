from instabot import Bot
import os
from getpass import getpass

bot = Bot()
username = input("Type Your Username: ")
password = getpass("Your Password: ")

name = input("Type The Username Of The Account: ")
ans = input("1 For Followers: \n2 For Following: ")


bot.login(username=username , password=password)


if ans == '1':
    f = bot.get_user_followers(name)
    
elif ans == '2':
    f = bot.get_user_following(name)



# creating a file path

os.mkdir(name)
os.chdir(name)

for follow in f:


    f = open(bot.get_username_from_user_id(follow) , 'x' , encoding='utf-8')
    f.write(str(bot.get_user_info(follow)))

    '''
    print(bot.get_user_info(follow))
    print()
    '''