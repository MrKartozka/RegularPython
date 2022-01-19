import re
def clean_code(code):
    code = re.sub('@\S+', '', code)
    code = re.sub('#\S+', '', code)
    code = re.sub('\s+', ' ', code)
    code = re.sub('http\S+\s*', '', code)
    code = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', code)
    code = re.sub('RT|cc', '', code)
    return code
code = '''@ошибка-кода Чтобы [я сделал# по другому, если бы,,, сегодня; учился программировать? https://t.co/lbwej0pxOd cc: @хэштег #статистика'''
print(clean_code(code))