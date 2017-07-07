#_*_ coding: UTF-8 _*_

from math import sqrt
import numpy as np
import cv2

class Imagem:



    def __init__(self,imgpath):
        self._img = cv2.imread(imgpath)
        self._gray = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
        self._middle = []
        self._lista_distancia = []
        self.face_cascade = cv2.CascadeClassifier('/home/projetoreconhecimentofacial/reconhecimentofacial/static/imagens/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('/home/projetoreconhecimentofacial/reconhecimentofacial/static/imagens/haarcascade_eye.xml')
        self.nose_cascade = cv2.CascadeClassifier('/home/projetoreconhecimentofacial/reconhecimentofacial/static/imagens/haarcascade_mcs_nose.xml')
        self.mouth_cascade = cv2.CascadeClassifier('/home/projetoreconhecimentofacial/reconhecimentofacial/static/imagens/haarcascade_mcs_mouth.xml')

    def _marcarFace(self,color,cascade):
        elementos = cascade.detectMultiScale(self._gray,1.05,5,0)
        for (x,y,w,h) in elementos:
            cv2.rectangle(self._img,(x,y),(x+w,y+h),color,2)
            roi_gray = self._gray[y:y+h, x:x+w]
            roi_color = self._img[y:y+h, x:x+w]
            yield roi_gray,roi_color

    def _marcarElementos(self,roi_color,roi_gray,color, cascade):
        elementos = cascade.detectMultiScale(roi_gray,1.05,5,0)
        for (x, y, w, h) in elementos:
            cv2.rectangle(roi_color, (x, y), (x + w, y + h),color, 2)
            roi_gray[y:y +h, x:x + w] = 0
            yield (x+w/2,y+h/2)

    def marcarFace(self):
        for (roi_gray, roi_color) in self._marcarFace((255, 0, 0), self.face_cascade):
            for middle_element in self._marcarElementos(roi_color, roi_gray, (0, 255, 0), self.eye_cascade):
                self._middle.append(middle_element)
            for middle_element in self._marcarElementos(roi_color, roi_gray, (0, 0, 255), self.nose_cascade):
                self._middle.append(middle_element)
            for middle_element in self._marcarElementos(roi_color, roi_gray, (0, 0, 0), self.mouth_cascade):
                self._middle.append(middle_element)
            self._calcularDistancia(roi_color)

    def _calcularDistancia(self,roi_color):
        for middle_element1 in self._middle:
           for middle_element2 in self._middle:
               if (middle_element1 != middle_element2):
                   cv2.line(roi_color, middle_element1, middle_element2, (255, 255, 255), 2)
                   self._lista_distancia.append(sqrt((middle_element1[0] - middle_element2[0])** 2 + ((middle_element1[1] - middle_element2[1])** 2)))
               else:
                   break
    def compararImagens(self,img):
        total = 0
        for i in range(len(self._lista_distancia)):
            total += (self._lista_distancia[i] - img._lista_distancia[i]) ** 2
        return sqrt(total)

    def mostrarImagem(self):
        cv2.imshow('img', self._img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def SalvarImagem(self,path):
        cv2.imwrite(path,self._img)

#_main_
