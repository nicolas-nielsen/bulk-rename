import os
import argparse

image_extensions = ['.jpg', '.jpeg', '.png']
document_extensions = ['.doc', '.pdf']

def extensions_to_string(extensions):
    return ', '.join(extensions)

file_type_choices = {
    '1': f'images ({extensions_to_string(image_extensions)})',
    '2': f'documents ({extensions_to_string(document_extensions)})',
    '3': 'exit the program'
}

rename_type_choices = {
    '1': 'prefix',
    '2': 'suffix',
    '3': 'exit the program'
}

parser = argparse.ArgumentParser(prog='bulk-rename', description='Bulk rename files')
parser.add_argument('-i', '--interactive', action='store_true', help='if flag is present, use bulk-rename in an interactive way in the CLI')
parser.add_argument('path', nargs='?', help='path to rename files')
parser.add_argument('-f', '--files', choices=['images', 'documents'], help='file type')
parser.add_argument('-t', '--type', choices=['prefix', 'suffix'], help='rename type')
args = parser.parse_args()

def choices_to_string(choices):
    choices_string = ''
    for key in choices:
        choices_string += f'{key}. {choices[key]} \n'

    return choices_string

def get_user_file_type_choice():
    user_choice = input(f'Which type of file do you want to rename? \n{choices_to_string(file_type_choices)}')

    if not file_type_choices.get(user_choice):
        print(f'{user_choice} is not a valid choice. Please make a valid choice.')
        get_user_file_type_choice()

    return user_choice

def get_user_rename_type_choice():
    user_choice = input(f'How do you want to rename files? \n{choices_to_string(rename_type_choices)}')

    if not rename_type_choices.get(user_choice):
        print(f'{user_choice} is not a valid choice. Please make a valid choice.')
        get_user_rename_type_choice()

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
    if args.interactive:
        dir_list = get_dir_list()
        user_file_choice = get_user_file_type_choice()
        user_rename_type_choice = get_user_rename_type_choice()

        match user_file_choice:
            case '1':
                extensions_to_rename = image_extensions
            case '2':
                extensions_to_rename = document_extensions
            case '3':
                exit()

        match user_rename_type_choice:
            case '1':
                rename_type = 'prefix'
            case '2':
                rename_type = 'suffix'
            case '3':
                exit()
    else:
        if not args.path or not args.files or not args.type:
            parser.error('If not interactive, path, --files and --type are required')
        match args.files:
            case 'images':
                extensions_to_rename = image_extensions
            case 'documents':
                extensions_to_rename = document_extensions

        dir_list = os.listdir(args.path)
        rename_type = args.type

    for filename in dir_list:
        file, extension = os.path.splitext(filename)
        if extension in extensions_to_rename:
            if rename_type == 'suffix':
                os.rename(filename, file + '_new' + extension)
            else:
                os.rename(filename, 'new_' + filename)

main()