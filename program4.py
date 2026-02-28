import pandas as pd
csv_file_path = csv_file_path = csv_file_path = r"C:\Users\totan\OneDrive\Desktop\sample_data.csv"
excel_file_path = r"C:\Users\totan\OneDrive\Desktop\sample_data.xlsx"
data_csv = pd.read_csv(csv_file_path)
print("CSV FILE DATA:")
print(data_csv)
data_excel = pd.read_excel(excel_file_path)
print("EXCEL FILE DATA:")
print(data_excel)
print("\nData Description: ")
print("\ncsv data description:")
print(data_csv.describe())
print("\nexcel data description:")
print(data_excel.describe())
print("\nData Types in csv file: ")
print(data_csv.dtypes)
print("\nData Types in excel file: ")       
print(data_excel.dtypes)