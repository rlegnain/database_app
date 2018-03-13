
from backend import Myfile, onImp


class controller(onImp):

    def __init__(self):
        self.bk = Myfile(self)


    def on_add(self):
        # updategui
        pass