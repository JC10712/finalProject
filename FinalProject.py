import flet as ft


def create_piece(color):
    return ft.Draggable(
        group="pieces",
        content=ft.Container(
            width=60,
            height=60,
            border_radius=30,
            bgcolor=color,
        ),
    )


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    board_controls = []

    for row in range(8):
        for col in range(8):

            if (row + col) % 2 == 0:
                square_color = "brown"
            else:
                square_color = "beige"

            board_controls.append(
                ft.Container(
                    width=80,
                    height=80,
                    bgcolor=square_color,
                    left=col * 80,
                    top=row * 80,
                )
            )

    black_positions = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23]

    for pos in black_positions:
        row = pos // 8
        col = pos % 8

        board_controls.append(
            ft.Container(
                left=col * 80 + 10,
                top=row * 80 + 10,
                content=create_piece("black"),
            )
        )

    green_positions = [40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]

    for pos in green_positions:
        row = pos // 8
        col = pos % 8

        board_controls.append(
            ft.Container(
                left=col * 80 + 10,
                top=row * 80 + 10,
                content=create_piece("green"),
            )
        )

    board = ft.Stack(
        width=640,
        height=640,
        controls=board_controls,
    )

    page.add(board)


ft.app(target=main)