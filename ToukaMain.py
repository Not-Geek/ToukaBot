import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f"{client.user} has connected to Discord!")

# client.run(TOKEN)
bot = commands.Bot(command_prefix='!')
@bot.command(name='99')
async def nine_nine(ctx, action, person: str):
    name = person
    brooklyn_99_quotes = [
        f'{name} is the human form of the 💯 emoji.',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        f'{name} Slept With My Wife, Kelly, In 1998!',
        f'{name} is Amazing human/genius',
        f'Okay, no hard feelings, but I hate you {name}. Not joking. Bye.',
        f'{name}\'s mother cried the day {name} was born because she knew she would never be prettier than {name}.'
    ]

    burns = [
        f'{name} is the reason God created the middle finger.',
        f'Light travels faster than sound which is why {name} seemed bright until {name} spoke.',
        f'I’ll never forget the first time I met {name}. But I’ll keep trying.',
        f'{name}\'s face makes onions cry.',
        f'I’m not insulting you {name}, I’m describing you.',
        f'{name} bring everyone so much joy…when {name} leave the room.',
        f'I thought of {name} today. It reminded me to take out the trash.',
        f'{name} if you’re going to be two-faced, at least make one of them pretty.',
        f'{name} is like a cloud. When {name} disappear it’s a beautiful day.',
        f'{name} is so full of shit, the toilet’s jealous.',
        f'{name} just might be why the middle finger was invented in the first place.',
        f'{name} *Thumbs down*',
        f'I’m busy right now, can I ignore you another time?',
        f'{name} if you have a problem with me, write the problem on a piece of paper, fold it, and shove it up your ass.',
        f'Well, the jerk store called and they’re running out of {name}.',
        f'{name} you have an entire life to be an idiot. Why not take today off?',
        f'{name} is the human version of period cramps.',
        f'{name} your face is just fine but we’ll have to put a bag over that personality. Nevermind, cover that face too!',
        f'Keep rolling your eyes {name}, you might eventually find a brain',
        f'{name} Hold still. I’m trying to imagine you with personality.',
    ]

    flirts = [
        f'{name} you\'re so hot, my zipper is falling for you.',
        f'{name} They say that kissing is a language of love, so would you mind starting a conversation with me?',
        f'{name} I’m on top of things. Would you like to be one of them? ',
        f'Hey! My name is Microsoft. Can I crash at your place tonight? {name}',
        f'Is your name winter? Because you’ll be coming soon. {name}',
        f'{name} Give me your car keys so I can drive you crazy ',
        f'{name} I love my bed but I’d rather be in yours.',
        f'{name} Your body is made up of 70% water. . .and I’m thirsty.',
        f'{name} Is it hot in here? Or is it just you?',
        f'{name} I lost my keys… Can I check your pants?',
        f'{name} Are you an elevator? Because I’ll go up and down on you.',
        f'That’s a nice shirt. Can I try it on after we have sex?',
        f'Can I borrow a kiss? I promise I’ll give it back.',
        f'What is a nice person like you doing in a dirty mind like mine?',
        f'I’m not feeling myself today. Can I feel you instead?',

    ]

    if action.lower()=="burn":
        response = random.choice(burns)
    elif action.lower()=="flirt":
        response = random.choice(flirts)

    elif action.lower()=="show":
        res = requests.get("https://api.wazirx.com/api/v2/tickers")
        if res.status_code == 200:
            data = res.json()
            key = person+"inr"
            name = "base_unit"
            #print(res.json())
            response = f'Coin = {data[key][name]}, current price = {data[key]["last"]}'
        else:
            await ctx.send("Error occurred")
    else:
        response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


bot.run(TOKEN)

