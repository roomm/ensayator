import os

from openpyxl import load_workbook, Workbook
from dateutil.parser import parse
from datetime import timedelta
from pathlib import Path


class ExcelLogic:

    def __init__(self, file_path):
        self.filePath = file_path
        self.ws = None
        self.preview = None

    def load_preview(self, n=250):
        wb = load_workbook("output.xlsx", read_only=True)
        self.ws = wb.active
        return_prev = []
        for row_idx, row in enumerate(self.ws.iter_rows()):
            row = [x.value for x in row]
            if row_idx == 0:
                return_prev.append(self.format_column_names(row))
                continue
            return_prev.append(row)
            if row_idx >= n:
                break
        self.preview = return_prev

    @classmethod
    def format_column_names(cls, cols):
        cols_reps = {}
        final_cols = []
        for col in cols:
            if col not in final_cols:
                final_cols.append(col)
                cols_reps[col] = 0
            else:
                cols_reps[col] += 1
                col += "." + str(cols_reps[col])
                final_cols.append(col)
        return final_cols

    def detect_ensay_start(self, master, threshold=10):
        columns = None
        previous_val = None
        col_index = None
        for row_idx, row in enumerate(self.ws.iter_rows()):
            row = [x.value for x in row]
            if row_idx == 0:
                columns = self.format_column_names(row)
                col_index = columns.index(master)
                continue
            if previous_val is None:
                previous_val = row[col_index]
                continue
            if abs(row[col_index] - previous_val) > threshold:
                return row, columns
            previous_val = row[col_index]
        return None, None

    def generate_excel(self, column_names, start, end, num, out_name):
        start_row = None
        end_row = None
        target_wb = Workbook(write_only=True)
        tws = target_wb.create_sheet()
        tws.append(column_names)
        for row_idx, row in enumerate(self.ws.iter_rows()):
            if row_idx == 0:
                continue
            row = [x.value for x in row]
            cur_date = parse(row[0])
            if start <= cur_date <= end:
                if start_row is None:
                    start_row = cur_date
                tws.append(row)
                continue
            if cur_date > end:
                end_row = cur_date
                break
        Path("ensay_outputs").mkdir(exist_ok=True, parents=True)
        target_wb.save("ensay_outputs" + os.sep + f"{out_name}_{num}.xlsx")
        return start_row, end_row

    def generate_excel_ensays(self, column_names, ensay_start, duration, offset, num_ensays, out_name, signal):
        ensay_start_date = parse(ensay_start[0])
        # total_ensays = math.ceil(total_duration / 50)
        ensay_rows = []
        for idx, num in enumerate(range(1, num_ensays + 1)):
            st_wo_offset = ensay_start_date + timedelta(minutes=(duration * (num - 1)))
            start_date = st_wo_offset - timedelta(minutes=offset)
            start_date = parse(start_date.strftime("%Y-%m-%d %H:%M:00"))
            end_date = st_wo_offset + timedelta(minutes=(duration + offset))
            end_date = parse(end_date.strftime("%Y-%m-%d %H:%M:00"))
            ensay_rows.append([num, st_wo_offset] + list(self.generate_excel(column_names, start_date, end_date, num, out_name)))
            signal.emit([int((idx + 1) / num_ensays * 100), ensay_rows])
        return ensay_rows

    def calculate_ensys(self, master_column, duration, offset, num_ensays, out_name, signal):
        ensay_start, column_names = self.detect_ensay_start(master_column)
        return self.generate_excel_ensays(column_names, ensay_start, duration, offset, num_ensays, out_name, signal)
