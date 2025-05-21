import sys
from antlr4 import FileStream, CommonTokenStream, InputStream, tree # ANTLR imports

from generated_parser.MiniCLexer import MiniCLexer
from generated_parser.MiniCParser import MiniCParser

from ast_builder_visitor import ASTBuilderVisitor # Our custom visitor to build our AST
import ast_nodes as custom_ast # Our custom AST node definitions (for reference/type checking)

import code_generator
from obfuscator_passes import Obfuscator


print(f"DEBUG: Path to imported 'code_generator' module: {code_generator.__file__}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.mc> [output_file.mc]")
        sys.exit(1)
