import json
import os
import re
import string
from SSHFileTransfer import *


class User:
    """
    This is the User class.

    This class contains the following attributes:
        -User (str)
        -Password (str)
        -Mail (str)
        -Color (str)
        -Music (list of str)
        -Answers (list of str)
        -Profile  (str)
        -Facial  (str)
        -Forbidden Words

    This class contains the methods:
        -CreateUser
        -GetUser
        -GetMail
        -GetColor
        -GetMusic
        -GetAnswer
        -GetProfile
        -GetFacial
        -SetAttributes
        -SetUser
        -ValidatePassword
        -ValidateUser
        -ValidateMail
        -CheckExist
        -SaveJson
        -DeleteJson
        -LoadJson
    """
    forbiddenWords = ["culo", "lerdo", "malparido", "patán", "puta", "puto", "playo", "picha",
                      "tarado", "zángano", "imbécil", "polla", "cabrón", "tonto", "tonta", "capullo",
                      "capulla", "idiota", "gilipollas"]

    def __init__(self, user, password, mail, color, music, answers, profile, facial):
        if self.ValidateUser(user) and self.ValidateMail(mail) and self.ValidatePassword(password):
            # When adding or removing attributes in this section, review __init__ load, SaveJson and LoadJson
            self.user = user
            self.password = password
            self.mail = mail
            self.color = color
            self.music = music
            self.answers = answers
            # ------------------------------------------------------------------------------------------------------ #
            self.avatar = 1
            self.animation = "S"
            self.textures = 1
            # ------------------------------------------------------------------------------------------------------ #
            self.profile = profile
            self.facial = facial
            self.validation = True
            self.errorType = None

            self.SaveJson(self.user, self.mail)
        else:
            self.validation = False

            if not self.ValidateUser(user):
                self.errorType = "user"
            elif not self.ValidatePassword(password):
                self.errorType = "password"
            elif not self.ValidateMail(mail):
                self.errorType = "mail"

        # -----------------------------------------Conexión con el servidor---------------------------------------------#
        hostname = '20.62.171.56'  # Cambia esto a la dirección IP de tu máquina virtual
        port = 22  # El puerto SSH predeterminado es 22
        username = 'eagleDefender'  # Tu nombre de usuario en la máquina virtual
        private_key_file = os.path.abspath('Code/eagleDefenderServer_key_1011.pem')
        self.ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
        # ----------------------------------------------------------------------------------------------------------------#

    # The class is overloaded because we need to verify that the user exists or not
    def __init__load(self, userDict):
        self.user = userDict["User"]
        self.password = userDict["Password"]
        self.mail = userDict["Mail"]
        self.color = userDict["Favorite Color"]
        self.music = userDict["Favorite Music"]
        self.answers = userDict["Answers"]
        # ------------------------------------------------------------------------------------------------------ #
        self.avatar = userDict["Avatar"]
        self.animation = userDict["Animation"]
        self.textures = userDict["Textures"]
        # ------------------------------------------------------------------------------------------------------ #
        self.profile = userDict["Profile"]
        self.facial = userDict["Facial Recognition"]

    @classmethod
    def CreateUser(cls, user, password, mail, color, music, answers, profile, facial):
        """
        Allows to create a user

        :param user:
        :param password:
        :param mail:
        :param answers:
        :param color:
        :param music:
        :param profile:
        :param facial:
        :return: User instance
        """
        return cls(user, password, mail, color, music, answers, profile, facial)

    # Change method to one that returns each element so that they are displayed on the screen
    def GetUserAttributes(self):
        """
        This method take User class details and print them in console

        :return: User
        """
        print(f"User: {self.user}")
        print(f"\t Password: {self.password}")
        print(f"\t Mail: {self.mail}")
        print(f"\t Favorite Color: {self.color}")
        print(f"\t Favorite Music: {self.music}")
        print("\t Answers:")
        for i, answer in enumerate(self.answers, start=1):
            print(f"\t \t Question {i}: {answer}")
        print(f"\t Profile: {self.profile}")
        print(f"\t Facial Recognition: {self.facial}")

    def GetAttribute(self, attribute, num=None):
        """
        Takes an attribute for object using a number that identifies a specific attribute

        :param attribute: int
        :param num:
        :return: self.attribute
        """
        if attribute == 1:
            return self.user
        elif attribute == 2:
            return self.password
        elif attribute == 3:
            return self.mail
        elif attribute == 4:
            return self.color
        elif attribute == 5:
            return self.music
        elif attribute == 6:
            if num is not None:
                if 1 <= num <= len(self.answers):
                    return self.answers[num - 1]
            else:
                return self.answers
        elif attribute == 7:
            return self.profile
        elif attribute == 8:
            return self.facial

    def SetAttributes(self, color=None, music=None, answers=None, numIndex=None, newAnswer=None, avatar=None,
                      animation=None, textures=None, profile=None,
                      facial=None):
        """
        Changes the attributes color, music, answers, profile and facial for an exist user

        :param color:
        :param music:
        :param answers:
        :param numIndex:
        :param newAnswer:
        :param avatar:
        :param animation:
        :param textures:
        :param profile:
        :param facial:
        :return:
        """
        if color is not None:
            self.color = color
        if music is not None:
            self.music = music
        if answers is not None:
            self.answers = answers
        if numIndex is not None:
            if newAnswer is not None:
                if 1 <= numIndex <= len(self.answers):
                    self.answers[numIndex - 1] = newAnswer
        if avatar is not None:
            self.avatar = avatar
        if animation is not None:
            self.animation = animation
        if textures is not None:
            self.textures = textures
        if profile is not None:
            self.profile = profile
        if facial is not None:
            self.facial = facial
        self.SaveJson(self.user, self.mail)

    def SetUser(self, user=None, password=None, mail=None):
        """
        Changes the user, password and mail, makes the respective validates

        :param user:
        :param password:
        :param mail:
        :return:
        """
        self.DeleteJson(self.user, self.mail)
        if self.ValidateUser(user):
            self.user = user
        if self.ValidatePassword(password):
            self.password = password
        if self.ValidateMail(mail):
            self.mail = mail
        self.SaveJson(self.user, self.mail)

    @classmethod
    def ValidatePassword(cls, password=None):
        """
        Verify that the password follows a fixed structure

        :param password: str
        :return: boolean
        """
        if password is not None:
            if not len(password) >= 8:
                return False
            if not any(c.islower() for c in password):
                return False
            if not any(c.isupper() for c in password):
                return False
            if not any(c.isdigit() for c in password):
                return False
            if not any(c in string.punctuation for c in password):
                return False
            else:
                return True

    @classmethod
    def ValidateUser(cls, user=None):
        """
        Verify that the username follows a fixed structure

        :param user: str
        :return: boolean
        """
        if user is not None:
            if len(user) > 25:
                print("El nombre de usuario registrado excede la capacidad maxima de caracteres permitida")
                return False
            if any(word in user.lower() for word in cls.forbiddenWords):
                print("El nombre de usuario posee vocabulario inapropiado")
                return False
            else:
                return True

    @classmethod
    def ValidateMail(cls, mail=None):
        """
        Verify that the email follows a fixed structure

        :param mail: str
        :return: boolean
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if mail is not None:
            if not re.match(pattern, mail):
                print("Ingrese correo nuevamente")
                return False
            else:
                return True

    def ValidateExistance(self, filename):
        """
        Confirm if there is an instance of User in a .json file

        :param filename: str
        :return:
        """
        pathFile = os.path.join("Users", filename + ".json")

        if filename == "":
            return False

        print(pathFile)
        if os.path.exists(pathFile):
            return True
        # -----------------------------------Access on Server------------------------------------#
        hostname = '20.62.171.56'
        port = 22
        username = 'eagleDefender'
        private_key_file = os.path.abspath('Code/eagleDefenderServer_key_1011.pem')
        ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
        archivo_remoto_a_verificar = f'/home/eagleDefender/files/users/{filename}.json'
        existance = ssh_transfer.remote_file_exists(archivo_remoto_a_verificar)
        ssh_transfer.__exit__()
        # -----------------------------------Access on Server------------------------------------#

        return existance

    def SaveJson(self, filename1, filename2):
        """
        Save an instances of User in a .json file

        :param filename1:
        :param filename2:
        :return: .json
        """
        pathFile1 = os.path.join("Code/GraphicalUserInterface/Users", filename1 + ".json")
        pathFile2 = os.path.join("Code/GraphicalUserInterface/Users", filename2 + ".json")
        userDict = {
            "User": self.user,
            "Password": self.password,
            "Mail": self.mail,
            "Favorite Color": self.color,
            "Favorite Music": self.music,
            "Answers": self.answers,
            "Avatar": self.avatar,
            "Animation": self.animation,
            "Textures": self.textures,
            "Profile": self.profile,
            "Facial Recognition": self.facial
        }
        with open(pathFile1, 'w') as json_file:
            json.dump(userDict, json_file, indent=4)
        with open(pathFile2, 'w') as json_file:
            json.dump(userDict, json_file, indent=4)
        # Ruta al archivo en tu sistema local

        # -------------------------------------SAVED ON THE SERVER-------------------------------#
        directorio_destino = '/home/eagleDefender/files/users/'
        hostname = '20.62.171.56'
        port = 22
        username = 'eagleDefender'
        private_key_file = os.path.abspath('Code/eagleDefenderServer_key_1011.pem')
        ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
        ssh_transfer.copy_file_to_remote(pathFile1, directorio_destino, filename1 + ".json")
        ssh_transfer.copy_file_to_remote(pathFile2, directorio_destino, filename2 + ".json")
        ssh_transfer.__exit__()
        # --------------------------------------------------------------------------------------- #

    @classmethod
    def DeleteJson(cls, filename1, filename2):
        """
        Deletes an instances of User stored in a .json file

        :param filename1:
        :param filename2:
        :return:
        """
        pathFile1 = os.path.join("Code/GraphicalUserInterface/Users", filename1 + ".json")
        pathFile2 = os.path.join("Code/GraphicalUserInterface/Users", filename2 + ".json")
        if os.path.exists(pathFile1) and os.path.exists(pathFile2):
            os.remove(pathFile1)
            if pathFile1!=pathFile2:
                os.remove(pathFile2)
            # -------------------------------------Delete Information on the Server-------------------------------#
            hostname = '20.62.171.56'
            port = 22
            username = 'eagleDefender'
            private_key_file = os.path.abspath('Code/eagleDefenderServer_key_1011.pem')
            ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
            ssh_transfer.delete_remote_file(f'/home/eagleDefender/files/users/{filename1}.json')
            if pathFile1!=pathFile2:
                ssh_transfer.delete_remote_file(f'/home/eagleDefender/files/users/{filename2}.json')
            # --------------------------------------Delete Information on the Server------------------------------#

    @classmethod
    def LoadJson(cls, filename):
        """
        Retrieves a user instance stored in a .json file

        :param filename: str
        :return: User
        """
        pathFile = os.path.join("Code/GraphicalUserInterface/Users", f"{filename}.json")

        # -----------------------------------Get Information From Server-------------------------#
        hostname = '20.62.171.56'
        port = 22
        username = 'eagleDefender'
        private_key_file = os.path.abspath('Code/eagleDefenderServer_key_1011.pem')
        ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
        # ---------------------------------------------------------------------------------------#

        if not os.path.exists(pathFile):  
            archivo_remoto = f'/home/eagleDefender/files/users/{filename}.json'
            directorio_destino_local = os.path.abspath("Code/GraphicalUserInterface/Users/")
            ssh_transfer.copy_file_from_remote(archivo_remoto, directorio_destino_local)
        if os.path.exists(pathFile):  
            with open(pathFile, 'r') as json_file:
                userDict = json.load(json_file)
            instance = cls(None, None, None, None, None, None, None, None)
            instance.__init__load(userDict)
            return instance
        else:
            print(f"El archivo {filename} no existe en el sistema")
