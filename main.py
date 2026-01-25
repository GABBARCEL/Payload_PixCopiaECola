import customtkinter as CTK
import genQrCode
from PIL import Image
import link


janela = CTK.CTk()
janela.title("Pix copia e cola")
janela.geometry("800x600")


#CHAT GPT
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# Isso aqui modifica conforme o código roda
LabelErro = CTK.CTkLabel(janela, text=f"", text_color="red")

def CommandQrcode():
    LabelErro.configure(text="", text_color="red")

    if chavePixEntry.get() == "":
        LabelErro.configure(text="A chave pix é obrigatória!")
        return
    if valorPixEntry.get() == "":
        LabelErro.configure(text="O valor do pix é obrigatório!")
        return
    if nomeEntry.get() == "":
        LabelErro.configure(text="O nome do recebedor é obrigatório!")
        return
    if cidadeEntry.get() == "":
        LabelErro.configure(text="A cidade do recebedor é obrigatória!")
        return

    try:
        valorLocal = float(valorPixEntry.get())
    except ValueError:
        LabelErro.configure(text="Valor em formato errado. Use decimal. Ex: 100.99")
        return

    try:
        payload = link.genLink(
            chavePixEntry.get(),
            valorLocal,
            nomeEntry.get(),
            cidadeEntry.get(),
            txtIdEntry.get() or "***"
        )
    except Exception as e:
        LabelErro.configure(text=f"Erro ao gerar link: {e}")
        return

    LabelErro.configure(text="Sucesso!", text_color="green")

    qr_pil = genQrCode.genQrCode(payload)
    qr_ctk = CTK.CTkImage(
        light_image=qr_pil,
        dark_image=qr_pil,
        size=(280, 280)
    )

    qrLabel.configure(image=qr_ctk)

# "h1" da janela
tituloAcima = CTK.CTkLabel(janela, text="Crie sua chave Pix copia e cola!", font=("Arial", 20))
tituloAcima.grid(row=0, column=0, sticky="ne", padx=20)

# orientaçãao da chave
orientacao = CTK.CTkLabel(janela, text="Digite a chave pix a ser utilizada*", font=("Arial", 15))
orientacao.grid(row=1, column=0, sticky="nw", padx=20)

# primeira caixa de input (Chave pix)
chavePixEntry = CTK.CTkEntry(janela, width=250, placeholder_text="Chave pix")
chavePixEntry.grid(row=2, column=0, sticky="nw", padx=20, pady=10)

# orientaação do valor
orientacaoValor = CTK.CTkLabel(janela, text="Digite o valor a ser cobrado*", font=("Arial",15))
orientacaoValor.grid(row=3, column=0, sticky="nw", padx=20)

# segunuda caixa de input (Valor)
valorPixEntry = CTK.CTkEntry(janela, width=250, placeholder_text="Valor em R$")
valorPixEntry.grid(row=4, column=0, sticky="nw", padx=20, pady=10)

# orientação do nome
nomeGUI = CTK.CTkLabel(janela, text="Digite o nome do recebedor*", font=("Arial", 15))
nomeGUI.grid(row=5, column=0, sticky="nw", padx=20)

# Terceira caixa de input (nome)
nomeEntry = CTK.CTkEntry(janela, width=250, placeholder_text="Nome completo")
nomeEntry.grid(row=6, column=0, sticky="nw", padx=20, pady=10)

# orientação cidade
cidadeGUI = CTK.CTkLabel(janela, text = "Digite a cidade do recebedor*", font = ("Arial", 15))
cidadeGUI.grid(row=7, column=0, sticky="nw", padx=20)

# Quarta caixa de input (cidade)
cidadeEntry = CTK.CTkEntry(janela, width=250, placeholder_text="Cidade (incluir estado é opcional)")
cidadeEntry.grid(row=8, column=0, sticky="nw", padx=20, pady=10)

#ultima orientação (totalmente opcional)
txtIdGUI = CTK.CTkLabel(janela, text="Identidicador (opcional)", font=("Arial", 15))
txtIdGUI.grid(row=9, column=0, sticky="nw", padx=20)

#Ultima caixa de input (TxtId)
txtIdEntry = CTK.CTkEntry(janela, width=250, placeholder_text="Identificador de transação")
txtIdEntry.grid(row=10, column=0, sticky="nw", padx=20, pady=10)

# Botão de resultado
botao = CTK.CTkButton(janela, text="Gerar Pix copia e cola", command= CommandQrcode)
botao.grid(row=11, column=0, sticky="nw", padx=65, pady=20)

# MENSAGEM DE ERRO
LabelErro.grid(row=12, column=0, sticky="nw", padx="62")

# Background do QRcode
qrFrame = CTK.CTkFrame(janela, width=300, height=300, corner_radius=12, border_width=2)
qrFrame.grid_propagate(False)
qrFrame.grid(row=0, column=1, rowspan=12)

qrFrame.grid_rowconfigure(0, weight=1)
qrFrame.grid_columnconfigure(0, weight=1)

# Texto dentro do frame do QRcode
qrLabel = CTK.CTkLabel(qrFrame, text="")
qrLabel.grid(row=0, column=0, sticky="nsew")



janela.mainloop()