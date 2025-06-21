from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    return 'OK', 200

def main():
    app.run(host='0.0.0.0', port=3000, debug=True)
    
if __name__ == '__main__':
    main()
