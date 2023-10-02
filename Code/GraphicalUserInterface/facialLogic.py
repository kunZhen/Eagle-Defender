import numpy as np
import cv2


class facialRecognogtion:
    def __init__(self,userName):
        self.userName=userName
    def getFaceInformation(self,option): 
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while True:
            ret, frame= cap.read()

        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(frame,1.3,5)
            for(x,y,w,h) in faces: 
                if(option!="takeAPhoto"):
                    cv2.rectangle(frame, (x,y), (x+w,x+y), (255,0,0, 5))
                    roi_gray = gray[y:y+w, x:x+w]
        
            cv2.imshow('frame', frame)

            if cv2.waitKey(1)== ord('q'):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                if option=="saveInformation":
                    cv2.imwrite("rostros/"+self.userName+".jpg",roi_gray)
                elif option=="takeAPhoto":
                    cv2.imwrite("perfiles/"+self.userName+".jpg",frame)
                else:
                    cv2.imwrite("rostros/"+self.userName+"LOG.jpg",roi_gray)
                break

    def comparation(self): 
        regFace = cv2.imread("rostros/"+self.userName+".jpg",0)     #Importamos el rostro del registro
        logFace = cv2.imread("rostros/"+self.userName+"LOG.jpg",0) 
        orb= cv2.ORB_create()
        kpa, descriptorLogFace = orb.detectAndCompute(logFace, None) 
        kpb, descriptorRegFace = orb.detectAndCompute(regFace, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #Creamos comparador de fuerza

        matches = comp.match(descriptorLogFace, descriptorRegFace)  #Aplicamos el comparador a los descriptores

        similitudes = [i for i in matches if i.distance < 70] #Extraemos las regiones similares en base a los puntos claves
   
        if len(matches) !=0: 
            print(len(similitudes)/len(matches))
            if len(similitudes)/len(matches)>0.90:
                return True
            return False
        return False
    def savePhoto(self,path):

        imagen = cv2.imread(path)

        if imagen is not None:
            # Guardar la imagen en una carpeta específica (en este caso, "carpeta_destino")
            cv2.imwrite('rostros/'+self.userName+".png", imagen)
            print("Imagen guardada correctamente.")
        else:
            print("No se pudo cargar la imagen.")
