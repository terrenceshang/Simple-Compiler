import lex
import sys

# All tokens must be name in advance
tokens = ("WORD", "NUMBER", "WHITESPACE", "PUNCTUATION", "HASHTAG", "NAME", "ILLEGAL")

#Token matching rules are written as regexs
t_WORD = r'[a-zA-Z_]+'
t_NUMBER = r'[0-9_]+'
t_WHITESPACE = r'(\ |\t)+'
t_PUNCTUATION = r'(\.|\,|\;|\!|\?)'
t_HASHTAG = r'(\#[a-zA-Z0-9]+)'
t_NAME = r'\@[a-zA-Z]+'
t_ILLEGAL = '.'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()
file = open (sys.argv[1], 'r')
data = file.read()
#data = "@Harry I know. Its not the same as it was!  #AsItWas"
lex.input(data)

output1 = ""
while True:
    output = ""
    tok = lex.token()
    if not tok: 
        break
    temp = str(tok)
    temp2= temp[temp.index("'")+1: ]
    output = temp[9:temp.index(',')] + "," + temp2[0:temp2.index("'")]        
    print(output)
    output1 = output1 + output + "\n"
    file1 = open(sys.argv[1][0:-4]+".tkn", 'w')
file1.write(output1)
