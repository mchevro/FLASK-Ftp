from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from static.FTP import Ftp
import os
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 # 25Mb max

#===================
# KONFIG FILES START
#===================
ALLOWED_EXTENSIONS = set(['pdf', 'PNG']) # Ekstensi file yang diizinkan
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#===================
# KONFIG FILES END
#===================

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data_file = request.files['file']
        if data_file and allowed_file(data_file.filename):
            try:
                filename = data_file.filename
                data_file.save(filename) # Menyimpan file ke lokal
                files = Ftp('ftp.tomcatsquad.web.id', 'mchevro@files.tomcatsquad.web.id', '2UTA@?Q*[##U') # FTP Account
                files.send(filename) # Kirim file ke ftp
                time.sleep(1.5) # Jeda 1.5 detik
                os.remove(filename) # Hapus file yang diupload ke dalam lokal, karena file yang diupload sudah dikirim ke ftp server
            except:
                abort(403)
            return 'Success Upload'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')