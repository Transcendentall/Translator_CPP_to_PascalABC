from source.GrammarParser import *
from source.PascalABCCodeGenerator import *
from source.SemanticAnalyzer import *
from source.Optimizator import *

if __name__ == '__main__':
    print("_____________________________________")
    print()
    print("ЛЕКСИЧЕСКИЙ АНАЛИЗАТОР: ")
    print()

    lexicalAnalyzer = LexicalAnalyzer('Input_Code_CPP.cpp')
    lexicalAnalyzerResult = lexicalAnalyzer.startParsing()
    lexicalAnalyzer.printLexemes()
    lexicalAnalyzer.printErrors()


    print()
    if lexicalAnalyzerResult:
        print()
        print()
        print("_____________________________________")
        print()
        print("ГРАММАТИЧЕСКИЙ АНАЛИЗАТОР: ")
        print()

        grammarParser = GrammarParser()
        grammarParser.parseJsonRules('grammar_rules.json')
        grammarParser.printRules()

        earley = Earley(grammarParser.rules, "<программа>")

        earleyParseResult = earley.parse(lexicalAnalyzer.lexemeArray)
        earley.printTableToFile()
        earley.printError()
        earleyTable = earley.table

        if earleyParseResult:
            treeBuilder = TreeBuilder(earleyTable, grammarParser.rules)

            treeBuilder.buildTree()
            treeBuilder.printTreeToFile()

            print()
            print()
            print("_____________________________________")
            print()
            print("ДЕРЕВО РАЗБОРА: ")
            print()

            with open("Output_ParseTree.txt", "r", encoding="utf-8") as f:
                text = f.read()
                print(text)

            print()
            print()
            print("_____________________________________")
            print()
            print("СГЕНЕРИРОВАННЫЙ КОД НА PASCAL ABC: ")
            print()

            generator = Generator(treeBuilder.tree)
            generator.generate()
            print(generator.resultCode)
            with open("Output_CodePascalABC.txt", "w+", encoding="utf-8") as file:
                file.write(generator.resultCode)

            variableStorage = VariableStorage()

            print("_____________________________________")
            semanticAnalyser = VariableSemanticAnalyser(treeBuilder.tree)
            semanticAnalyser.parse(treeBuilder.tree, variableStorage)

            optimizer = Optimizer(treeBuilder.tree, grammarParser.rules)
            optimizer.optimize()

    print()