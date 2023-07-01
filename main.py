import PySimpleGUI as sg
from numpy import *
from math import *

"""Função que tem como parametro o tipo de layout da interface 
e retorna uma mensagem padrão para o momento"""
def return_messege(type_window):
    return type_window["m"].update(f"O momento em relação ao eixo é: ({round(Mx, 3)}i {round(My, 3)}j {round(Mz, 3)}k)")


sg.theme('DarkTanBlue')
value_font = ('Courier New', 20)
value_size = (50, 10)

"""Layout do menu inicia com as opções"""
layout = [[sg.Text("BEM-VINDO", size=value_size, font=value_font)],
    [sg.Text("Escolha uma opção:", font=value_font)],
    [sg.Button("FORÇA RETANGULAR", font=value_font),
     sg.Button("FORÇA POLAR", font=value_font),
     sg.Button("EIXO POLAR", font=value_font)],
]

"""Primeira janela/menu que diz respeito a forças retangulares, onde recebe 
como campo de digitação, os vetores de: força(x,y,z), distância(x,y,z) de vetor unitário(x,y,z)"""
layout_forca_1 = [
    [sg.Text("Insira os respectivos valores", size=value_size, font=value_font)],
    [sg.Text("Componentes da força (x,y,z):", font=value_font), sg.InputText(key="f", font=value_font)],
    [sg.Text("Componentes da distância (x,y,z):", font=value_font), sg.InputText(key="d", font=value_font)],
    [sg.Text("Componentes do vetor unitário (x,y,z):", font=value_font), sg.InputText(key="n", font=value_font)],
    [sg.Button("CALCULAR", font=value_font)],
    [sg.Text("", key="m", font=value_font)],
]

"""Segunda janela/menu que diz respeito a força polar, onde recebe 
como campo de digitação: intensidade da força (escalar), angulo(theta, omega, alfa), vetor distância (x,y,z)
e vetor unitário"""
layout_forca_2 = [
    [sg.Text("Insira os respectivos valores",size=value_size, font=value_font)],
    [sg.Text("Intensidade da Força:",  font=value_font), sg.InputText(key="f", font=value_font)],
    [sg.Text("Angulos (x,y,z):",  font=value_font), sg.InputText(key="a", font=value_font)], #angulos em graus que a força faz com cada eixo
    [sg.Text("Componentes da distância (x,y,z):",  font=value_font), sg.InputText(key="d", font=value_font)],
    [sg.Text("Componentes do eixo (x,y,z):",  font=value_font), sg.InputText(key="n", font=value_font)],
    [sg.Button("CALCULAR", font=value_font)],
    [sg.Text("", key="m")],
]

"""Terceira janela que recebe as componentes do eixo, distancia e força e calcula o momento em relação a um eixo
quando o eixo está expresso pela suas componentes polares (angulo)"""
layout_eixo = [
    [sg.Text("Insira os respectivos valores", size=value_size, font=value_font)],
    [sg.Text("Componentes do eixo (x,y,z):",  font=value_font), sg.InputText(key="e", font=value_font)],
    [sg.Text("Componentes da distância (x,y,z):",  font=value_font), sg.InputText(key="d", font=value_font)],
    [sg.Text("Componentes da força (x,y,z):",  font=value_font), sg.InputText(key="f", font=value_font)],
    [sg.Button("CALCULAR", font=value_font)],
    [sg.Text("", key="m")],
    [sg.Text("", key="m0")],

]

"""chama a primeira janela, referente ao menu inicial"""
janela = sg.Window("MOMENTO EM TORNO DE UM EIXO", layout)

#Loop de interação com as janelas, recebe um evento (clik) e repassa valores (value)
while True:
    evento, valores = janela.read()
    #evento padrão para quando fechar a aba
    if(evento == sg.WINDOW_CLOSED):
        break
    # primeiro evento, força retangular, chama a janela referente ao evento
    elif(evento == "FORÇA RETANGULAR"):
        Window = sg.Window("FORÇA RETANGULAR", layout_forca_1)
        # Início da interação
        while True:
            evento, valores = Window.read()
            # Evento padrão para fechar aba
            if(evento == sg.WINDOW_CLOSED):
                break
            #declaração de variáveis, que recebe os valores iniciais
            f = array(eval(valores["f"]))
            d = array(eval(valores["d"]))
            n = array(eval(valores["n"]))

            if(evento == "CALCULAR"):
                mx = d[1] * f[2] - d[2] * f[1]
                my = d[2] * f[0] - d[0] * f[2]
                mz = d[0] * f[1] - d[1] * f[0]
                m = mx * n[0] + my * n[1] + mz * n[2]  # momento em torno de um ponto que passa o eixo arbitrário
                Mx = m * n[0]
                My = m * n[1]
                Mz = m * n[2]
                return_messege(Window)
        Window.close()
    # Segundo evento, força polar, chama a janela referente ao evento FORÇA POLAR
    if(evento == "FORÇA POLAR"):
        Window_2 = sg.Window("FORÇA POLAR", layout_forca_2)

        while True:
            evento, valores = Window_2.read()
            if(evento == sg.WINDOW_CLOSED):
                break

            f = int(valores["f"])
            a = array(eval(valores["a"]))
            #CONVERSÃO DOS ANGULOS
            ax = (a[0]*pi)/180
            ay = (a[1]*pi)/180
            az = (a[2]*pi)/180
            d = array(eval(valores["d"]))
            n = array(eval(valores["n"]))

            if(evento == "CALCULAR"):
                fz = sin(az) * f
                fxy = cos(az) * f
                fx = cos(ax)*fxy
                fy = cos(ay)*fxy

                mx = d[1] * fz - d[2] * fy
                my = d[2] * fx - d[0] * fz
                mz = d[0] * fy - d[1] * fx
                m = mx * n[0] + my * n[1] + mz * n[2]
                Mx = m * n[0]
                My = m * n[1]
                Mz = m * n[2]
                return_messege(Window_2)
        Window_2.close()

    # Terceiro evento, eixo polar, chama a janela referente ao evento EIXO POLAR
    if(evento == "EIXO POLAR" ):
        Window_eixo = sg.Window("EIXO POLAR", layout_eixo)
        while True:
            evento, valores = Window_eixo.read()
            if(evento == sg.WINDOW_CLOSED):
                break
            eixo = array(eval(valores["e"]))
            f = array(eval(valores["f"]))
            d = array(eval(valores["d"]))
            if(evento == "CALCULAR"):
                x = cos((eixo[0] * pi) / 180)
                y = cos((eixo[1] * pi) / 180)
                z = cos((eixo[2] * pi) / 180)
                mx = d[1] * f[2] - d[2] * f[1]
                my = d[2] * f[0] - d[0] * f[2]
                mz = d[0] * f[1] - d[1] * f[0]
                m = mx * x + my * y + mz * z  # momento em torno de um ponto que passa o eixo
                Mx = m * x
                My = m * y
                Mz = m * z
                # calcula o momento
                print((Window_eixo["m"].update(f"O momento é: {m}")))
                return_messege(Window_eixo)
        Window_eixo.close()
janela.close()