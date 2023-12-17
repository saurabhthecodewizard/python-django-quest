import PyPDF2

file = open('Working_Business_Proposal.pdf', 'rb')

reader = PyPDF2.PdfReader(file)

print(len(reader.pages))

page_one = reader.pages[0]
print(page_one.extract_text())

writer = PyPDF2.PdfWriter()
writer.add_page(page_one)

output = open('pdf_output,pdf', 'wb')
writer.write(output)

file.close()
