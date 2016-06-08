import ply.lex as lex, ply.yacc as yacc

tokens = (
    'NUM',
    'STR',
    'IDEN',
    'LBRACE',
    'RBRACE',
    'EQUAL',
    'MINUS'
    )


t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUAL = r'\='
t_MINUS = r'-'

def t_NUM(t):
    r'\d+\.\d+|\d+'
    #t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0], t.lexer.lineno)
    t.lexer.skip(1)

def t_IDEN(t):
    r'[A-Za-z_][0-9A-Za-z_\:]*'
    return t

def t_STR(t):
    r'".*"'
    return t

# Build the lexer
lexer = lex.lex()

data = '''6 = { }'''

lexer.input(data)

# Tokenize
##while True:
##    tok = lexer.token()
##    if not tok: 
##        break      # No more input
##    print(tok)

def p_start_list(p):
    'start : list'
    p[0] = p[1]

def p_start_dict(p):
    'start : dict'
    p[0] = p[1]

def p_start_listc(p):
    'start : listcontents'
    p[0] = p[1]

def p_start_dictc(p):
    'start : dictcontents'
    p[0] = p[1]

def p_list(p):
    'list : LBRACE listcontents RBRACE'
    p[0] = p[2]

def p_listcontents_list(p):
    'listcontents : listcontents list'
    p[0] = ([] + p[1])+[p[2]]

def p_listcontents_dict(p):
    'listcontents : listcontents dict'
    p[0] = ([] + p[1])+[p[2]]

def p_listcontents_atom(p):
    'listcontents : listcontents atom'
    p[0] = ([] + p[1])+[p[2]]

def p_listcontents_list_one(p):
    'listcontents : list'
    p[0] = [p[1]]

def p_listcontents_dict_one(p):
    'listcontents : dict'
    p[0] = [p[1]]

def p_listcontents_atom_one(p):
    'listcontents : atom'
    p[0] = [p[1]]

def p_listcontents_atom_one(p):
    'listcontents : atom'
    p[0] = [p[1]]

def p_listcontents_empty(p):
    'listcontents : empty'
    p[0] = []
    
def p_empty(p):
    'empty :'
    pass

def p_dict(p):
    'dict : LBRACE dictcontents RBRACE'
    p[0] = p[2]

def p_dictcontents(p):
    '''dictcontents : dictcontents atom EQUAL list
        | dictcontents atom EQUAL dict
        | dictcontents atom EQUAL atom'''
    p[0] = ([] + p[1])+[(p[2], p[4])]

def p_dictcontents_oddball(p):
    '''dictcontents : dictcontents EQUAL EQUAL list
        | dictcontents EQUAL EQUAL dict
        | dictcontents EQUAL EQUAL atom'''
    p[0] = ([] + p[1])

def p_dictcontents_end(p):
    '''dictcontents : atom EQUAL list
        | atom EQUAL dict
        | atom EQUAL atom'''
    p[0] = [(p[1], p[3])]

def p_dictcontents_end2(p):
    '''dictcontents : empty'''
    p[0] = []

def p_atom(p):
    '''atom : IDEN
    | STR
    | NUM'''
    p[0] = p[1]

def p_atom_neg(p):
    'atom : MINUS NUM'
    p[0] = '-' + p[2]

# Error rule for syntax errors
def p_error(p):
    print(p)
    print("Syntax error in input!")

# Build the parser
psr = yacc.yacc()

#result = parser.parse(data)
#print(result)

def paradox_dict_get_child_by_name(d, name):
    for i in d:
        if i[0] == name:
            return i[1]
