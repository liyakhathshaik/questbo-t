import fitz

def remove_text_from_pdf(input_path, output_path, text_to_remove):
    pdf_document = fitz.open(input_path)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text_instances = page.search_for(text_to_remove)
        
        for inst in text_instances:
            page.add_redact_annot(inst, fill=(1, 1, 1)) 
            page.apply_redactions() 
    

    pdf_document.save(output_path)
    pdf_document.close()
    print(f"Text '{text_to_remove}' removed and saved to '{output_path}'")


input_pdf = "C:\\Users\\Suraj\\Downloads\\OneDrive_1_3-1-2025\\pathfinder-cds-combined-defence-expertsarihant-90f15b25.pdf"
output_pdf = "Pathfinder_CDS_cleaned.pdf"
text_to_remove = " CDS Pathfinder" 


remove_text_from_pdf(input_pdf, output_pdf, text_to_remove)
