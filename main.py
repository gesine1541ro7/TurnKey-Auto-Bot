# -*- coding: utf-8 -*-
"""
TurnKey Auto Bot — Airdrop (Insiders)
Neon-styled terminal interface for testnet airdrop automation.
"""
import os
import sys

try:
    import colorama
    colorama.init(autoreset=True)
except ImportError:
    pass

from utils import ensure_env


class C:
    NEON_CYAN   = '\033[96m'
    NEON_MAGENTA= '\033[95m'
    NEON_GREEN  = '\033[92m'
    NEON_YELLOW = '\033[93m'
    NEON_BLUE   = '\033[94m'
    RED         = '\033[91m'
    DIM         = '\033[2m'
    BOLD        = '\033[1m'
    RESET       = '\033[0m'
    BG_BLACK    = '\033[40m'
    REVERSE     = '\033[7m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

LOGO = r"""
 ______  __ __  ____   ____   __  _    ___  __ __          ____  __ __  ______   ___          ____    ___   ______ 
|      ||  |  ||    \ |    \ |  |/ ]  /  _]|  |  |        /    ||  |  ||      | /   \        |    \  /   \ |      |
|      ||  |  ||  D  )|  _  ||  ' /  /  [_ |  |  | _____ |  o  ||  |  ||      ||     | _____ |  o  )|     ||      |
|_|  |_||  |  ||    / |  |  ||    \ |    _]|  ~  ||     ||     ||  |  ||_|  |_||  O  ||     ||     ||  O  ||_|  |_|
  |  |  |  :  ||    \ |  |  ||     \|   [_ |___, ||_____||  _  ||  :  |  |  |  |     ||_____||  O  ||     |  |  |  
  |  |  |     ||  .  \|  |  ||  .  ||     ||     |       |  |  ||     |  |  |  |     |       |     ||     |  |  |  
  |__|   \__,_||__|\_||__|__||__|\_||_____||____/        |__|__| \__,_|  |__|   \___/        |_____| \___/   |__|
"""

def print_logo():
    """Render the ASCII logo with neon-style colouring."""
    for line in LOGO.strip().split('\n'):
        out = ''
        for i, c in enumerate(line):
            if c == ' ':
                out += C.DIM + c
            elif c == '$':
                out += C.NEON_GREEN + c
            elif c in ('|', '\\', '/'):
                out += C.NEON_CYAN + c
            elif c == '_':
                out += C.NEON_MAGENTA + c
            else:
                out += C.NEON_YELLOW + c
        print(out + C.RESET)
    print()

def draw_box(lines, title=None):
    """Draw a bordered box around *lines* with an optional *title*."""
    width = max(len(l) for l in lines) + 4
    if title:
        width = max(width, len(title) + 4)
    top = C.NEON_CYAN + '\u2554' + '\u2550' * (width - 2) + '\u2557' + C.RESET
    bot = C.NEON_CYAN + '\u255a' + '\u2550' * (width - 2) + '\u255d' + C.RESET
    print(top)
    if title:
        t = C.NEON_MAGENTA + ' ' + title.center(width - 4) + ' ' + C.RESET
        print(C.NEON_CYAN + '\u2551' + C.RESET + t + C.NEON_CYAN + '\u2551' + C.RESET)
        print(C.NEON_CYAN + '\u2560' + '\u2550' * (width - 2) + '\u2563' + C.RESET)
    for line in lines:
        padded = line.ljust(width - 4)
        print(C.NEON_CYAN + '\u2551' + C.RESET + ' ' + padded + ' ' + C.NEON_CYAN + '\u2551' + C.RESET)
    print(bot)

def menu_line(num, text):
    s = f"  [{num}] {text}"
    return C.NEON_YELLOW + f"[{num}]" + C.RESET + C.DIM + " " + text + C.RESET

@ensure_env
def main_menu():
    """Main menu with numbered action items per Insiders.md."""
    options = [
        (1, "Install Dependencies"),
        (2, "Settings"),
        (3, "About"),
        (4, "Load Wallets"),
        (5, "Run Bot"),
        (6, "Export Results"),
        (0, "Exit"),
    ]
    while True:
        clear_screen()
        print_logo()
        draw_box(
            [menu_line(n, t) for n, t in options],
            title="MAIN MENU"
        )
        print()
        print(C.NEON_GREEN + "  > Enter option number (0-6): " + C.RESET, end='')
        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            choice = '0'
        if choice == '0':
            print(C.NEON_MAGENTA + "\n  [ EXIT ] Goodbye.\n" + C.RESET)
            sys.exit(0)
        if choice == '1':
            run_install_dependencies()
        elif choice == '2':
            run_settings()
        elif choice == '3':
            run_about()
        elif choice == '4':
            run_load_wallets()
        elif choice == '5':
            run_bot()
        elif choice == '6':
            run_export_results()
        else:
            print(C.RED + "  Invalid option. Press Enter..." + C.RESET)
            input()

def run_install_dependencies():
    """Install Python dependencies from requirements.txt."""
    clear_screen()
    print_logo()
    draw_box(["Installing dependencies from requirements.txt..."], title="INSTALL DEPENDENCIES")
    print()
    req_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
    if not os.path.isfile(req_path):
        print(C.RED + "  requirements.txt not found." + C.RESET)
    else:
        import subprocess
        r = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', req_path], shell=False)
        if r.returncode == 0:
            print(C.NEON_GREEN + "  Dependencies installed successfully." + C.RESET)
        else:
            print(C.RED + "  Installation failed. Check pip." + C.RESET)
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()

def run_settings():
    """Open the interactive settings editor."""
    from src.settings import run_settings_ui
    run_settings_ui(C, draw_box, clear_screen, print_logo)

def run_about():
    """Display project information."""
    clear_screen()
    print_logo()
    lines = [
        "TurnKey Auto Bot — Airdrop (Insiders)",
        "Version: 1.0.0",
        "",
        "Automation for testnet airdrop tasks.",
        "Neon-styled terminal interface.",
        "",
        "Python 3.10+ required.",
        "See Insiders.md for full documentation.",
    ]
    draw_box(lines, title="ABOUT")
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()

def run_load_wallets():
    """Load wallet addresses from the configured wallets file."""
    from src.bot import load_wallets
    clear_screen()
    print_logo()
    draw_box(["Loading wallets from file..."], title="LOAD WALLETS")
    print()
    count, path = load_wallets()
    if count >= 0:
        print(C.NEON_GREEN + f"  Loaded {count} wallet(s) from {path}" + C.RESET)
    else:
        print(C.RED + f"  File not found or error: {path}" + C.RESET)
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()

def run_bot():
    """Start the airdrop bot cycle."""
    from src.bot import run_bot_cycle
    clear_screen()
    print_logo()
    draw_box(["Starting bot cycle..."], title="RUN BOT")
    print()
    run_bot_cycle(C, draw_box)
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()

def run_export_results():
    """Export bot results to the exports/ directory."""
    from src.export import export_results
    clear_screen()
    print_logo()
    draw_box(["Exporting results to exports/..."], title="EXPORT RESULTS")
    print()
    path = export_results()
    if path:
        print(C.NEON_GREEN + f"  Exported to: {path}" + C.RESET)
    else:
        print(C.NEON_YELLOW + "  No data to export or export folder created." + C.RESET)
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()

if __name__ == '__main__':
    main_menu()
