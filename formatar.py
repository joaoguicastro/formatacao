import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import re

def corrigir_numero(numero):
    numero_limpo = re.sub(r'\D', '', numero)
    if len(numero_limpo) == 11 and numero_limpo[2] == '9':
        numero_corrigido = numero_limpo[:2] + numero_limpo[3:]
        return numero_corrigido
    return numero_limpo

def carregar_arquivo():
    arquivo_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if arquivo_path:
        df = pd.read_excel(arquivo_path)
        df['telefone'] = df['telefone'].apply(corrigir_numero)
        salvar_arquivo(df)

def salvar_arquivo(df):
    arquivo_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if arquivo_path:
        df.to_excel(arquivo_path, index=False)
        messagebox.showinfo("Informação", "Arquivo salvo com sucesso!")

app = tk.Tk()
app.title("Correção de Números de Telefone")

label = tk.Label(app, text="Selecione o arquivo Excel com os números de telefone dos alunos:")
label.pack(pady=10)

botao_carregar = tk.Button(app, text="Carregar Arquivo", command=carregar_arquivo)
botao_carregar.pack(pady=10)

app.mainloop()
