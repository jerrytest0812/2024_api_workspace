from pprint import pprint
from openpyxl import load_workbook, Workbook, worksheet

def get_aqi(excel_name:str) -> list[dict]:
    wb:Workbook = load_workbook(excel_name)
    sheet:worksheet = wb.worksheets[0]

    sheets:list=[]

    colums_name = [cell.value for cell in list(sheet)[0]]
    # colums_name=[cell.value, cell.value, cell.value ....]
    for row in list(sheet)[1:]:
        site:dict = { colums_name[idx]:item.value for idx,item in enumerate(row) }
        
        sheets.append(site)

    return sheets

def get_sitenames(excel_name:str)->list[str]:
    data:list[dict] = get_aqi(excel_name)
    sitenames:list = []
    for item in data:
        sitenames.append(item['sitename'])
    sitenames=list(set(sitenames))
    return sitenames