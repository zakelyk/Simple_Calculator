import flet
from control import CalculatorApp

def main(page: flet):
    page.title = "Calculator"

    calc = CalculatorApp()
    page.window_width = 330       # window's width is 200 px
    page.window_height = 370      # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    page.add(calc)

flet.app(target=main)