from PyQt4 import uic,QtGui,QtCore
import re,copy,math,sys,main_work,report_gui,main_window_gui
from main_work import *


flag_zakrit = 0

def sohranit():
	text_otcheta = window_Analiz_oshibok.text_Errors.toPlainText()
	fail_otcheta = QtGui.QFileDialog.getSaveFileName(Analiz_oshibok, u'Выбор файла', 'D:\\Work\\Диплом\\',"*.txt")
	fail_otcheta = unicode(fail_otcheta)
	fileqq = open(fail_otcheta,"w")
	fileqq.write(text_otcheta)
	global flag_zakrit
	flag_zakrit = 1
	
	
def viborFaila():
        window_Analiz_oshibok.text_Errors.clear()
        fail_dlia_analiza = QtGui.QFileDialog.getOpenFileName(Glavnoe_Okno, u'Выбор файла', 'D:\\Work\\Диплом\\',"*.c;*.cpp")
        fail_dlia_analiza = unicode(fail_dlia_analiza)
        if fail_dlia_analiza.endswith(".c") or  fail_dlia_analiza.endswith(".cpp"):
                if fail_dlia_analiza != u"":
                        fileqq=open(fail_dlia_analiza)
                        codee = fileqq.read()
                        rezultat = Main_function(codee)	
                        Analiz_oshibok.show()
                        textt = ""
                        for j in rezultat:
                                textt+=j
                        window_Analiz_oshibok.text_Errors.insertPlainText(textt)
                        return True
	else:
		QtGui.QMessageBox.critical(Glavnoe_Okno,u"Ошибка",u"Файл не выбран"
                        ,buttons = QtGui.QMessageBox.Ok,defaultButton =  QtGui.QMessageBox.Ok)

def vihod():
	sys.exit(app.exec_())


def zakrit():
	global flag_zakrit
	if flag_zakrit != 1:
		
		rez = QtGui.QMessageBox.warning(Analiz_oshibok,u"Отчет не сохранен",u"Отчет не сохранен. Хотите ли вы сохранить отчет?"
                        ,buttons = QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,defaultButton =  QtGui.QMessageBox.Yes)
		if rez == QtGui.QMessageBox.Yes:
			sohranit()
			Analiz_oshibok.close()
			flag_zakrit = 0
		else:
			Analiz_oshibok.close()
			flag_zakrit = 0
	else:	
		Analiz_oshibok.close()
		flag_zakrit = 0

app = QtGui.QApplication(sys.argv)
Glavnoe_Okno = QtGui.QWidget()
window_Glavnoe_Okno = main_window_gui.Ui_Dialog()
window_Glavnoe_Okno.setupUi(Glavnoe_Okno)

Analiz_oshibok = QtGui.QWidget()
window_Analiz_oshibok = report_gui.Ui_Dialog()
window_Analiz_oshibok.setupUi(Analiz_oshibok)

#Glavnoe_Okno.setupUi(QtGui.QWidget)
#Analiz_oshibok = QtGui.QWidget()
#ui1 = main_windows.Ui_Dialog.setupUi(Glavnoe_Okno)
#ui2 = report.setupUi(Analiz_oshibok)
#Glavnoe_Okno = uic.loadUi("1.ui")
#Glavnoe_Okno = main_windows.setupUI()
#Analiz_oshibok = uic.loadUi("2.ui")

directory = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)

translator = QtCore.QTranslator()
translator.load(u'qt_ru', u'C:\\Python27\\PyQt4\\translations') #как я понял, расширение файла (.qm) Qt сам добавит?
app.installTranslator(translator)
 
Glavnoe_Okno.show()
rezz = QtCore.QObject.connect(window_Glavnoe_Okno.Button_Vibor_Faila,QtCore.SIGNAL("clicked()"),viborFaila)
rezz  = QtCore.QObject.connect(window_Glavnoe_Okno.Button_Exit,QtCore.SIGNAL("clicked()"),vihod)
rezz  = QtCore.QObject.connect(window_Analiz_oshibok.Button_OK,QtCore.SIGNAL("clicked()"),zakrit)
rezz  = QtCore.QObject.connect(window_Analiz_oshibok.Button_Sohranit,QtCore.SIGNAL("clicked()"),sohranit)
sys.exit(app.exec_())
