# -*- coding: utf-8 -*-
'''
Create Date: 2023/07/16
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os

def rename_files(folder_path, prefix):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-JPG files
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]
    
    # Sort the JPG files in alphanumeric order
    jpg_files.sort()
    
    # Rename the JPG files sequentially
    for index, file in enumerate(jpg_files):
        # Split the filename and extension
        filename, extension = os.path.splitext(file)
        
        # Create the new filename
        new_filename = f"{prefix}{index+1:03}{extension}"
        
        # Get the current file path and the new file path
        current_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(current_path, new_path)
        print(f"Renamed {file} to {new_filename}")
        
# Usage
folder_path = './cup_up'  # Replace with your folder path
prefix = 'cup_up_'  # Replace with your desired prefix
rename_files(folder_path, prefix)

import os
import random
import shutil
#資料夾路徑
O_path = 'C:/Users/user/Desktop/天氣黑客松/Data/'
tr_path = 'C:/Users/user/Desktop/天氣黑客松/Data_train/'
ve_path = 'C:/Users/user/Desktop/天氣黑客松/Data_verify/'
te_path = 'C:/Users/user/Desktop/天氣黑客松/Data_test/'
#取得資料夾下的所有子資料夾
subfolders = [f.name for f in os.scandir(O_path) if f.is_dir()]
#子資料夾
for subfolder in subfolders:
    source_folder = O_path + subfolder # 原始資料夾
    output_folder_1 = tr_path + subfolder # 目標資料夾1
    output_folder_2 = ve_path + subfolder  # 目標資料夾2
    output_folder_3 = te_path + subfolder  # 目標資料夾3
    #不存在則創建
    for folder in [output_folder_1, output_folder_2, output_folder_3]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    txt_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]
    # 根據 7:2:1 的比例計算檔案分配數量
    num_files = len(txt_files)
    num_files_folder_1 = int(num_files * 0.7)
    num_files_folder_2 = int(num_files * 0.2)
    num_files_folder_3 = num_files - num_files_folder_1 - num_files_folder_2
    # 隨機洗牌 .txt 檔案清單
    random.shuffle(txt_files)
    # 分配檔案到目標資料夾
    for i, file in enumerate(txt_files):
        source_path = os.path.join(source_folder, file) 
        if i < num_files_folder_1:
            output_path = os.path.join(output_folder_1, file)
        elif i < num_files_folder_1 + num_files_folder_2:
            output_path = os.path.join(output_folder_2, file)
        else:
            output_path = os.path.join(output_folder_3, file) 
        # 複製檔案到目標資料夾
        shutil.copy(source_path, output_path)