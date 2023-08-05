ADRESSBOOK = {}

def input_error(inner):
    def wrap(*args):        
        try:            
            if (inner(*args)) == None:
                return 'Unknown command'
            return inner(*args)
        except KeyError:
            return "This name is not in the address book"
        except ValueError:
            return "Phone must contain only numbers"
        except IndexError:
            return "Give me name and phone please"         
    return wrap

@input_error
def add_hundler(data):      # Функція додавання контакту з номером тел.
    name = data[0].title()
    phone = int(data[1])    # Провокуємо помилку ValueError якщо тел. містить не тільки цифри або IndexError якщо тел. не введено
    ADRESSBOOK[name] = phone    
    return 'Done'

@input_error
def change_hundler(data):    # Функція зміни номеру тел. контакту
    name = data[0].title()
    phone = ADRESSBOOK[name] # Провокуємо помилку KeyError якщо такого контакту немає
    new_phone = int(data[1]) # Провокуємо помилку ValueError якщо тел. містить не тільки цифри або IndexError якщо тел. не введено
    ADRESSBOOK[name] = new_phone
    return 'Done'         
    
@input_error
def phone_hundler(data):      # Функція отримання номеру тел. за іменем контакту
    name = data[0].title()
    phone = ADRESSBOOK[name]  # Провокуємо помилку KeyError якщо такого контакту немає
    return phone
    
def showall_hundler(data):      # Функція виводу всього переліку контактів з номерами тел.
    if ADRESSBOOK:
        return ADRESSBOOK
    else:
        return 'ADRESSBOOK is empty'

def exit_hundler(*args):         # Завершення роботи
    return 'Good bye!'

def hello_hundler(*args):        # Привітання
    return 'How can I help you?'

@input_error
def command_parser(raw_str: str): # Парсер команд
    elements = raw_str.split()    
    for key, value in COMMANDS.items():
        for cmd in value:
            if cmd.startswith(elements[0].lower()) and ' ' in cmd:
                double_word_cmd = elements[0] + ' ' + elements[1]
                elements[0] = double_word_cmd
                del elements[1]
        if elements[0].lower() in value:
            return key(elements[1:])    
    # return 'Unknown command'        # Повертаэмо помилку, якщо команду не розпізнано 
    
COMMANDS = {
    add_hundler: ['add', '+'],
    exit_hundler: ['good bye', 'close', 'exit'],
    hello_hundler: ['hello'],
    change_hundler: ['change'],
    phone_hundler: ['phone'],
    showall_hundler: ['show all']
}

def main(): # Цикл запит-відповідь

    while True:
        user_input = input('Phone bot>>> ')   
        if not user_input:
            print('Enter command please!')
            continue
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break
        
if __name__ == "__main__":
    main()
