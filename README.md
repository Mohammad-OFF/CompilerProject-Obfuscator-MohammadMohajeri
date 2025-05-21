# 🛠️ Mini-C Obfuscator & Code Transformer

An educational yet powerful toolkit designed to parse, analyze, and obfuscate code written in the **Mini-C** language. Built using **ANTLR**, **Python**, and **Tkinter**, this project is ideal for exploring compiler construction, code security, and syntax tree manipulation.

---

## 👥 Contributors
- Mohammad Mohajeri
- Arash Barkhordarioon
- Arian Daliri
---

## 📘 What is Mini-C?

**Mini-C** is a reduced version of the C programming language used for teaching compiler principles. This language supports:

- Basic types: `int`, `char`, `bool`
- Operators: arithmetic, logical, relational
- Control flow: `if`, `else`, `while`, `for`, `return`
- I/O: `scanf`, `printf`
- User-defined functions

---

## 🚀 Project Capabilities

This project handles the entire pipeline of source code transformation:

1. **Parsing** Mini-C code using ANTLR and a custom grammar (`MiniC.g4`)
2. Constructing an **Abstract Syntax Tree (AST)** via a Visitor pattern
3. Applying multiple **obfuscation passes** on the AST
4. Generating the transformed code in `output.mc`
5. Providing a **GUI** to configure transformations interactively

---

## 🔧 Key Components

| Module | Description |
|--------|-------------|
| `MiniC.g4` | ANTLR grammar for Mini-C |
| `ast_nodes.py` | Classes for AST node structure |
| `ast_builder_visitor.py` | Builds AST from parsed code |
| `obfuscator_passes.py` | Implements transformation passes |
| `code_generator.py` | Converts modified AST back to Mini-C |
| `main.py` | Integrates GUI and processing pipeline |

---

## 🧠 Obfuscation Techniques Implemented

- **Variable & Function Renaming**: Replaces identifiers with meaningless names
- **Dead Code Insertion**: Adds code that doesn’t affect semantics
- **Equivalent Expression Replacement**: Swaps expressions with same effect
- **Control Flow Flattening**: Obscures execution order
- **Function Inlining**: Replaces calls with function bodies
- **Dummy Function Injection**: Adds unused but realistic-looking functions

---

## 🖥️ GUI Interface

The app includes a **Tkinter-based GUI** to:
- Choose the input `.mc` file
- Select obfuscation techniques to apply
- Export the obfuscated version with one click

---

## 🧰 Getting Started

### Requirements
- Python 3.6 or later
- `antlr4-python3-runtime==4.13.1`
- Java (for generating parser with ANTLR)

### Installation
Install ANTLR runtime:
```bash
pip install antlr4-python3-runtime==4.13.1
```
Generate ANTLR parser files (after installing Java & ANTLR):
```bash
java -jar antlr-4.13.2-complete.jar MiniC.g4 -Dlanguage=Python3 -visitor
```
Run the main GUI:
```bash
python main.py
```

---
## 🧪 Example

Transform `input.mc` into `output.mc` using selected techniques in the GUI or CLI (future versions may include CLI mode).

---

## 📌 Notes

This project is the **first phase** of a larger compiler construction journey. Planned extensions include:
- Type checking & semantic analysis
- Intermediate code generation
- Optimization techniques
- Target code compilation (e.g., LLVM IR or bytecode)
