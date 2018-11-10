#ftp.cwd(r"/home/doric482/public_ftp/incoming/")
#os.chdir(r"/Users/ricardoacandrade/Dropbox/Desenvolvimento/Python/ironman-scrap/")
import ftplib
import os
import time

files = os.listdir('files/')
files = [f for f in files if f.endswith('.csv')]

with ftplib.FTP('ftp.doricardo.com') as ftp:

    try:
        ftp.login('results@doricardo.com', 'results')
        wdir = ftp.pwd()

        for filename in files:
            with open('files/' + filename, 'rb') as fp:
                res = ftp.storlines("STOR " + filename, fp)
                print('OK: ' + filename)
                if not res.startswith('226'):
                    print('Upload failed: ' + res + ' -' + filename)
            time.sleep(1)
            os.rename('files/' + filename, 'files/bkp/' + filename)

    except ftplib.all_errors as e:
        print('FTP error:', e)
