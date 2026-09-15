from rich import print
import time

def welcomeMessage():
    print("[red]-----------------------------------------------------------[/red]")
    print("[orange]-----------------------------------------------------------[/orange]")
    print("[yellow]██████╗ ██╗   ██╗ ██████╗ ██████╗ ██╗      ██████╗ ██████╗[/yellow]")
    print("[green]██╔══██╗╚██╗ ██╔╝██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗[/green]")
    print("[blue]█P█H██╔╝ ╚██E█╔╝ ██║     ██║   ██║██║     ██║   ██║██R█N█╔╝[/blue]")
    print("[indigo]██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║     ██║   ██║██╔══██╗[/indigo]")
    print("[violet]██║        ██║   ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║[/violet]")
    print("[red]╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝[/red]")
    print("[orange]-----------------------------------------------------------[/orange]")
    print("[yellow]-----------------------------------------------------------[/yellow]")
    

# countdown timer 
def countdownTimer(seconds): 
    print("Starting", end="")
    for i in range(seconds):
        print(".", end="")
        time.sleep(0.2)
    print("Started")
