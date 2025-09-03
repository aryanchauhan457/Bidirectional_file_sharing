---

# 📂 Bidirectional File Sharing over WiFi

A simple **Flask-based web app** that allows you to **share files bidirectionally** (upload & download) over the same WiFi network.

With this project, you can:

* Upload files from any device (PC, mobile, tablet) connected to your WiFi.
* Download files available in the server’s directory.
* Enjoy a clean and responsive drag & drop UI for file uploads.

---

## 🚀 Features

* 📥 Drag & drop or click-to-upload functionality.
* 📤 Download any uploaded file directly.
* 🌐 Works across all devices connected to the same WiFi network.
* 🖥️ No external dependencies other than Flask.
* ⚡ Lightweight and fast (runs locally).

---

## 📦 Requirements

Make sure you have the following installed:

* Python 3.7+
* Flask

You can install Flask using pip:

```
pip install flask
```

---

## ▶️ How to Run

1. **Clone or copy** the project to your computer.

2. Open a terminal inside the project folder and run:

```
python app.py
```

3. The terminal will show something like:

```
Server running on http://192.168.x.x:5000
```

4. Open the shown URL (`http://192.168.x.x:5000`) in your browser (on **any device** connected to the same WiFi).

5. Start uploading and downloading files! 🎉

---

## 🖼️ Interface Preview

* **Upload Section**: Drag & drop or click to select files.
* **File List**: Displays all files in the current directory with download links.

---

## 📂 Project Structure

```
Bidirectional_File_Sharing/
│── app.py              # Main Flask app
│── (Uploaded files)    # Files will be stored here
```

---

## 🔒 Notes

* All uploaded files are stored in the **same directory** as `app.py`.
* Ensure your firewall allows connections on port `5000`.
* Only devices on the **same WiFi network** can access the server.

---

## 🤝 Contributing

Feel free to fork the repo, open issues, or submit pull requests with improvements (like authentication, file preview, or UI enhancements).

---

## 📜 License

This project is open-source and available under the **MIT License**.

---
