import re
from enum import Enum

class ErrorType(Enum):
    # LexicalAnalyzer error
    INVALID_EXPONENTIAL_NUMBER = 'LEXICAL-ERROR-INVALID_EXPONENTIAL_NUMBER'
    INVALID_INTEGER_NUMBER = 'LEXICAL-ERROR-INVALID_INTEGER_NUMBER'


class LexemeType(Enum):
    # Operators
    PLUS = 'LEXEME-PLUS'
    INCREMENT = 'LEXEME-INCREMENT'
    MINUS = 'LEXEME-MINUS'
    DECREMENT = 'LEXEME-DECREMENT'
    MULTIPLICATION = 'LEXEME-MULTIPLICATION'
    DIVISION = 'LEXEME-DIVISION'
    MOD = 'LEXEME-MOD'
    ASSIGNMENT = 'LEXEME-ASSIGNMENT'
    EQUAL = 'LEXEME-EQUAL'
    NOT_EQUAL = 'LEXEME-NOT_EQUAL'
    LESS_THAN = 'LEXEME-LESS_THAN'
    MORE_THAN = 'LEXEME-MORE_THAN'
    LESS_OR_EQUAL = 'LEXEME-LESS_OR_EQUAL'
    MORE_OR_EQUAL = 'LEXEME-MORE_OR_EQUAL'
    NOT = 'LEXEME-NOT'
    AND = 'LEXEME-AND'
    OR = 'LEXEME-OR'

    # Data type
    VOID = 'LEXEME-VOID'
    INT = 'LEXEME-INT'
    LONG = 'LEXEME-LONG'
    SHORT = 'LEXEME-SHORT'
    UNSIGNED = 'LEXEME-UNSIGNED'
    BOOL = 'LEXEME-BOOL'
    FLOAT = 'LEXEME-FLOAT'
    DOUBLE = 'LEXEME-DOUBLE'
    CHAR = 'LEXEME-CHAR'

    # Cycle operators
    FOR = 'LEXEME-FOR'
    WHILE = 'LEXEME-WHILE'

    # Branching operators
    IF = 'LEXEME-IF'
    ELSE = 'LEXEME-ELSE'

    # Reserved constants
    TRUE = 'LEXEME-TRUE'
    FALSE = 'LEXEME-FALSE'

    # Reserved service names
    INCLUDE = 'LEXEME-INCLUDE'
    STD = 'LEXEME-STD'
    MAIN = 'LEXEME-MAIN'
    RETURN = 'LEXEME-RETURN'

    # Reserved functions names
    COUT = 'LEXEME-COUT'
    CIN = 'LEXEME-CIN'
    ABS = 'LEXEME-ABS'
    SQR = 'LEXEME-SQR'
    SQRT = 'LEXEME-SQRT'
    POW = 'LEXEME-POW'
    FLOOR = 'LEXEME-FLOOR'
    CEIL = 'LEXEME-CEIL'

    # Separators
    ROUND_OPEN_BRACKET = 'LEXEME-ROUND_OPEN_BRACKET'
    ROUND_CLOSE_BRACKET = 'LEXEME-ROUND_CLOSE_BRACKET'
    CURLY_OPEN_BRACKET = 'LEXEME-CURLY_OPEN_BRACKET'
    CURLY_CLOSE_BRACKET = 'LEXEME-CURLY_CLOSE_BRACKET'
    SQUARE_OPEN_BRACKET = 'LEXEME-SQUARE_OPEN_BRACKET'
    SQUARE_CLOSE_BRACKET = 'LEXEME-SQUARE_CLOSE_BRACKET'
    SEMICOLON = 'LEXEME-SEMICOLON'
    COLON = 'LEXEME-COLON'

    # Number type
    INT_NUMBER = 'LEXEME-INT_NUMBER'
    REAL_NUMBER = 'LEXEME-REAL_NUMBER'
    EXPONENTIAL_NUMBER = 'LEXEME-EXPONENTIAL_NUMBER'
    # VAR_NAME = 'LEXEME-VAR_NAME'

    # Char data
    CHAR_DATA = 'LEXEME-CHAR_DATA'
    STRING_DATA = 'LEXEME-STRING_DATA'

    WORD = 'LEXEME-WORD'

    UNDEFINED = 'LEXEME-UNDEFINED'

    EOF = 'LEXEME-END_OF_FILE'


DictionaryOfLexemes = {
    # Operators
    '+': LexemeType.PLUS,
    '++': LexemeType.INCREMENT,
    '-': LexemeType.MINUS,
    '--': LexemeType.DECREMENT,
    '*': LexemeType.MULTIPLICATION,
    '/': LexemeType.DIVISION,
    '%': LexemeType.MOD,
    '=': LexemeType.ASSIGNMENT,
    '==': LexemeType.EQUAL,
    '!=': LexemeType.NOT_EQUAL,
    '<': LexemeType.LESS_THAN,
    '>': LexemeType.MORE_THAN,
    '<=': LexemeType.LESS_OR_EQUAL,
    '>=': LexemeType.MORE_OR_EQUAL,
    '!': LexemeType.NOT,
    '&&': LexemeType.AND,
    '||': LexemeType.OR,

    # Data type
    'void': LexemeType.VOID,
    'int': LexemeType.INT,
    'long': LexemeType.LONG,
    'short': LexemeType.SHORT,
    'unsigned': LexemeType.UNSIGNED,
    'bool': LexemeType.BOOL,
    'float': LexemeType.FLOAT,
    'double': LexemeType.DOUBLE,
    'char': LexemeType.CHAR,

    # Cycle operators
    'for': LexemeType.FOR,
    'while': LexemeType.WHILE,

    # Branching operators
    'if': LexemeType.IF,
    'else': LexemeType.ELSE,

    # Reserved constants
    'true': LexemeType.TRUE,
    'false': LexemeType.FALSE,

    # Reserved service names
    'include': LexemeType.INCLUDE,
    'std': LexemeType.STD,
    'main': LexemeType.MAIN,
    'return': LexemeType.RETURN,

    # Reserved functions names
    'cout': LexemeType.COUT,
    'cin': LexemeType.CIN,
    'abs': LexemeType.ABS,
    'sqr': LexemeType.SQR,
    'sqrt': LexemeType.SQRT,
    'pow': LexemeType.POW,
    'floor': LexemeType.FLOOR,
    'ceil': LexemeType.CEIL,

    # Separators
    '(': LexemeType.ROUND_OPEN_BRACKET,
    ')': LexemeType.ROUND_CLOSE_BRACKET,
    '{': LexemeType.CURLY_OPEN_BRACKET,
    '}': LexemeType.CURLY_CLOSE_BRACKET,
    '[': LexemeType.SQUARE_OPEN_BRACKET,
    ']': LexemeType.SQUARE_CLOSE_BRACKET,
    ';': LexemeType.SEMICOLON,
    ':': LexemeType.COLON,

}


class ErrorTypeSemantic(Enum):
    # Semantic error
    TYPE_MISMATCH = 'SEMANTIC-ERROR-TYPE-MISMATCH'
    UNDECLARED_VARIABLE = 'SEMANTIC-ERROR-UNDECLARED-VARIABLE'
    UNDECLARED_FUNCTION = 'SEMANTIC-ERROR-UNDECLARED-FUNCTION'
    USAGE_OF_RESERVED_IDENTIFIER = 'SEMANTIC-ERROR-USAGE-OF-RESERVED-IDENTIFIER'
    MULTIPLE_VARIABLE_DECLARATION = 'SEMANTIC-ERROR-MULTIPLE-VARIABLE-DECLARATION'
    FUNCTION_TYPE_MISMATCH = 'SEMANTIC-ERROR-FUNCTION_TYPE_MISMATCH'
    FUNCTION_PARAMETERS_MISMATCH = 'SEMANTIC-ERROR-FUNCTION_PARAMETERS_MISMATCH'
    EXPRESSION_MULTIPLE_TYPES = 'SEMANTIC-ERROR-EXPRESSION-MULTIPLE-TYPES'
    UNFINISHED_EXPRESSION = 'SEMANTIC-ERROR-UNFINISHED-EXPRESSION'
    MISSING_VARIABLE_NAME = 'SEMANTIC-ERROR-MISSING-VARIABLE-NAME'
    UNKNOWN_DATA_TYPE = 'SEMANTIC-ERROR-UNKNOWN-DATA-TYPE'


class LexicalAnalyzer:
    class LexemeArrayType(object):
        def __init__(self, lexeme, lexemeType, lineNumber):
            self.lexeme = lexeme
            self.lexemeType = lexemeType
            self.lineNumber = lineNumber

        def __repr__(self):
            return '{0} - {1}. Line: {2}'.format(self.lexemeType, self.lexeme, self.lineNumber)

        def __str__(self):
            return self.lexeme

    class ErrorType(object):
        def __init__(self, lineNumber, word):
            self.lineNumber = lineNumber
            self.word = word

    def __init__(self, fileName):
        self.inputFile = open(fileName, 'r')
        self.lexemeArray = []
        self.errors = []

    def __del__(self):
        self.inputFile.close()

    def __removeSpaces(self, line):
        # self.inputFile = self.inputFile.replace("\n", "")
        return " ".join(line.split())

    def __splitBySeparators(self, line):
        resultLine = " ( ".join(line.split("("))
        resultLine = " ) ".join(resultLine.split(")"))
        resultLine = " [ ".join(resultLine.split("["))
        resultLine = " ] ".join(resultLine.split("]"))
        resultLine = " { ".join(resultLine.split("{"))
        resultLine = " } ".join(resultLine.split("}"))
        resultLine = " ; ".join(resultLine.split(";"))
        return " : ".join(resultLine.split(":")).rstrip()

    def __checkBySymbol(self, word, lineNumber):
        if re.match('^-?\d+\.?$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.INT_NUMBER, lineNumber))
            return

        if re.match('^-?\d+.?\d+[e|E]{1}[+|-]?\d+$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.EXPONENTIAL_NUMBER, lineNumber))
            return

        if re.match('^-?\d*.\d+$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.REAL_NUMBER, lineNumber))
            return

        if re.match('^\+\+$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.INCREMENT, lineNumber))
            return

        if re.match('^--$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.DECREMENT, lineNumber))
            return

        if re.match('^\+\+.+', word):
            self.lexemeArray.append(self.LexemeArrayType('++', LexemeType.INCREMENT, lineNumber))
            self.__checkBySymbol(word.replace('++', ''), lineNumber)
            return

        if re.match('.+\+\+$', word):
            self.__checkBySymbol(word.replace('++', ''), lineNumber)
            self.lexemeArray.append(self.LexemeArrayType('++', LexemeType.INCREMENT, lineNumber))
            return

        if re.match('^--.+', word):
            self.lexemeArray.append(self.LexemeArrayType('--', LexemeType.DECREMENT, lineNumber))
            self.__checkBySymbol(word.replace('--', ''), lineNumber)
            return

        if re.match('.+--$', word):
            self.__checkBySymbol(word.replace('--', ''), lineNumber)
            self.lexemeArray.append(self.LexemeArrayType('--', LexemeType.DECREMENT, lineNumber))
            return

        if re.match('^\".*\"$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.STRING_DATA, lineNumber))
            return

        if re.match('^\'.*\'$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.CHAR_DATA, lineNumber))
            return

        if re.match('^.*$', word):
            self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.WORD, lineNumber))
            return

        self.errors.append(self.ErrorType(lineNumber, word))
        self.lexemeArray.append(self.LexemeArrayType(word, LexemeType.UNDEFINED, lineNumber))

    def __removeComments(self, line):
        return re.sub('//.*', '', line)

    def startParsing(self):
        if not self.inputFile.read(1):
            return False
        else:
            self.inputFile.seek(0)

        lineNumber = 0
        for line in self.inputFile.readlines():
            lineNumber += 1
            removedComments = self.__removeComments(line)
            splitedLine = self.__splitBySeparators(removedComments)
            if splitedLine != '':
                for word in splitedLine.split():
                    try:
                        self.lexemeArray.append(self.LexemeArrayType(word, DictionaryOfLexemes[word], lineNumber))
                    except KeyError as e:
                        self.__checkBySymbol(word, lineNumber)

        if self.errors or len(self.lexemeArray) == 0:
            return False
        else:
            return True

    def printErrors(self):
        if not self.errors:
            print("No errors found.")
        for error in self.errors:
            print("Line: %s - Word: %s" % (error.lineNumber, error.word))

    def printLexemes(self):
        if self.lexemeArray:
            width = max(map(lambda lexeme: len(lexeme.lexemeType.name), self.lexemeArray)) + 1
            for lexeme in self.lexemeArray:
                print("Line: %s - [ %s ] - %s" % (lexeme.lineNumber, lexeme.lexemeType.name.rjust(width), lexeme.lexeme))


    def returnLexemes(self, testCaseNumber):
        return self.lexemeArray[testCaseNumber].lexemeType.name