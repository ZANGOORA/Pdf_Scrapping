import PyPDF2

pdf_path = r"C:\Users\ZANG\OneDrive\Desktop\Puneet\Solar_Radian_Energy_Over_India.pdf"

import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Iterate through each page in the PDF
        for page in reader.pages:
            text += page.extract_text() + "\n"  # Extract text and add a newline for each page
        
        return text

# Extract the text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Print the extracted text (for checking)
print(extracted_text[:1000])  # Printing the first 1000 characters for a quick preview

# Optionally, save the extracted text to a text file
with open('extracted_text.txt', 'w') as text_file:
    text_file.write(extracted_text)
