import PyPDF2
import spacy

def extract_info_from_pdf(pdf_file_path):
    # Open and extract text from the PDF
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extractText()
    
    # Load spaCy NLP model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy
    doc = nlp(pdf_text)
    
    # Initialize variables to store extracted information
    company_name = None
    bill_number = None

    # Extract company names and bill numbers using NER
    for entity in doc.ents:
        if entity.label_ == "ORG" and not company_name:
            company_name = entity.text
        elif entity.label_ == "CARDINAL" and not bill_number:
            bill_number = entity.text

    # Return the extracted information
    return {
        'Company Name': company_name,
        'Bill Number': bill_number,
        # Add more key-value pairs for other extracted information
    }

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'your_pdf_file.pdf'

# Call the function to extract information from the PDF
extracted_info = extract_info_from_pdf(pdf_file_path)

# Print the extracted information
print("Extracted Information:")
print(extracted_info)
