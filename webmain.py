from flask import Flask, request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['document']
    filename = file.filename
    size = file.content_length    
    # Process the uploaded file as needed
    # For example, save it to a specific location:
    file.save('file.pdf')
    # Return a response or redirect as necessary
    return 'file.pdf'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)