from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QDialog
from good_form import GoodsForm
import sqlite3
from db import Bicycle_db
import re
from collections import OrderedDict
from main_ui_fixes import FixesMainWindow
from decimal import Decimal
import time
from random import randint
from custom_widgets import NumericItem, InputDialog
from library.sublings import category_ids
from collections import defaultdict


class Views_Main_Window(FixesMainWindow):
    def __init__(self):
        self.current_row = {}
        self.goods_from_category = []
        self.cart_items = []
        self.total_price = 0
        self.total_income = 0
        self.course = 27.69
    
    def change_product_qty_in_cart(self):
        #get values
        if self.tableWidget_2.currentColumn() == 2:
            values = self.tableWidget_2.parse_row()
            counter = 0
            for cart_item in self.cart_items:
                counter+=1
                if cart_item['Название'] == values['название']:
                    qty = cart_item['Кол-во.']
                    if int(cart_item['Кол-во.']) == 1:
                        QtWidgets.QMessageBox.about(self.tab, 'Error','Товар в единичном количестве')
                    else:
                        dialog = InputDialog(value=str(values["название"]), qty=str(qty))
                        if dialog.exec():
                            new_qty = dialog.getInputs()
                            item = NumericItem()
                            item.setData(QtCore.Qt.DisplayRole, (new_qty))
                            self.tableWidget_2.setItem((counter-1),2,QtWidgets.QTableWidgetItem(item))



    def parse_row_and_move_to_cart(self):
        values = self.tableWidget.parse_row()
        if int(values['Кол-во.']) > 0:
                # qty = int(dialog.getInputs())
            self.total_price = 0
            row = self.tableWidget_2.rowCount()
            values = self.tableWidget.parse_row()
            self.tableWidget_2.insertRow(row + 1)
            self.tableWidget_2.setRowCount(row + 1)
            item = NumericItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)


            item.setData(QtCore.Qt.DisplayRole, values["Название"])
            self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, (values["ГРН"]))
            self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))
            self.counting_price_income_from_cart_items("ГРН", "Закупка", "Продаж")
            values['qty_item_in_cart'] = 1
            items_price = int(values['ГРН'])*int(values['qty_item_in_cart'])
            self.total_price+= items_price
            self.label_37.setText(str(self.total_price))
            self.label_38.setText(str(round(self.total_income)))
            item.setData(QtCore.Qt.DisplayRole, (items_price))
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(item))
            item.setData(QtCore.Qt.DisplayRole, values['qty_item_in_cart'])
            self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(item))
            self.cart_items.append(values)
        else:
            QtWidgets.QMessageBox.about(self.tab, 'Error','Нельзя добавить товар с количеством 0')
    def remove_from_cart(self):
        values = self.tableWidget_2.parse_row()

    def calculate_good_income(self, sell, buy):
        income = round(abs((float(sell) - float(buy))) * self.course, 1)
        self.total_income += income

    def counting_price_income_from_cart_items(
        self, grivna_keyword, sell_keyword=False, buy_keyword=False, sale=False
    ):
        for item in self.cart_items:
            self.total_price += int(item[grivna_keyword])

            if "Арт" in item:
                if sell_keyword:
                    income = self.calculate_good_income(
                        item[sell_keyword], item[buy_keyword]
                    )
        if sale:
            self.total_price -= int(sale)

    def show_insert_window(self):
        pass

    def get_cart_items(self):
        pass

    def cart_qty_handler(self):
        cart_items = self.tableWidget_2.get_values_from_cart()
        key_for_search = "кол-во"
        unique = []
        for item in cart_items:
            if item not in unique:
                unique.append(item)
        print(unique)


    def get_values_from_db(self):
        self.set_into_table_goods()
        self.set_into_categories_table()

    def find_child_category(self, list_with_results):
        id_with_child = []
        for result in list_with_results:
            if result["parent_id"] == -1:
                id_with_child.append({"id": result["id"], "childs": []})
            else:
                for number in range(len(id_with_child)):
                    if id_with_child[number]["id"] == result["parent_id"]:
                        id_with_child[number]["childs"].append(result["name_category"])
        return id_with_child

    def get_category_values(self):
        list_dict_with_results = []
        db = Bicycle_db()
        result = db.edit("Select * FROM categories")
        count = len(result)
        for item in result:
            id = item[0]
            name_category = item[1]
            parent_id = item[2]
            export_date = item[3]
            list_dict_with_results.append(
                {
                    "id": id,
                    "name_category": name_category,
                    "parent_id": parent_id,
                    "export_date": export_date,
                }
            )
        # sort_by_id
        return sorted(list_dict_with_results, key=lambda k: k["parent_id"])

    def fill_tree(self):
        list_with_results = self.get_category_values()
        childs_categories = self.find_child_category(list_with_results)
        for res in list_with_results:
            if res["parent_id"] == -1:
                item = QtWidgets.QTreeWidgetItem([res["name_category"]])
                current_index = self.treeWidget.currentItem()
                self.treeWidget.addTopLevelItem(item)
                for child in childs_categories:
                    if res["id"] == child["id"]:
                        if len(child["childs"]) != 0:
                            for element in child["childs"]:
                                QtWidgets.QTreeWidgetItem(item, [element])

    def display_goods_from_category(self, for_search=False):
        goods_for_display = []
        try:
            category = self.treeWidget.currentItem().text(0)
        except:
            category = "Всі"
        category_number = category_ids[category]
        for good in self.tableWidget.goods_from_table:
            if str(category_number) in good["category"]:
                goods_for_display.append(good["article"])
        for row in range(self.tableWidget.rowCount()):
            twItem = self.tableWidget.item(row, 0)
            if int(twItem.text()) in goods_for_display:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def find_in(self, textinput, column):
        text = textinput.text()
        if column == 1:
            for row in range(self.tableWidget.rowCount()):
                twItem = self.tableWidget.item(row, column)
                if "{}".format(text.lower()) in str(twItem.text()).lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)
        else:
            for row in range(self.tableWidget.rowCount()):
                twItem = self.tableWidget.item(row, column)
                text_in_window = twItem.text()
                if "{}".format(str(text).lower()) in str(text_in_window).lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)

    def set_current_category(self, category):
        db = Bicycle_db()

        query = "CREATE TABLE IF NOT EXISTS cur_category (id INTEGER PRIMARY KEY AUTOINCREMENT, name_category TEXT);"
        query_2 = 'insert into cur_category(name_category) values("{}")'.format(
            category
        )
        db.insert(query)
        db.insert(query_2)
        db.close()

    def hander_for_handy_buttons(self, line_edit, button):
        self.total_price = 0
        price = line_edit.text()
        specific = button.text()
        row = self.tableWidget_2.rowCount()
        item = QtWidgets.QTableWidgetItem()
        item.setData(QtCore.Qt.DisplayRole, (price))
        self.tableWidget_2.insertRow(row + 1)
        self.tableWidget_2.setRowCount(row + 1)
        self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(specific)))
        self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(item))

        if button == self.sale_button:
            self.counting_price_income_from_cart_items("ГРН", sale=price)
        else:
            self.cart_items.append({"Название": specific, "ГРН": price})
            self.counting_price_income_from_cart_items("ГРН")
        self.label_37.setText(str(self.total_price))
        self.label_38.setText(str(round(self.total_income)))
        self.tableWidget_2.setItem(
            row, 2, QtWidgets.QTableWidgetItem(str((self.total_price)))
        )

    def clean_cart(self):
        self.total_price = 0
        self.cart_items = []
        self.total_income = 0
        self.tableWidget_2.clean_table()

    def add_actions(self):
        # calling in UI

        self.add_additional_custom_elements()
        # self.add_goods_action.triggered.connect(self.show_insert_window)
        self.treeWidget.clicked.connect(self.display_goods_from_category)
        self.tableWidget.doubleClicked.connect(self.parse_row_and_move_to_cart)
        # show name good on bottom
        self.tableWidget.clicked.connect(
            lambda: self.statusBar.showMessage(
                self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
            )
        )
        self.tableWidget_2.clicked.connect(
            self.change_product_qty_in_cart
        )
        self.tableWidget_2.clicked.connect(
            lambda: self.statusBar.showMessage(
                self.tableWidget_2.item(
                    self.tableWidget_2.currentRow(), self.tableWidget_2.currentColumn()
                ).text()
            )
        )
        self.tableWidget_2.doubleClicked.connect(self.remove_from_cart)
        self.tableWidget.clicked.connect(lambda: print(self.tableWidget.currentRow()))
        self.treeWidget.clicked.connect(
            lambda: self.statusBar.showMessage(self.treeWidget.currentItem().text(0))
        )
        self.treeWidget.clicked.connect(
            lambda: self.set_current_category(self.treeWidget.currentItem().text(0))
        )
        # self.tableWidget.c
        self.materials_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(
                self.lineEdit_3, self.materials_button
            )
        )
        self.workshop_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(self.lineEdit_5, self.workshop_button)
        )
        self.sale_button.clicked.connect(
            lambda: self.hander_for_handy_buttons(self.lineEdit_6, self.sale_button)
        )

        # clean cart button
        self.pushButton_4.clicked.connect(self.clean_cart)
        self.lineEdit.textChanged.connect(lambda: self.find_in(self.lineEdit, 0))
        self.lineEdit_4.textChanged.connect(lambda: self.find_in(self.lineEdit_4, 1))
        self.lineEdit.inputRejected.connect(lambda: self.find_in(self.lineEdit, 0))
        self.lineEdit_4.inputRejected.connect(lambda: self.find_in(self.lineEdit_4, 1))
        self.pushButton_8.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton_8.clicked.connect(lambda: self.lineEdit_4.clear())