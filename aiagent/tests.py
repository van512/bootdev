# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

#"""
#my tests
def test():
    # run_python_file tests
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))

    #write_file tests
    #print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    #print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    #print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    # get_file_content tests
    #print(get_file_content("calculator", "lorem.txt"))
    #print(get_file_content("calculator", "main.py"))
    #print(get_file_content("calculator", "pkg/calculator.py"))
    #print(get_file_content("calculator", "/bin/cat")) 

    # get_files_info tests
    #print(get_files_info("calculator", "main.py")) #works
    #print(get_files_info("calculator", "blabla")) #works
    #print(get_files_info("calculator", ".")) #works
    #print(get_files_info("calculator", "pkg")) #works
    #print(get_files_info("calculator", "/bin")) #works
    #print(get_files_info("calculator", "../")) #works
    #print(get_files_info("calculator")) #works
#"""

if __name__ == "__main__":
    test()




"""
#correction :
def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()
"""