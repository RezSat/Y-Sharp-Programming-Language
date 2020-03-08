import os
import sys
import lexer
import parser
import objgen
import platform

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

def main():
    
    content  = ""           # This variable will hold the contents of the source code
    path     = os.getcwd()  # Holds path this script was executed from

    # Holds the name of the file the user wants to compile
    try: fileName = sys.argv[1]
    except:
        print(color.GREEN+' +---------------------------------------------+')
        print(color.GREEN+' |               Y# - v1.0                     |')
        print(color.GREEN+' |          Developed By Yehan Wasura          |')
        print(color.GREEN+' +---------------------------------------------+')
        print(color.BLUE+"     Operating System : " + platform.system())
        print(color.BLUE+"     Release          : " + platform.release())
        print(color.BLUE+"     Y# Version       : v1.2.0")
        print(color.GREEN+' +---------------------------------------------+')
        print(color.RED+"Please use this command for run a program on this compiler : python3 main.py filename.yshp")
        return

    # Check if the file extension is correct
    if fileName[len(fileName) - 5:len(fileName)] != ".yshp":
        print("[ERROR] File extension not recognised please make sure extension is '.yshp'")
        return # quit programme

    # Check to make sure that only one argument is passed
    try:
        print('[ERROR] Expected 1 argument found 2 (' + sys.argv[1] + ", " + sys.argv[2] + ')')
        return # quit programme
    except: pass

    # Open source code file and get it's content and save it to the 'contents' var
    try:
        with open(path + "/" + fileName, "r") as file:
            content = file.read()
    except: 
        print('Cannot find "' + fileName + '"')
    
    # --------------------------------------
    #  LEXER
    # --------------------------------------

    # Create an instance of the lexer class
    lex = lexer.Lexer()

    # Call lexer method to perform lexical analysis on code
    tokens = lex.tokenize(content)

    # --------------------------------------
    #  PARSER
    # --------------------------------------

    # Create an instance of the parser class
    Parser = parser.Parser(tokens)

    # Call the parser method and pass in the tokens as arguments
    source_ast = Parser.parse(tokens)

    # --------------------------------------
    # Object Generation
    # --------------------------------------

    # Create an instance of the Object Generator (objgen) class
    object_generator = objgen.ObjectGenerator(source_ast)

    # Call the object definer to get python exec() string
    exec_string = object_generator.object_definer(False)

    # Execute the Y# code that has been transpiled to python code to get output
    print(color.GREEN+' +---------------------------------------------+')
    print(color.GREEN+' |               Y# - v1.0                     |')
    print(color.GREEN+' |          Developed By Yehan Wasura          |')
    print(color.GREEN+' +---------------------------------------------+')
    print(color.BLUE+"     Operating System : " + platform.system())
    print(color.BLUE+"     Release          : " + platform.release())
    print(color.BLUE+"     Y# Version       : v1.2.0")
    print(color.GREEN+' +---------------------------------------------+\n\n')
    


    print(color.OKBLUE+"Filename: " + fileName + color.OKBLUE+'\n\n')
    print(color.YELLOW +'|||||||||||||||||||||||  OUTPUT  ||||||||||||||||||||||| \n' + color.BOLD)
    exec(exec_string)
    print(color.YELLOW +'\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n')

main()

