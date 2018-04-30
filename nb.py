#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nb.py
------------

Clase genérica para realizar el método de clasificación de naive bayes.

"""

__author__ = 'juliowaissman'


class NaiveBayes:
    """
    Clase genérica del clasificador naive bayes, para entradas con
    dominio discreto y finito

    """

    def __init__(self, vals=None, clases=None):
        """Inicializa el algoritmo de NB

        @param vals: diccionario donde vals[var] = set([val1, ..., valm])
                     son los valores que puede tomar la variable var.
                     Si vals es None, entonces vals se construye con los
                     valores que se tienen en el conjunto d aprendizaje.

        @param clases: es un conjuto (o lista) [clase1, ..., clasek],
                       con el nombre de las k clases que nos
                       interesan.

        """
        self.vals = vals
        self.clases = clases
        self.num_datos = 0
        if vals is not None and cls_nombre is not None:
            self.genera_cuentas()
        else:
            self.cuentas = None

    def genera_cuentas(self):
        """
        Para poder hacer un aprendizaje incremental, esto es, poder
        agregar nuevos ejemplos de aprendizaje en linea, en lugar de
        guardar las CPTs, vamos a utilizar un diccionario con
        frecuencias.

        self.frecuencias['clases'] es un diccionario, donde en cada
        nombre de clase guarda la frecuencia encontrada (esto permite
        inclusive agregar nuevas clases en linea). Así, por cada valor
        en la lista self.cls_nombre habra una entrada del diccionario
        self.frecuencias['clases].

        Por cada variable habrá otros dicionarios, de manera que
        self.frecuencias[var][clase][val] es el numero de ocurrencias
        del valor val, de la variable var, cuando los datos están
        asociados a la clase clase.

        """
        self.frecuencias = {var: {clase: {val: 0 for val in self.vals[var]}
                                  for clase in self.clases}
                            for var in self.vars}
        self.frecuencias['clases'] = {clase: 0 for clase in self.clases}

        self.log_probs = {var: {clase: {val: 0 for val in self.vals[var]}
                                  for clase in self.clases}
                            for var in self.vars}
        self.log_probs['clases'] = {clase: 0 for clase in self.clases}

    def aprende(self, datos, clases):
        """
        Aprende los valores de la CPT, es el trabajo a realizar

        """
        if self.vals is None:
            self.vals = {i: set([datos[j][i]
                                            for j in range(len(datos))])
                         for i in range(len(self.vars))}
            self.clases = set(clases)
            self.genera_cuentas()

        # Primero se actualiza el valor de las frecuencias para calcular la
        # probabilidad a priori y se calcula el logaritmo de las probabilidades
        for clase in self.clases:

            #  ---------------------------------------------------
            #  agregar aqui el código
            pass
            #  ---------------------------------------------------

        # Ahora se actualiza el valor de las frecuencias por cada atributo y
        # para cada posible clase para calcular las verosimilitudes
        # y se calcula el logaritmo de las probabilidades.
        #
        # Recuerda utilizar el modificador de Laplace.
        for variable in self.vals.keys():
            for clase in self.clases:

                #  --------------------------------------------------
                #  agregar aquí el código
                pass
                #  --------------------------------------------------

    def reconoce(self, datos):
        """
        Identifica la clase a la que pertenece cada uno de los datos que
        se solicite, de acuerdo al clasificador.

        @param datos = [dato(1), dato(2), ...] es una lista de datos
                       para clasificar, donde dato(i) = [dato(i,1),
                       ..., dato(i,n)] es el valor del dato en cada
                       atributo. Hay que recordar que se puede
                       utilizar el método de naive bayes si no se
                       conocen todos los atributos. Si un atributo no
                       se conoce dato(i,n) = None.

        """
        clases = []

        #  ---------------------------------------------------
        #  agregar aquí el código
        #  ---------------------------------------------------

        return clases


def test():
    """
    Esta funcion sirve para poder ir probando y corrigiendo el programa.

    Hay 3 pruebas básicas, una para probar la inicialización, otra
    para probar el aprendizaje (o el llenado de cuentas) y la 3ra para
    probar si el reconocimiento se hace correctamente. hasta que pasen
    todas las pruebas no hay que pasar al problema que se encuentra en
    el archivo naive_bayes.py

    """

    valores = {'uno': {1, 2, 3, 4}, 'dos': {10, 20}}
    clases = {'N', 'P'}
    nb = NaiveBayes(valores, clases)

    assert nb.frecuencias['clases'] == {'N': 0, 'P': 0}
    assert nb.frecuencias['uno']['N'] == {1: 0, 2: 0, 3: 0, 4: 0}

    print("La primera prueba se completo con exito")

    data = [[1, 10], [2, 10], [3, 10], [4, 10],
            [1, 20], [2, 20], [3, 20], [4, 20]]
    clases = ['N', 'P', 'P', 'N', 'N', 'P', 'N', 'N']

    nb = NaiveBayes()

    assert nb.frecuencias is None

    nb.aprende(data, clases)
    assert nb.frecuencias['clases'] == {'N': 5, 'P': 3}
    assert nb.frecuencias[0]['N'] == {1: 2, 2: 0, 3: 1, 4: 2}
    assert nb.cuentas[1]['P'] == {10: 2, 20: 1}
    assert nb.cuentas[1]['N'] == {10: 2, 20: 3}

    print("La segunda prueba se completó con exito")

    data_test = [[2, 20], [4, 10]]
    clase_test = nb.reconoce(data_test)
    assert clase_test == ['P', 'N']

    print("La tercera prueba se completó con exito")


if __name__ == "__main__":
    test()
