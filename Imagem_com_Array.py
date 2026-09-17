import numpy as np
import cv2

# Cria uma matriz 600x600 preenchida com zeros (imagem inteiramente preta)
black = np.zeros([600,600])

# Fatia e armazena apenas a segunda linha (índice 1) da matriz
f_row = black[1:2]

# Exibe os valores da segunda linha no terminal
print(f_row)

# Fatia e armazena apenas a segunda coluna (índice 1) de todas as linhas
f_col = black[:, 1:2]

# Exibe os valores da segunda coluna no terminal
print(f_col)

# Altera os pixels da região central (linhas 200 a 399, colunas 200 a 399) para 255 (quadrado branco)
black[200:400, 200:400] = 255

# Exibe no terminal a matriz modificada com os valores 255 no centro
print(black)

# Abre uma janela chamada "preto" para exibir a imagem gerada
cv2.imshow("preto", black)

# Pausa a execução do programa até que alguma tecla seja pressionada na janela da imagem
cv2.waitKey(0)