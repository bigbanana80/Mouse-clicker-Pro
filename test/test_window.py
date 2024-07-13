def test_1():
    import main
    from PySide6.QtWidgets import QApplication,QMainWindow
    import sys

    app = QApplication(sys.argv)
    window = main.MainWindow()
    assert isinstance(window, main.MainWindow) is True
    assert isinstance(app, QApplication) is True
