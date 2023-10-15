import numpy as np
import cv2
import os

from SSHFileTransfer import SSHFileTransfer


class facialRecognogtion:
    def __init__(self, userName):
        self.userName = userName

    def getFaceInformation(self, option):

        port = 22  # El puerto SSH predeterminado es 22
        username = 'eagleDefender'  # Tu nombre de usuario en la máquina virtual
        private_key_file = os.path.abspath('eagleDefenderServer_key_1011.pem')
        directorio_destino = '/home/eagleDefender/files/photos/'
        directorio_destino_1 = '/home/eagleDefender/files/biometricalData/'
        hostname = '20.62.171.56'  # Cambia esto a la dirección IP de tu máquina virtual

        ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)

        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(os.path.abspath("haarcascade_frontalface_default.xml"))
        while True:
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            for (x, y, w, h) in faces:
                if (option != "takeAPhoto"):
                    cv2.rectangle(frame, (x, y), (x + w, x + y), (255, 0, 0, 5))
                    roi_gray = gray[y:y + w, x:x + w]

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('q'):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if option == "saveInformation":
                    cv2.imwrite("rostros/" + self.userName + ".jpg", roi_gray)
                    ssh_transfer.copy_file_to_remote(os.path.abspath("rostros/" + self.userName + ".jpg"),
                                                     directorio_destino_1, self.userName + ".jpg")
                    ssh_transfer.__exit__()

                elif option == "takeAPhoto":
                    cv2.imwrite("perfiles/" + self.userName + ".jpg", frame)
                    ssh_transfer.copy_file_to_remote(os.path.abspath("perfiles/" + self.userName + ".jpg"),
                                                     directorio_destino, self.userName + ".jpg")
                    ssh_transfer.__exit__()
                else:
                    cv2.imwrite("rostros/" + self.userName + "LOG.jpg", roi_gray)
                break

    def comparation(self):
        regFace = cv2.imread("rostros/" + self.userName + ".jpg", 0)  # Importamos el rostro del registro
        logFace = cv2.imread("rostros/" + self.userName + "LOG.jpg", 0)
        orb = cv2.ORB_create()
        kpa, descriptorLogFace = orb.detectAndCompute(logFace, None)
        kpb, descriptorRegFace = orb.detectAndCompute(regFace, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Creamos comparador de fuerza

        matches = comp.match(descriptorLogFace, descriptorRegFace)  # Aplicamos el comparador a los descriptores

        similitudes = [i for i in matches if
                       i.distance < 80]  # Extraemos las regiones similares en base a los puntos claves

        if len(matches) != 0:
            print(len(similitudes) / len(matches))
            if len(similitudes) / len(matches) > 0.90:
                return True
            return False
        return False

    def savePhoto(self, path):

        imagen = cv2.imread(path)

        if imagen is not None:
            port = 22  # El puerto SSH predeterminado es 22
            username = 'eagleDefender'  # Tu nombre de usuario en la máquina virtual
            private_key_file = os.path.abspath('eagleDefenderServer_key_1011.pem')
            directorio_destino = '/home/eagleDefender/files/photos/'
            hostname = '20.62.171.56'  # Cambia esto a la dirección IP de tu máquina virtual
            ssh_transfer = SSHFileTransfer(hostname, port, username, private_key_file)
            # Guardar la imagen en una carpeta específica (en este caso, "carpeta_destino")
            cv2.imwrite('perfiles/' + self.userName + ".jpg", imagen)
            ssh_transfer.copy_file_to_remote(os.path.abspath("perfiles/" + self.userName + ".jpg"), directorio_destino,
                                             self.userName + ".jpg")
            ssh_transfer.__exit__()
            print("Imagen guardada correctamente.")
        else:
            print("No se pudo cargar la imagen.")

    def overWritePerfil(self, path):
        path = 'perfiles/' + path + ".jpg"
        print(path)
        imagen = cv2.imread(path)

        if imagen is not None:
            # Guardar la imagen en una carpeta específica (en este caso, "carpeta_destino")
            cv2.imwrite('perfiles/' + self.userName + ".jpg", imagen)
            print("Imagen guardada correctamente.")
        else:
            print("No se pudo cargar la imagen.")

    def overWriteBiometricalData(self, path):
        path = "rostros/" + path + ".jpg"

        imagen = cv2.imread(path)
        print(path)
        if imagen is not None:
            # Guardar la imagen en una carpeta específica (en este caso, "carpeta_destino")
            cv2.imwrite('rostros/' + self.userName + ".jpg", imagen)
            print("Imagen guardada correctamente.")
        else:
            print("No se pudo cargar la imagen.")
