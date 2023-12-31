from flet import *
from custom_checkbox import CustomCheckBox


def main(page: Page):
    # Set the theme mode to "dark" for white text and icons
    page.theme_mode = "dark"

    # Define color constants
    BG = "#041955"  # Background color
    FWG = "#97b4ff"  # A shade of blue
    FG = "#3450a1"  # Another shade of blue
    PINK = "#eb06ff"  # Pink color

    # Create a circular avatar using Stack and Container controls
    circle = Stack(
        controls=[
            Container(
                width=100, height=100, border_radius=50, bgcolor="white12"
            ),  # Circular background
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=["#00000000", PINK],
                ),  # Circular gradient overlay
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment="center",
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://cdn.filestackcontent.com/rotate=deg:exif/resize=width:1200,height:630,fit:crop/aikCnyIXTZuZomCWwxLt",
                                ),  # Circular avatar with an image
                            ),
                        )
                    ],
                ),
            ),
        ]
    )

    # Function to shrink the page
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            35, 0, 35, 0
        )  # Set border radius for animation

        page_2.update()

    # Function to restore the page
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()

    # Create a button for creating tasks
    create_task_view = Container(
        content=Container(
            on_click=lambda _: page.go("/"), height=40, width=40, content=Text("x")
        )
    )

    # Create a column to display tasks
    tasks = Column(height=400, scroll="auto")

    # Add sample tasks to the column
    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor=BG,
                border_radius=25,
                padding=padding.only(
                    left=20,
                    top=25,
                ),
                content=CustomCheckBox(color=PINK, label="Create interesting content!"),
            ),
        )

    # Create a row to display categories
    categories_card = Row(scroll="auto")
    categories = ["School", "Family", "Friends"]

    # Add categories to the row
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text("Tasks"),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        ),
                    ]
                ),
            )
        )

    # Create the content for the first page
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            on_click=lambda e: shrink(e), content=Icon(icons.MENU)
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED),
                            ],
                        ),
                    ],
                ),
                Container(height=20),
                Text(value="What's up, Logan!"),
                Text(value="CATEGORIES"),
                Container(
                    padding=padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=icons.ADD,
                            on_click=lambda _: page.go("/create_task"),
                        ),
                    ]
                ),
            ],
        ),
    )

    # Create the first page
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(
                    alignment="end",
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(
                                top=13,
                                left=13,
                            ),
                            height=50,
                            width=50,
                            border=border.all(color="white", width=1),
                            on_click=lambda e: restore(e),
                            content=Text("<"),
                        )
                    ],
                ),
                Container(height=20),
                circle,
                Text("Iker\nLogan", size=32, weight="bold"),
                Container(height=25),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color="white60"),
                        Text(
                            "Templates",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL, color="white60"),
                        Text(
                            "Templates",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CALCULATE_OUTLINED, color="white60"),
                        Text(
                            "Templates",
                            size=15,
                            weight=FontWeight.W_300,
                            color="white",
                            font_family="poppins",
                        ),
                    ]
                ),
                Image(
                    src=f"./images/1.png",
                    width=300,
                    height=200,
                ),
                Text(
                    "Good",
                    color=FG,
                    font_family="poppins",
                ),
                Text(
                    "Be Happy!",
                    size=22,
                ),
            ]
        ),
    )

    # Create the second page
    page_2 = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[first_page_contents]),
            )
        ],
    )

    # Create a container to switch between pages
    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2,
            ]
        ),
    )

    # Define views and route change handling
    pages = {
        "/": View(
            "/",
            [container],
        ),
        "/create_task": View(
            "/create_task",
            [create_task_view],
        ),
    }

    # Function to handle route changes
    def route_change(route):
        page.views.clear()
        page.views.append(pages[page.route])

    page.on_route_change = route_change
    page.go(page.route)


# Start the Flet app
app(target=main, assets_dir="assets")
