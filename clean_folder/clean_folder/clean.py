from pathlib import Path
import sys
import os
import shutil
import re
import zipfile
import tarfile

p = Path(sys.argv[1])
groups = {
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'image': ['jpeg', 'png', 'jpg', 'svg'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'archives': ['zip', 'gz', 'tar'],
}


def create_folders(path):
    for f in groups:
        folder = os.path.join(path, f)
        if not os.path.exists(folder):
            os.mkdir(folder)


def sort_files(target_path, move_to=None):
    if move_to is None:
        move_to = target_path

    b = [k for f, k in groups.items()]
    for el in target_path.iterdir():

        if el.is_file():
            extension = el.name.split('.')[-1]

            if extension.lower() in b[3]:
                destination = move_to / 'documents'
                new_location = shutil.move(el, destination)
            if extension.lower() in b[0]:
                destination = move_to / 'video'
                new_location = shutil.move(el, destination)
            if extension.lower() in b[1]:
                destination = move_to / 'audio'
                new_location = shutil.move(el, destination)
            if extension.lower() in b[2]:
                destination = move_to / 'image'
                new_location = shutil.move(el, destination)
            if extension.lower() in b[4]:
                destination = move_to / 'archives'
                new_location = shutil.move(el, destination)
        if el.is_dir():
            if el.name in groups.keys():
                pass
            else:
                sort_files(el, move_to)


def normalize(meme):
    dictionary = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': 'y',
        'ы': 'y',
        'ь': "'",
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Yo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ъ': 'Y',
        'Ы': 'Y',
        'Ь': "'",
        'Э': 'E',
        'Ю': 'Yu',
        'Я': 'Ya',
        'і': 'i',
    }

    new_string = ""
    for s in meme:
        if s in dictionary:
            new_string += dictionary[s]
        elif s == " ":
            new_string += "_"
        else:
            new_string += s
    extension = '.' + new_string.split('.')[-1]
    new_string2 = new_string.replace(extension, '')

    s1 = re.sub("[^A-Za-z0-9]", "_", new_string2)

    return s1


def new_names(destiny):
    for el in destiny.iterdir():
        if el.is_file():
            expansion = el.name.split('.')[-1]
            for f in groups:
                if expansion.lower() in groups[f]:
                    file_oldname = os.path.join(destiny, el.name)
                    file_newname_newfile = os.path.join(destiny, normalize(el.name) + '.' + expansion)
                    os.rename(file_oldname, file_newname_newfile)

        if el.is_dir():
            new_names(el)
            old_folder = os.path.join(destiny, el.name)
            new_folder = os.path.join(destiny, normalize(el.name))
            os.rename(old_folder, new_folder)


#
def extract_archives():
    path = p / 'archives'
    for el in path.iterdir():
        extension = el.name.split('.')[-1]
        if extension == 'zip':
            main = zipfile.ZipFile(el)
            main.extractall(path)

        if extension == 'tar':
            hehe = tarfile.open(el)
            hehe.extractall(path)
        if extension == 'tar.gz':
            meme = tarfile.open(el)
            meme.extractall(path)


def del_empty_dirs(path):
    for el in path.iterdir():
        if el.is_dir():
            del_empty_dirs(el)
            if len(os.listdir(el)) == 0:
                os.rmdir(el)


if __name__ == '__main__':
    create_folders(p)
    sort_files(p, move_to=None)
    new_names(p)
    extract_archives()
    del_empty_dirs(p)
