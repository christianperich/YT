import os
from pathlib import Path
from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)


home = Path.home()
path = "Videos"
url_downloads = str(home / path)


@app.route('/', methods=["GET", "POST"])
def index():
    global url
    if request.method == "POST":
        if request.form.get("link"):
            link = request.form.get("link")
            url = link
            if not link:
                return render_template("index.html")            
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filesize = int(stream.filesize / 1024 /1024)
            video_info = yt            
            return render_template("index.html", video_info=video_info, filesize=filesize)      
        if request.form.get("descargar"):
            ytube = YouTube(url)
            download_info = ytube
            stream = ytube.streams.get_highest_resolution()
            stream.download(output_path=url_downloads)
            return render_template("index.html", download_info=download_info, url_downloads=url_downloads)       
    return render_template("index.html")
   
if __name__ == '__main__':
    app.run()