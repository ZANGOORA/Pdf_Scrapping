import camelot

# Specify the path to your PDF file
pdf_path = r"C:\Users\ZANG\OneDrive\Desktop\Puneet\Solar_Radian_Energy_Over_India.pdf"

# Use Camelot to extract tables from the PDF
tables = camelot.read_pdf(pdf_path, pages='all')

# Check how many tables were extracted
print(f"Total tables extracted: {len(tables)}")

# Iterate through the extracted tables and print the first few rows for each table
for i, table in enumerate(tables):
    print(f"\nTable {i + 1}:")
    print(table.df.head())  # Print the first few rows of the table

    # Optionally, save each table to an Excel file
    table.to_excel(f'table_{i + 1}.xlsx')
