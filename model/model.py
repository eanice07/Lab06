import mysql

from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            query= "SELECT * FROM automobili"
            cursor.execute(query)
            results = cursor.fetchall()

            automobili = [Automobile(*row) for row in results]

            cursor.close()
            cnx.close()

            return automobili if automobili else None
        except Exception as e:
            print(f"❌ Errore durante la lettura delle automobili dal database: {e}")
            return None



    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        try:
            cnx = get_connection()
            cursor = cnx.cursor()

            query= """SELECT id_auto, marca, modello,anno, disponibile
                    FROM automobili
                    WHERE modello=%s"""
            cursor.execute(query, (modello,))
            results = cursor.fetchall()

            automobili =[Automobile(*row) for row in results]

            cursor.close()
            cnx.close()

            return automobili if automobili else None
        except Exception as e:
            print(f"❌ Errore durante la ricerca per modello '{modello}': {e}")
            return None
