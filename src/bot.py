# -*- coding: utf-8 -*-
"""Bot logic and wallet loading for TurnKey airdrop automation."""
import os
import time
from src.settings import load_config, CONFIG_PATH

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_wallets_cache = []

def _wallets_path():
    cfg = load_config()
    p = cfg.get('wallets_path', 'wallets.txt')
    if not os.path.isabs(p):
        p = os.path.join(BASE_DIR, p)
    return p

def load_wallets():
    """Load wallet addresses from file.  Returns (count, path) or (-1, error_message)."""
    global _wallets_cache
    path = _wallets_path()
    if not os.path.isfile(path):
        return -1, path
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith('#')]
        _wallets_cache = lines
        return len(_wallets_cache), path
    except Exception as e:
        return -1, str(e)

def get_loaded_wallets():
    return _wallets_cache

def run_bot_cycle(C, draw_box):
    """Execute one bot cycle (simulation based on current settings)."""
    cfg = load_config()
    delay_min = cfg.get('delay_min', 5)
    delay_max = cfg.get('delay_max', 15)
    max_retries = cfg.get('max_retries', 3)
    wallets = get_loaded_wallets()
    if not wallets:
        load_wallets()
        wallets = get_loaded_wallets()
    if not wallets:
        print(C.RED + "  No wallets loaded. Use Load Wallets first." + C.RESET)
        return
    print(C.NEON_CYAN + f"  Wallets: {len(wallets)}" + C.RESET)
    print(C.DIM + f"  Delay: {delay_min}-{delay_max} sec, max_retries: {max_retries}" + C.RESET)
    print()
    for i, w in enumerate(wallets[:5], 1):
        addr = w[:8] + '...' + w[-6:] if len(w) > 20 else w
        print(C.NEON_GREEN + f"  [{i}] Processing {addr}..." + C.RESET)
        time.sleep(1)
    if len(wallets) > 5:
        print(C.DIM + f"  ... and {len(wallets) - 5} more (demo: only 5 steps)." + C.RESET)
    print(C.NEON_GREEN + "  Bot cycle finished." + C.RESET)
