# -*- coding: UTF-8 -*-
"""
PROJECT_NAME Python_projects
PRODUCT_NAME PyCharm
NAME run
AUTHOR Pfolg
TIME 2025/2/26 19:51
"""
from PyQt6.QtGui import QIcon, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView, QComboBox
import sys
from PyQt6 import uic
import pandas as pd


def get_data():
    table = pd.read_excel("sample.xlsx", sheet_name="sheet1")
    header = []
    # 获取表头
    for it in table:
        header.append(it)
    # print(header)
    np_table = table.to_numpy()
    # print(np_table, header, len(np_table), len(np_table[0]))
    # print(*header)
    # for i in np_table:
    # print(*i)
    return header, np_table


if __name__ == '__main__':
    table_header, table_data = get_data()
    app = QApplication(sys.argv)
    ui = uic.loadUi("./ui.ui")
    tableWidget: QTableWidget = ui.tableWidget

    row = len(table_data)
    column = len(table_header)
    tableWidget.setRowCount(row)
    tableWidget.setColumnCount(column + 1)
    tableWidget.setHorizontalHeaderLabels(["选择状态", *table_header])

    for i in range(row):
        for j in range(column):
            if j == 2:
                tableWidget.setItem(i, j + 1, QTableWidgetItem(
                    QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\solid\display.svg"),
                    str(table_data[i][j])))
            elif j == 0:
                tableWidget.setItem(i, j + 1, QTableWidgetItem(
                    QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\solid\dove.svg"),
                    str(table_data[i][j])))
            elif j == 1:
                data = QTableWidgetItem(
                    QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\solid\list.svg"),
                    str(table_data[i][j]))
                data.setBackground(QBrush(QColor("#2fb376")))
                tableWidget.setItem(i, j + 1, data)
            elif j == 3:
                data = QTableWidgetItem(
                    QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\solid\marker.svg"),
                    str(table_data[i][j]))
                data.setForeground(QBrush(QColor("#367ed9")))
                tableWidget.setItem(i, j + 1, data)
            elif j == 4:
                tableWidget.setItem(i, j + 1, QTableWidgetItem(
                    QIcon(r"D:\Users\21460\Pictures\fontawesome-free-6.7.2-desktop\svgs\solid\seedling.svg"),
                    str(table_data[i][j])))
            elif j in [7, 6]:
                tableWidget.setColumnWidth(j, 300)  # 设置列宽
                tableWidget.setItem(i, j + 1, QTableWidgetItem(str(table_data[i][j])))
            else:
                tableWidget.setItem(i, j + 1, QTableWidgetItem(str(table_data[i][j])))

        tableWidget.setRowHeight(i, 140)  # 设置行高

        Combobox = QComboBox()
        Combobox.addItems(["正在修读", "可以修读", "未修读", "不可修读"])
        Combobox.setCurrentIndex(1)
        tableWidget.setCellWidget(i, 0, Combobox)
    # tableWidget.resizeRowsToContents()  # 设置行高随内容改变
    # tableWidget.resizeColumnsToContents()  # 设置列宽随内容改变
    tableWidget.setAlternatingRowColors(True)  # 斑马线
    tableWidget.horizontalHeader().setStretchLastSection(True)  # 最后一列填满表格
    tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)  # 设置编辑模式=不可编辑
    # tableWidget.sortItems(0, Qt.SortOrder.DescendingOrder)  # 降序 0列,A为升序
    # tableWidget.setSpan(0, 0, 2, 2)  # 合并单元格
    print(row, column)
    ui.show()
    sys.exit(app.exec())
