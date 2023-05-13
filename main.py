import dearpygui.dearpygui as dpg
from src.UI.UI import UI


def main():
    """The main entrypoint of the simulation application.
    """
    plot = UI(dpg)
    plot.setUpSimulation()
    plot.run()


if __name__ == '__main__':
    main()
