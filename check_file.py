import os

def check_if_personal_file_exists():
    return os.path.exists('../user_data.db')

check = check_if_personal_file_exists()