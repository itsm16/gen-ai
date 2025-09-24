# file = open("file_test.txt", "w")

# try:
#     file.write("From,\n\t11_exceptions/08_file_handling.py, complete the vid")
# finally:
#     file.close()

with open("file_test.txt", "w") as file:
    file.write("From,\n\t11_exceptions/08_file_handling.py\n\n check the file to know proper handling and writing\n using with keyword")