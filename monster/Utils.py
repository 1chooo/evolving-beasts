# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/07
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os

def check_dir(file_path) -> None:

    if not os.path.isdir(file_path):
        os.mkdir(file_path, mode=0o777)
        print(file_path, 'has been created successfully.')

    return None

def get_output_path(file_path, current_date, id, file_type) -> str:

    filename = f"{current_date}_{id}{file_type}"
    output_path = os.path.join(file_path, filename)
    
    return output_path