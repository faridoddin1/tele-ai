import telebot
import os
import openai
from base64 import b64decode

#insert your botfather token
bot = telebot.TeleBot('123456789:a*************************')

@bot.message_handler(commands=['gen'])
def generate_image(message):
    prompt = message.text
    #insert your open ai api key hnere
    openai.api_key = 'sk-**********************************'

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size='1024x1024',
        response_format='b64_json'
    )

    
    image_data = b64decode(response['data'][0]['b64_json'])
    file_name = '_'.join(prompt.split(' '))

    with open(f'{file_name}.png', 'wb') as file:
        file.write(image_data)

    bot.send_photo(message.chat.id, open(f'{file_name}.png', 'rb'))

bot.polling()
