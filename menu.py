from rich import print

from rich.console import Console
import time
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt
import sys




def welcomeMessage(console: Console, clear=False):
    if clear:
        console.clear()
    console.print("\n[red]-----------------------------------------------------------[/red]")
    console.print("[orange]-----------------------------------------------------------[/orange]")
    console.print("[yellow]██████╗ ██╗   ██╗ ██████╗ ██████╗ ██╗      ██████╗ ██████╗[/yellow]")
    console.print("[green]██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗[/green]")
    console.print("[blue]█P█H██╔╝ ╚██E█╔╝ ██║     ██║   ██║██║     ██║   ██║██R█N█╔╝[/blue]")
    console.print("[indigo]██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║     ██║   ██║██╔══██╗[/indigo]")
    console.print("[violet]██║        ██║   ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║[/violet]")
    console.print("[red]╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝[/red]")
    console.print("[orange]-----------------------------------------------------------[/orange]")
    console.print("[yellow]-----------------------------------------------------------[/yellow]")


def mainMenu(console: Console):
    table = Table.grid(padding=(0, 2))

    table.add_row("[bold cyan]1[/]", "Select Screen Region")
    table.add_row("[bold cyan]2[/]", "Eyedropper")
    table.add_row("[bold cyan]3[/]", "Exit")

    console.print(
        Panel.fit(
            table,
            title="[bold]Main Menu[/bold]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    
    selection = Prompt.ask(
        "Select",
        choices=["1", "2", "3"]
    )
    
    if selection == "1":
        return "1"
    if selection == "2":
        return "2"
    if selection == "3":
        sys.exit()


def areaSubMenu(console: Console):
    table = Table.grid(padding=(0, 2))

    table.add_row("[bold cyan]1[/]", "Average RGB of area")
    table.add_row("[bold cyan]2[/]", "Search for RGB")
    table.add_row("[bold cyan]3[/]", "Exit")

    console.print(
        Panel.fit(
            table,
            border_style="cyan",
            padding=(1, 2),
        )
    )
    
    selection = Prompt.ask(
        "Select",
        choices=["1", "2", "3"]
    )
    
    if selection == "1":
        return "1"
    if selection == "2":
        return "2"
    if selection == "3":
        sys.exit()
        
    


def tryAgain(console: Console):
    table = Table.grid(padding=(0, 2))

    table.add_row("[bold cyan]1[/]", "Yes")
    table.add_row("[bold cyan]2[/]", "No")

    console.print(
        Panel.fit(
            table,
            title="[bold]Try Again?[/bold]",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    
    selection = Prompt.ask(
        "Select",
        choices=["1", "2"]
    )
    
    if selection == "1":
        return True
    if selection == "2":
        sys.exit()
    else:
        sys.exit()
    



def printColorValue(console: Console, rgb: tuple):
    r, g, b = rgb
    color = f"rgb({r},{g},{b})"
    hex_value = f"#{r:02X}{g:02X}{b:02X}"

    text = Text()
    text.append("RGB:  ", style="bold white")
    text.append(str(rgb), style=color)

    text.append("\nHEX:  ", style="bold white")
    text.append(hex_value, style=color)

    console.print(
        Panel.fit(
            text,
            title="[white][bold]Selected Color[/bold][/white]",
            border_style=color,
            padding=(1, 2),
        )
    )


def printMousePos(pos: tuple, rgb = None):
    if rgb:
        color = f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"
        content = f"\r[rgb({rgb[0]},{rgb[1]},{rgb[2]})]--  x: {pos.x}  y: {pos.y}  --[/]"
    else:
        color = "cyan"
        content = f"\r--  x: {pos.x}  y: {pos.y}  --"
        
    return Panel.fit(
        content,
        border_style=color,
        padding=(1, 2),
    )



# countdown timer 
def countdownTimer(console: Console, seconds, clear=False): 
    if clear:
        console.clear()
    console.print("Starting", end="")
    for i in range(seconds):
        console.print(".", end="")
        time.sleep(0.2)
    console.print("Started")
