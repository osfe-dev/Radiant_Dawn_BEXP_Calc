from BEXP_calcs import *
from BEXP_GUI import *
import ctypes

def main():
    app = QApplication([])
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('RD_BEXP_CALC')

    app_icon = QtGui.QIcon()
    app_icon.addFile(APP_ICON)
    app.setWindowIcon(app_icon)

    window = BEXP_Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()