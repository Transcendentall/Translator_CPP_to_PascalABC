import unittest
import sys
import os

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from source.EarleyAlgorithm import Earley
from source.GrammarParser import GrammarParser


class TestEarleyAlgorithm(unittest.TestCase):
    def test_earley_is_ok(self):
        parser = GrammarParser()
        parser.parseJsonRules('../grammar_rules.json')
        earley = Earley(parser.rules, "<программа>")
        self.assertEqual(earley.isOk(), False)

    def test_earley_error(self):
        parser = GrammarParser()
        parser.parseJsonRules('../grammar_rules.json')
        earley = Earley(parser.rules, "<программа>")
        self.assertEqual(earley.semanticError, None)

    def test_earley_table(self):
        parser = GrammarParser()
        parser.parseJsonRules('../grammar_rules.json')
        earley = Earley(parser.rules, "<программа>")
        self.assertEqual(earley.table, None)





