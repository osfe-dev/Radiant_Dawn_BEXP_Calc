from GUI_source import *
from Music_Player import *
from random import randint

# QLineEdit used to set custom starting/ending EXP
class ExpEdit():
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.exp = 0

        # Create exp box
        self.lbl = create_label("Exp", RIGHT, LBL_FONT, HEADING_SZ)
        self.exp_box = create_exp_box()
        self.exp_box.setAlignment(LEFT)
        self.exp_box.textChanged.connect(self.validate_exp)

        self.layout.addWidget(self.lbl, 1)
        self.layout.addWidget(self.exp_box, 1)

    # Ensures EXP is in range [0,99], inclusive
    def validate_exp(self):
        if(self.exp_box.text() == ""):
            self.exp = 0
            return
        try:
            self.exp = int(self.exp_box.text())
            if(self.exp < MIN_EXP):
                self.exp_box.setText(str(MIN_EXP))
            elif(self.exp > MAX_EXP):
                self.exp_box.setText(str(MAX_EXP))
        except ValueError:
            self.exp_box.setText("")


class BEXP_Edit():
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.bexp = 0

        # Create bexp box
        self.bexp_btn = QPushButton(text="Calculate Max Attainable Level with BEXP")
        self.lbl = create_label("Your BEXP", RIGHT, LBL_FONT, HEADING_SZ)
        self.bexp_box = create_exp_box()
        self.bexp_box.setAlignment(LEFT)
        self.bexp_box.setStyleSheet("QLineEdit{color: #02db02; font-weight: bold; font-size: 16;}")
        self.bexp_box.textChanged.connect(self.validate_BEXP)

        self.layout.addWidget(self.lbl, 1)
        self.layout.addWidget(self.bexp_box, 1)
        self.layout.addWidget(self.bexp_btn, 4)

    # Ensures BEXP is a valid int
    def validate_BEXP(self):
        if(self.bexp_box.text() == ""):
            self.bexp = 0
            return
        try:
            self.bexp = int(self.bexp_box.text())
        except ValueError:
            self.bexp_box.setText("")

# Dialog that displays a message welcoming the user
class Welcome_Dialog(QDialog):
    def __init__(self, welcome_msg, parent=None):
        super().__init__(parent)
        layout = QGridLayout()

        # Create welcome message
        self.label = QLabel()
        self.label.setText(welcome_msg)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, 0, 0, 1, 4)

        # Create confirmation button
        startBtn = QPushButton("Get Started")
        startBtn.clicked.connect(self.close)
        layout.addWidget(startBtn, 1, 1, 1, 2)

        self.setLayout(layout)
        self.setWindowTitle("Welcome")


class BEXP_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.welcome_dlg = Welcome_Dialog(WELCOME, self)
        self.initTimer()

    def initUI(self):
        # Initialize window and basic layout
        self.setWindowTitle('Radiant Dawn BEXP Calculator')
        self.setFixedSize(WIDTH, HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)


        self.startLvlTier = 0
        self.EndLvlTier = 1
        self.createDropdowns()

        # Generate Starting Tier/Level forms, defaulting to Tier 1 Beorc
        startLvlForm = QHBoxLayout()
        startLvlForm.addWidget(create_label("Starting Level:", RIGHT, LBL_FONT, HEADING_SZ), 4)
        self.startTierDropdowns = QStackedWidget()
        self.startTierDropdowns.addWidget(self.start_tier_dropdown_beorc)
        self.startTierDropdowns.addWidget(self.start_tier_dropdown_laguz)
        startLvlForm.addWidget(self.startTierDropdowns, 2)
        self.startLvlDropdowns = QStackedWidget()
        self.startLvlDropdowns.addWidget(self.start_lvl_dropdown_beorc)
        self.startLvlDropdowns.addWidget(self.start_lvl_dropdown_laguz)
        startLvlForm.addWidget(self.startLvlDropdowns, 3)
        self.startExpBox = ExpEdit()
        startLvlForm.addLayout(self.startExpBox.layout, 2)
        self.generalLayout.addLayout(startLvlForm)

        # Generate Ending Tier/Level forms, defaulting to Tier 1 Beorc
        endLvlForm = QHBoxLayout()
        endLvlForm.addWidget(create_label("Ending Level:", RIGHT, LBL_FONT, HEADING_SZ), 4)
        self.endTierDropdowns = QStackedWidget()
        self.endTierDropdowns.addWidget(self.end_tier_dropdown_beorc)
        self.endTierDropdowns.addWidget(self.end_tier_dropdown_laguz)
        endLvlForm.addWidget(self.endTierDropdowns, 2)
        self.endLvlDropdowns = QStackedWidget()
        self.endLvlDropdowns.addWidget(self.end_lvl_dropdown_beorc)
        self.endLvlDropdowns.addWidget(self.end_lvl_dropdown_laguz)
        endLvlForm.addWidget(self.endLvlDropdowns, 3)
        self.endExpBox = ExpEdit()
        endLvlForm.addLayout(self.endExpBox.layout, 2)
        self.generalLayout.addLayout(endLvlForm)

        # Create Difficulty Mode Options
        difficultyOptions = QHBoxLayout()

        diffLbl = create_label("Difficulty:", LEFT, LBL_FONT, HEADING_SZ)
        difficultyOptions.addWidget(diffLbl)

        # Use radios, only one difficulty mode can be selected at a time
        self.radio = QRadioButton("Easy", self)
        self.radio.toggled.connect(self.updateDifficulty)
        difficultyOptions.addWidget(self.radio)

        self.radio = QRadioButton("Normal", self)
        self.radio.toggled.connect(self.updateDifficulty)
        self.radio.toggle()
        difficultyOptions.addWidget(self.radio)

        self.radio = QRadioButton("Hard", self)
        self.radio.toggled.connect(self.updateDifficulty)
        difficultyOptions.addWidget(self.radio)

        self.diffMod = DIFF_MOD_NORMAL

        # Generate Laguz Checker Box to adjust Tier/Level Ranges
        self.laguzCheck = QCheckBox(text="Laguz?")
        self.laguzCheck.pressed.connect(self.updateDropdowns)
        difficultyOptions.addWidget(self.laguzCheck)

        # Check box to mute/unmute audio
        self.muteBox = QCheckBox(text="Mute Audio")
        self.muteBox.pressed.connect(self.updateAudio)
        difficultyOptions.addWidget(self.muteBox)

        self.generalLayout.addLayout(difficultyOptions)

        # Button to calculate max level reached with fixed BEXP
        self.bexp_input = BEXP_Edit()
        self.bexp_input.bexp_btn.clicked.connect(self.displayMaxBexpLvlReached)
        self.generalLayout.addLayout(self.bexp_input.layout)

        # Button to Calculate Final Bexp Cost
        calcBtn = QPushButton(text="Calculate Total BEXP Cost")
        calcBtn.clicked.connect(self.displayBexpCost)
        self.generalLayout.addWidget(calcBtn, 10)

        self.bexpCostDisplay = QHBoxLayout()
        self.bexpCostLbl = create_label("TOTAL BEXP COST:", RIGHT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.bexpCostLbl)
        self.totalBexpCost = create_label(str(0), LEFT, TITLE_FONT, HEADING_SZ)
        self.totalBexpCost.setStyleSheet("QLabel{color: #02db02;}")
        self.bexpCostDisplay.addWidget(self.totalBexpCost)
        self.generalLayout.addLayout(self.bexpCostDisplay)

        # Music Player for BGM
        if(randint(1,ODDS_OF_FUN) == 1):
            music = BACKUP
        else:
            music = BGM
        self.music_player = MusicPlayer(music)

        self.center()
        self.show()

    def center(self):
        qRect = self.frameGeometry()
        center = self.screen().availableGeometry().center()
        qRect.moveCenter(center)
        self.move(qRect.topLeft())

    def initTimer(self):
        # Creates single-shot delay for welcome message
        QTimer.singleShot(DELAY, self.welcome_dlg.exec)
        QTimer.singleShot(DELAY, self.music_player.play_BGM)

    def updateEndLvlTier(self):
        match self.sender().text():
            case "Tier 1":
                self.endLvlTier = 0
            case "Tier 2":
                self.endLvlTier = 1
            case "Tier 3":
                self.endLvlTier = 2

    # Track changes to difficulty picker
    def updateDifficulty(self):
        match self.sender().text():
            case "Easy":
                self.diffMod = DIFF_MOD_EASY
            case "Normal":
                self.diffMod = DIFF_MOD_NORMAL
            case "Hard":
                self.diffMod = DIFF_MOD_HARD

    # The computational meat of the program
    def displayBexpCost(self):
        if(self.laguzCheck.isChecked()):
            race = RACE_LAGUZ
            lvl_mod = LVL_MOD_LAGUZ
        else:
            race = RACE_BEORC
            lvl_mod = LVL_MOD_BEORC
        start_lvl = convertToInternalLevel(int(self.startTierDropdowns.currentWidget().currentText()[5:])-1, int(self.startLvlDropdowns.currentWidget().currentText()[6:]))
        end_lvl = convertToInternalLevel(int(self.endTierDropdowns.currentWidget().currentText()[5:])-1, int(self.endLvlDropdowns.currentWidget().currentText()[6:]))
        bexp_cost = calc_bexp_cost(start_lvl, self.startExpBox.exp, end_lvl, self.endExpBox.exp, lvl_mod, self.diffMod, race)
        if(bexp_cost < 0):
            display_error_msg("Invalid level range selected, please try again.")
            bexp_cost = 0
        if(len(self.bexp_input.bexp_box.text()) < 1):
            self.totalBexpCost.setText(str(bexp_cost))
        elif(self.bexp_input.bexp < bexp_cost):
            self.totalBexpCost.setText(f"{str(bexp_cost)} (You don't have enough BEXP!)")
        elif(self.bexp_input.bexp >= bexp_cost):
            self.totalBexpCost.setText(f"{str(bexp_cost)} ({self.bexp_input.bexp-bexp_cost} BEXP Leftover)")
        self.bexpCostLbl.setText("TOTAL BEXP COST:")
        
    # Calculate and display Max Level Reached given fixed BEXP
    def displayMaxBexpLvlReached(self):
        if(self.laguzCheck.isChecked()):
            race = RACE_LAGUZ
            lvl_mod = LVL_MOD_LAGUZ
        else:
            race = RACE_BEORC
            lvl_mod = LVL_MOD_BEORC
        start_lvl = convertToInternalLevel(int(self.startTierDropdowns.currentWidget().currentText()[5:])-1, int(self.startLvlDropdowns.currentWidget().currentText()[6:]))
        final_lvl_str = calc_max_attainable_lvl(start_lvl, self.startExpBox.exp, self.bexp_input.bexp, lvl_mod, self.diffMod, race)
        self.totalBexpCost.setText(str(final_lvl_str))
        self.bexpCostLbl.setText("Max Attainable Level:")

    # Creates all lvl/tier dropdowns
    def createDropdowns(self):
        self.start_lvl_dropdown_beorc = createLvlDropdown(MAX_DISP_LVL_BEORC)
        self.start_lvl_dropdown_beorc.currentTextChanged.connect(self.resetStartExpBox)
        self.start_lvl_dropdown_laguz = createLvlDropdown(MAX_DISP_LVL_LAGUZ)
        self.start_lvl_dropdown_laguz.currentTextChanged.connect(self.resetStartExpBox)
        self.start_tier_dropdown_beorc = createTierDropdown(MAX_TIERS_BEORC)
        self.start_tier_dropdown_beorc.currentTextChanged.connect(self.resetStartExpBox)
        self.start_tier_dropdown_laguz = createTierDropdown(MAX_TIERS_LAGUZ)
        self.start_tier_dropdown_laguz.currentTextChanged.connect(self.resetStartExpBox)
        self.end_lvl_dropdown_beorc = createLvlDropdown(MAX_DISP_LVL_BEORC)
        self.end_lvl_dropdown_beorc.currentTextChanged.connect(self.resetEndExpBox)
        self.end_lvl_dropdown_laguz = createLvlDropdown(MAX_DISP_LVL_LAGUZ)
        self.end_lvl_dropdown_laguz.currentTextChanged.connect(self.resetEndExpBox)
        self.end_tier_dropdown_beorc = createTierDropdown(MAX_TIERS_BEORC)
        self.end_tier_dropdown_beorc.currentTextChanged.connect(self.resetEndExpBox)
        self.end_tier_dropdown_laguz = createTierDropdown(MAX_TIERS_LAGUZ)
        self.end_tier_dropdown_laguz.currentTextChanged.connect(self.resetEndExpBox)
    
    # Updates dropdown when switching between laguz and beorc
    def updateDropdowns(self):
        if(self.laguzCheck.isChecked()):
            # Switch to beorc
            self.startTierDropdowns.setCurrentIndex(RACE_BEORC)
            self.startLvlDropdowns.setCurrentIndex(RACE_BEORC)
            self.endTierDropdowns.setCurrentIndex(RACE_BEORC)
            self.endLvlDropdowns.setCurrentIndex(RACE_BEORC)
        else:
            # Switch to laguz
            self.startTierDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.startLvlDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.endTierDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.endLvlDropdowns.setCurrentIndex(RACE_LAGUZ)
        self.resetDropdowns()
        self.resetStartExpBox()
        self.resetEndExpBox()

    # Resets dropdowns to have first item selected
    def resetDropdowns(self):
        self.start_tier_dropdown_beorc.setCurrentIndex(0)
        self.start_tier_dropdown_laguz.setCurrentIndex(0)
        self.start_lvl_dropdown_beorc.setCurrentIndex(0)
        self.start_lvl_dropdown_laguz.setCurrentIndex(0)
        self.end_tier_dropdown_beorc.setCurrentIndex(0)
        self.end_tier_dropdown_laguz.setCurrentIndex(0)
        self.end_lvl_dropdown_beorc.setCurrentIndex(0)
        self.end_lvl_dropdown_laguz.setCurrentIndex(0)

    def updateAudio(self):
        if(self.muteBox.isChecked()):
            self.music_player.audio_output.setVolume(BGM_VOL)
        else:
            self.music_player.audio_output.setVolume(0)

    def resetStartExpBox(self):
        reset_exp_box(self.startExpBox.exp_box)

    def resetEndExpBox(self):
        reset_exp_box(self.endExpBox.exp_box)

def create_label(text, alignment, font, size):
    label = QLabel()
    label.setText(text)
    label.setFont(QFont(font, size))
    label.setAlignment(alignment)
    return label

def createLvlDropdown(max_lvl):
    lvlDropdown = QComboBox()
    for lvl in range(max_lvl):
        lvlDropdown.addItem("Level "+str(lvl+1))
    return lvlDropdown

def createTierDropdown(max_tier):
    tierDropdown = QComboBox()
    for tier in range(max_tier):
        tierDropdown.addItem("Tier "+str(tier+1))
    return tierDropdown

def create_exp_box():
    exp_box = QLineEdit()
    # reset_exp_box(exp_box)
    return exp_box

def reset_exp_box(exp_box):
    exp_box.setText("")

# Generic error message displayed as pop-up window
def display_error_msg(error_msg):
    msg_box = QMessageBox()
    msg_box.setText(error_msg)
    msg_box.exec()
