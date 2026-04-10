import jast

arquive = "java/simples/helloworld.java"
# Parse the Java source file
with open(arquive) as file:
    tree = jast.parse(file.read())


class ParsingCode(jast.JNodeVisitor):
    def __init__(self) -> None:
        self.countADD = 0
        self.fors = 0
        self.ifs = 0

    # def visit(self, node: jast.JAST):
    # loc()

    def visit_Method(self, node: jast.Method):
        self.visit(node.body)

    def visit_If(self, node):
        self.visit(node.body)
        self.ifs += 1

    # def visit_identifier(self, node):
    #   print(node)
    def visit_For(self, node: jast.For):
        self.fors += 1
        # self.visit(node.init)
        self.visit(node.test)
        self.visit(node.body)

    def visit_BinOp(self, node: jast.BinOp):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Add(self, node):
        self.countADD += 1
        return


class VisitParents(jast.JNodeVisitor):

    def visit_Class(self, node: jast.Class):
        self.countChildren = 0
        print(node.extends)
        if node.extends == None:
            return node.extends
        # else:
        #     with open("java/"+ str(node.extends) +".java") as file:
        #         self.f = jast.parse(file.read())
        #     # recursividade
        #     self.p = VisitParents()
        #     self.p.visit(self.f)
        #     self.countChildren += 1

        return node.extends


def loc():
    count = 0
    with open(arquive, "r") as f:
        for line in f.readlines():
            count += 1
    print(count)


visitor = ParsingCode()
visitor.visit(tree)


# parents = VisitParents()
# parents.visit(tree)

print(visitor.countADD)
print("Quantidade de For: " + str(visitor.fors))
print("Quantidade de If: " + str(visitor.ifs))
# class ParsedCode(jast.JNodeVisitor):
#
#    def __init__(self):
#        self.fors = []
#
#        with open("java/HelloWorld.java") as file:
#            self.tree = jast.parse(file.read())
#            self.visit(self.tree)
#
#        self.operators = len(self.fors)
#
#
#
#    def visit_For(self, node):
#
#        self.fors.append("For")
#
#        self.visit(node.init)
#        self.visit(node.test)
#        self.visit(node.body)
#
#    def visit_BinOp(self, node):
#        self.visit(node.left)
#        self.visit(node.right)
#
#    def visit_Constant(self, node):
#        print(node.value)
#
#    def visit_Add(self, node):
#        return "+"
#
#    def visit_identifier(self, node):
#        pass
#
# visitor = ParsedCode()
