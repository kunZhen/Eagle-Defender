import json
import os

# Recordar establecer limitaciones y otros para la contrasenna, nombre, correo; agregar foto y archivo para reconocimiento facial
class User:
    def __init__(self, user, name, password, age, mail, answers):
        self.user = user
        self.name = name
        self.password = password
        self.age = age
        self.mail = mail
        self.answers = answers
        self.saveJson(self.user)

    def getUser(self):
        print(f"User: {self.user}")
        print(f"\tName: {self.name}")
        print(f"\tPassword: {self.password}")
        print(f"\tAge: {self.age}")
        print(f"\tMail: {self.mail}")
        print("\tanswers:")
        for i, answer in enumerate(self.answers, start=1):
            print(f"\t\tQuestion {i}: {answer}")

    def getAnswer(self, num):
        if num <= 5:
            for i, answer in enumerate(self.answers, start=1):
                if num == i:
                    print(f"Question {i}: {answer}")

    def setUser(self, user=None, name=None, password=None, age=None, mail=None, answers=None):
        if user is not None:
            self.user = user
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if age is not None:
            self.age = age
        if mail is not None:
            self.mail = mail
        if answers is not None:
            self.answers = answers

        self.saveJson(self.user)

    def saveJson(self, filename):
        pathFile = os.path.join("Users", filename)
        userDict = {
            "Username": self.user,
            "Name": self.name,
            "Password": self.password,
            "Age": self.age,
            "Mail": self.mail,
            "Answers": self.answers
        }
        with open(pathFile, 'w') as file:
            json.dump(userDict, file)

    @classmethod
    def loadJson(cls, filename):
        pathFile = os.path.join("Users", filename)
        if os.path.exists(pathFile):
            with open(pathFile, 'r') as file:
                userDict = json.load(file)
            return cls(
                user=userDict["Username"],
                name=userDict["Name"],
                password=userDict["Password"],
                age=userDict["Age"],
                mail=userDict["Mail"],
                answers=userDict["Answers"]
            )
        else:
            print(f"El archivo {filename} no existe en el sistema")

