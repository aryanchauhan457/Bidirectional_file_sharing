#Bidirectional_File_Sharing
import os
from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()

# HTML template (upload + file list)
HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>WiFi File Share</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    .dropzone {
        border: 2px dashed #888;
        padding: 40px;
        text-align: center;
        color: #555;
    }
    .dropzone.dragover {
        border-color: #00aaff;
        color: #00aaff;
    }
    ul { list-style: none; padding: 0; }
    li { margin: 5px 0; }
    a { text-decoration: none; color: blue; }
  </style>
</head>
<body>
  <h2>📂 WiFi File Share</h2>
  
  <div class="dropzone" id="dropzone">Drag & Drop files here or click to upload</div>
  <form id="uploadForm" method="post" enctype="multipart/form-data" action="/upload" style="display:none;">
    <input type="file" name="file" multiple onchange="this.form.submit()">
  </form>

  <h3>Files in this directory:</h3>
  <ul>
    {% for file in files %}
      <li><a href="/files/{{ file }}" download>{{ file }}</a></li>
    {% endfor %}
  </ul>

  <script>
    const dz = document.getElementById('dropzone');
    const form = document.getElementById('uploadForm');

    dz.addEventListener('click', () => form.querySelector('input').click());

    dz.addEventListener('dragover', e => {
        e.preventDefault();
        dz.classList.add('dragover');
    });
    dz.addEventListener('dragleave', e => dz.classList.remove('dragover'));
    dz.addEventListener('drop', e => {
        e.preventDefault();
        dz.classList.remove('dragover');
        const files = e.dataTransfer.files;
        const formData = new FormData();
        for (let f of files) formData.append('file', f);
        fetch('/upload', {method: 'POST', body: formData}).then(() => location.reload());
    });
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route("/files/<path:filename>")
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = request.files.getlist("file")
    for f in uploaded_files:
        if f.filename:
            f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return ("", 204)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    import socket

    # Get local IP
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Server running on http://{ip}:5000")
    run_simple("0.0.0.0", 5000, app)
