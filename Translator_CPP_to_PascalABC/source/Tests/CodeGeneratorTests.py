import unittest
from source.LexicalAnalyzer import LexicalAnalyzer
from source.GrammarParser import *
from source.PascalABCCodeGenerator import *
from source.SemanticAnalyzer import *
from source.Optimizator import *

if __name__ == '__main__':

 for number in range (1,10):
    print("_____________________________________")
    print("ТЕСТ НОМЕР " + str(number) + " : ")
    lexicalAnalyzer = LexicalAnalyzer('tests_input_cpp_programs/test'+str(number)+'.cpp')
    lexicalAnalyzerResult = lexicalAnalyzer.startParsing()
    lexicalAnalyzer.printLexemes()
    lexicalAnalyzer.printErrors()
    if lexicalAnalyzerResult:
        grammarParser = GrammarParser()
        grammarParser.parseJsonRules('../grammar_rules.json')
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
            generator = Generator(treeBuilder.tree)
            generator.generate()
            print(generator.resultCode)
            with open("tests_output_code_generation/code_PascalABC_test"+str(number)+".txt", "w+", encoding="utf-8") as file:
                file.write(generator.resultCode)
            variableStorage = VariableStorage()
            semanticAnalyser = VariableSemanticAnalyser(treeBuilder.tree)
            semanticAnalyser.parse(treeBuilder.tree, variableStorage)
            optimizer = Optimizer(treeBuilder.tree, grammarParser.rules)
            optimizer.optimize()

if __name__ == '__main__':
    unittest.main()
