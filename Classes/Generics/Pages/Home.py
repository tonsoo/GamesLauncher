from Classes.Generics.Page import Page

class Home(Page):

    def __init__(self) -> None:
        Page.__init__(self, pageTitle='Home', pageIcon='sid-el-cienceiro.ico')