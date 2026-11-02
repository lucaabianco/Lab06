import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_strumenti(self, e):
        lista_DB = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()

        if lista_DB is not None:
            for strumento in lista_DB:
                self._view.lista_strumenti.controls.append(ft.Text(str(strumento)))
        else:
            self._view.show_alert("Nessuno strumento trovato")

        self._view.update()

    def cerca_per_tipo(self,e):
        tipo = self._view.input_tipo_strumento.value
        lista_risultati = self._model.cerca_strumenti_per_tipo(tipo)
        self._view.lista_strumenti.controls.clear()

        if tipo is None:
            self._view.show_alert("Inserisci un tipo valido")
        else:
            if lista_risultati is not None:
                for strumento in lista_risultati:
                    self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(strumento)))
            else:
                self._view.show_alert("Nessuno strumento trovato")

        self._view.update()