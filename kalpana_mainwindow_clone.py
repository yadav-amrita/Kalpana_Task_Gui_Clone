# TAB - QWidget, QPushButton, QTabWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QMainApplication, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTabWidget, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtCore import QTimer, Qt
from kalpana_graph_clone import tab1
#from kalpana_telemetry import Tab2
#from kalpana_map import Tab3
#from kalpana_telecast import Tab4

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setWindowTitle("Main Window for all the Tabs")
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("""
            QMainWindow{background-color:qlineargradient(
                    x1: 0,y1: 0,x2: 1,y2: 1,
                    stop:0 #030303,stop:1 #9370DB
                 );
            }
        """)
        
        self.widget1 = QWidget(self)
        self.widget2 = QWidget(self)
        self.widget3 = QWidget(self)
        
        self.widget1.setGeometry(0, 0, 1920, 160)
        self.widget1.setStyleSheet("background-color: #0A1172;")
        self.layout1 = QHBoxLayout(self.widget1)
        header_style_sheet = """QLabel{font-size:'60px';color:'#C2D8D3';background-color:'#0A1172';font-weight: bold;}"""
        header_input_style = """QLabel{font-size:'40px';color:'black';background-color:'white';font-weight: bold;
        border: 2px solid #7C0A02; border-radius:10%;}"""
        
        self.logo_label = QLabel(self.widget1)
        logo_image = QPixmap("Kalpana_Task_Gui_Clone\\Add Ons\\Team Kalpana Logo 1.png").scaledToWidth(80,Qt.TransformationMode.SmoothTransformation)
        self.logo_label.setPixmap(logo_image)
        self.logo_label.setGeometry(770,90,80,74)
        
        
        self.label1 = QLabel(self)
        self.label1.setText("SOFTWARE STATE")
        self.label1.setFixedSize(200, 10)
        self.label1.setStyleSheet(header_style_sheet)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label1_input = QLabel("0", self.widget1)
        self.label1_input.setGeometry(250,94,100,30)
        self.label1_input.setStyleSheet(header_input_style)
        
        self.label2 = QLabel(self)
        self.label2.setText("TEAM KALPANA:2024-CANSAT-ASI-023")
        self.label2.setFixedSize(400, 10)
        self.label2.setStyleSheet(header_style_sheet)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3 = QLabel(self)
        
        self.label3.setText("PACKET COUNT")
        self.label3.setFixedSize(100,10)
        self.label3.setStyleSheet(header_style_sheet)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label3_input = QLabel("0", self.widget1)
        self.label3_input.setGeometry(1214,94,90, 30)
        self.label3_input.setStyleSheet(header_input_style)
        
        self.label4 = QLabel(self)
        self.label4.setText("TIME")
        self.label4.setFixedSize(200,10)
        self.label4.setStyleSheet(header_style_sheet)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)   
        
        self.label4_input = QLabel("0", self.widget1)
        self.label4_input.setGeometry(1598,94,70, 30)
        self.label4_input.setStyleSheet(header_input_style)     
        
        self.widget1.setLayout(self.layout1)
        
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.label2)
        self.layout1.addWidget(self.label3)
        self.layout1.addWidget(self.label4)
        
        self.widget2.setGeometry(0, 160, 1840, 750)
        self.widget2.setStyleSheet("background-color:None;")
        
        self.tabwidget = QTabWidget(self.widget2)
        self.tabwidget.setGeometry(60, 20, 1920, 1080)

        self.tabwidget.setStyleSheet("""
        QTabWidget::pane{
            background-color: None;
        }
        QTabBar::tab{
            font-size: 20px; 
            font-family: Arial; 
            color: black; 
            border: 4px solid black; 
            border-radius: 30px;
            background-color: #82EEFD;
            padding: 10px 20px;
            margin: 5px;
            min-width: 390px; 
            min-height: 40px;
        }
        QTabBar::tab:hover{
            border: 4px solid black; 
            border-radius: 30px;
            background-color:Gray;
        }
        QTabBar::tab:selected{
            background-color:Gray;
            border-radius: 30px;
            border: 0px solid None;  
        }
        """)      
        
       

        # Create Tabs
        #self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        
        # Add tabs to the QTabWidget
        #self.tabwidget.addTab(self.tab1, "Graphs")
        self.tabwidget.addTab(tab1(), "Graphs")
        self.tabwidget.addTab(self.tab2, "Telemetry Data")
        self.tabwidget.addTab(self.tab3, "Map And 3-D Plotting")
        self.tabwidget.addTab(self.tab4, "Live Telecast")
        
        self.widget3.setGeometry(0, 915, 1920, 80)
        self.widget3.setStyleSheet('''background-color:None;''')
        self.layout3 = QHBoxLayout(self.widget3)

        def display_button1(self):
            print("ON/OFF command executed")
            
        def display_button2(self):
            print("Boot command enable")
            
        def display_button3(self):
            print("Calibrate command is enabled")
            
        def display_button4(self):
            print("Sim Enable command received")
            
        def display_button5(self):
            print("Sim Disabled successfully")
            
        def display_button6(self):
            print("Sim Activated successfully")
            
        def display_button7(self):
            print("CX command executed")
            
        def display_button8(self):
            print("Set Time command enabled successfully")
         
        footer_button_style = """
            QPushButton{
                font-size: 20px; 
                font-family: Arial; 
                color: orange; 
                border: 4px solid black; 
                border-radius: 10px;
                background-color:qlineargradient(
                    x1: 0,y1: 0,x2: 1,y2: 1,
                    stop:0 #00308F,stop:1 #00CED1
                );
                padding : 0px 20px;
            }
            
            QPushButton:hover{
                border: 4px solid black; 
                border-radius: 10px;
                background-color:qlineargradient(
                    x1: 0,y1: 0,x2: 1,y2: 1,
                    stop:0 #00CED1,stop:1 #004F98
                );
            }
            
            QPushButton:pressed{
                background-color:qlineargradient(
                    x1: 0,y1: 0,x2: 1,y2: 1,
                    stop:0 #00CED1,stop:1 #004F98
                );
                border-radius: 0px;
                border: 0px solid None; 
            }
        """

                                      
        button1 = QPushButton("ON/OFF", self.widget3)
        button1.clicked.connect(display_button1)
        button1.setStyleSheet(footer_button_style)
        button1.setFixedSize(200,40)
        self.layout3.addWidget(button1)
        
        button2 = QPushButton("BOOT", self.widget3)
        button2.clicked.connect(display_button2)
        button2.setFixedSize(200,40)
        button2.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button2)
        
        button3 = QPushButton("CALIBRATE", self.widget3)
        button3.clicked.connect(display_button3)
        button3.setFixedSize(200,40)
        button3.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button3)
        
        button4 = QPushButton("SIM ENABLE", self.widget3)
        button4.clicked.connect(display_button4)
        button4.setFixedSize(200,40)
        button4.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button4)
        
        button5 = QPushButton("SIM DISABLE", self.widget3)
        button5.clicked.connect(display_button5)
        button5.setFixedSize(200,40)
        button5.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button5)
        
        button6 = QPushButton("SIM ACTIVATE", self.widget3)
        button6.clicked.connect(display_button6)
        button6.setFixedSize(200,40)
        button6.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button6)
        
        button7 = QPushButton("CX", self.widget3)
        button7.clicked.connect(display_button7)
        button7.setFixedSize(200,40)
        button7.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button7)
        
        button8 = QPushButton("SET TIME", self.widget3)
        button8.clicked.connect(display_button8)
        button8.setFixedSize(200,40)
        button8.setStyleSheet(footer_button_style)
        self.layout3.addWidget(button8)
        
        
if __name__ == '__main__':
    win = QApplication(sys.argv)
    ex = window()
    sys.exit(win.exec())