import phonenumbers

from phonenumbers import geocoder

phone = input('Informe o telefone no formato +PAISestadoNUMERO: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))