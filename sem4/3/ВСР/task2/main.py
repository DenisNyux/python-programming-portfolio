from instabot import Bot
bot = Bot()
INST_USERNAME = 'denisnyux'
with open('pswrd.txt', 'r') as file:
    INST_PASSWORD = file.readline()
bot.login(username = INST_USERNAME,  password = INST_PASSWORD)
user_followers = bot.get_user_followers(INST_USERNAME) # Список подписчиков

usernames = []
for each in user_followers:
    usernames.append(bot.get_username_from_user_id(each))

with open('followers.txt', 'w') as logs:
    for item in usernames:
        logs.write("%s\n" % item)
print(usernames)