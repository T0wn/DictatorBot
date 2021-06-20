from get_docker_secret import get_docker_secret
from DictatorBot import DictatorBot

BOT_TOKEN = get_docker_secret("bot_token")
    
bot = DictatorBot()
bot.run(BOT_TOKEN)