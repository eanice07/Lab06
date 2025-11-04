import flet as ft
from UI.view import View
from model.model import Autonoleggio


'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
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

    def handler_btn_mostra_automobili(self,e):

        automobili = self._model.get_automobili()
        self._view.lista_automobili.clean()

        if automobili is None or len(automobili) == 0:
            self._view.lista_automobili.controls.append(
                ft.Text("❌ Nessuna automobile trovata nel database.")
            )
        else:
            for auto in automobili:
                testo_auto = f"{auto.id_auto} - {auto.marca} {auto.modello} ({auto.anno})"
                self._view.lista_automobili.controls.append(ft.Text(testo_auto))

        self._view.update_page()

    def handler_btn_cerca_modello(self,e):

        modello = self._view.input_modello.value.strip()
        self._view.lista_risultati.clean()

        if not modello:
            self._view.show_alert(" Inserisci un modello per effettuare la ricerca.")
            return

        automobili = self._model.cerca_automobili_per_modello(modello)

        if automobili is None or len(automobili) == 0:
            self._view.lista_risultati.controls.append(
                ft.Text(f"❌ Nessuna automobile trovata per il modello '{modello}'.")
            )
        else:
            for auto in automobili:
                testo_auto = f"{auto.id_auto} - {auto.marca} {auto.modello} ({auto.anno})"
                self._view.lista_risultati.controls.append(ft.Text(testo_auto))

        self._view.update_page()


