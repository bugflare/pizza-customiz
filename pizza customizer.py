import flet as ft
import os

def main(page: ft.Page):
    page.title = "Pizza Customizer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f5"
    page.padding = 20

    IMAGE_DIR = r"C:\Users\Johanns Yi\Documents"
    
    try:
        base_pizza = ft.Image(
            src=os.path.join(IMAGE_DIR, "base_pizza.png"),
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )
    except Exception as e:
        print(f"Error loading base pizza image: {e}")
        base_pizza = ft.Container(
            width=300,
            height=300,
            bgcolor="#f0e68c",
            border_radius=150,
            content=ft.Text("Pizza Base", color="black")
        )
    
    def create_topping_image(filename, fallback_color):
        try:
            return ft.Image(
                src=os.path.join(IMAGE_DIR, filename),
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                visible=False
            )
        except:
            return ft.Container(
                width=300,
                height=300,
                visible=False,
                content=ft.Text(fallback_color, color="white", size=20)
            )
    
    pepperoni_img = create_topping_image("pepperoni.png", "Pepperoni")
    mushrooms_img = create_topping_image("mushrooms.png", "Mushrooms")
    olives_img = create_topping_image("olives.png", "Olives")
    
    pizza_stack = ft.Stack(
        [
            base_pizza,
            pepperoni_img,
            mushrooms_img,
            olives_img,
        ],
        width=300,
        height=300,
    )
    
    def toggle_topping(e):
        topping = e.control.data
        if topping == "pepperoni":
            pepperoni_img.visible = e.control.value
        elif topping == "mushrooms":
            mushrooms_img.visible = e.control.value
        elif topping == "olives":
            olives_img.visible = e.control.value
        page.update()
    
    pepperoni_switch = ft.Switch(
        label="Pepperoni",
        on_change=toggle_topping,
        data="pepperoni",
        active_color="#ff5252"
    )
    
    mushrooms_switch = ft.Switch(
        label="Mushrooms",
        on_change=toggle_topping,
        data="mushrooms",
        active_color="#8d6e63"
    )
    
    olives_switch = ft.Switch(
        label="Olives",
        on_change=toggle_topping,
        data="olives",
        active_color="#2e7d32"
    )
    
    toppings_column = ft.Column(
        [
            ft.Text("Customize Your Pizza", size=24, weight="bold"),
            pepperoni_switch,
            mushrooms_switch,
            olives_switch,
        ],
        spacing=15,
    )
    
    page.add(
        ft.Row(
            [
                pizza_stack,
                ft.Container(width=30),
                toppings_column,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
