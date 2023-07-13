from flask import Flask, render_template, request, send_file, make_response
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    if file:
        # Save the uploaded file
        file.save('files/input.csv')

        # Convert CSV to HTML table
        html_table = csv_to_html('files/input.csv')

        # Save the HTML table as a file
        save_html('files/output.html', html_table)

        return render_template('index.html', converted=True)
    else:
        return render_template('index.html', error=True)


@app.route('/download', methods=['GET'])
def download():
    response = make_response(
        send_file('files/output.html', as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename=converted_table.html"
    return response

def csv_to_html(csv_file):
    html = '<table border="1">\n'

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        # Add table headers
        headers = next(reader)
        html += '\t<tr>\n'
        html += '\t\t<th>Serial No.</th>\n'
        for header in headers:
            html += f'\t\t<th>{header}</th>\n'
        html += '\t</tr>\n'

        # Add table rows
        for i, row in enumerate(reader, start=1):
            html += '\t<tr>\n'
            html += f'\t\t<td>{i}</td>\n'
            for value in row:
                html += f'\t\t<td>{value}</td>\n'
            html += '\t</tr>\n'

    html += '</table>'
    return html


def save_html(file_path, html):
    with open(file_path, 'w') as file:
        file.write(html)


if __name__ == '__main__':
    app.run(debug=True)