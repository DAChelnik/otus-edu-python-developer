import random

def generate_password(length=8,
                      use_digits=True,
                      use_uppercase_letters=True,
                      use_lowercase_letters=True,
                      use_special_chars=True):
    chars = ''
    if use_digits:
        chars += '0123456789'
    if use_uppercase_letters:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lowercase_letters:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if use_special_chars:
        chars += '!@#$%^&*()_+~`|}{[]:;?><,./-='

    # Проверяем минимальную длину (4 символа)
    length = max(length, 4)

    # Генерируем пароль
    password = ''.join(random.sample(chars, length))
    return password

# Пример вызова:
print(generate_password(12))  # Пароль без спец. символов, длиной 12 символов

print(generate_password(17))

print(generate_password())
