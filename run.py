import sys
import os
from app import app  


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

if __name__ == '__main__':
    app.run(debug=True, port=5002)





