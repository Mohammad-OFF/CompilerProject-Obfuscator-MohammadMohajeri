import sys
from antlr4 import FileStream, CommonTokenStream, InputStream, tree  # ANTLR imports

from generated_parser.MiniCLexer import MiniCLexer
from generated_parser.MiniCParser import MiniCParser

from ast_builder_visitor import ASTBuilderVisitor  # Our custom visitor to build our AST
import ast_nodes as custom_ast  # Our custom AST node definitions (for reference/type checking)

import code_generator
from obfuscator_passes import Obfuscator


print(f"DEBUG: Path to imported 'code_generator' module: {code_generator.__file__}")



def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file.mc> [output_file.mc]")
        sys.exit(1)

    input_filepath = sys.argv[1]
    output_filepath = "output.mc"
    if len(sys.argv) > 2:
        output_filepath = sys.argv[2]

    try:
        input_stream = FileStream(input_filepath, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    print(f"Attempting to parse '{input_filepath}'...")

    lexer = MiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)

    parse_tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"Parsing failed for '{input_filepath}' due to {parser.getNumberOfSyntaxErrors()} syntax error(s).")
        sys.exit(1)

    print("ANTLR parsing successful. Building custom AST...")

    ast_builder = ASTBuilderVisitor()
    custom_ast_tree = ast_builder.visit(parse_tree)

    if not custom_ast_tree or not isinstance(custom_ast_tree, custom_ast.ProgramNode):
        print("Custom AST construction failed or did not produce a ProgramNode.")
        if custom_ast_tree:
            print(f"AST Builder returned type: {type(custom_ast_tree)}")
        sys.exit(1)

    print("Custom AST built successfully.")

    techniques_to_apply = ["rename_identifiers", "dead_code"]

    obfuscator = Obfuscator(techniques=techniques_to_apply)

    print("\n--- Applying Obfuscation Passes ---")
    modified_ast = obfuscator.apply_passes(custom_ast_tree)
    print("--- Obfuscation Complete ---\n")


    generator = code_generator.CodeGenerator()

    print(f"Type of generator object: {type(generator)}")
    print(f"Attributes of generator object (dir(generator)): {dir(generator)}")
    if hasattr(generator, 'generate'):
        print("Generator object HAS 'generate' attribute.")
    else:
        print(
            "Generator object DOES NOT HAVE 'generate' attribute. Check the file printed by the DEBUG line at the top.")

    generated_code = generator.generate(modified_ast)  # This line was causing the error

    print("\n--- Generated (Obfuscated) Code ---")
    print(generated_code)
    print("--- End Generated (Obfuscated) Code ---\n")

    if output_filepath:
        try:
            with open(output_filepath, 'w') as f:
                f.write(generated_code)
            print(f"Generated code written to '{output_filepath}'")
        except Exception as e:
            print(f"Error writing to output file '{output_filepath}': {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()