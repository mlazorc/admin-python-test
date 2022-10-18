import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Funciones():

    def __init__(self, driver):
        self.driver = driver


    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, url, Tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        print("Página abierta")
        return t

    def Texto_xpath(self, xpath, texto, Tiempo):
        valor = self.driver.find_element(By.XPATH, xpath)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def Texto_xpath_valida(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            t = time.sleep(tiempo)
            print("Se completó el campo {}".format(xpath))
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    def check_xpath(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("ELemento visible {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)
            return t

    def check_xpath_multiples(self, tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val = Select(val)
                val.select_by_value(num)
                print("Click en el elemento {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento" + num)
                return t

    def IngresarTexto(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            print("Elemento {} visible".format(xpath))
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se pudo localizar el elemento")
            return t

    def dar_click(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No fue posible localizar el elemento {}".format(xpath))
            return t
