import os
from google.genai import types

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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



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



