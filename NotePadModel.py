import os
import speech_recognition as s
import traceback


class Model:
    def __init__(self):
        self.key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.offset = 5

    def encrypt(self, plaintext):
        result = ''
        for ch in plaintext:
            try:
                i = (self.key.index(ch) + self.offset) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += ch
        return result

    def decrypt(self, ciphertext):
        result = ''
        for ch in ciphertext:
            try:
                i = (self.key.index(ch) - self.offset) % len(self.key)
                result += self.key[i]
            except ValueError:
                result += ch
        return result

    def save_file(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url
        filename, file_extension = os.path.splitext(file)
        if file_extension in ".ntxt":
            msg = self.encrypt(msg)
        with open(file, 'w', encoding='utf-8') as fw:
            fw.write(msg)

    def save_as(self, msg, url):
        if type(url) is not str:
            file = url.name
        else:
            file = url
        msg = self.encrypt(msg)

        with open(file, 'w') as fw:
            fw.write(msg)

    def read_file(self, url):
        ''' basename = os.path.basename(url)  # basename=filename+file_extension'''
        filename, file_extension = os.path.splitext(url)
        fi = open(url, 'r')
        msg = fi.read()
        if file_extension in ".ntxt":
            msg = self.decrypt(msg)
        fi.close()
        return msg, filename + file_extension

    def takeQuery(self):
        sr = s.Recognizer()
        sr.pause_threshold = 1
        print("Speak")
        with s.Microphone() as m:
            try:
                sr.adjust_for_ambient_noise(m) ## Cancle Noise
                audio = sr.listen(m)  # input is audio from microphone or audio data and returns audiodata
                query = sr.recognize_google(audio, language='eng-in')
                print(query)
                return query
            except Exception as e:
                print("exception in this", e)
                print("Not Recognized")
                print(traceback.format_exc())
