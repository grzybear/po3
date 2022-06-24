from App import App
import sys, os, time

def main():
    #os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = App()
    #app.Go()
    sys.exit(app.qt_app.exec_())


if __name__ == "__main__":
    main()