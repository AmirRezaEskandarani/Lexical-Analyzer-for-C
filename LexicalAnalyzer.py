import re
from tkinter import *

with open("program.c", "r") as file:
    text = file.read()
print(text)

rules = [
    ("keyword_main", r"main"),  # main
    ("keyword_void", r"void"), #void
    ("keyword_goto", r"goto"), #goto
    ("keyword_continue", r"continue"), #continue
    ("keyword_break", r"break"), #break
    ("keyword_switch", r"switch"), #switch
    ("keyword_case", r"case"), #case
    ("keyword_return", r"return"), #return
    ("keyword_sizeof", r"sizeof"), #sizeof
    ("keyword_int", r"int"),  # int
    ("keyword_short", r"short"), #short
    ("keyword_double", r"double"),#double
    ("keyword_long", r"long"), #long
    ("keyword_float", r"float"),  # float
    ("keyword_if", r"if"),  # if
    ("keyword_else", r"else"),  # else
    ("keyword_for", r"for"), #for
    ("keyword_while", r"while"),  # while
    ("keyword_do", r"do"), #do
    ("keyword_prinf", r"printf"),  # print
    ("LBRACKET", r"\("),  # (
    ("RBRACKET", r"\)"),  # )
    ("LBRACE", r"\{"),  # {
    ("RBRACE", r"\}"),  # }
    ("RSBRACKET", r"\["),  # []
    ("LSBRACKET", r"\]"),  # ]
    ("delimiter_comma", r","),  # ,
    ("delimiter_semicolon", r";"),  # ;
    ("operator_equal", r"=="),  # ==
    ("operator_nequal", r"!="),  # !=
    ("operator_lequal", r"<="),  # <=
    ("operator_hequal", r">="),  # >=
    ("operator_lshift", r"<<"),  # <<
    ("operator_rshift", r">>"),  # >>
    ("operator_or", r"\|\|"),  # ||
    ("operator_and", r"&&"),  # &&
    ("operator_less", r"<"),  # <
    ("operator_great", r">"),  # >
    ("operator_plusa", r"\+="),  # +=
    ("operator_minusa", r"\-="),  # -=
    ("operator_pluss", r"\+(\+)*"),  # ++
    ("operator_minuss", r"\-(\-)*"),  # --
    ("operator_plus", r"\+"),  # +
    ("operator_minus", r"-"),  # -
     ("operator_ass", r"\="),  # =
    ("operator_multiply", r"\*"),  # *
    ("operator_xor", r"^"),  # ^
    ("operator_comlement", r"~"),  # ~
    ("operator_division", r"\/"),  # /
    ("operator_remainder", r"%"),  # %
    ("identifier", r"[a-zA-Z]\w*"),  # IDENTIFIERS
    ("Literal", r"[\"a-zA-Z]\w*"),  # string
    ("number_float",r"\d(\d)*\.\d(\d)*"),  # FLOAT
    ("number_int", r"\d(\d)*"),  # INT
    ("NEWLINE", r"\n"),  # NEW LINE
    ("SKIP", r"[ \t]+"),  # SPACE and TABS
    ("MISMATCH", r'.')
]

tokens_join = "|".join("(?P<%s>%s)" % x for x in rules)
# print(tokens_join)

lin_start = 0
lin_num = 1
block_number = 0
i = -30
window=Tk()
window.geometry("1920x1080")
# It analyzes the code to find the lexemes and their respective Tokens
for m in re.finditer(tokens_join, text):
    token_type = m.lastgroup #keyword_int
    token_lexeme = m.group(token_type) #int

    if "_" in token_type:
        index = token_type.index("_")
        token_type = token_type[:index]

    if "LBRACE" in token_type:
        block_number += 1
    elif "RBRACE" in token_type:
        block_number -= 1

    if token_type == "NEWLINE":
        lin_start = m.end()
        lin_num += 1
    elif token_type == "SKIP":
        continue
    elif token_type == "MISMATCH":
        raise RuntimeError(f"{token_lexeme} unexpected on line {lin_num}")
    else:
        i += 30
        column = m.start() - lin_start
        # print(
        #     f"Token = {token_lexeme}, TokenType = '{token_type}', Row = {lin_num}, Column = {column}, Block number = {block_number}"
        # )
        lbl=Label(window, text=f"Token = {token_lexeme}, TokenType = '{token_type}', Row = {lin_num}, Column = {column}, Block number = {block_number}",
         fg='black', font=("Helvetica", 14))
        lbl.place(x=0, y=0+i)
        
window.mainloop()