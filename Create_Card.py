# Modificando imagem através do módulo OpenCV
import cv2

# Carrega/lê a imagem "poster.jpg" e a armazena na variável 'img'
img = cv2.imread("poster.jpg")

# Recorta uma região específica da imagem (linhas de 120 a 360, colunas de 400 a 500)
rocket = img[120:360,400:500]

# Cola/substitui a região recortada ('rocket') em uma nova posição da imagem
img[0:240,500:600] = rocket

# Define o texto que será escrito sobre a imagem
text_to_show = "Eu amo programar!!"

# Desenha/escreve o texto na imagem com posição, fonte, tamanho e cor (vermelho em BGR)
cv2.putText(
            img,
            text_to_show,
            (20, 220),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=0.6,
            color=(0,0,255)
            )

# Exibe a imagem alterada em uma janela chamada "resultado"
cv2.imshow("resultado", img)

# Salva a imagem resultante em um novo arquivo chamado "Greetings.jpg"
cv2.imwrite("Greetings.jpg", img)

# Aguarda o usuário pressionar qualquer tecla para fechar a janela
cv2.waitKey(0)