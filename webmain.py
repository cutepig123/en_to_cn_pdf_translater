from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')
    
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['document']
    # Process the uploaded file as needed
    # For example, save it to a specific location:
    file.save('file.pdf')
    # Return a response or redirect as necessary
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()