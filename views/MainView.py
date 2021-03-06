from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QMessageBox
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from views.mainUi import Ui_MainWindow
import sys

class MainView(QMainWindow):

    #Property
    __app = None
    __mainWindow = None
    __controller = None
    __model = None
    __ui = None
    __scene = None
    __redBrush = QBrush(Qt.red)
    __blueBrush = QBrush(Qt.blue)
    __blackPen = QPen(Qt.black)
    __blackPen.setWidth(1)
    __elevatorObj = []
    __passenger_txt = []

    def __init__(self, model, controller):
        super().__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__scene = QGraphicsScene()
        self.__ui.display_view.setScene(self.__scene)

        # connect widgets to controllers
        self.__ui.startBtn.clicked.connect(self.__controller.startClick)
        self.__ui.pauseBtn.clicked.connect(self.__controller.pauseClick)
        self.__ui.stopBtn.clicked.connect(self.__controller.stopClick)
        self.__ui.actionClose.triggered.connect(self.__controller.windowExit)
        self.__ui.actionAbout_us.triggered.connect(self.__controller.aboutUs)

        # listen to model event signals
        self.__model.startBtn_changed.connect(self.startBtnClicked)
        self.__model.pauseBtn_changed.connect(self.pauseBtnClicked)
        self.__model.stopBtn_changed.connect(self.stopBtnClicked)
        self.__model.windowExit_changed.connect(self.close)
        self.__model.aboutUs_changed.connect(self.about)
        self.__model.moveElevator_changed.connect(self.moveE)
    
    @pyqtSlot(int, int)
    def moveE(self, id, value):
        maxHeight = self.__ui.display_view.height() - 20
        nFloor = int(self.__ui.nFloor.currentText())
        if value > 0:
            self.__elevatorObj[id].moveBy(0, -maxHeight//nFloor)
        else:
            self.__elevatorObj[id].moveBy(0, maxHeight//nFloor)
    
    @pyqtSlot(bool)
    def startBtnClicked(self, value):
        #if(self.__ui.inputMax.text() == ""): return
        nElevator = int(self.__ui.nElevator.currentText())
        nFloor = int(self.__ui.nFloor.currentText())
        temp = 0
        temp2 = 0
        maxWidth = self.__ui.display_view.width() - 20
        maxHeight = self.__ui.display_view.height() - 20
        # Vertical lines
        for i in range(1, 4+nElevator):
            self.__scene.addLine(temp, 0, temp, maxHeight)
            if i < 3:
                temp2 += (maxWidth//nElevator)//4
                temp = temp2
            else:
                temp += (maxWidth-temp2)//nElevator
                if i < nElevator+3:
                    rect = self.__scene.addRect(temp - (maxWidth-temp2)//nElevator, maxHeight-(maxHeight//nFloor), (maxWidth-((maxWidth//nElevator)//2))//nElevator, maxHeight//nFloor, self.__blackPen, self.__redBrush)
                    rect.setFlag(QGraphicsItem.ItemIsMovable)
                    txt = self.__scene.addText("E{}\nUp: 0, Down: 0".format(i-2))
                    txt.setPos(temp - maxWidth//nElevator + (maxWidth//nElevator)//4, maxHeight-(maxHeight//nFloor))
                    txt.setParentItem(rect)
                    self.__elevatorObj.append(rect)
        temp = 0
        # Horizontal lines
        for i in range(1, 2+nFloor):
            if i < nFloor+1:
                txt = self.__scene.addText("F: {}".format(nFloor+1 - i))
                txt.setPos(maxWidth//nElevator//4//4, temp + maxHeight//nFloor//2)
                txt_pass = self.__scene.addText("P: 0")
                txt_pass.setPos(maxWidth//nElevator//4, temp + maxHeight//nFloor//2)
                self.__passenger_txt.insert(0, txt_pass)
            self.__scene.addLine(0, temp, maxWidth, temp)
            temp += maxHeight//nFloor 
        #old_text = self.__ui.inputMax.text()
        #self.__ui.inputMax.setText(old_text + "Clicked!")
        self.__ui.inputMax.setReadOnly(True) 
        self.__ui.inputLambda.setReadOnly(True) 
        self.__ui.inputFrom.setReadOnly(True) 
        self.__ui.inputTo.setReadOnly(True) 
        self.__ui.nFloor.setEnabled(False) 
        self.__ui.nElevator.setEnabled(False) 
        self.__ui.nDinning.setEnabled(False) 

    @pyqtSlot(bool)
    def pauseBtnClicked(self, value):
        maxHeight = self.__ui.display_view.height() - 20
        nFloor = int(self.__ui.nFloor.currentText())
        #self.__ui.inputMax.setText(str(item_lst[0]))
        #item_lst[0].setBrush(self.__blueBrush)
        #self.__elevatorObj[0].childItems()[0].setPlainText("test")
        #self.__passenger_txt[2].setPlainText("P.S.G:\n2")
        self.__elevatorObj[0].moveBy(0, -maxHeight//nFloor)
        #item_lst[0].setRect(new_x, new_y, 200, 200)

    @pyqtSlot(bool)
    def stopBtnClicked(self, value):
        self.__ui.inputMax.setReadOnly(False) 
        self.__ui.inputLambda.setReadOnly(False) 
        self.__ui.inputFrom.setReadOnly(False) 
        self.__ui.inputTo.setReadOnly(False) 
        self.__ui.nFloor.setEnabled(True) 
        self.__ui.nElevator.setEnabled(True) 
        self.__ui.nDinning.setEnabled(True) 

    @pyqtSlot(bool)
    def close(self, value):
        if value:
            QCoreApplication.quit()

    @pyqtSlot(bool)
    def about(self, value):
        memberLst = """
                                Member\n
            Mr.Kantachat Janya          60090500402\t\t\n
            Mr.Patipon Buason           60090500412\t\t\n
            Mr.Puksanon Posang          60090500413\t\t\n
            Mr.Rawit Praditrungchan     60090500416\t\t\n
            Mr.Wongsakorn Pakinang      60090500420\t\t\n
            Mr.Sanhapas Arunruviwat     60090500450\t\t\n
        """
        QMessageBox.about(self, "Member list", memberLst)