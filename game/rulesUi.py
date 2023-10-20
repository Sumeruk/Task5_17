from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 386)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(-5, -9, 511, 401))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Правила игры"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head"
                                                      "><meta name=\"qrichtext\" content=\"1\" /><style "
                                                      "type=\"text/css\">\n""p, li { white-space: pre-wrap; "
                                                      "}\n""</style></head><body style=\" font-family:\'MS Shell Dlg "
                                                      "2\'; font-size:7.8pt; font-weight:400; "
                                                      "font-style:normal;\">\n""<p style=\" margin-top:0px; "
                                                      "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                      "-qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                                      "font-family:\'-apple-system,BlinkMacSystemFont,Roboto,"
                                                      "Open Sans,Helvetica Neue,Noto Sans Armenian,Noto Sans Bengali,"
                                                      "Noto Sans Cherokee,Noto Sans Devanagari,Noto Sans Ethiopic,"
                                                      "Noto Sans Georgian,Noto Sans Hebrew,Noto Sans Kannada,"
                                                      "Noto Sans Khmer,Noto Sans Lao,Noto Sans Osmanya,"
                                                      "Noto Sans Tamil,Noto Sans Telugu,Noto Sans Thai,sans-serif\'; "
                                                      "font-size:14pt; color:#000000; "
                                                      "background-color:#ffffff;\">Первой выбирается любая клетка, "
                                                      "затем можно выбрать рядом стоящую клетку или клетку через одну, "
                                                      "которая совпадает по цвету или фигуре. Цель - заполнить все "
                                                      "клетки."
                                                      ""
                                                      "Зинченко Константин 2 курс 3 группа ФКН ВГУ"
                                                      "vk.com/rutopa"
                                                      "</span></p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())