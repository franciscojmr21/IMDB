import tkinter as tk
from tkinter import ttk

class CTkTable:
    def __init__(self, parent, headers, rows):
        self.parent = parent

        # Crear un canvas para la tabla y agregar barras de desplazamiento
        self.canvas = tk.Canvas(parent)
        self.scrollbar_y = tk.Scrollbar(parent, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_x = tk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Agregar la tabla al canvas
        self.table = ttk.Treeview(self.canvas, columns=headers, show='headings')
        for header in headers:
            self.table.heading(header, text=header.title())
        for row in rows:
            self.table.insert('', 'end', values=row)

        # Configurar el canvas para que se expanda junto con la ventana
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.table, anchor=tk.NW)
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

    def _on_canvas_configure(self, event):
        # Ajustar el tamaño del canvas para que sea lo suficientemente grande para mostrar la tabla completa
        canvas_width = max(self.table.winfo_reqwidth(), event.width)
        canvas_height = max(self.table.winfo_reqheight(), event.height)
        self.canvas.configure(scrollregion=(0, 0, canvas_width, canvas_height))

    def remove_table(self):
        # Borrar la tabla del canvas
        self.scrollbar_y.pack_forget()
        self.scrollbar_x.pack_forget()
        self.table.pack_forget()
        self.canvas.pack_forget()

