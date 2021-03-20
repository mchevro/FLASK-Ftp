import ftplib

class Ftp():
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
    
    def send(self, nameFile):
        try:
            session = ftplib.FTP(self.host, self.user, self.password)
            files = open(nameFile, 'rb') # Sesuaikan dengand directory tempat file disimpan
            session.storbinary(f'STOR music/{nameFile}', files) # Sesuaikan tempat directory pada ftp server/hosting account ftp
            files.close()
            session.quit()
        except ftplib.all_errors as e:
            print('FTP Error: ', e)