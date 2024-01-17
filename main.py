import tkinter as tk
from tkinter import messagebox

class CalculadoraDosagemMedicamento:
    def __init__(self, root):
        # ... (code for initializing the GUI elements)

        # Adicionar campos de entrada (entry)
        self.entry_med_nome = tk.Entry(root)
        self.entry_dose_prescrita = tk.Entry(root)
        self.entry_peso_paciente = tk.Entry(root)

        # Adicionar placeholders
        self.entry_med_nome.insert(0, "Digite o nome do medicamento")
        self.entry_dose_prescrita.insert(0, "Insira a dose prescrita")
        self.entry_peso_paciente.insert(0, "Insira o peso do paciente")

        # ... (same as before)

        # Rótulos para informações adicionais do medicamento
        self.label_apresentacao = tk.Label(root, text="Apresentação:")
        self.label_apresentacao.pack()

        self.label_via = tk.Label(root, text="Via de Administração:")
        self.label_via.pack()

        # Rótulos para informações adicionais sobre a dosagem calculada
        self.label_dosagem_max = tk.Label(root, text="Dosagem Máxima Recomendada:")
        self.label_dosagem_max.pack()

        self.label_faixa_segura = tk.Label(root, text="Faixa Segura de Dosagem:")
        self.label_faixa_segura.pack()

        # Rótulo para dosagem calculada
        self.label_dosagem_calculada = tk.Label(root, text="Dosagem Calculada:")
        self.label_dosagem_calculada.pack()

        # Rótulo para resultado do teste de faixa segura
        self.label_resultado_faixa_segura = tk.Label(root, text="")
        self.label_resultado_faixa_segura.pack()

        # Botão para calcular dosagem
        self.btn_calcular = tk.Button(root, text="Calcular Dosagem", command=self.calcular_dosagem)
        self.btn_calcular.pack()

        # Botão para limpar os dados
        self.btn_limpar = tk.Button(root, text="Limpar Dados", command=self.limpar_dados)
        self.btn_limpar.pack()

    # ... (same as before)
