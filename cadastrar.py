import flet as ft
HEIGHT = 480

def main(page: ft.Page):
    # Função para alterar o estado do botão quando selecionar o switch
    def on_terms_switch_changed(e):
        submit_button.disabled = not e.control.value
        submit_button.bgcolor = ft.colors.GREEN if e.control.value else ft.colors.GREEN
        submit_button.update()
    
    # Função definida apenas para formatação (DD/MM/YYYY)  
    def format_date(e):
        # Remove caracteres não numéricos
        text = ''.join(filter(str.isdigit, e.control.value))
        # Aplica a formação (DD/MM/YYYY)
        if len(text) > 2:
            text = text[:2] + '/' + text[2:]
        if len(text) > 5:
            text = text[:5] + '/' + text[5:]
        e.control.value = text[:10]
        e.control.update()
        
    form_items = [
        ft.Text("Cadastre-se aqui", style="headlineLarge", color=ft.colors.WHITE70, size=35),
        ft.TextField(label="Nome", width=500, bgcolor=ft.colors.BLACK12, color=ft.colors.WHITE70),
        ft.TextField(label="Sobrenome", width=500, bgcolor=ft.colors.BLACK12, color=ft.colors.WHITE70),
        ft.TextField(label="E-mail", width=500, bgcolor=ft.colors.BLACK12, color=ft.colors.WHITE70),
        
        # Campo da data de nascimento formatada!
        ft.TextField(
            label="Data de nascimento (DD/MM/YYYY)",
            width=500,
            bgcolor=ft.colors.BLACK12,
            color=ft.colors.WHITE70,
            on_change=format_date, # Chamando a função para formatar a data
            keyboard_type="number" # Definindo que será apenas numeros nessa coluna 
        ),
        
        ft.Dropdown(
            label="Gênero",
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Feminino"),
                ft.dropdown.Option("Outros")
                
            ],
            width=250,
            #bgcolor=ft.colors.BLACK12,
            #color=ft.colors.WHITE
        ),
        
        ft.Container(
            content=ft.DatePicker(),
            width=500
        ),
        
        ft.Row(
            controls=[
                ft.Switch(
                    active_color=ft.colors.GREEN,
                    on_change=on_terms_switch_changed
                ),
                ft.Text("Aceito os termos e condições aplicadas", color=ft.colors.GREEN_50)
            ]
        )
    ]
    submit_button = ft.ElevatedButton(
        text="Enviar",
        on_click=lambda e: print("Cadastro enviado!"),
        bgcolor=ft.colors.GREY,
        color=ft.colors.BLACK,
        disabled=True
    )
    
    form_items.append(submit_button) # Adicionando o botão ao final dos itens
    
    col = ft.Column(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=form_items,
        height=HEIGHT
    )
    
    # Adicionando o formulário na página do Flet
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Formulário de cadastro teste",
                    color=ft.colors.WHITE,
                    size=50
                ),
            ]
        ),
        ft.Container(content=col, bgcolor=ft.colors.BLACK12),
    )

ft.app(main)