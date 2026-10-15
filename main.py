from nicegui import ui
import os

num1 = None
num2 = None
resultado = None

def calcular():
    try:
        n1 = float(num1.value) if num1.value else 0
        n2 = float(num2.value) if num2.value else 0
        r = n1 + n2
        resultado.set_text(f'Resultado: {r}')
    except:
        resultado.set_text('Pon números válidos')

def borrar_todo():
    num1.set_value('')
    num2.set_value('')
    resultado.set_text('Resultado: ')
    ui.notify('Borrado', color='purple')

def borrar_ultimo(campo):
    if campo.value:
        campo.set_value(campo.value[:-1])

with ui.column().classes('items-center w-full mt-10 gap-3'):
    ui.label('Calculadora Mine').classes('text-3xl font-bold text-purple-600')
    
    with ui.column().classes('w-72 gap-2'):
        with ui.row().classes('w-full items-center gap-1'):
            num1 = ui.input(label='Número 1').classes('flex-1')
            ui.button('⌫', on_click=lambda: borrar_ultimo(num1)).classes('bg-gray-200').props('dense')
        
        with ui.row().classes('w-full items-center gap-1'):
            num2 = ui.input(label='Número 2').classes('flex-1')
            ui.button('⌫', on_click=lambda: borrar_ultimo(num2)).classes('bg-gray-200').props('dense')

    with ui.row().classes('gap-2 mt-2'):
        ui.button('Sumar', on_click=calcular).classes('bg-purple-500 text-white w-32')
        ui.button('Borrar Todo', on_click=borrar_todo).classes('bg-pink-400 text-white w-32')

    resultado = ui.label('Resultado: ').classes('text-xl mt-4 font-bold')

port = int(os.environ.get("PORT", 8080))
ui.run(host='0.0.0.0', port=port, title='Calculadora Mine')
