### Modules and packages ###

# Importing existing flask modules
from flask import Flask

# Importing created modules
# If you wanna import just one method you can write as below
# From package.calculator import add 
# Otherwise you can import the whole module
import package.calculator as calculator

app = Flask(__name__)

@app.route('/')
def home():
    result = calculator.add(5, 3)
    return f"The result of the addition is: {result}"

if __name__ == '__main__':
    app.run()
