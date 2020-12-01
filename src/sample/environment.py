import datetime


class Environment:
    def getTime(self):
        return datetime.datetime.now().hour

    def playWavFile(self):
        pass

    def wavWasPlayed(self):
        return True

    def resetWav(self):
        return False
