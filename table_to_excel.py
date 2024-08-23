import pytesseract
from pdf2image import convert_from_path
import pandas as pd

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract path

# Path to the PDF file
pdf_path = r"C:\Users\ZANG\OneDrive\Desktop\Puneet\Solar_Radian_Energy_Over_India.pdf"  # Update with your PDF path

# Convert the specific page of the PDF to an image (e.g., page 100)
page_number = 291  # Update with the correct page number
pages = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)

# Save the page as an image
image_path = r"page_image.png"
pages[0].save(image_path, 'PNG')

# Perform OCR to extract text from the image
text = pytesseract.image_to_string(image_path)

# Print extracted text for debugging
print(text)

# Process the text into a list of rows, split by newlie
rows = text.split('\n')

# Filter out any empty rows
rows = [row for row in rows if row.strip() != ""]

# Split each row into columns based on whitespace
data = [row.split() for row in rows]

# Convert list of lists into a DataFrame
df = pd.DataFrame(data)

# Rename columns based on the first row (header)
df.columns = df.iloc[0]
df = df[1:]

# Save the DataFrame to an Excel file
excel_path =r'extracted_table.xlsx'  # Update with desired output path
df.to_excel(excel_path, index=False)

print(f"Data has been extracted and saved to {excel_path}")
