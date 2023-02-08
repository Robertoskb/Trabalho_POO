from data.jsonhandler import JsonHandler
import speech_recognition as sr
from say_it import say
from datetime import datetime
from checkexpirations import check_expirations, parser_date
import re

check_day = lambda string: re.search(r'\b(um dia|\d+)\b', string)
check_index = lambda string: re.search(r'\b(primeiro|\d+|primeiro lembrete)\b', string)

file = JsonHandler('data/data.json')
recognizer = sr.Recognizer()


def listen(show_all=False):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            if show_all:
                return recognizer.recognize_google(audio, language='pt-BR', show_all=True)
            return recognizer.recognize_google(audio, language='pt-BR').lower()

        except sr.UnknownValueError:
            return ''

        except sr.RequestError:
            return ''


def confirm(msg):
    reply = ''

    while reply not in ['sim', 'não']:
        reply = listen()

        if reply not in ['sim', 'não']:
            say(msg)

    return reply


def add_remind():
    data = file.read_json
    
    say('Qual o conteudo do lembrete?')
    
    content = ''
    while not content:
        content = listen()
        
        if not content:
            say('Desculpe, não consegui entender. Por favor, fale novamente o conteudo do lembrete')
    
    say('o seu lembrete tem data para expiração? Sim ou Não')

    confirm_expr = confirm('Desculpe, não consegui entender. o Seu lembrete tem data para expiração? Sim ou Não')
        
    if confirm_expr == 'sim':
        num_days = ''

        say('diga o número de dias de 1 a 30')
        while num_days not in map(str, range(1, 31)):
            result = check_day(str(listen(True)))
            num_days = result.group(0) if result else ''
            if num_days == "um dia":
                num_days = "1"
            if num_days not in map(str, range(1, 31)):
                say('Por favor, fale um número de 1 a 30')

        num_days = int(num_days)

    elif confirm_expr == 'não':
        say('Ok, seu lembrete expira em dois dias')
        num_days = 2
    
    data.append({'content': content, 'expiration': num_days, 'date': str(datetime.now())})
    file.write_json(data)
    say('lembrete salvo com sucesso!')


def list_reminds():
    data = check_expirations()
    now = datetime.now()
    data.sort(key=lambda d: d['expiration'] - (now - datetime.strptime(d['date'], r"%Y-%m-%d %H:%M:%S.%f")).days)

    if not data:
        say("Nenhum lembrete salvo")

        return

    for cont, remind in enumerate(data, 1):
        date = parser_date(remind['date'])
        days = remind['expiration']

        difference = days - (datetime.now() - date).days
        say(f"lembrete {cont}, {remind['content']}. {difference} {'dias restantes' if difference != 1 else 'dia restante'}")

    say('fim da lista de lembretes')


def delete_remind():
    data = check_expirations()
    num_reminds = len(data)

    if not data:
        say('Nenhum lebrete salvo')

        return

    if num_reminds == 1:
        say('apenas um lembrete salvo. deseja exclir? Sim ou Não?')
        conf = confirm('não entendi. você quer excluir o lembrete? sim ou não')

        if conf == 'sim':
            data.pop()
            file.write_json(data)
            say('lebrete excluido com sucesso')

            return

    say('Atenção! Utilize o comando "listar lembretes" para evitar excluir um lembrete errado!')

    while True:
        say(f'diga o número do lembrete que você quer excluir de 1 a {num_reminds}')

        try:
            result = check_index(str(listen(True)))
            index = result.group(0) if result else ''

            if index == 'primeiro' or index == 'primeiro lembrete':
                index = '1'

            remind = data[abs(int(index)-1)]

            say(f'você quer excluir o lembrete {remind["content"]}? sim ou não')
            conf = confirm(f'não entendi, você quer excluir o lembrete {remind["content"]}? sim ou não')

            if conf == 'sim':
                data.pop(abs(int(index)-1))

                file.write_json(data)
                say('lembrete excluido com sucesso!')

            break

        except ValueError:
            say('posição inválida!')

        except IndexError:
            say('número inválido!')

        except TypeError:
            say('número inválido!')


if __name__ == '__main__':
    # add_reminder()

    delete_remind()
    list_reminds()

