def save_pdf(pdf_file):
    local_file_path = "./File_system/rozklad.pdf"
    with open(local_file_path, "wb") as local_file:
        local_file.write(pdf_file)
