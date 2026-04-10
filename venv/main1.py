import jast
import os

arquivo = "java/simples/helloworld.java"
print("Path existente= ")
print(os.path.exists(arquivo))
# Parse the Java source file
with open(arquivo) as file:
    tree = jast.parse(file.read())


class ParsingCode(jast.JNodeVisitor):
    def __init__(self) -> None:
        self.countADD = 0
        self.fors = 0
        self.ifs = 0
        self.countline = 0

    def loc(self):
        with open(arquivo, "r") as f:
            linhas = f.readlines()
            for i in linhas:
                self.countline += 1
        return self.countline

    def locEfficiency(self):
        self.countline = 0
        blockComment = False
        with open(arquivo, 'r') as f:
            for line in f: # f.split('\n')
                if blockComment == True and !line[1:] == '*/':
                    continue
                else:
                    blockComment = False
                if line[:1] == '/*':
                    blockComment = True
                    continue
                if line[:1] == '//':
                    continue
                self.countline += 1
                

    def visit_Method(self, node: jast.Method):
        self.visit(node.body)

    def visit_If(self, node):
        self.visit(node.body)
        self.ifs += 1

    def visit_identifier(self, node):
        print(node)


visitor = ParsingCode()
visitor.visit(tree)
print(visitor.loc())
