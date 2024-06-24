import pandas as pd
import csv
import os
import datetime
from functools import reduce

FILE_PATH = ""


def generate_csv(section: str, students_present: dict):

    path = f"{os.getcwd()}\\section_attendance\\{section}"
    if not (os.path.exists(path)):
        os.mkdir(path)
    # old_dir = os.getcwd()
    # os.chdir(path)

    current_dt = datetime.datetime.now()
    file_name = f"{current_dt.strftime('%d_%m_%Y - %H_%M_%S')}.csv"
    csv_file_path = os.path.join(path, file_name)
    global FILE_PATH
    FILE_PATH = csv_file_path
    with open(csv_file_path, "w+", newline="") as employee_file:
        employee_writer = csv.writer(employee_file)
        employee_writer.writerow(["Total", len(students_present)])
        employee_writer.writerow(["Total Present", sum(students_present.values())])
        employee_writer.writerow([])
        for name, present in students_present.items():
            employee_writer.writerow([name, present])


def getLastFilePath():
    return FILE_PATH
