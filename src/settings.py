# -*- coding: utf-8 -*-
"""Configuration management via config.json for TurnKey settings."""
import os
import json

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')

DEFAULTS = {
    "rpc_url": "",
    "delay_min": 5,
    "delay_max": 15,
    "wallets_path": "wallets.txt",
    "max_retries": 3,
}

def load_config():
    if os.path.isfile(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {**DEFAULTS, **data}
        except Exception:
            pass
    return DEFAULTS.copy()

def save_config(data):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def run_settings_ui(C, draw_box, clear_screen, print_logo):
    """Interactive settings editor."""
    cfg = load_config()
    while True:
        clear_screen()
        print_logo()
        lines = [
            f"  [1] RPC URL .............. {cfg.get('rpc_url') or '(empty)'}",
            f"  [2] Delay min (sec) ...... {cfg.get('delay_min', 5)}",
            f"  [3] Delay max (sec) ...... {cfg.get('delay_max', 15)}",
            f"  [4] Wallets path ......... {cfg.get('wallets_path', 'wallets.txt')}",
            f"  [5] Max retries .......... {cfg.get('max_retries', 3)}",
            "",
            "  [0] Save and back to menu",
        ]
        draw_box(lines, title="SETTINGS")
        print()
        print(C.NEON_GREEN + "  > Select field (0-5): " + C.RESET, end='')
        try:
            opt = input().strip()
        except (EOFError, KeyboardInterrupt):
            opt = '0'
        if opt == '0':
            save_config(cfg)
            print(C.NEON_GREEN + "  Settings saved." + C.RESET)
            break
        if opt == '1':
            print(C.NEON_CYAN + "  New RPC URL: " + C.RESET, end='')
            try:
                v = input().strip()
            except (EOFError, KeyboardInterrupt):
                v = cfg.get('rpc_url', '')
            cfg['rpc_url'] = v
        elif opt == '2':
            print(C.NEON_CYAN + "  Delay min (seconds): " + C.RESET, end='')
            try:
                v = input().strip()
            except (EOFError, KeyboardInterrupt):
                v = str(cfg.get('delay_min', 5))
            try:
                cfg['delay_min'] = int(v)
            except ValueError:
                pass
        elif opt == '3':
            print(C.NEON_CYAN + "  Delay max (seconds): " + C.RESET, end='')
            try:
                v = input().strip()
            except (EOFError, KeyboardInterrupt):
                v = str(cfg.get('delay_max', 15))
            try:
                cfg['delay_max'] = int(v)
            except ValueError:
                pass
        elif opt == '4':
            print(C.NEON_CYAN + "  Wallets file path: " + C.RESET, end='')
            try:
                v = input().strip() or 'wallets.txt'
            except (EOFError, KeyboardInterrupt):
                v = cfg.get('wallets_path', 'wallets.txt')
            cfg['wallets_path'] = v
        elif opt == '5':
            print(C.NEON_CYAN + "  Max retries: " + C.RESET, end='')
            try:
                v = input().strip()
            except (EOFError, KeyboardInterrupt):
                v = str(cfg.get('max_retries', 3))
            try:
                cfg['max_retries'] = int(v)
            except ValueError:
                pass
    print(C.DIM + "\n  Press Enter to return to menu..." + C.RESET)
    input()
