import time
#import random
#from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import datetime
#from selenium.webdriver.common.action_chains import ActionChains

tam = 10


class Examen():
    def inicio(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)

        self.datos = {'nombre': [], 'apellido': [], 'correo': []}

    def fin(self):
        self.driver.quit()

    def get_nombres(self):
        nom = []
        ape = []
        nom.append("Andres")
        nom.append("Pablo")
        nom.append("Pedro")
        nom.append("Carlos")
        nom.append("Erick")
        nom.append("Sandro")
        nom.append("Jorge")
        nom.append("Ramiro")
        nom.append("Paul")
        nom.append("Saul")
        ape.append("Loja")
        ape.append("Rodrigues")
        ape.append("Morocho")
        ape.append("Perez")
        ape.append("Azul")
        ape.append("Verde")
        ape.append("Rozado")
        ape.append("Jam")
        ape.append("Yes")
        ape.append("NONO")
        self.datos['nombre'] = nom
        self.datos['apellido'] = ape

    def get_correos(self):
        cor = []
        est = []
        cor.append("aloja619@gmail.com")
        cor.append("619aloja@gmail.com")
        cor.append("aloja619@yahoo.com")
        cor.append("alojam@est.ups.edu.ec")
        cor.append("andres.loja@bestpointauditores.com")
        cor.append("aloja619@gmail.com")
        cor.append("619aloja@gmail.com")
        cor.append("aloja619@yahoo.com")
        cor.append("alojam@est.ups.edu.ec")
        cor.append("andres.loja@bestpointauditores.com")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        est.append("activo")
        self.datos['correo'] = cor
        self.datos['estado'] = est

    def to_correos(self):
        txt = ""
        for i in range(0, len(self.datos['correo'])):
            txt = txt + self.datos['correo'][i] + ","
        return txt

    def escribir(self, body):
        for i in range(0, len(self.datos['nombre'])):
            body.send_keys(self.datos["nombre"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["apellido"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["correo"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["estado"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(Keys.ENTER)
            
        time.sleep(1)

    def login(self, id, password):
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_element_by_id("email")
        email.send_keys(id)
        Password = self.driver.find_element_by_id("pass")
        Password.send_keys(password)
        self.driver.find_element_by_id("u_0_d").click()

    def post_content(self):
        time.sleep(1)
        self.driver.find_element_by_css_selector(".jm1wdb64 > .a8c37x1j").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".notranslate")
        activepostarea = self.driver.switch_to_active_element()
        activepostarea.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        today = date.today()
        activepostarea.send_keys(format(today.day),"/",format(today.month),"/",format(today.year)," Todo 6 Vamos alvarito")
        e = self.driver.find_element_by_css_selector(
            ".k4urcfbm > .oajrlxb2 > .rq0escxv > .rq0escxv > .d2edcug0 > .a8c37x1j")
        e.click()
        time.sleep(5)

    def copiar_imagen(self):
        self.driver.get(
            "https://github.com/Andres0Loja/Simulacion/blob/main/imagen.png?raw=true")
        ele = self.driver.find_element_by_css_selector("img")
        ele.click()
        ele.click()
        activepostarea = self.driver.switch_to_active_element()
        activepostarea.send_keys(Keys.CONTROL, 'c')

    def ubicar_celdas(self, txt):
        seldas = self.driver.find_element_by_id('t-name-box')
        seldas.clear()
        seldas.send_keys(txt)
        time.sleep(1)
        seldas.send_keys(Keys.ENTER)
        time.sleep(1)

    def escribir_exel(self):
        self.driver.get(
            "https://docs.google.com/spreadsheets/d/1FcpyXM5XCTuk1xBGITsEoaYJkaRD4MeemBWdwt5K5nw/edit?usp=sharing")
        self.ubicar_celdas("A2:D20")
        cel_del = self.driver.find_element_by_id('waffle-rich-text-editor')
        cel_del.send_keys(Keys.DELETE)
        time.sleep(1)
        self.ubicar_celdas("A2")
        body = self.driver.find_element_by_class_name('cell-input')
        self.escribir(body)

    def correo(self, correos, asunto="Flyer Elecciones"):
        self.driver.get(
            'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1612797357&rver=7.0.6737.0&wp=MBI_SSL'
            '&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3db97197b5-ba7d-e675-321b'
            '-8f36488fb774&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

        email = self.driver.find_element_by_name('loginfmt')
        email.send_keys('aloja619@hotmail.com')
        time.sleep(1)
        email.send_keys(Keys.ENTER)
        pasw = self.driver.find_element_by_name('passwd')
        pasw.send_keys('enanopavo2L6')
        time.sleep(1)
        self.driver.find_element_by_id('idSIButton9').click()
        time.sleep(1)
        self.driver.find_element_by_id("id__5").click()
        time.sleep(3)
        para = self.driver.find_element_by_class_name("ms-BasePicker-input")
        para.send_keys(correos)
        time.sleep(1)
        para.send_keys(Keys.TAB)
        time.sleep(1)
        asu = self.driver.find_element_by_class_name("ms-TextField-field")
        asu.send_keys(asunto)
        time.sleep(1)
        asu.send_keys(Keys.TAB)
        mot = self.driver.find_element_by_class_name("_4utP_vaqQ3UQZH0GEBVQe")
        mot.send_keys(asunto)
        time.sleep(1)
        mot.send_keys(Keys.CONTROL, 'v')
        time.sleep(7)
        mot.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(2)
        self.driver.get("https://outlook.live.com/mail/0/sentitems")
        
    def comentario(self):
        self.driver.get("https://www.google.com/")
        self.driver.get('https://www.facebook.com/andres.loja.9/')
        come=self.driver.find_element_by_id("mount_0_0")
        #a=come.get("mount_0_0")
        print(come)
        


if __name__ == '__main__':
    t = Examen()
    t.inicio()
    t.get_correos()
    t.get_nombres()
    #t.escribir_exel()
    t.copiar_imagen()
    t.login("aloja619@gmail.com", "enanopavo2L6")
    t.post_content()
    t.correo(t.to_correos(), "Examen Simulación")
    #t.comentario()