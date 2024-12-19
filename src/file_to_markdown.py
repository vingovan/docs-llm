from markitdown import MarkItDown

def get_file_type(file_path: str) -> str:
    """Get file type from file path"""
    if file_path.endswith('.xlsx'):
        return 'excel'
    elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        return 'image'
    else:
        return 'unknown'

def process_excel_file(file_path: str, md: MarkItDown) -> str:
    """Process Excel file and convert to markdown"""
    result = md.convert(file_path)
    return result.text_content

def process_image_file(file_path: str) -> str:
    """Process image file and convert to markdown using GPT-4"""
    client = OpenAI()
    md = MarkItDown(llm_client=client, llm_model="gpt-4o")
    result = md.convert(file_path)
    return result.text_content

def file_to_markdown(file_path: str) -> str:
    result = ""
    md = MarkItDown()
    
    file_type = get_file_type(file_path)
    
    if file_type == 'excel':
        result = process_excel_file(file_path, md)
    elif file_type == 'image':
        result = process_image_file(file_path)
    
    return result
