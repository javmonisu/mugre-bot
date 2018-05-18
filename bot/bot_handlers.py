"""
Bot message handlers.
"""
from random import randint
from bot.polling import Bot
from bot.general import Gif, Dog, Excel, empty_command, long_text, help
from bot.fishes import fishes
from os import environ
import re

# Bot TOKEN
creator = 8143995
token = environ['BOT_TOKEN']
bot = Bot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    username = message.from_user.first_name
    text = 'Hola {}. Escribe /help para conocer más.'.format(username)
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    text = help()
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['eccel'])
def get_eccel(message):
    chat_id = message.chat.id
    text_list = Excel().select(chat_id)
    if text_list:
        text = 'El maravilloso <b>eccelmovil</b> de Da🍯:\n\n'
        for index, line in enumerate(text_list):
            text += "[{}] {}\n".format(index+1, line)
        text += '\nPara añadir un dahonysmo nuevo: /addeccel@TheMugrestBot (texto)'

    else:
        text = 'Dahoney no tiene nada que hacer... Debe ser un error.'
    bot.send_message(chat_id, text, parse_mode='HTML')


@bot.message_handler(commands=['addeccel'])
def add_to_excel(message):
    chat_id = message.chat.id
    # Only works in groups < 0
    if chat_id < 0:
        message = message.text.strip()
        space = message.find(' ')
        if space == -1:
            text = 'La próxima vez escribe algo, botarate.\n\n' \
                   '/addeccel@TheMugrestBot Una moto nueva'
        else:
            real_text = message[space + 1:].strip()
            if Excel().write(chat_id, real_text):
                text = 'Esta es la mierda que has añadido:\n\n{}'.format(real_text)
            else:
                text = 'No pude añadir eso...'
        bot.send_message(chat_id, text)


@bot.message_handler(commands=['doggo'])
def send_doggo(message):
    chat_id = message.chat.id
    people = Dog().select(chat_id)
    text = ''
    if people:
        for person in people:
            text += '@{} '.format(person)
    else:
        text = 'No hay doggerfags.'
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['adddoggo'])
def get_doggo(message):
    chat_id = message.chat.id
    username = message.from_user.username
    if username not in Dog().select(chat_id):
        Dog().write(chat_id, username)
        bot.send_message(chat_id, '@{} has sido añadido a la lista. /doggo@TheMugrestBot para citar.'.format(username))
    else:
        bot.send_message(chat_id, 'Ya estás en la lista, popegrades.')


@bot.message_handler(commands=['deldoggo'])
def del_doggo(message):
    chat_id = message.chat.id
    username = message.from_user.username
    if username in Dog().select(chat_id):
        Dog().remove(chat_id, username)
        bot.send_message(chat_id, '@{} has sido borrado de la lista.'.format(username))
    else:
        bot.send_message(chat_id, 'No estás en la lista, pacard@.')


@bot.message_handler(commands=['kirigiri'])
def kirigiri(message):
    chat_id = message.chat.id
    username = message.from_user.username
    text = '@{} se siente como <b>kirigiri</b>.'.format(username)
    bot.send_message(chat_id, text, parse_mode='HTML')


@bot.message_handler(commands=['gif'])
def gif(message):
    chat_id = message.chat.id
    gif_to_send = Gif().select
    if gif_to_send:
        bot.send_document(chat_id, data=gif_to_send)
    else:
        text = 'No te puedo enviar nada, lo siento.'
        bot.send_message(chat_id, text)


@bot.message_handler(commands=['addgif'])
def add_gif(message):
    chat_id = message.chat.id
    if chat_id == creator:
        bot.send_message(chat_id, 'Manda el gif.')
        bot.register_next_step_handler(message, get_gif)


def get_gif(message):
    chat_id = message.chat.id
    if message.content_type == 'document':
        gif_to_add = message.document.file_id
        if Gif().write(gif_to_add):
            bot.send_message(chat_id, 'Añadido.')
    else:
        bot.send_message(chat_id, 'No puedo insertar eso, amigo.')


@bot.message_handler(commands=['dice'])
def dice(message):
    space = empty_command(message.text)
    if space == -1:
        dice = randint(1,6)
    else:
        try:
            dice = randint(1, int(message.text.strip()[space+1:]))
        except ValueError:
            dice = '¿Estás tonto?'
    bot.reply_to(message, dice)


@bot.message_handler(commands=['google'])
def google(message):
    chat_id = message.chat.id
    google = 'http://www.google.com/search?q='
    try:
        text_to_search = message.reply_to_message.text
        text_to_search = google + text_to_search.strip().replace(',', ' ').strip().replace(' ', '+').strip()
    except:
        space = empty_command(message.text)
        if space > 0:
            text_to_search = google + message.text[space+1:].strip().replace(',', ' ').strip().replace(' ', '+').strip()
        else:
            text_to_search = 'Busca algo, ¿no?'
    finally:
        bot.send_message(chat_id, text_to_search, disable_web_page_preview=True)


@bot.message_handler(commands=['word'])
def word(message):
    chat_id = message.chat.id
    word = 'http://www.wordreference.com/es/translation.asp?tranword='
    space = empty_command(message.text)
    if space > 0:
        text_to_search = word + message.text[space + 1:].strip().replace(',', ' ').strip().replace(' ', '+').strip()
    else:
        text_to_search = 'http://www.wordreference.com/random/enes'
    bot.send_message(chat_id, text_to_search, disable_web_page_preview=True)


@bot.message_handler(commands=['animally'])
def animally(message):
    chat_id = message.chat.id
    text = long_text()
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['dylanface'])
def dylanface(message):
    chat_id = message.chat.id
    dylanface = 'AgADBAADIKwxG32FgFPwhkJH30Am6F21mxoABMBX6pXwx8iH7nIBAAEC'
    bot.send_photo(chat_id, photo=dylanface)


@bot.message_handler(commands=['aboutme'])
def aboutme(message):
    chat_id = message.chat.id
    text = 'Visítame en:\n\nhttps://github.com/dmonter/mugre-bot\n\nY dale a la <b>estrellita</b>, cabrón.'
    bot.send_message(chat_id, text, parse_mode='HTML')


@bot.message_handler(commands=['pescado'])
def pescado(message):
    chat_id = message.chat.id
    text = fishes()
    bot.send_message(chat_id, text, parse_mode='HTML')


# To add hardcoded images as /dylanface
#@bot.message_handler(content_types='photo')
@bot.message_handler(commands=['addimage'])
def read_image(message):
    chat_id = message.chat.id
    if chat_id == creator:
        bot.send_message(chat_id, message.photo)


regex = re.compile('(\s(en)\s(la)?(tu)?(mi)?(su)?\svida(\.)?$|(\s)?no\sse\sni\scoger\s)', re.IGNORECASE)


def handle_messages(messages):
    for message in messages:
        if message.text is not None:
            if re.search(regex, message.text) is not None:
                    bot.reply_to(message, 'hulio')


bot.set_update_listener(handle_messages)

