import pywhatkit as pwk
import time
import os

# Função para enviar uma imagem
def enviar_imagem(numero, caminho_imagem, tempo_espera=15):
    pwk.sendwhats_image(numero, caminho_imagem, tab_close=True, close_time=tempo_espera)

# Função para enviar uma mensagem de texto
def enviar_mensagem(numero, mensagem, tempo_espera=15):
    pwk.sendwhatmsg_instantly(numero, mensagem, wait_time=tempo_espera, tab_close=True, close_time=tempo_espera)

# Caminho da pasta onde estão as imagens
caminho_pasta = r'C:\zfotos_envio_catalogo'

# Lista de contatos
contatos = ["+5591989699902", "+5581989847285"]

# Obter a lista de imagens na pasta
imagens = [os.path.join(caminho_pasta, f) for f in os.listdir(caminho_pasta) if f.endswith('.png')]

# Verificar se há imagens na pasta
if not imagens:
    print("Nenhuma imagem encontrada na pasta especificada.")
else:
    # Enviar para cada contato
    for contato in contatos:
        # Enviar a primeira imagem (capa)
        enviar_imagem(contato, imagens[0])
        time.sleep(5)  # Esperar um pouco antes de enviar a próxima mensagem

        # Enviar um ponto (.) para separar
        enviar_mensagem(contato, ".")
        time.sleep(5)

        # Enviar as demais imagens em lotes de 4
        for i in range(1, len(imagens), 4):
            lote = imagens[i:i+4]
            for imagem in lote:
                enviar_imagem(contato, imagem)
                time.sleep(5)  # Esperar um pouco entre cada imagem do lote

            # Enviar um ponto (.) para separar os lotes, se ainda houver imagens a enviar
            if i + 4 < len(imagens):
                enviar_mensagem(contato, ".")
                time.sleep(5)

print("Envio de imagens concluído.")