# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h:\CME495\desktop-app\homebrew-controller\newRecipe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newRecipe(object):
    def setupUi(self, newRecipe):
        newRecipe.setObjectName("newRecipe")
        newRecipe.resize(1071, 668)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        newRecipe.setFont(font)
        newRecipe.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(newRecipe)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(newRecipe)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(newRecipe)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(newRecipe)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 5, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(newRecipe)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 3)
        self.doneButton = QtWidgets.QPushButton(newRecipe)
        self.doneButton.setObjectName("doneButton")
        self.gridLayout.addWidget(self.doneButton, 5, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addInstructionButton = QtWidgets.QPushButton(newRecipe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addInstructionButton.sizePolicy().hasHeightForWidth())
        self.addInstructionButton.setSizePolicy(sizePolicy)
        self.addInstructionButton.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addInstructionButton.setFont(font)
        self.addInstructionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addInstructionButton.setObjectName("addInstructionButton")
        self.verticalLayout.addWidget(self.addInstructionButton)
        self.removeInstructionButton = QtWidgets.QPushButton(newRecipe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeInstructionButton.sizePolicy().hasHeightForWidth())
        self.removeInstructionButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.removeInstructionButton.setFont(font)
        self.removeInstructionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeInstructionButton.setObjectName("removeInstructionButton")
        self.verticalLayout.addWidget(self.removeInstructionButton)
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recipeName = QtWidgets.QLineEdit(newRecipe)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recipeName.setFont(font)
        self.recipeName.setObjectName("recipeName")
        self.horizontalLayout.addWidget(self.recipeName)
        self.toolButton = QtWidgets.QToolButton(newRecipe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(newRecipe)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(newRecipe)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 8)

        self.retranslateUi(newRecipe)
        QtCore.QMetaObject.connectSlotsByName(newRecipe)

    def retranslateUi(self, newRecipe):
        _translate = QtCore.QCoreApplication.translate
        newRecipe.setWindowTitle(_translate("newRecipe", "Dialog"))
        self.label.setText(_translate("newRecipe", "Recipe Builder"))
        self.label_2.setText(_translate("newRecipe", "Instructions"))
        self.cancelButton.setText(_translate("newRecipe", "Cancel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("newRecipe", "Ingredient"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("newRecipe", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("newRecipe", "Unit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("newRecipe", "Temp"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("newRecipe", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("newRecipe", "Stage"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("newRecipe", "Note"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.doneButton.setText(_translate("newRecipe", "Done"))
        self.addInstructionButton.setText(_translate("newRecipe", "+"))
        self.removeInstructionButton.setText(_translate("newRecipe", "-"))
        self.recipeName.setPlaceholderText(_translate("newRecipe", "Recipe Name"))
        self.toolButton.setText(_translate("newRecipe", "..."))
        self.radioButton.setText(_translate("newRecipe", "Fahrenheit"))
        self.radioButton_2.setText(_translate("newRecipe", "Celcius"))
