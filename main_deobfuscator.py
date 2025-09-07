import os
from antlr4 import InputStream, CommonTokenStream

from generated_parser.MiniCLexer import MiniCLexer
from generated_parser.MiniCParser import MiniCParser
from ast_builder_visitor import ASTBuilderVisitor
from code_generator import CodeGenerator
from deobfuscator_passes import Deobfuscator

def main():
    # مسیر فایل ورودی و خروجی در همان دایرکتوری
    input_file = os.path.join(os.getcwd(), "input.mc")
    output_file = os.path.join(os.getcwd(), "cleaned.mc")

    # 1) خواندن کد مبهم از input.mc
    with open(input_file, 'r' ,encoding='utf-8') as f:
        code = f.read()

    # 2) ساخت Parse Tree
    lexer = MiniCLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    tree = parser.program()

    # 3) ساخت AST
    builder = ASTBuilderVisitor()
    ast_root = builder.visit(tree)

    # 4) اعمال پاس‌های de-obfuscation
    deob = Deobfuscator()
    simplified_ast = deob.simplify(ast_root)

    # 5) تولید کد تمیز
    generator = CodeGenerator()
    cleaned_code = generator.generate(simplified_ast)

    # 6) ذخیره در فایل cleaned.mc
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_code)

    print(f"[+] Deobfuscation finished. Clean code written to {output_file}")


if __name__ == "__main__":
    main()
