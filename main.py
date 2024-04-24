import os
import argparse

image_extensions = ['.jpg', '.jpeg', '.png']
document_extensions = ['.doc', '.pdf']
file_type_choices = {
    '1': 'images',
    '2': 'documents',
    '3': 'exit'
}

rename_type_choices = {
    '1': 'prefix',
    '2': 'suffix'
}

file_type_choices_string = ''
for key in file_type_choices:
    file_type_choices_string += f'{key}. {file_type_choices[key]} \n'

def get_user_file_type_choice():
    user_choice = input(f'Which type of file do you want to rename? \n{file_type_choices_string}')

    if not file_type_choices.get(user_choice):
        print(f'{user_choice} is not a valid choice. Please make a valid choice.')
        get_user_file_type_choice()

    return user_choice

def get_dir_list():
    dir_choice = input('Path to rename files? \n')
    try:
        return os.listdir(dir_choice)
    except:
        print(f'{dir_choice} does not exit \n')
        print('Please provide an existing path')
        get_dir_list()

def main():
    dir_list = get_dir_list()

    user_choice = get_user_file_type_choice()

    match user_choice:
        case '1':
            extensions_to_rename = image_extensions
        case '2':
            extensions_to_rename = document_extensions
        case '3':
            exit()

    for filename in dir_list:
        file, extension = os.path.splitext(filename)
        if extension in extensions_to_rename:
            os.rename(filename, file + '_new' + extension)

main()