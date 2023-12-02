import math
import sys
from typing import Optional, Union
from operator import add, sub, mul, truediv
from decimal import *

from PySide6.QtWidgets import QApplication, QMainWindow

from Calulator2 import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    '×': mul,
    '/': truediv
}
error_zero_div = 'Деление на ноль'
error_undefined = 'Результат не определён'
error_root_minus = 'Нельзя взять корень'
error_limit = 'Достигнут предел'

default_font_size = 14
change_font_size = 30

list_history = []
x = -1
side_scroll = 0

theme = True


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.Operucia.maxLength()

        # num
        self.ui.Bttn_0.clicked.connect(lambda: self.add_num('0'))
        self.ui.Bttn_1.clicked.connect(lambda: self.add_num('1'))
        self.ui.Bttn_2.clicked.connect(lambda: self.add_num('2'))
        self.ui.Bttn_3.clicked.connect(lambda: self.add_num('3'))
        self.ui.Bttn_4.clicked.connect(lambda: self.add_num('4'))
        self.ui.Bttn_5.clicked.connect(lambda: self.add_num('5'))
        self.ui.Bttn_6.clicked.connect(lambda: self.add_num('6'))
        self.ui.Bttn_7.clicked.connect(lambda: self.add_num('7'))
        self.ui.Bttn_8.clicked.connect(lambda: self.add_num('8'))
        self.ui.Bttn_9.clicked.connect(lambda: self.add_num('9'))

        # actions
        self.ui.Bttn_Clear.clicked.connect(self.clear_all)
        self.ui.Bttn_CE.clicked.connect(self.Clear_entry)
        self.ui.Bttn_drob.clicked.connect(self.add_point)
        self.ui.Bttn_Delete.clicked.connect(self.del1)
        self.ui.Bttn_Otricianie.clicked.connect(self.negate)
        self.ui.Bttn_Degree.clicked.connect(self.dou_x)
        self.ui.Bttn_Root.clicked.connect(self.root)
        self.ui.Bttn_Fraction.clicked.connect(self.one_div_x)
        self.ui.Bttn_Percent.clicked.connect(self.percent)
        self.ui.Bttn_left.clicked.connect(self.scrolling_history_left)
        self.ui.Bttn_right.clicked.connect(self.scrolling_history_right)
        self.ui.Bttn_basket.clicked.connect(self.clear_history)
        self.ui.Bttn_color.clicked.connect(self.change_theme)

        # math
        self.ui.Bttn_rowno.clicked.connect(self.calcul)
        self.ui.Bttn_plus.clicked.connect(lambda: self.math_operations('+'))
        self.ui.Bttn_minus.clicked.connect(lambda: self.math_operations('-'))
        self.ui.Bttn_Umnoj.clicked.connect(lambda: self.math_operations('×'))
        self.ui.Bttn_Delem.clicked.connect(lambda: self.math_operations('/'))

    def add_num(self, btn_text: str) -> None:
        self.remove_error()
        self.clear_entry()
        if self.ui.Operucia.text() == '0':
            self.ui.Operucia.setText(btn_text)
        else:
            self.ui.Operucia.setText(self.ui.Operucia.text() + btn_text)
        self.adjust_entry_font_size()

    def clear_all(self) -> None:
        self.remove_error()
        self.ui.Operucia.setText('0')
        self.adjust_entry_font_size()
        self.ui.Story.clear()
        self.adjust_temp_font_size()

    def Clear_entry(self) -> None:
        self.remove_error()
        self.clear_entry()
        self.ui.Operucia.setText('0')
        self.adjust_entry_font_size()

    def add_point(self) -> None:
        self.clear_entry()
        if '.' not in self.ui.Operucia.text():
            self.ui.Operucia.setText(self.ui.Operucia.text() + '.')
            self.adjust_entry_font_size()

    def negate(self):
        self.clear_entry()
        entry = self.ui.Operucia.text()
        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]
        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.Operucia.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.Operucia.setMaxLength(self.entry_max_len)
        self.ui.Operucia.setText(entry)
        self.adjust_entry_font_size()

    @staticmethod
    def remove_zero(numer: str) -> str:
        n = str(float(numer))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self, math_sign: str):
        if not self.ui.Story.text() or self.get_math_sign() == '=':
            self.ui.Story.setText(self.remove_exponential(self.remove_zero(self.ui.Operucia.text())) + f' {math_sign} ')
            self.adjust_temp_font_size()
            self.ui.Operucia.setText('0')
            self.adjust_entry_font_size()

    def get_entry_num(self) -> Decimal:
        entry = self.ui.Operucia.text().strip('.')
        return Decimal(entry) if '.' in entry else Decimal(entry)

    def del1(self) -> None:
        self.remove_error()
        num = self.ui.Operucia.text()
        if not self.get_math_sign() == '=':
            if len(num) != 1:
                if len(num) == 2 and '-' in num:
                    self.ui.Operucia.setText('0')
                    self.adjust_entry_font_size()
                else:
                    self.ui.Operucia.setText(self.ui.Operucia.text()[:-1])
                    self.adjust_entry_font_size()
            else:
                self.ui.Operucia.setText('0')
                self.adjust_entry_font_size()
        else:
            self.ui.Story.setText('')
            self.adjust_temp_font_size()

    def clear_entry(self) -> None:
        if self.get_math_sign() == '=':
            self.ui.Story.clear()
            self.adjust_temp_font_size()

    def get_temp_num(self) -> Union[Decimal, None]:
        if self.ui.Story.text():
            temp = self.ui.Story.text().strip('.').split()[0]
            return Decimal(temp) if '.' in temp else Decimal(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.Story.text():
            return self.ui.Story.text().strip('.').split()[-1]

    def calcul(self) -> Optional[str]:
        operate = self.ui.Operucia.text()
        num = self.ui.Story.text()
        if num:
            try:
                result = self.remove_zero(
                    str(
                        operations[self.get_math_sign()]((self.get_temp_num()), self.get_entry_num()))
                )
                self.ui.Story.setText(num + self.remove_exponential(self.remove_zero(operate)) + ' =')
                self.adjust_temp_font_size()
                self.ui.Operucia.setText(self.remove_exponential(result))
                self.limit(result)
                self.add_in_history_calculator()
                self.adjust_entry_font_size()
                return result
            except KeyError:
                pass
            except ZeroDivisionError:
                self.error_with_zero()
            except InvalidOperation:
                self.error_with_zero()

    def math_operations(self, math_sign: str):
        try:
            temp = self.ui.Story.text()
            if not temp:
                self.add_temp(math_sign)
            else:
                if self.get_math_sign() != math_sign:
                    if self.get_math_sign() == '=':
                        self.add_temp(math_sign)
                    else:
                        self.ui.Story.setText(temp[:-3] + f' {math_sign} ')
                        self.adjust_temp_font_size()
                else:
                    self.ui.Story.setText(self.remove_exponential(self.calcul()) + f' {math_sign} ')
                    self.adjust_temp_font_size()
        except TypeError:
            pass

    def show_error(self, text: str) -> None:
        self.ui.Operucia.setMaxLength(len(text))
        self.ui.Operucia.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.ui.Operucia.text() in (error_undefined, error_zero_div, error_root_minus, error_limit):
            self.ui.Operucia.setMaxLength(self.entry_max_len)
            self.ui.Operucia.setText('0')
            self.disable_buttons(False)
        self.adjust_entry_font_size()

    def disable_buttons(self, disable: bool) -> None:
        self.ui.Bttn_rowno.setDisabled(disable)
        self.ui.Bttn_Delem.setDisabled(disable)
        self.ui.Bttn_minus.setDisabled(disable)
        self.ui.Bttn_plus.setDisabled(disable)
        self.ui.Bttn_Umnoj.setDisabled(disable)
        self.ui.Bttn_drob.setDisabled(disable)
        self.ui.Bttn_Otricianie.setDisabled(disable)
        self.ui.Bttn_Percent.setDisabled(disable)
        self.ui.Bttn_Root.setDisabled(disable)
        self.ui.Bttn_Fraction.setDisabled(disable)
        self.ui.Bttn_Degree.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        rowno_color = 'color: white;' if disable else 'color: black;'
        self.change_color_btn_error(color, rowno_color)

    def change_color_btn_error(self, css_color: str, rowno_color: str) -> None:
        self.ui.Bttn_rowno.setStyleSheet(rowno_color)
        self.ui.Bttn_Delem.setStyleSheet(css_color)
        self.ui.Bttn_minus.setStyleSheet(css_color)
        self.ui.Bttn_plus.setStyleSheet(css_color)
        self.ui.Bttn_Umnoj.setStyleSheet(css_color)
        self.ui.Bttn_drob.setStyleSheet(css_color)
        self.ui.Bttn_Otricianie.setStyleSheet(css_color)
        self.ui.Bttn_Percent.setStyleSheet(css_color)
        self.ui.Bttn_Root.setStyleSheet(css_color)
        self.ui.Bttn_Fraction.setStyleSheet(css_color)
        self.ui.Bttn_Degree.setStyleSheet(css_color)

    def get_entry_text_width(self) -> int:
        return self.ui.Operucia.fontMetrics().boundingRect(self.ui.Operucia.text()).width() + 5

    def get_temp_text_width(self) -> int:
        return self.ui.Story.fontMetrics().boundingRect(self.ui.Story.text()).width() + 5

    def adjust_entry_font_size(self) -> None:
        font_size = change_font_size
        while self.get_entry_text_width() > self.ui.Operucia.width() - 20:
            font_size -= 1
            self.ui.Operucia.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')
        font_size = 1
        while self.get_entry_text_width() < self.ui.Operucia.width() - 60:
            font_size += 1
            if font_size > change_font_size:
                break
            self.ui.Operucia.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.ui.Story.width() - 20:
            font_size -= 1
            self.ui.Story.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888')
        font_size = 1
        while self.get_temp_text_width() < self.ui.Story.width() - 45:
            font_size += 1
            if font_size > default_font_size:
                break
            self.ui.Story.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888')

    def resizeEvent(self, event):
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()

    def dou_x(self):
        equation = self.ui.Story.text()
        if not equation:
            num = self.remove_exponential(self.remove_zero(self.ui.Operucia.text()))
            self.ui.Story.setText(num + ' × ' + num + ' =')
            self.adjust_temp_font_size()
            rez = self.get_entry_num() ** 2
            self.ui.Operucia.setText(self.remove_exponential(self.remove_zero(str(rez))))
            self.limit(rez)
            self.add_in_history_calculator()
            self.adjust_entry_font_size()
        else:
            try:
                if not self.get_math_sign() == '=':
                    per = self.get_entry_num() ** 2
                    return self.dop_operate(per, equation)
                if self.get_math_sign() == '=':
                    per = self.get_entry_num() ** 2
                    self.ui.Story.setText(
                        self.remove_exponential(self.ui.Operucia.text()) + ' × ' + self.remove_exponential(
                            self.ui.Operucia.text()) + ' =')
                    self.adjust_temp_font_size()
                    self.ui.Operucia.setText(self.remove_exponential(per))
                    self.limit(per)
                    self.add_in_history_calculator()
                    return self.adjust_entry_font_size()
            except KeyError:
                pass
            except ZeroDivisionError:
                self.error_with_zero()
            except InvalidOperation:
                self.error_with_zero()

    def root(self):
        if '-' in self.ui.Operucia.text():
            return self.show_error(error_root_minus)
        equation = self.ui.Story.text()
        if not equation or self.get_math_sign() == '=':
            self.ui.Story.setText('√' + self.remove_exponential(self.remove_zero(self.ui.Operucia.text())) + ' =')
            self.adjust_temp_font_size()
            rez = self.get_entry_num() ** Decimal(0.5)
            self.ui.Operucia.setText(self.remove_exponential(self.remove_zero(str(rez))))
            self.limit(rez)
            self.add_in_history_calculator()
            self.adjust_entry_font_size()
        else:
            try:
                if not self.get_math_sign() == '=':
                    per = self.get_entry_num() ** Decimal(0.5)
                    return self.dop_operate(per, equation)
            except KeyError:
                pass
            except ZeroDivisionError:
                self.error_with_zero()
            except InvalidOperation:
                self.error_with_zero()

    def percent(self) -> Optional[str]:
        if '-' in self.ui.Operucia.text():
            return self.show_error(error_undefined)
        equation = self.ui.Story.text()
        try:
            if equation and not self.get_math_sign() == '=':
                per = self.remove_exponential((self.get_temp_num() / 100) * Decimal(self.ui.Operucia.text()))
                return self.dop_operate(per, equation)
            if not equation or self.get_math_sign() == '=':
                per = self.remove_exponential(self.remove_zero(str(Decimal(self.ui.Operucia.text()) / 100)))
                self.ui.Story.setText(self.ui.Operucia.text() + ' / 100 =')
                self.adjust_temp_font_size()
                self.ui.Operucia.setText(per)
                self.limit(per)
                self.add_in_history_calculator()
                return self.adjust_entry_font_size()
        except KeyError:
            pass
        except ZeroDivisionError:
            self.error_with_zero()
        except InvalidOperation:
            self.error_with_zero()

    def one_div_x(self):
        equation = self.ui.Story.text()
        if not equation or self.get_math_sign() == '=':
            try:
                self.ui.Story.setText(
                    '1 / ' + self.remove_exponential(self.remove_zero(self.ui.Operucia.text())) + ' =')
                self.adjust_temp_font_size()
                rez = 1 / self.get_entry_num()
                self.ui.Operucia.setText(self.remove_exponential(self.remove_zero(str(rez))))
                self.limit(rez)
                self.add_in_history_calculator()
                self.adjust_entry_font_size()
            except KeyError:
                pass
            except ZeroDivisionError:
                self.error_with_zero()
            except InvalidOperation:
                self.error_with_zero()
        else:
            try:
                per = 1 / self.get_entry_num()
                return self.dop_operate(per, equation)
            except KeyError:
                pass
            except ZeroDivisionError:
                self.error_with_zero()
            except InvalidOperation:
                self.error_with_zero()

    def dop_operate(self, per, equation) -> Optional[str]:
        rez = self.remove_zero(
            str(
                operations[self.get_math_sign()]((self.get_temp_num()), Decimal(per))))
        self.ui.Story.setText(equation + self.remove_exponential(self.remove_zero(str(per))) + ' =')
        self.adjust_temp_font_size()
        self.ui.Operucia.setText(self.remove_exponential(self.remove_zero(rez)))
        self.limit(rez)
        self.add_in_history_calculator()
        self.adjust_entry_font_size()
        return rez

    def error_with_zero(self):
        if self.get_temp_num() == 0:
            self.show_error(error_undefined)
        else:
            self.show_error(error_zero_div)

    @staticmethod
    def remove_exponential(result) -> str:
        return f"{Decimal(result):f}"

    def limit(self, result):
        if len(self.remove_exponential(result)) >= self.ui.Operucia.maxLength():
            if self.ui.Operucia.text() == '0.00000000000000':
                return self.show_error(error_limit)
            elif len(self.remove_exponential(math.floor(Decimal(result)))) > 16:
                return self.show_error(error_limit)

    def add_in_history_calculator(self):
        story = self.ui.Story.text()
        operation = self.ui.Operucia.text()
        if '=' in story and not(operation in (error_undefined, error_zero_div, error_root_minus, error_limit)):
            global list_history
            list_history.append(''.join(story + operation))
            global x
            x = -1

    @staticmethod
    def clear_history():
        global list_history
        list_history.clear()

    def scrolling_history_right(self):
        global x, list_history, side_scroll
        if not list_history:
            return
        if side_scroll == -1:
            x += 1
        side_scroll = 1
        if x >= 0:
            x = -len(list_history)
        try:
            if list_history[x] == ''.join(self.ui.Story.text()+self.ui.Operucia.text()):
                x += 1
            self.scroll_history(x)
            x += 1
        except IndexError:
            x = -len(list_history)
            self.scroll_history(x)
            x += 1

    def scrolling_history_left(self):
        global x, list_history, side_scroll
        if not list_history:
            return
        if side_scroll == 1:
            x -= 1
        side_scroll = -1
        try:
            if list_history[x] == ''.join(self.ui.Story.text()+self.ui.Operucia.text()):
                x -= 1
            self.scroll_history(x)
            x -= 1
        except IndexError:
            x = -1
            self.scroll_history(x)
            x -= 1

    def scroll_history(self, i):
        operation = list_history[i].split('=')
        story = (operation[0] + '=')
        result = operation[1]
        self.ui.Operucia.setText(result)
        self.adjust_entry_font_size()
        self.ui.Story.setText(story)
        self.adjust_temp_font_size()
        self.clear_all()

    def change_theme(self):
        global theme
        theme = not theme
        if theme:
            f = open('ui/theme/Dark.css', 'r')
        else:
            f = open('ui/theme/White.css', 'r')
        style = f.read()
        f.close()
        self.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()

    sys.exit(app.exec())
