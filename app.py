from flask import Flask, request, render_template
import ply.lex as lex

# Define lexical rules using Ply.lex
tokens = (
    'ID',  # Identifiers
    'INT',   # Integers
    'FLOAT', # Floating-point numbers
    'PLUS',  # Addition operator
    'MINUS', # Subtraction operator
    'MUL',   # Multiplication operator
    'DIV',   # Division operator
    'LPAREN', # Left parenthesis
    'RPAREN', # Right parenthesis
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INT = r'-?\d+'
t_FLOAT = r'-?\d+\.\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignore whitespace
t_ignore = ' \t'

# Handle errors during lexing
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()

# Flask app creation and routing (unchanged)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # Parse the text using the Ply lexer
        lexer.input(text)
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(str(tok))  # Convert Ply tokens to strings
        return render_template('index.html', tokens=tokens, text=text)
    return render_template('index.html', tokens=None, text=None)

if __name__ == '__main__':
    app.run(debug=True)