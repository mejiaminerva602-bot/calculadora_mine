from nicegui import ui
import os

# Tu calculadora
def sumar():
    try:
        r = float(num1.value) + float(num2.value)
        resultado.set_text(f'Resultado: {r}')
    except:
        resultado.set_text('Pon números válidos')

with ui.column().classes('items-center w-full mt-10'):
    ui.label('Calculadora Mine').classes('text-3xl font-bold text-purple-600')
    
    num1 = ui.input(label='Número 1').classes('w-64')
    num2 = ui.input(label='Número 2').classes('w-64')
    
    ui.button('Sumar', on_click=sumar).classes('bg-purple-500 text-white w-64')
    
    resultado = ui.label('Resultado: ').classes('text-xl mt-4')

# Esto es lo que faltaba para Render
port = int(os.environ.get("PORT", 8080))
ui.run(host='0.0.0.0', port=port)
