import os

#"""
# #my function
def get_files_info(working_directory, directory=None):

    if directory is None:
        directory = '.'

    directory_path = os.path.join(working_directory, directory)

    # handle errors
    if not os.path.isdir(os.path.abspath(directory_path)): #the directory argument is not a directory, return an error string
        return f'   Error: "{directory}" is not a directory'
    if not os.path.exists(directory_path): #the directory argument does not exist, return an error string
        return f'   Error: "{os.path.abspath(directory_path)}" does not exist'
    if directory.startswith(('../','/')):
        return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # string to hold the information about files and directories
    info_par = ''
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        info_str= f' - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}'
        info_par = '\n'.join((info_par, info_str))
    
    return info_par
#"""


#If any errors are raised by the standard library functions, 
# catch them and instead return a string describing the error. 
# Always prefix error strings with "Error:".

    
    #os.path.abspath(): Get an absolute path from a relative path
    #os.path.join(): Join two paths together safely (handles slashes)
    #.startswith(): Check if a string starts with a substring
    #os.path.isdir(): Check if a path is a directory
    #os.listdir(): List the contents of a directory
    #os.path.getsize(): Get the size of a file
    #os.path.isfile(): Check if a path is a file
    #.join(): Join a list of strings together with a separator



""" 
#correction :
def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
        
"""
