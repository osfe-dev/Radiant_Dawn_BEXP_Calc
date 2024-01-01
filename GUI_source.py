# Definitions for various imports/constants to be used by Inheritance_GUI

# Imports
from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QMessageBox,
    QWidget,
    QMainWindow, 
    QGridLayout, 
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QFrame,
    QSizePolicy,
    QDialog,
    QDialogButtonBox,
    QSpacerItem,
    QRadioButton,
    QCheckBox,
    QStackedWidget,
)
from PyQt6 import (
    QtGui, 
    QtWidgets
)
from PyQt6.QtCore import (
    Qt,
    QUrl,
    QTimer,
    QSize,
)
from PyQt6.QtGui import (
    QPixmap,
    QPalette, 
    QFont,
    QPainter,
    QBrush,
    QPen,
    QFontMetrics,
    QPainterPath,
    QColor,
)
from PyQt6.QtMultimedia import (
    QSoundEffect,
    QMediaPlayer,
    QAudioOutput
)

import sys, time
from BEXP_calcs import *


# Various Constant Definitions
# Dimensions
WIDTH       =   640
HEIGHT      =   180
LINE_WIDTH  =   1
IMG_WIDTH   =   int(0.4*WIDTH)
IMG_HEIGHT  =   int(0.25*HEIGHT)

# Font
TITLE_FONT  =   'Helvetica'
TITLE_SIZE  =   24
LBL_FONT    =   'Helvetica'
LBL_SIZE    =   12
FORM_FONT   =   'Helvetica'
FORM_SIZE   =   8
HEADING_SZ  =   16

# Alignment flags
LEFT    =   Qt.AlignmentFlag.AlignLeft
CENTER  =   Qt.AlignmentFlag.AlignCenter
RIGHT   =   Qt.AlignmentFlag.AlignRight

# Colors for various buttons/fields
LTBLUE  =   "#b8e0f5"
LTTAN   =   "#faf2cd"
LTGRAY  =   "#E6E6E6"
LTGRAY2 =   "#E0E0E0"
BEXP_G  =   "#02F902"
DARK_G  =   "02DB02"

# Colors to be passed to QtQui.Color(R,G,B)
COL_LTGRAY      =   (212,212,212)
COL_WHT         =   (0,0,0)
COL_BEXP_GREEN  =   (2,249,2)

# Specific colors for various types of elements
SEP_COL     =   COL_WHT

# Music Defaults
BGM             =   'Resources/BGM.mp3'
BGM_VOL         =   0.1
BGM_LOOPS       =   -1      # Infinite Loops

# Misc File Path Stuff
APP_ICON        =   'Resources/AppIcon.png'
D0              =   'nothingtoseehere'
D1              =   'noneofyourbusiness'
D2              =   'turnaroundnow'
D3              =   'lastchance'
D4              =   'dontsayididntwarnyou'
D5              =   'hereitis'
BACKUP          =   f'Resources/{D0}/{D1}/{D2}/{D3}/{D4}/{D5}/secret.mp3'

# Misc Constants
DELAY           =   500     # ms
ODDS_OF_FUN     =   25      # The odds of having fun

# Error Messages


# Dialog Messages
WELCOME         =   """ Welcome to the FE10 BEXP Cost Calculator!
This program lets you calculate the total BEXP Cost for any (valid) pair of starting and ending levels! 
You can also include how much BEXP you currently have and immediately see how much you have left!
There's also an option to see how many levels you can get with a given amount of BEXP!
Enjoy!"""
