# CSV to HTML Converter

The CSV to HTML Converter is a web application built with Python and Flask that allows users to convert a CSV file into an HTML table with borders and serial numbers. It provides an intuitive user interface for uploading a CSV file, converting it, and downloading the converted HTML file.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

<details>
<summary><b>Install Flask using pip:</b></summary>
<div style="background-color: #f0f0f0; padding: 10px;">
<pre>
pip install flask
</pre>
</div>
</details>

<details>
<summary><b>Run the Flask application:</b></summary>
<div style="background-color: #f0f0f0; padding: 10px;">
<pre>
python app.py
</pre>
</div>
</details>

 Open your web browser and go to `http://localhost:5000` to access the CSV to HTML Converter.

## How to Use

1. Access the CSV to HTML Converter in your web browser.

2. Click the "Choose File" button and select a CSV file from your local storage.

3. Click the "Convert" button to initiate the conversion process.

4. After the conversion is completed, you will see a message indicating that the CSV file has been converted successfully.

5. You can now download the converted HTML file by clicking the "Download Converted HTML" link.

6. To convert another CSV file, simply reload the page and repeat the process.

## Features

- Convert CSV files into HTML tables with borders and serial numbers.
- Easy-to-use web interface for uploading and converting CSV files.
- Option to download the converted HTML file.

## Project Structure

- `app.py`: The main Flask application that handles the routing and conversion process.
- `templates`: Folder containing the HTML template for the user interface.
- `uploads`: Folder for storing uploaded CSV and converted HTML files.

## Known Issues/Limitations

- The application is designed for small to medium-sized CSV files. Large files may take longer to process.
- The user interface may not be optimized for all screen sizes.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgments

This project was inspired by the need for a simple CSV to HTML conversion tool and was built using Flask and Python.

