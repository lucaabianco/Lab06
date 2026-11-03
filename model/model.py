import database
from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
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

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        connessione = database.DB_connect.get_connection()

        if connessione is None:
            raise ConnectionError("Impossibile connettersi al database")
        lista_strumenti = []
        cursore = connessione.cursor()
        query = 'SELECT * FROM strumento'
        cursore.execute(query)
        rows = cursore.fetchall()
        for row in rows:
            strumento = Strumento(row[0], row[1], row[2], row[3], row[4], row[5])
            lista_strumenti.append(strumento)
        connessione.close()
        cursore.close()
        if lista_strumenti:
            return lista_strumenti
        else:
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        connessione = database.DB_connect.get_connection()

        if connessione is None:
            raise ConnectionError("Impossibile connettersi al database")
        lista_selezionati = []
        cursore = connessione.cursor()
        query = f"""SELECT * 
                            FROM strumento 
                            WHERE strumento.tipo = %s"""
        cursore.execute(query, (tipo,))
        rows = cursore.fetchall()
        for row in rows:
            strumento = Strumento(row[0], row[1], row[2], row[3], row[4], row[5])
            lista_selezionati.append(strumento)
        connessione.close()
        cursore.close()
        if lista_selezionati:
            return lista_selezionati
        else:
            return None
