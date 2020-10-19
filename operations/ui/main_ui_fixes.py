from PySide2 import QtCore, QtGui, QtWidgets, Qt
from widgets.main_table import CustomTableWithGoods
from widgets.category_tree import CustomTreeWidget
from widgets.cart_table import CartTable
from widgets.cassa_table import CustomCashierTable


class FixesMainWindow:



    def add_additional_custom_elements(self):
        self.add_custom_tree()
        self.add_custom_table()
        self.fill_tree()
        self.resize_tableWidget()
        self.tableWidget.display_goods()
        self.change_search_widget_section()
        self.fixes_on_cart()
        self.add_custom_cart_table()
        self.add_combobox_with_qty()
        self.ui_fixes()
        self.init_cassa_table()
        self.create_labels_above_cassa_table()
        self.rename_commentary_buttons()


    def ui_fixes(self):
        self.label_22.setText("Наличные")
        self.label_22.setFont(QtGui.QFont("Sans Serif", 11))
        # set no editable
        # self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()
        # change basket section
        self.tableWidget_2.setGeometry(960, 140, 500, 431)
        self.label_2.setGeometry(960, 610, 81, 21)
        self.label_5.setGeometry(960, 650, 81, 21)
        self.pushButton_4.setGeometry(960, 690, 91, 41)
        self.pushButton_5.setGeometry(1140, 610, 101, 31)
        self.pushButton_6.setGeometry(1140, 650, 101, 31)
        self.pushButton_7.setGeometry(1140, 690, 101, 41)
        self.spacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )  # or Fixed
        self.firstVTabLayout.addItem(self.spacer)
        self.firstVTabLayout.addStretch(1)

        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.materials_button = QtWidgets.QPushButton(self.tab)
        self.materials_button.setGeometry(1000, 60, 141, 21)
        self.materials_button.setText("материалы")
        self.workshop_button = QtWidgets.QPushButton(self.tab)
        self.workshop_button.setGeometry(QtCore.QRect(1000, 80, 141, 21))
        self.workshop_button.setText("работа")
        self.sale_button = QtWidgets.QPushButton(self.tab)
        self.sale_button.setGeometry(QtCore.QRect(1000, 100, 141, 21))
        self.sale_button.setText("скидка")
        self.materials_button.show()
        self.workshop_button.show()
        self.sale_button.show()

    def fixes_on_cart(self):
        self.lineEdit_5.setGeometry(950, 80, 50, 18)
        self.lineEdit_6.setGeometry(950, 100, 50, 18)
        self.lineEdit_3.setGeometry(950, 60, 50, 18)
        self.label_8.setGeometry(QtCore.QRect(1010, 80, 131, 20))
        self.label_9.setGeometry(QtCore.QRect(1010, 100, 131, 20))
        self.pushButton_5.setText("Наличные")
        # total price and total income labels
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setGeometry(1020, 610, 81, 21)
        self.label_37.show()
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setGeometry(1020, 650, 81, 21)
        self.label_38.show()

    def change_search_widget_section(self):
        self.lineEdit.setFixedWidth(50)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 40, 490, 20))
        self.pushButton_8.setGeometry(QtCore.QRect(680, 40, 31, 21))
        self.comboBox.hide()
        self.tableWidget.setFixedHeight(600)
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addStretch()
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

    def resize_tableWidget(self):
        values = [50, 480, 50, 50, 50, 50, 50, 70]
        for i in range(len(values)):
            self.tableWidget.setColumnWidth(i, values[i])
        pass

    def resize_tableWidget_2(self):
        values = [305, 60, 60, 60]
        for i in range(len(values)):
            self.tableWidget_2.setColumnWidth(i, values[i])
        self.tableWidget_2.showFullScreen()

    def add_top_element_in_tree_widget(self, item_name):
        current_index = self.treeWidget.current_item()
        self.treeWidget.insertTopLevelItems(current_index, item_name)

    def add_custom_tree(self):
        self.treeWidget = CustomTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 40, 131, 850))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setHeaderHidden(True)

    def add_custom_cart_table(self):
        self.tableWidget_2 = CartTable(self.tab, self.label_37, self.label_38)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(9)
        self.tableWidget_2.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText("название")
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText("цена")
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText("сумма")
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText("кол-во")
        self.tableWidget_2.raise_()
        self.resize_tableWidget_2()
        self.tableWidget_2.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.firstVTabLayout = QtWidgets.QVBoxLayout(self.tab)
        self.firstHTabLayout = QtWidgets.QHBoxLayout(self.tab)
        self.firstVTabLayout.addLayout(self.firstHTabLayout)
        self.tab.setLayout = self.firstVTabLayout

    def add_combobox_with_qty(self):
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.addItem('все')
        self.comboBox.addItem('в наличии')
        self.comboBox.addItem('отсутствуют')
        self.comboBox.setGeometry(QtCore.QRect(710, 40, 100, 20))
        self.comboBox.show()


    def add_custom_table(self):
        # refactor after code from design-generator
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget = CustomTableWithGoods(self.tab, self.treeWidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 801, 521))
        # self.tableWidget.setMaximumSize(QtCore.QSize(801, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, i, item)
        # refactor this after
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Арт"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Закупка"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Нац"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Продаж"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Кол-во."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ГРН"))
        self.tableWidget.verticalHeader().setDefaultSectionSize(9)
        self.tableWidget.verticalHeader().setVisible(False)



    def init_cassa_table(self):
        self.tableWidget_6 = CustomCashierTable(self.tab_2)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 110, 1011, 600))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(6, item)
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(192, 252, 187))
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText( "Дата")
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText( "Арт")
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText( "Название")
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText( "Кол")
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText("Сумма")
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText( "Прибыль")
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText( "Тип")
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText( "НКТ")
        item = self.tableWidget_6.horizontalHeaderItem(8)
        # item.setText( "НКТ")
        self.tableWidget_6.verticalHeader().setVisible(False)
        values = [150, 50, 500, 50, 50, 80, 50, 50 ]

        for i in range(len(values)):
            self.tableWidget_6.setColumnWidth(i, values[i])

    def create_labels_above_cassa_table(self):
        def set_font_for_labels(label):
            font = QtGui.QFont()
            font.setFamily("Noto Sans Mono CJK JP")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            label.setLineWidth(4)

        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(350, 68, 151, 21))
        self.label_17.setText('0')
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(350, 17, 151, 41))
        self.label_18.setText('получено')
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(460, 17, 151, 41))
        self.label_20.setText("прибыль")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(460, 68, 151, 21))
        self.label_19.setText("0")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(560, 17, 151, 41))
        self.label_31.setText('магазин')
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(560, 60, 151, 41))
        self.label_32.setText("0")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(810, 17, 151, 41))
        self.label_33.setText('расходы')
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(810, 60, 151, 41))
        self.label_34.setText("0")
        self.label_35 = QtWidgets.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(690, 17, 151, 41))
        self.label_35.setText("работа")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(690, 60, 151, 41))
        self.label_36.setText("0")
        self.label_39 = QtWidgets.QLabel(self.tab_2)
        self.label_39.setGeometry(QtCore.QRect(925, 17, 151, 41))
        self.label_39.setText('авансы')
        self.label_40 = QtWidgets.QLabel(self.tab_2)
        self.label_40.setGeometry(QtCore.QRect(925, 60, 151, 41))
        self.label_40.setText('0')
        labels = [self.label_17,self.label_18,self.label_19,
                    self.label_20,self.label_32,self.label_31, self.label_33,self.label_34,self.label_35,self.label_36,self.label_39,self.label_40]
        for label in labels:
            set_font_for_labels(label)
    
    def button_color_changer(self, button):
        button_name = button.text()
        red_state = ['наличка', 'терминал', 'карта']
        blue_state = ['аванс', 'расходы', 'товар']
        if button_name in red_state:
            condition = self.buttons_condition[button_name]
            if condition != 0:
                #make button red
                pass
            else:
                #change_default
                pass
        elif
    
    def rename_commentary_buttons(self):
        self.pushButton_11.setText('наличка')
        self.pushButton_12.setText('карта')
        self.pushButton_13.setText('терминал')
        self.pushButton_16.setText('аванс')
        self.pushButton_14.setText('расходы')
        self.pushButton_15.setText('товар')


