import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NzE3NzE1NjAyNzc2Nzg0OTA2.XtfNrg.UVCK0MNzxtCOrtdjUr7BoJwwUgQ'
self_bot_token = 'NzEyMjA2NjQ5Mjk2OTQ1MTYz.XsOMZA.Er836KJaQ25HKoTXDQnLQJBROYE'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id='717760593637015632')

input_hq_private  = [
    "712206649296945163",
    "459842150323060736",
    "580198028950896640",
	    "513818250652680213",
	    "595639586726740049",
	    "568617830258442255",
	    "569420198717816852",
	    "591600008353021953",
	    "585285701671714826",
	    "595301050374815757",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "595301050374815757", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['712206649296945163']
command_channel = '712206649296945163' #trivia-answers
admin_chat = '712206649296945163' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
