class PseudoGUI:
    """Helps testing
    """

    def __init__(self):

        self.args = None

    def show_error(self,message):
        self.args = message

    def show_warning(self,message):
        self.args = message

    def ask_are_you_sure(self,question):
        self.args = question
        return False

    def get_method_call_args(self):
        return self.args
