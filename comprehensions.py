
def devowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels = [letter for letter in sentence if letter not in vowels]
    return ''.join(no_vowels)

print(devowel('List Comprehensions are the Greatest!'))

with open('data.csv') as open_file:
    next(open_file)
    contents = open_file.readlines()
data_list = [row.replace('\n', "").split(',') for row in contents]


def water_temps(data_list):
    temps = [row[4] for row in data_list]
    return temps
print(water_temps(data_list))


def water_temp_floats(data_list):
    temp_floats = [float(row[4]) for row in data_list]
    return temp_floats
print(water_temp_floats(data_list))


def fahrenheit(data_list):
    degrees_f = [int((float(row[4]) * 1.8) + 32) for row in data_list]
    return degrees_f
print(fahrenheit(data_list))


def date_waveheight(data_list):
    date_wh = {row[5]: row[1] for row in data_list}
    return date_wh
print(date_waveheight(data_list))
