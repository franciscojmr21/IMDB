import tkinter as tk


class CTkListbox(tk.Listbox):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.selected = []

        self.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        # Reiniciar la lista de elementos seleccionados
        self.selected = []

        # Obtener los índices de los elementos seleccionados
        selection = event.widget.curselection()

        # Agregar los elementos seleccionados a la lista de elementos seleccionados
        for i in selection:
            self.selected.append(event.widget.get(i))

    def get_selected(self):
        return self.selected
