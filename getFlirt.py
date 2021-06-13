import random

def flirt(name: str):
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

	return random.choice(flirts)