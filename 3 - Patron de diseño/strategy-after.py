import string
import random
from typing import List
from abc import ABC, abstractmethod


def generar_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SoporteTiquet:

    def __init__(self, cliente, inconveniente):
        self.id = generar_id()
        self.cliente = cliente
        self.inconveniente = inconveniente


class EstrategiaOrdenTicket(ABC):
    @abstractmethod
    def crear_orden(self, list: List[SoporteTiquet]) -> List[SoporteTiquet]:
        pass


class PrimeroLoPrimero(EstrategiaOrdenTicket):
    def crear_orden(self, list: List[SoporteTiquet]) -> List[SoporteTiquet]:
        return list.copy()


class Siguiente(EstrategiaOrdenTicket):
    def crear_orden(self, list: List[SoporteTiquet]) -> List[SoporteTiquet]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class AlAzar(EstrategiaOrdenTicket):
    def crear_orden(self, list: List[SoporteTiquet]) -> List[SoporteTiquet]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class AgujeroNegro(EstrategiaOrdenTicket):
    def crear_orden(self, list: List[SoporteTiquet]) -> List[SoporteTiquet]:
        return []


class SoporteCliente:

    def __init__(self, EstrategiaProceso: EstrategiaOrdenTicket):
        self.tickets = []
        self.EstrategiaProceso = EstrategiaProceso

    def crear_ticket(self, cliente, inconveniente):
        self.tickets.append(SoporteTiquet(cliente, inconveniente))

    def procesar_tiquetes(self):
        # create the ordered list
        ticket_list = self.EstrategiaProceso.crear_orden(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.procesar_ticket(ticket)

    def procesar_ticket(self, ticket: SoporteTiquet):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.cliente}")
        print(f"Issue: {ticket.inconveniente}")
        print("==================================")


# create the application
app = SoporteCliente(AlAzar())

# register a few tickets
app.crear_ticket("John Smith", "My computer makes strange sounds!")
app.crear_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.crear_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.procesar_tiquetes()
