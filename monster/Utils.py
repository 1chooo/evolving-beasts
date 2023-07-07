import os

def check_dir(file_path) -> None:

    if not os.path.isdir(file_path):
        os.mkdir(file_path, mode=0o777)
        print(file_path, 'has been created successfully.')

    return None