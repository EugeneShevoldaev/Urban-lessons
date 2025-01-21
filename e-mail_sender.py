def send_email(message='Привет!', recipient='vasyok1337@gmail.com',*,sender="university.help@gmail.com"):
    # проверка на наличие символа '@'
    if '@' not in sender or '@' not in recipient:
        print(f'не возможно отправить письмо с адреса {sender} на адрес {recipient} нет собаки')
        return
    # проверка наличия доменов
    valid_domains = ['.ru', '.com', '.net']
    resolt_for_sender = any(domain in sender for domain in valid_domains)
    resolt_for_recipient = any(domain in recipient for domain in valid_domains)
    resolt = resolt_for_sender + resolt_for_recipient
    if resolt < 2:
        print(f'не возможно отправить письмо с адреса {sender} на адрес {recipient} нет домена')
        return

    # проверка на отправку себе
    if sender == recipient or recipient == sender:
        print('не возможно отправить письмо самому себе')
        resolt = resolt - 1
        return

    if sender != "university.help@gmail.com":
        print(f'не стандартный отправитель, письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        resolt = resolt + 1
    if resolt == 2:
        print(f'письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email()


# я поправил код и протестировал вроде бы все возможные комбинации, у меня выходит лишь одно какое-либо сообщение
# если в коде вновь обнаружится ошибка, пожалуйста напишите комбинацию условий при которых это происходит