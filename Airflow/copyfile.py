from datetime import datetime
import shutil

# Task 2: Copy the CSV file into another folder
def copy_csv():
    source_folder = r"D:\SampleData\sales"  # Use "r" before the string to treat it as a raw string
    destination_folder = r"D:\SampleData\sales\dest"  # Use "r" before the string to treat it as a raw string
    file_to_copy = 'sales_data_sample.csv'
    # Copy the CSV file from the source folder to the destination folder
    shutil.copyfile(source_folder + '\\' + file_to_copy, destination_folder + '\\' + file_to_copy)
    print("Task 2: Copy the CSV file into another folder")

copy_csv()
