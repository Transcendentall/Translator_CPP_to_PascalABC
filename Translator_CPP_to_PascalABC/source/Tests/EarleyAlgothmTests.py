import unittest
import sys
import os

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from source.EarleyAlgorithm import Earley
from source.GrammarParser import GrammarParser


class TestEarleyAlgorithm(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = GrammarParser()
        self.parser.parseJsonRules('../grammar_rules.json')

    def test_earley_is_ok_1(self):
        earley = Earley(self.parser.rules, "<программа>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_2(self):
        earley = Earley(self.parser.rules, "<предложение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_3(self):
        earley = Earley(self.parser.rules, "<идентификатор>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_4(self):
        earley = Earley(self.parser.rules, "<объявление процедуры>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_5(self):
        earley = Earley(self.parser.rules, "<объявление функции>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_6(self):
        earley = Earley(self.parser.rules, "<формальные параметры>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_7(self):
        earley = Earley(self.parser.rules, "<тело процедуры>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_8(self):
        earley = Earley(self.parser.rules, "<выход>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_9(self):
        earley = Earley(self.parser.rules, "<тело функции>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_10(self):
        earley = Earley(self.parser.rules, "<возврат значения>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_11(self):
        earley = Earley(self.parser.rules, "<инструкция>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_12(self):
        earley = Earley(self.parser.rules, "<вывод данных>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_13(self):
        earley = Earley(self.parser.rules, "<начало вывода>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_14(self):
        earley = Earley(self.parser.rules, "<тело вывода>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_15(self):
        earley = Earley(self.parser.rules, "<выводимые данные>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_16(self):
        earley = Earley(self.parser.rules, "<конец вывода>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_17(self):
        earley = Earley(self.parser.rules, "<ввод данных>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_18(self):
        earley = Earley(self.parser.rules, "<тело ввода>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_19(self):
        earley = Earley(self.parser.rules, "<подключение библиотеки>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_20(self):
        earley = Earley(self.parser.rules, "<инициализация переменной>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_21(self):
        earley = Earley(self.parser.rules, "<обновление переменной>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_22(self):
        earley = Earley(self.parser.rules, "<новая переменная>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_23(self):
        earley = Earley(self.parser.rules, "<тип данных>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_24(self):
        earley = Earley(self.parser.rules, "<имя переменной>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_25(self):
        earley = Earley(self.parser.rules, "<зарезервированное имя>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_26(self):
        earley = Earley(self.parser.rules, "<буква>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_27(self):
        earley = Earley(self.parser.rules, "<цифра>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_28(self):
        earley = Earley(self.parser.rules, "<булева константа>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_29(self):
        earley = Earley(self.parser.rules, "<число>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_30(self):
        earley = Earley(self.parser.rules, "<целое число>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_31(self):
        earley = Earley(self.parser.rules, "<вещественное число>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_32(self):
        earley = Earley(self.parser.rules, "<вызов процедуры>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_33(self):
        earley = Earley(self.parser.rules, "<вызов функции>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_34(self):
        earley = Earley(self.parser.rules, "<фактические параметры>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_35(self):
        earley = Earley(self.parser.rules, "<ветвление>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_36(self):
        earley = Earley(self.parser.rules, "<условие>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_37(self):
        earley = Earley(self.parser.rules, "<иначе>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_38(self):
        earley = Earley(self.parser.rules, "<цикл>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_39(self):
        earley = Earley(self.parser.rules, "<цикл for>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_40(self):
        earley = Earley(self.parser.rules, "<выражение for1>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_41(self):
        earley = Earley(self.parser.rules, "<цикл while>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_42(self):
        earley = Earley(self.parser.rules, "<выражение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_43(self):
        earley = Earley(self.parser.rules, "<алгебраическое выражение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_44(self):
        earley = Earley(self.parser.rules, "<бинарный алгебраический оператор>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_45(self):
        earley = Earley(self.parser.rules, "<унарный алгебраический оператор>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_46(self):
        earley = Earley(self.parser.rules, "<алгебраический операнд>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_47(self):
        earley = Earley(self.parser.rules, "<булево выражение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_48(self):
        earley = Earley(self.parser.rules, "<простое булево выражение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_49(self):
        earley = Earley(self.parser.rules, "<сложное булево выражение>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_50(self):
        earley = Earley(self.parser.rules, "<булев операнд>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_51(self):
        earley = Earley(self.parser.rules, "<главная функция>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_52(self):
        earley = Earley(self.parser.rules, "<логический оператор>")
        self.assertEqual(False, earley.isOk())

    def test_earley_is_ok_53(self):
        earley = Earley(self.parser.rules, "<оператор сравнения>")
        self.assertEqual(False, earley.isOk())

    def test_earley_error(self):
        self.assertRaises(ValueError, lambda: Earley(self.parser.rules, "<несуществующий оператор>"))
