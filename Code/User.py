import json
import os
import re
import string


# Recordar establecer limitaciones y otros para la contrasenna, nombre, correo; agregar foto y archivo para reconocimiento facial

class User:
    """
    This is the User class.

    This class contains the following attributes:
        -User (str)
        -Name (str)
        -Nickname (str)
        -Password (str)
        -Age (int)
        -Mail (str)
        -Answers (list of str)
        -Profile Image (str)
        -Facial Image (str)
        -Forbidden Words

    This class contains the methods:
        -GetUser
        -GetAnswer
        -SetName
        -SetNickname
        -SetPassword
        -SetAge
        -SetMail
        -SetAnswer
        -SetProfile
        -SetFacial
        -ValidatePassword
        -ValidateUser
        -ValidateMail
        -SaveJson
        -LoadJson
    """
    forbiddenWords = ["puta", "imbecil", "perra", "picha"]

    def __init__(self, user, name, nickname, password, age, mail, answers, profileImage, facialImage):
        if (self.ValidatePassword(password)
                and self.ValidateUser(user)
                and self.ValidateMail(mail)):
            self.user = user
            self.name = name
            self.nickname = nickname
            self.password = password
            self.age = age
            self.mail = mail
            self.answers = answers
            self.profileImage = profileImage
            self.facialImage = facialImage

            self.SaveJson(self.user)

    # Change class to one that returns each element so that they are displayed on the screen
    def GetUser(self):
        """
        This method take User class details and print them in console

        :return: User
        """
        print(f"User: {self.user}")
        print(f"\t Name: {self.name}")
        print(f"\t Nickname: {self.nickname}")
        print(f"\t Password: {self.password}")
        print(f"\t Age: {self.age}")
        print(f"\t Mail: {self.mail}")
        print("\t Answers:")
        for i, answer in enumerate(self.answers, start=1):
            print(f"\t \t Question {i}: {answer}")
        print(f"\t Profile Image: {self.profileImage}")
        print(f"\t Facial Recognition: {self.facialImage}")

    def GetAnswer(self, num):
        """
        This method found the answer of the answers list attribute

        :param num:
        :return: answers[num]
        """
        if 1 <= num <= len(self.answers):
            print(f"Answer: {self.answers[num-1]}")

    def SetName(self, name):
        """
        Changes the name attribute

        :param name:
        :return:
        """
        self.name = name
        self.SaveJson(self.user)

    def SetNickname(self, nickname):
        """
        Changes the nickname attribute

        :param nickname:
        :return:
        """
        self.nickname = nickname
        self.SaveJson(self.user)

    def SetPassword(self, password):
        """
        Changes the password attribute

        :param password:
        :return:
        """
        if self.ValidatePassword(password):
            self.password = password
            self.SaveJson(self.user)

    def SetAge(self, age):
        """
        Changes the age attribute

        :param age:
        :return:
        """
        self.age = age
        self.SaveJson(self.user)

    def SetMail(self, mail):
        """
        Changes the mail attribute

        :param mail:
        :return:
        """
        if self.ValidateMail(mail):
            self.mail = mail
            self.SaveJson(self.user)

    def SetAnswer(self, num, newAnswer):
        """
        Changes an answer for the list answer attribute

        :param num:
        :param reply:
        :return:
        """
        if 1 <= num <= len(self.answers):
            self.answers[num-1] = newAnswer
            self.SaveJson(self.user)

    def SetProfile(self, profileImage):
        """
        Changes the profile image attribute

        :param profileImage:
        :return:
        """
        self.profileImage = profileImage
        self.SaveJson(self.user)

    def SetFacial(self, facialImage):
        """
        Changes the facial image attribute

        :param facialImage:
        :return:
        """
        self.facialImage = facialImage
        self.SaveJson(self.user)

    @classmethod
    def ValidatePassword(cls, password):
        """
        Verify that the password follows a fixed structure

        :param password: str
        :return: boolean
        """
        if (len(password) >= 8
                and any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c in string.punctuation for c in password)):
            return True
        else:
            print("La contraseña no cumple con los requisitos")
            return False

    @classmethod
    def ValidateUser(cls, user):
        """
        Verify that the username follows a fixed structure

        :param user:
        :return: boolean
        """
        pathFile = os.path.join("Users", user)
        if not(len(user) > 10
                and any(word in user.lower() for word in cls.forbiddenWords)
                and os.path.exists(pathFile)):
            return True
        else:
            print("El usuario registrado no cumple con los requisitos")
            return False

    @classmethod
    def ValidateMail(cls, mail):
        """
        Verify that the email follows a fixed structure

        :param mail:
        :return: boolean
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, mail):
            return True
        else:
            print("El correo electrónico no es valido")
            return False

    def SaveJson(self, filename):
        """
        Save an instances of User in a .json file

        :param filename: str
        :return: .json
        """
        pathFile = os.path.join("Users", filename)
        userDict = {
            "User": self.user,
            "Name": self.name,
            "Nickname": self.nickname,
            "Password": self.password,
            "Age": self.age,
            "Mail": self.mail,
            "Answers": self.answers,
            "Profile Image": self.profileImage,
            "Facial Recognition": self.facialImage
        }
        with open(pathFile, 'w') as json_file:
            json.dump(userDict, json_file)

    @classmethod
    def LoadJson(cls, filename):
        """
        Retrieves a user instance stored in a .json file
        :param filename: str
        :return: User
        """
        pathFile = os.path.join("Users", filename)
        if os.path.exists(pathFile):
            with open(pathFile, 'r') as json_file:
                userDict = json.load(json_file)
            return cls(
                user=userDict["User"],
                name=userDict["Name"],
                nickname=userDict["Nickname"],
                password=userDict["Password"],
                age=userDict["Age"],
                mail=userDict["Mail"],
                answers=userDict["Answers"],
                profileImage=userDict["Profile Image"],
                facialImage=userDict["Facial Recognition"]
            )
        else:
            print(f"El archivo {filename} no existe en el sistema")

