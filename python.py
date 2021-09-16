def pyfile(file_name_with_py):
    """ create a python file """
    
    open(file_name_with_py, "x")
    
    with open(file_name_with_py, "w") as py:
        py.write("# thanks for using auto-file")
        
def html(name_with_html):
    """create a html file"""
    
    open(name_with_html, "x")
    
def custom(file_name_with_custom_extension):
    """create file with custom extension"""
    
    open(file_name_with_custom_extension, "x")