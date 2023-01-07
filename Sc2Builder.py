import sys
import error
import os
import json
import shelve
from engine import *
from unit import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *

#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

VERSION = 1.3

def SecondToStr(sec):
    m = sec // 60
    sec -= 60*m
    return "%02d : %02d"%(m,sec)

#format list of missing items to string
def listToString(errorMessage):
    if type(errorMessage) == list:
        errorMessage = '\n'.join(errorMessage)
    return errorMessage

def IconPath(name, race):
    path = 'jpgFiles/' + race
    if os.path.exists(path):
        path = 'jpgFiles/' + race
    elif os.path.exists('../../jpgFiles'):
        path = '../../jpgFiles'
    else:
        return error.NoPathExists

    for root, dirs, files in os.walk(path):
        if name+".jpg" in files:
            return os.path.join(root, name)+".jpg"
        if name+".png" in files:
           return os.path.join(root, name)+".png"
        if name+".gif" in files:
            return os.path.join(root, name)+".gif"
    return error.NoPathExists

class sc2buildUI(QMainWindow):
    def __init__(self, race, filename=''):
        super().__init__()
        self.race = race
        self.savefilename = filename
        self.cursor = 0
        self.inputNo = []
        self.engine = Engine(race)
        self.initUI()
        self.autoscrollOption = True

# initialize main interface
    def initUI(self):
        #self.setFixedSize(1330,760)
        self.setMinimumSize(1400,840)
        self.center()
        self.setWindowTitle('sc2builder')

        #smaller font to test column spacing
        #testFont = QFont()
        #testFont.setPointSize(5)
        #self.setFont(testFont)
        
        filename = IconPath('sc2icon', self.race)
        if filename != error.NoPathExists:
            self.setWindowIcon(QIcon(filename))

        menu = self.menuBar()
        # this works on for several kinds of OS
        menu.setNativeMenuBar(False)

        menu_file = menu.addMenu('File')

        menu_file_new = QMenu('New',self)
        menu_file_new_protoss = QAction('Protoss SC2',self)
        #menu_file_new_protoss.setShortcut('Ctrl+P')
        menu_file_new_protoss.triggered.connect(lambda state,x='protoss':self.NewWindow(x))
        menu_file_new_terran = QAction('Terran SC2',self)
        #menu_file_new_terran.setShortcut('Ctrl+T')
        menu_file_new_terran.triggered.connect(lambda state,x='terran':self.NewWindow(x))
        menu_file_new_zerg = QAction('Zerg SC2',self)
        #menu_file_new_zerg.setShortcut('Ctrl+Z') CTRL Z is commonly used for undo command
        menu_file_new_zerg.triggered.connect(lambda state,x='zerg':self.NewWindow(x))
        
        #additional menu items for Brood War
        menu_file_new_protossBW = QAction('Protoss BW',self)
        menu_file_new_protossBW.triggered.connect(lambda state,x='protossBW':self.NewWindow(x))
        menu_file_new_terranBW = QAction('Terran BW',self)
        menu_file_new_terranBW.triggered.connect(lambda state,x='terranBW':self.NewWindow(x))
        menu_file_new_zergBW = QAction('Zerg BW',self)
        menu_file_new_zergBW.triggered.connect(lambda state,x='zergBW':self.NewWindow(x))
        
        menu_file_new.addAction(menu_file_new_protoss)
        menu_file_new.addAction(menu_file_new_terran)
        menu_file_new.addAction(menu_file_new_zerg)

        menu_file_new.addAction(menu_file_new_protossBW)
        menu_file_new.addAction(menu_file_new_terranBW)
        menu_file_new.addAction(menu_file_new_zergBW)
        menu_file.addMenu(menu_file_new)

        menu_file_open = QAction('Open',self)
        menu_file_open.setShortcut('Ctrl+O')
        menu_file_open.triggered.connect(self.Open)
        menu_file.addAction(menu_file_open)

        menu_file_save = QAction('Save',self)
        menu_file_save.setShortcut('Ctrl+S')
        menu_file_save.triggered.connect(self.Save)
        menu_file.addAction(menu_file_save)

        menu_file_saveas = QAction('Save As',self)
        menu_file_saveas.setShortcut('Ctrl+A')
        menu_file_saveas.triggered.connect(self.SaveAs)
        menu_file.addAction(menu_file_saveas)

        menu_file_exit = QAction('Exit',self)
        #menu_file_exit.setShortcut('Ctrl+X')
        menu_file_exit.triggered.connect(self.close)
        menu_file.addAction(menu_file_exit)

        menu_view = menu.addMenu('View')
        menu_view_autoscroll = QAction('Autoscroll', self, checkable=True)
        menu_view_autoscroll.setStatusTip('Autoscroll table as units are built')
        menu_view_autoscroll.setChecked(True)
        menu_view_autoscroll.triggered.connect(self.AutoscrollToggle)
        menu_view.addAction(menu_view_autoscroll)

        menu_help = menu.addMenu('Help')
        menu_help_about = QAction('About',self)
        menu_help_about.setShortcut('Ctrl+H')
        menu_help_about.triggered.connect(self.About)
        menu_help.addAction(menu_help_about)
        
        self.label = QLabel(self)
        self.label.move(980,15)
        self.label.resize(450,60)

        self.label2 = QLabel(self)
        self.label2.move(1190,20)
        self.label2.resize(200,200)

        self.inputTable = QTableWidget(self)
        self.inputTable.resize(960, 80)
        self.inputTable.move(10,40)
        self.inputTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.inputTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inputTable.horizontalHeader().hide()
        self.inputTable.verticalHeader().hide()
        self.inputTable.setRowCount(1)
        self.inputTable.setRowHeight(0,40)
        self.inputTable.setIconSize(QSize(40, 40))
        self.inputTable.cellDoubleClicked.connect(self.eraseInputItem)
        #self.inputTable.setAutoScroll(True)
        

        self.board = QTableWidget(self)
        self.board.resize(960,600)
        self.board.move(10,120)
        self.board.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.board.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.board.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.board.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.board.horizontalHeader().hide()
        self.board.horizontalHeader().setMinimumSectionSize(1) #required for windows users to have smaller than 20px columns
        
        self.board.verticalHeader().hide()
        self.board.setColumnCount(10000) #10000 default
        self.board.setRowCount(50)
        for i in range(self.board.columnCount()):
            self.board.setColumnWidth(i,5)
        for i in range(self.board.rowCount()):
            self.board.setRowHeight(i,50)
        self.board.horizontalScrollBar().valueChanged.connect(self.moveCursor)
        self.board.cellActivated.connect(self.enterCell)
        self.board.cellEntered.connect(self.enterCell)
        self.board.cellDoubleClicked.connect(self.eraseItem)
        #self.board.setAutoScroll(True)

        #change background of every 60 columns to denote a minute
        for i in range(self.board.columnCount()):
            if i % 60 == 0:
                for j in range(self.board.rowCount()):
                    self.board.setItem(j, i, QTableWidgetItem (""))
                    self.board.item(j, i).setBackground(QColor(140,140,140))

        #moveable cursor 
        self.cursorLine = QWidget(self.board)
        self.cursorLine.setStyleSheet("background-color: rgb(0,0,0)")
        self.cursorLine.resize(2,600)
        self.cursorLine.move(0,0)

        self.unitList = QTableWidget(self)
        self.unitList.resize(200, 313)
        self.unitList.move(1190, 180)
        self.unitList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.unitList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.unitList.horizontalHeader().hide()
        self.unitList.verticalHeader().hide()
        self.unitList.setColumnCount(1)
        self.unitList.setRowCount(50)
        self.unitList.setColumnWidth(0, 195)

        self.buildingList = QTableWidget(self)
        self.buildingList.resize(200, 313)
        self.buildingList.move(1190, 513)
        self.buildingList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.buildingList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.buildingList.horizontalHeader().hide()
        self.buildingList.verticalHeader().hide()
        self.buildingList.setColumnCount(1)
        self.buildingList.setRowCount(50)
        self.buildingList.setColumnWidth(0, 195)

        self.unitButton = []
        self.buildingButton = []
        self.upgradeButton = []
        self.mineralButton = QPushButton(self)
        self.gasButton = QPushButton(self)
        self.scoutButton = QPushButton(self)
        self.mineralButton.resize(40,40) #default 30
        self.gasButton.resize(40,40) #default 30
        self.scoutButton.resize(40,40) #default 30
        self.mineralButton.move(980, 85)
        self.gasButton.move(1020,85) #default 1010
        self.scoutButton.move(1060,85)
        filename = IconPath('mineral', self.race)
        if filename != error.NoPathExists:
            self.mineralButton.setIcon(QIcon(filename))
        self.mineralButton.setIconSize(QSize(38,38)) #default 28
        filename = IconPath('gas', self.race)
        if filename != error.NoPathExists:
            self.gasButton.setIcon(QIcon(filename))
        self.gasButton.setIconSize(QSize(38,38)) #default 28
        filename = IconPath('scouting', self.race)
        if filename != error.NoPathExists:
            self.scoutButton.setIcon(QIcon(filename))
        self.scoutButton.setIconSize(QSize(38,38)) #default 28
        self.mineralButton.clicked.connect(lambda: self.gatherMineral())
        self.mineralButton.setToolTip("Move worker from gas to minerals")
        self.gasButton.clicked.connect(lambda: self.gatherGas())
        self.gasButton.setToolTip("Move worker from minerals to gas")
        self.scoutButton.clicked.connect(lambda: self.gatherScout())
        self.scoutButton.setToolTip("Move worker from minerals to scouting")

        #2 buttons next to minerals, gas, and scout
        self.skillButton = []
        for x in range(2):
            self.skillButton.append(QPushButton(self))
            self.skillButton[-1].resize(40,40)
            self.skillButton[-1].move(1100+40*x, 85) #default +30
            self.skillButton[x].clicked.connect(lambda state, xx = x: self.useSkill(xx))
        if self.race == "protoss":
            filename = IconPath('chronoboost', self.race)
            if filename != error.NoPathExists:
                self.skillButton[0].setIcon(QIcon(filename))
            self.skillButton[0].setIconSize(QSize(38,38)) #default 28
        if self.race == "zerg":
            filename = IconPath('spawnlarva', self.race)
            if filename != error.NoPathExists:
                self.skillButton[0].setIcon(QIcon(filename))
            self.skillButton[0].setIconSize(QSize(38,38)) #default 28
        if self.race == "terran":
            filename = IconPath('mule', self.race)
            if filename != error.NoPathExists:
                self.skillButton[0].setIcon(QIcon(filename))
            self.skillButton[0].setIconSize(QSize(38,38)) #default 28
        
        #unit table
        unit_ = list(unit_dict['unit'][self.race].items())
        if len(unit_) < 20:
            unitLength = 4
        elif len(unit_) < 25:
            unitLength = 5
        else:
            unitLength = 6
        for y in range(unitLength):
            for x in range(5):
                self.unitButton.append(QPushButton(self))
                self.unitButton[-1].resize(40,40)
                self.unitButton[-1].move(980+40*x,125+40*y) #default +30
                self.unitButton[-1].clicked.connect(lambda state,i=5*y+x: self.unitBuild(i))
        for i in range(len(unit_)):
            filename = IconPath(unit_[i][0], self.race)
            if filename == error.NoPathExists:
                continue
            if type(filename) == type(""):
                self.unitButton[unit_[i][1]['no']].setIcon(QIcon(filename))
                self.unitButton[unit_[i][1]['no']].setIconSize(QSize(38,38)) #default 28
                self.unitButton[unit_[i][1]['no']].setToolTip(str(unit_[i][0] + "\n m: " + str(unit_[i][1]['mineral']) + "\n g: " + str(unit_[i][1]['gas']) + "\n s: " + str(unit_[i][1]['supply']) + "\n t: " + str(unit_[i][1]['buildtime'])))
        
        #building table
        if unitLength <= 4:
            buildingOffset = 285
        elif unitLength == 5:
            buildingOffset = 335
        else:
            buildingOffset = 375
        building_ = list(unit_dict['building'][self.race].items())
        
        if len(building_) < 25:
            buildingLength = 5
        else:
            buildingLength = 6
        for y in range(5):
            for x in range(5):
                self.buildingButton.append(QPushButton(self))
                self.buildingButton[-1].resize(40,40)
                self.buildingButton[-1].move(980+40*x,buildingOffset+40*y) #default +30
                self.buildingButton[-1].clicked.connect(lambda state,i=5*y+x: self.structureBuild(i))
        for i in range(len(building_)):
            filename = IconPath(building_[i][0], self.race)
            if filename == error.NoPathExists:
                continue
            if type(filename) == type(""):
                self.buildingButton[building_[i][1]['no']].setIcon(QIcon(filename))
                self.buildingButton[building_[i][1]['no']].setIconSize(QSize(38,38)) #default 28
                self.buildingButton[building_[i][1]['no']].setToolTip(str(building_[i][0] + "\n m: " + str(building_[i][1]['mineral']) + "\n g: " + str(building_[i][1]['gas']) + "\n t: " + str(building_[i][1]['buildtime'])))

        #upgrade table
        if unitLength <= 4:
            upgradeOffset = 495
        elif unitLength == 5:
            upgradeOffset = 545
        else:
            upgradeOffset = 585
        upgrade_ = list(unit_dict['upgrade'][self.race].items())
        if len(upgrade_) >= 36:
            upgradeRange = 8
        elif len(upgrade_) >= 31:
            upgradeRange = 7
        else:
            upgradeRange = 6
        for y in range(upgradeRange):
            for x in range(5):
                self.upgradeButton.append(QPushButton(self))
                self.upgradeButton[-1].resize(40,40)
                self.upgradeButton[-1].move(980+40*x,upgradeOffset+40*y) #default +30
                self.upgradeButton[-1].clicked.connect(lambda state,i=5*y+x: self.upgradeBuild(i))
        for i in range(len(upgrade_)):
            filename = IconPath(upgrade_[i][0], self.race)
            if filename == error.NoPathExists:
                continue
            if type(filename) == type(""):
                self.upgradeButton[upgrade_[i][1]['no']].setIcon(QIcon(filename))
                self.upgradeButton[upgrade_[i][1]['no']].setIconSize(QSize(38,38)) #default 28
                self.upgradeButton[upgrade_[i][1]['no']].setToolTip(str(upgrade_[i][0] + "\n m: " + str(upgrade_[i][1]['mineral']) + "\n g: " + str(upgrade_[i][1]['gas']) + "\n t: " + str(upgrade_[i][1]['buildtime'])))

        self.show()

#toggle autoscroll variable
    def AutoscrollToggle(self, state):
        
        if state:
            self.autoscrollOption = True
        else:
            self.autoscrollOption = False

# move the window to the center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
#menu items
    def Save(self):
        if self.savefilename == "":
            self.SaveAs()
        else:
            with open(self.savefilename, 'w') as f:
                f.write(str(VERSION)+"\n")
                f.write(self.race+"\n")
                json.dump(self.engine.input,f)
#save as
    def SaveAs(self):
        savefilename = QFileDialog.getSaveFileName(self, 'Save File', '.', '*.s2b')
        if savefilename[0]:
            if len(savefilename[0]) < 5 or savefilename[0][-4:] != '.s2b':
                self.savefilename = savefilename[0] + '.s2b'
            else:
                self.savefilename = savefilename[0]
            self.Save()
#menu open
    def Open(self):
        savefilename = QFileDialog.getOpenFileName(self, 'Open File', '.', '*.s2b')
        if savefilename[0]:
            self.savefilename = savefilename[0]
            with open(self.savefilename, 'r') as f:
                text = f.readlines()
                if len(text)<3:
                    err = error.WrongFileFormat
                    errmsg = error.ErrorMsg(err)
                    msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                    return err

                if text[0]:
                    try:
                        version = float(text[0])
                    except ValueError:
                        err = error.WrongFileFormat
                        errmsg = error.ErrorMsg(err)
                        msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                        return err
                    if version > VERSION or version<1.0:
                        err = error.IncompatibleVersion
                        errmsg = error.ErrorMsg(err)
                        msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                        return err
                else:
                    err = error.WrongFileFormat
                    errmsg = error.ErrorMsg(err)
                    msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                    return err

                if version == 1.0:
                    if text[1]:
                        race = text[1]
                        race = race[:-1]
                        if race not in ["protoss","terran","zerg"]:
                            err = error.WrongRace
                            errmsg = error.ErrorMsg(err)
                            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                            return err
                    else:
                        err = error.WrongFileFormat
                        errmsg = error.ErrorMsg(err)
                        msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                        return err

                    if text[2]:
                        newinput = json.loads(text[2])
                    else:
                        err = error.WrongFileFormat
                        errmsg = error.ErrorMsg(err)
                        msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                        return err

                    self.close()
                    newMD = sc2buildUI(race,self.savefilename)
                    newMD.engine.input = newinput
                    err, missingpreReq = newMD.engine.Rearrange()

                    if err < 0:
                        errmsg = error.ErrorMsg(err)
                        msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                        return err
                    else:
                        newMD.drawBoard()
                        newMD.newCursor(err)
                        return newMD.cursor
        return 0
#menu new window
    def NewWindow(self, race, filename=''):
        self.storeShelf(race)
        self.close()
        newMD = sc2buildUI(race)
#menu about
    def About(self):
        msg = QMessageBox.information(self,"About...",\
            "sc2builder version: " + str(VERSION) +\
            "\nMade by 민병욱(Min Byeonguk)\n"+\
            "contact me : phraust1612@gmail.com\n"+\
            "https://github.com/phraust1612\n"\
            "Updated by StarkTemplar\n"+\
            "https://github.com/StarkTemplar/starcraftbuilder",\
            QMessageBox.Ok, QMessageBox.Ok)

# called when scroller moved (event)
    def moveCursor(self):
        HScroll = self.board.horizontalScrollBar().value()
        self.cursorLine.move(5*(self.cursor - HScroll), 0)

# order a worker to gather minerals who used to mine gases
    def gatherMineral(self):
        self.engine.AddItem("mineral", "mineral")
        err, missingpreReq = self.engine.Rearrange()
        if err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err

        self.drawBoard()
        return 0

# order a worker to gather gases who used to mine minerals
    def gatherGas(self):
        self.engine.AddItem("gas", "gas")
        err, missingpreReq = self.engine.Rearrange()
        if err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err

        self.drawBoard()
        self.newCursor(err)
        return 0

# order a worker to scout who used to mine minerals
    def gatherScout(self):
        self.engine.AddItem("scout", "scout")
        err, missingpreReq = self.engine.Rearrange()
        if err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err

        self.drawBoard()
        self.newCursor(err)
        return 0

#use special skill
    def useSkill(self,no):
        if self.race == "protoss" and no == 0:
            self.engine.AddItem("chronoboost","skill")
            return 0
        elif self.race == "zerg" and no == 0:
            self.engine.AddItem("spawnlarva","skill")
            err, missingpreReq = self.engine.Rearrange()
            if err < 0:
                errmsg = error.ErrorMsg(err)
                msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                self.engine.DeleteItem(-1)
                return err
        elif self.race == "terran" and no == 0:
            self.engine.AddItem("mule","skill")
            err, missingpreReq = self.engine.Rearrange()
            if err < 0:
                errmsg = error.ErrorMsg(err)
                msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
                self.engine.DeleteItem(-1)
                return err
        self.drawBoard()
        self.newCursor(err)
        return 0

#unitbuild
    def unitBuild(self, no):
        k = unit_dict['unit'][self.race].keys()
        item = 0
        for i in k:
            if unit_dict['unit'][self.race][i]['no'] == no and unit_dict['unit'][self.race][i]['race'] == self.race:
                item = i
                break
        if item == 0:
            # unit doesn't exist
            msg = QMessageBox.warning(self,'error!','Unit does not exist', QMessageBox.Ok, QMessageBox.Ok)
            return error.WrongUnitName

        # do not build larva when button is pressed
        if item == "larva":
            err = error.CannotBuildLarva
        else: #all other items get sent to additem function
            self.engine.AddItem(item, "unit")
            err, missingpreReq = self.engine.Rearrange()
            #format list of missing items to string
            missingpreReq = listToString(missingpreReq)
        
 
        #check for error responses
        if err == error.ConditionNotSatisfied:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing requirements:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err == error.NoBarrackExists:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing target building:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err == error.AlreadyBoosted:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1) #delete most recent unit
            self.engine.DeleteItem(-1) #delete most recent chronoboost
            return err
        elif err == error.ChronoNotAvailable or err == error.ChronoCooldown:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1) #delete most recent unit
            self.engine.DeleteItem(-1) #delete most recent chronoboost
            return err
        elif err == error.CannotBuildLarva:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            return err
        elif err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        else:
            self.drawBoard()
            self.newCursor(err)
            return self.cursor
#structure build
    def structureBuild(self, no):
        k = unit_dict['building'][self.race].keys()
        item = 0
        for i in k:
            if unit_dict['building'][self.race][i]['no'] == no and unit_dict['building'][self.race][i]['race'] == self.race:
                item = i
                break
        
        if item == 0:
            # unit doesn't exist
            msg = QMessageBox.warning(self,'error!','Building does not exist', QMessageBox.Ok, QMessageBox.Ok)
            return error.WrongBuildingName

        # do not build terran addons when button is pressed
        if item in ["barracks tech lab","factory tech lab","starport tech lab"]:
            err = error.CannotBuildAddons
        else: #all other items get sent to additem function
            self.engine.AddItem(item, "building")
            err, missingpreReq = self.engine.Rearrange()

        #format list of missing items to string
        missingpreReq = listToString(missingpreReq)

        if err == error.ConditionNotSatisfied:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing requirements:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err == error.NoBarrackExists:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing target building:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err == error.CannotBuildAddons:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            return err
        elif err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        else:
            self.drawBoard()
            self.newCursor(err)
            return self.cursor
#upgrade build
    def upgradeBuild(self, no):
        k = unit_dict['upgrade'][self.race].keys()
        item = 0
        for i in k:
            if unit_dict['upgrade'][self.race][i]['no'] == no and unit_dict['upgrade'][self.race][i]['race'] == self.race:
                item = i
                break
        if item == 0:
            # unit doesn't exist
            msg = QMessageBox.warning(self,'error!','Upgrade doesn\'t exist', QMessageBox.Ok, QMessageBox.Ok)
            return error.WrongUpgradeName

        self.engine.AddItem(item, "upgrade")
        err, missingpreReq = self.engine.Rearrange()

        #format list of missing items to string
        missingpreReq = listToString(missingpreReq)

        if err == error.ConditionNotSatisfied:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing requirements:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err == error.NoBarrackExists:
            #errmsg = error.ErrorMsg(err)
            errmsg = "Check if you are missing target building:\n" + missingpreReq
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        elif err < 0:
            errmsg = error.ErrorMsg(err)
            msg = QMessageBox.warning(self,'error!',errmsg, QMessageBox.Ok, QMessageBox.Ok)
            self.engine.DeleteItem(-1)
            return err
        else:
            self.drawBoard()
            self.newCursor(err)
            return self.cursor
#draw board function
    def drawBoard(self):
        self.board.clearSpans()
        self.inputTable.clearSpans()

        storedColumn = 0

        # draw inputTable items
        self.inputTable.setColumnCount(len(self.engine.input))
        for i in range(len(self.engine.input)):
            self.inputTable.setColumnWidth(i, 40)
            filename = IconPath(self.engine.input[i][0], self.race)
            if filename == error.NoPathExists:
                continue
            if type(filename) == type(""):
                self.inputTable.setItem(0, i, QTableWidgetItem())
                icon = QIcon(filename)
                self.inputTable.item(0,i).setIcon(icon)

            #store the row number so we can autoscroll horizontal bar
            storedColumn += 1

        #autoscroll inputTable only if setting is true
        if self.autoscrollOption:
            self.inputTable.scrollToItem(self.inputTable.item(0,storedColumn), QAbstractItemView.EnsureVisible)      
            
        # draw items from engine.queue
        # this includes units, buildings, upgrades
        self.inputNo = []
        for item in self.engine.queue:
            if item.state != "start":
                continue
            level = 0
            storedLevel = self.board.columnSpan(level, item.starttime)
            while self.board.columnSpan(level, item.starttime) != 1 or self.board.columnSpan(level, item.endtime) != 1:
                storedLevel = self.board.columnSpan(level, item.starttime)
                level += 1

            self.board.setSpan(level, item.starttime, 1, item.endtime - item.starttime)
            self.board.setItem(level, item.starttime, QTableWidgetItem(item.name))
            self.board.item(level,item.starttime).setToolTip(item.name + "\nstart: " + SecondToStr(item.starttime) + "\nend: " + SecondToStr(item.endtime))
            
            #store the column number so we can autoscroll horizontal bar
            if item.starttime > storedColumn:
                storedColumn = item.starttime

            # for the case of chronoboosted units or upgrades would have blue background color
            # and if it was boosted partially, it gets little lighter blue background
            if item.type == 'unit' or item.type == 'upgrade':
                if item.boosted > 1:
                    self.board.item(level, item.starttime).setBackground(QColor(128,182,255)) #darker blue
                elif item.boosted == 1:
                    self.board.item(level, item.starttime).setBackground(QColor(191,219,255)) #lighter blue
                else:
                    self.board.item(level, item.starttime).setBackground(QColor(255,255,255)) #white
            else:
                self.board.item(level, item.starttime).setBackground(QColor(255,255,255)) #white
            self.inputNo.append( (level, item.starttime, item.inputlink) )

        # draw items from engine.worker for the case of gathering gases/minerals/scouts
        for i in range(len(self.engine.worker.time)):
            #if self.engine.worker.gas[i] == 0:
             #   continue
            
            if self.engine.worker.gas[i] < 0:
                text = "gas"+str(self.engine.worker.gas[i])
            elif self.engine.worker.gas[i] > 0:
                text = "gas+"+str(self.engine.worker.gas[i])
            elif self.engine.worker.scouting[i] > 0:
                text = "scout+"+str(self.engine.worker.scouting[i])
            else:
                continue


            level = 0
            storedLevel = self.board.columnSpan(level, self.engine.worker.time[i])
            while self.board.columnSpan(level, self.engine.worker.time[i]) != 1 or self.board.columnSpan(level, self.engine.worker.time[i]+11) != 1:
                storedLevel = self.board.columnSpan(level, self.engine.worker.time[i])
                level += 1
            self.board.setSpan(level, self.engine.worker.time[i], 1, 16)
            self.board.setItem(level, self.engine.worker.time[i], QTableWidgetItem(text))
            self.board.item(level,self.engine.worker.time[i]).setToolTip(text + "\nstart: " + SecondToStr(self.engine.worker.time[i]))

            #store the column number so we can autoscroll horizontal bar
            if self.engine.worker.time[i] > storedColumn:
                storedColumn = self.engine.worker.time[i]
        
        # draw larva injections for zerg or MULE drops for terran
        if self.race in ["zerg","terran"]:
            for i in self.engine.queue:
                if i.name in ["hatchery","lair","hive","orbital command"] and i.state == 'end':
                    if len(i.secondaryQueue) > 0:
                        for j in i.secondaryQueue:
                            level = 0
                            storedLevel = self.board.columnSpan(level, j.starttime)
                            while self.board.columnSpan(level, j.starttime) != 1 or self.board.columnSpan(level, j.endtime) != 1 or self.board.columnSpan(level, j.starttime + 10) != 1 or self.board.columnSpan(level, j.starttime + 20) != 1 or self.board.columnSpan(level, j.starttime + 30) != 1:
                                storedLevel = self.board.columnSpan(level, j.starttime)
                                level += 1

                            self.board.setSpan(level, j.starttime, 1, j.endtime - j.starttime)
                            self.board.setItem(level, j.starttime, QTableWidgetItem(j.name))
                            self.board.item(level,j.starttime).setToolTip(j.name + "\nstart: " + SecondToStr(j.starttime) + "\nend: " + SecondToStr(j.endtime))
                            self.board.item(level,j.starttime).setBackground(QColor(191,219,255)) #lighter blue

                            #store the column number so we can autoscroll horizontal bar
                            if j.starttime > storedColumn:
                                storedColumn = j.starttime

        #autoscroll board only if setting is true
        if self.autoscrollOption:
            self.board.scrollToItem(self.board.item(0,storedColumn), QAbstractItemView.EnsureVisible)
            


    def eraseItem(self, row, col):
        err = error.NoItemToDelete
        
        #check inputNo array. This contains all units and buildings. Not workers
        for i in self.inputNo:
            if i[0] == row and i[1] == col:
                err = self.engine.DeleteItem(i[2])
                err = err[0]
                break

        # if there was no item clicked, move cursor to there
        if err <0:
            self.newCursor(col)
            self.board.clearSelection()
            return err
        self.board.item(row, col).setBackground(QColor(255,255,255))
        self.newCursor(err)
        self.drawBoard()
        self.board.clearSelection()
        return 0

# call newCursor function when cell is entered to update status
    def enterCell(self, row, col):
        err = error.NoItemToDelete
        self.newCursor(col)
        self.board.clearSelection()
        return err

    def eraseInputItem(self, row, col):
        err = error.NoItemToDelete
        err = self.engine.DeleteItem(col)
        err = err[0]
        if err <0:
            return err
        self.newCursor(err)
        self.drawBoard()
        return 0

# set cursor value and show current status
    def newCursor(self, val):
        self.cursor = val
        HScroll = self.board.horizontalScrollBar().value()
        self.cursorLine.move(5*(self.cursor - HScroll), 0)

        mineral, gas = self.engine.AccResources(self.cursor)
        curSup, maxSup = self.engine.CurrentSupply(self.cursor)
        wMineral = self.engine.countMineralWorkers(self.cursor)
        wGas = self.engine.countGasWorkers(self.cursor)
        wScouting = self.engine.countScoutingWorkers(self.cursor)
        wScouting = self.engine.countScoutingWorkers(self.cursor)
        wBuilding = self.engine.countBuildingWorkers(self.cursor)
        wIdle = self.engine.countDoingNothingWorkers(self.cursor)
        wMule = self.engine.countMules(self.cursor)
        text = "game time: "+SecondToStr(self.cursor)+", mineral: "+str(mineral)+", gas: "+str(gas)+", supply: "+str(curSup)+"/"+str(maxSup)
        self.label.setText(text)
        text = "workers minerals : " + str(wMineral)
        if self.engine.race == 'terran':
            text += "\nMULEs minerals : " + str(wMule)
        text += "\nworkers gas : " + str(wGas)
        text += "\nworkers scouting : " + str(wScouting)
        text += "\nworkers building : " + str(wBuilding)
        text += "\nworkers idle : " + str(wIdle)
        self.label2.setText(text)

        ind = 0
        self.unitList.clearContents() #clear list before entering items
        for i in unit_dict['unit'][self.race]:
            count = self.engine.unitCount(i, self.cursor)
            if count <= 0 and i != "larva": #always show larva count
                continue
            text = i + " : " + str(count)
            self.unitList.setItem(ind, 0, QTableWidgetItem(text))
            ind += 1

        ind = 0
        self.buildingList.clearContents() #clear list before entering items
        for i in unit_dict['building'][self.race]:
            count = self.engine.buildingCount(i, self.cursor, False)
            if count <= 0:
                continue
            text = i + " : " + str(count)
            self.buildingList.setItem(ind, 0, QTableWidgetItem(text))
            ind += 1

#update shelf to store last used race
    def storeShelf(self, lastUsedRace):
        s = shelve.open("sc2builder.config")
        try:
            s['lastUsedRace'] = lastUsedRace
        finally:
            s.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        MD = sc2buildUI(sys.argv[1])
    else:
        s = shelve.open('sc2builder.config')
        try:
            templastUsedRace = s['lastUsedRace']
        except:
            templastUsedRace = ""
            s.close()
        finally:
            s.close()
        
        if templastUsedRace in ["protoss","terran","zerg","protossBW","terranBW","zergBW"]:
            MD = sc2buildUI(templastUsedRace)
        else:
            MD = sc2buildUI('terran') #fallback to terran if shelf has not stored a lastUsedRace
    sys.exit(app.exec_())

