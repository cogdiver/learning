import os
import pandas as pd
from multiprocessing import Pool


def report_errors(folder_informs, folder_errs, ft):
    files_temp = os.listdir(folder_errs)

    if files_temp:

        files_with_errors = [f'{folder_errs}/{f}' for f in files_temp]
        path = f'{folder_informs}/reporte_errores_{ft}.xlsx'
        list_export = {}

        with pd.ExcelWriter(path) as w:
            columns = [23, 37, 'err'] if ft == 'ft01' else [11, 'err']
            column_comer = 37 if ft == 'ft01' else 11

            for f in files_with_errors:
                temp = pd.read_excel(f, dtype=str)
                # obtener columnas necesarias
                temp = temp.loc[:, columns]

                comer = temp.loc[0, column_comer]
                list_group = [23, 'err'] if ft == 'ft01' else 'err'
                temp_report = temp.groupby(list_group).size().reset_index()
                del temp

                temp_report['origen'] = f.split("/")[-1]


                if comer not in list_export:
                    list_export[comer] = []
                list_export[comer].append(temp_report)

            print('-'*50, ft, 'Archivo')

            comers = list(list_export.keys())[:]
            for comer in comers:
                temp_report = pd.concat(list_export[comer], axis=0).reset_index(drop=True)
                del list_export[comer]

                list_group = [23, 'err'] if ft == 'ft01' else 'err'
                temp_report = temp_report.groupby(list_group).agg({'origen': 'unique', 0: 'sum'}).reset_index()

                temp_report.to_excel(w, index=False, sheet_name=comer)


def read_excel(f, ft, columns, column_comer):
    temp = pd.read_excel(f, dtype=str)
    # obtener columnas necesarias
    temp = temp.loc[:, columns]

    comer = temp.loc[0, column_comer]
    list_group = [23, 'err'] if ft == 'ft01' else 'err'
    temp_report = temp.groupby(list_group).size().reset_index()
    del temp

    temp_report['origen'] = f.split("/")[-1]

    return comer, temp_report


def report_errors_pool(folder_informs, folder_errs, ft):
    files_temp = os.listdir(folder_errs)

    if files_temp:

        files_with_errors = [f'{folder_errs}/{f}' for f in files_temp]
        path = f'{folder_informs}/reporte_errores_{ft}.xlsx'
        list_export = {}

        with pd.ExcelWriter(path) as w:
            columns = [23, 37, 'err'] if ft == 'ft01' else [11, 'err']
            column_comer = 37 if ft == 'ft01' else 11

            with Pool(5) as p:
                files_result = p.map(read_excel, files_with_errors)
            
            for comer, temp_report in files_result:

                if comer not in list_export:
                    list_export[comer] = []
                list_export[comer].append(temp_report)

            print('-'*50, ft, 'Archivo')

            comers = list(list_export.keys())[:]
            for comer in comers:
                temp_report = pd.concat(list_export[comer], axis=0).reset_index(drop=True)
                del list_export[comer]

                list_group = [23, 'err'] if ft == 'ft01' else 'err'
                temp_report = temp_report.groupby(list_group).agg({'origen': 'unique', 0: 'sum'}).reset_index()

                temp_report.to_excel(w, index=False, sheet_name=comer)

