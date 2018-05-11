"""
Classes for reading & writing to the database.
"""
from database.mongo import db
from random import choice


def empty_command(text):
    return text.strip().find(' ')


def help():
    text = ('Usa /comando@TheMugrestBot para que funcione correctamente.\n\n'
            '/start - Saludo\n'
            '/eccel - Muestro el eccelmovil\n'
            '/addeccel - addeccel (texto) para añadir una entrada\n'
            '/dice - (número) Lanzo un dado de (número) caras, por defecto 6\n'
            '/doggo - Cito a los doggerfags\n'
            '/adddoggo - Te añado a la lista de doggerfags\n'
            '/deldoggo - Te borro de la lista de doggerfags\n'
            '/dylanface - Dylanface\n'
            '/google - (texto) Busco (texto) en google. También funciona citando\n'
            '/gif - Envía un gif aleatorio\n'
            '/animally - Muestro un tocho milenario\n'
            '/kirigiri - Me siento como…\n'
            '/help - Muestra la ayuda\n'
    )
    return text


class Excel:
    def select(self, chat_id):
        try:
            excel_collection = db.eccel.find({'chat_id': chat_id})
            text_list = [row['text'] for row in excel_collection]
            return text_list
        except:
            return None

    def write(self, chat_id, text):
        try:
            db.eccel.insert_one({
                'chat_id': chat_id,
                'text': text
            })
            return 1
        except:
            return None


class Dog:
    def select(self, chat_id):
        try:
            people_collection = db.doggos.find({'chat_id': chat_id})
            people = set(person['username'] for person in people_collection)
            return people
        except:
            return None

    def write(self, chat_id, username):
        try:
            db.doggos.insert_one({
                'chat_id': chat_id,
                'username': username
            })
            return 1
        except:
            return None

    def remove(self, chat_id, username):
        try:
            db.doggos.remove({
                'chat_id': chat_id,
                'username': username
            })
            return 1
        except:
            return None


class Gif:
    @property
    def select(self):
        try:
            gifs_collection = db.gifs.find()
            gifs = [gif for gif in gifs_collection]
            return choice(gifs)['gif_id']
        except:
            return None

    def write(self, gif_id):
        try:
            db.gifs.insert_one({'gif_id': gif_id})
            return 1
        except:
            return None


def long_text():
    text = ('Te tomaras a broma o chiste esto pero me tomare la molestia de escribirlo. '
            'Sabes, no tengo nada en contra de gente del foro, ni en la vida real. '
            'Tengo peña, mis ligues, folleteos, trabajos puntuales, alegrias, proyectos. '
            'Lo tipico de todos. Seguramente tu tambien lo tengas, seguramente tengas unos amigos '
            'geniales y una novia maravillosa o yo que se. Asi que cmo persona cualquiera te comento '
            'de buenas: deja de dar por culo. Ni bromas ni chistes, ya todo lo tuyo no me hace ni puta '
            'gracia ni pena, me da asco. Ya ni te ries de lloros, directamente buscas cada post mio cual '
            'puto obseso enfermo para reirte de ello. No tienes nada mejor que hacer con tu vida? '
            'Te dedico 5 minutos escribiendo esto, pero si quieres puedo dedicarte unas cuantas horas '
            'charlando con mods o con ciertas personas de la policia para ver si lo que haces esta bien. '
            'Te repito de nuevo, estoy siendo bueno por ahora. No me pongas mas razones para que esta '
            'tontetia tuya de niño pequeño malcriado vaya a peores.'
    )
    return text