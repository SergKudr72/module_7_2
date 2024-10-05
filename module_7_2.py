import io

def custom_write(file_name: str, strings: list):
    strings_positions = {}
    number_str = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte_start_str = file.tell()
        file.write(f'{string}\n')
        strings_positions[(number_str, byte_start_str)] = string
        number_str += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
