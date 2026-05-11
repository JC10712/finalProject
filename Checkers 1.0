import flet as ft

def create_piece(color):
    return ft.Draggable(
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=60,
                    height=60,
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=color,
                )
            ]
        )
    )

def main(page: ft.Page):
    rows = 8
    columns = 8

    tableGrid = ft.GridView(
        height=650,
        width=650,
        controls=[],
        runs_count=columns
    )

    
    for i in range(rows):
        for j in range(columns):

            if i % 2 == 0:
                if j % 2 == 0:
                    color = ft.Colors.BLACK
                else:
                    color = ft.Colors.RED
            else:
                if j % 2 != 0:
                    color = ft.Colors.BLACK
                else:
                    color = ft.Colors.RED

            tableGrid.controls.append(
                ft.DragTarget(
                    content=ft.Container(
                        width=80,
                        height=80,
                        bgcolor=color,
                    )
                )
            )

    
    black_positions = [0, 2, 4, 6, 9, 11, 13, 15, 16, 18, 20, 22]

    for pos in black_positions:
        tableGrid.controls[pos].content = create_piece(ft.Colors.BLACK)

    
    blue_positions = [40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]

    for pos in blue_positions:
        tableGrid.controls[pos].content = create_piece(ft.Colors.BLUE)

    page.add(tableGrid)

ft.run(main=main)

# IF YOU WILL COMMITE A CHANGES WITHIN THE CODE PLS GIVE WORD ABOUT IT AND YOU MUST GET APPROVAL FROM THE PREVIOUS EDITOR IF THEY HAVE FINISHED THE PART OR NO
