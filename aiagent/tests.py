# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

#"""
#my tests
def test():
    # get_file_content tests
    #print(get_file_content("calculator", "lorem.txt"))
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat")) 


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