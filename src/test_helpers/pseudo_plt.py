
class PseudoPlt:
    """Helps testing. Can be injected to analysis tasks using plt
    """
    def __init__(self):
        self.args = None
        self.show_was_called = False

    def show(self):
        self.show_was_called = True

    def bar(self,*args):
        self.args = args

    def scatter(self,*args,alpha):
        self.args = args

    def get_method_call_args(self):
        return self.args
