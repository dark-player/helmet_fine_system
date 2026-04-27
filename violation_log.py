import openpyxl
from datetime import datetime
import os

FILE = "violations.xlsx"

def create_file():
    if not os.path.exists(FILE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Plate", "Fine", "Image", "Time"])
        wb.save(FILE)

def add_violation(plate, fine, image):
    create_file()
    wb = openpyxl.load_workbook(FILE)
    ws = wb.active
    ws.append([plate, fine, image, str(datetime.now())])
    wb.save(FILE)