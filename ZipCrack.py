import zipfile

def main():

    passwordlist = "DW1000.txt"
    target = "test.zip"

    password = None
    zip_file = zipfile.ZipFile(target)
    with open(passwordlist, 'r') as a:
        for line in a.readlines():
            password = line.strip('\n')
            try:
                    zip_file.extractall(pwd=password)
                    password = 'Password found: %s' % password
            except:
                pass
    print(password)

main()
