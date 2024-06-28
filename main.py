import tkinter as tk
from tkinter import filedialog
import pywhatkit as kit
import os
import csv
from datetime import datetime, timedelta

# Função para postar no WhatsApp
def postar_whatsapp(imagens, descricoes, grupo):
    for imagem in imagens:
        nome_arquivo = os.path.basename(imagem)
        nome_produto = os.path.splitext(nome_arquivo)[0]  # Remove a extensão do arquivo
        mensagem = descricoes.get(nome_produto, 'Descrição não encontrada')

        # Enviar mensagem para o grupo no WhatsApp imediatamente
        kit.sendwhatmsg_to_group(grupo, mensagem, datetime.now().hour, datetime.now().minute + 1)  

# Função para postar no Telegram
def postar_telegram(imagens, descricoes):
    for imagem in imagens:
        nome_arquivo = os.path.basename(imagem)
        nome_produto = os.path.splitext(nome_arquivo)[0]  # Remove a extensão do arquivo
        descricao = descricoes.get(nome_produto, 'Descrição não encontrada')
        # Implemente aqui a lógica para postar no Telegram
        print(f"Postando no Telegram: {descricao}")

# Função para postar no Instagram
def postar_instagram(imagens, descricoes):
    for imagem in imagens:
        nome_arquivo = os.path.basename(imagem)
        nome_produto = os.path.splitext(nome_arquivo)[0]  # Remove a extensão do arquivo
        descricao = descricoes.get(nome_produto, 'Descrição não encontrada')
        # Implemente aqui a lógica para postar no Instagram
        print(f"Postando no Instagram: {descricao}")

# Função para ler imagens e descrições
def ler_imagens_descricoes(pasta_imagens, arquivo_descricoes):
    imagens = sorted([os.path.join(pasta_imagens, img) for img in os.listdir(pasta_imagens) if img.endswith('.png')])
    descricoes = {}
    with open(arquivo_descricoes, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                nome_produto = row['Nome do Produto'].strip()
                descricao = f"{row['de:']} {row['por:']} {row['Compre aqui:']}".strip()
                descricoes[nome_produto] = descricao
            except ValueError:
                print(f"Erro ao processar linha: {row}")
    return imagens, descricoes

# Interface Gráfica
def criar_interface():
    def selecionar_imagens():
        arquivos = filedialog.askopenfilenames(initialdir="E:/ProjetosPython/Publicacao/Imagens/AMAZON", title="Selecione as Imagens", filetypes=(("png files", "*.png"), ("all files", "*.*")))
        if arquivos:
            entrada_imagens.delete(0, tk.END)
            for arquivo in arquivos:
                entrada_imagens.insert(tk.END, arquivo + ";")
            entrada_imagens.config(state=tk.NORMAL)

    def selecionar_arquivo_descricoes():
        arquivo = filedialog.askopenfilename(initialdir="E:/ProjetosPython/Publicacao/Imagens/AMAZON", title="Selecione o Arquivo de Descrições", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if arquivo:
            entrada_descricoes.delete(0, tk.END)
            entrada_descricoes.insert(0, arquivo)
            global imagens, descricoes
            imagens, descricoes = ler_imagens_descricoes("E:/ProjetosPython/Publicacao/Imagens/AMAZON", arquivo)

    def postar():
        imagens_selecionadas = entrada_imagens.get().split(";")
        imagens_selecionadas = [img.strip() for img in imagens_selecionadas if img.strip()]  # Remove itens vazios

        # Verifica se foi selecionada alguma plataforma
        if var_whatsapp.get():
            grupo = "Promoções do Dia #10"  # Nome do grupo para o WhatsApp
            postar_whatsapp(imagens_selecionadas, descricoes, grupo)
        
        if var_telegram.get():
            postar_telegram(imagens_selecionadas, descricoes)
        
        if var_instagram.get():
            postar_instagram(imagens_selecionadas, descricoes)

    # Inicializa as variáveis de imagens e descrições
    imagens, descricoes = [], {}

    janela = tk.Tk()
    janela.title("Postagem Automática")

    # Frames para organizar os widgets
    frame_descricoes = tk.Frame(janela)
    frame_descricoes.grid(row=0, column=0, padx=10, pady=10)

    frame_imagens = tk.Frame(janela)
    frame_imagens.grid(row=1, column=0, padx=10, pady=10)

    frame_opcoes = tk.Frame(janela)
    frame_opcoes.grid(row=2, column=0, padx=10, pady=10)

    # Widgets para o arquivo de descrições
    tk.Label(frame_descricoes, text="Arquivo de Descrições:").grid(row=0, column=0, sticky=tk.W)
    entrada_descricoes = tk.Entry(frame_descricoes, width=50)
    entrada_descricoes.grid(row=0, column=1, padx=5)
    tk.Button(frame_descricoes, text="Selecionar", command=selecionar_arquivo_descricoes).grid(row=0, column=2, padx=5)

    # Widgets para as imagens
    tk.Label(frame_imagens, text="Imagens:").grid(row=0, column=0, sticky=tk.W)
    entrada_imagens = tk.Entry(frame_imagens, width=50)
    entrada_imagens.grid(row=0, column=1, padx=5)
    entrada_imagens.config(state=tk.DISABLED)  # Inicialmente desativado
    tk.Button(frame_imagens, text="Selecionar", command=selecionar_imagens).grid(row=0, column=2, padx=5)

    # Checkbuttons para escolha das plataformas
    var_whatsapp = tk.BooleanVar()
    var_telegram = tk.BooleanVar()
    var_instagram = tk.BooleanVar()

    tk.Checkbutton(frame_opcoes, text="WhatsApp", variable=var_whatsapp).grid(row=0, column=0, padx=5, sticky=tk.W)
    tk.Checkbutton(frame_opcoes, text="Telegram", variable=var_telegram).grid(row=0, column=1, padx=5, sticky=tk.W)
    tk.Checkbutton(frame_opcoes, text="Instagram", variable=var_instagram).grid(row=0, column=2, padx=5, sticky=tk.W)

    # Botão para postar
    tk.Button(janela, text="Postar", command=postar).grid(row=3, column=0, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()