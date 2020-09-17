import NotePadModel


class Controller:
    def __init__(self):
        self.notepadModel = NotePadModel.Model()

    def encrypt(self, plaintext):
        self.result = self.notepadModel.encrypt(plaintext)
        return self.result

    def decrypt(self, ciphertext):
        self.result = self.notepadModel.decrypt(ciphertext)
        return self.result

    def save_file(self, msg, url):
        self.notepadModel.save_file(msg, url)

    def save_as(self, msg, url):
        self.notepadModel.save_as(msg, url)

    def read_file(self, url):
        self.msg, self.base = self.notepadModel.read_file(url)
        return self.msg, self.base

    def saysomething(self):
        self.takeAudio = self.notepadModel.takeQuery()
        return self.takeAudio

##c = Controller()
##c.saysomething()