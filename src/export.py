# -*- coding: utf-8 -*-
"""Export bot results to the exports/ directory."""
import os
from datetime import datetime
from src.bot import get_loaded_wallets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORTS_DIR = os.path.join(BASE_DIR, 'exports')

def export_results():
    """Export wallet log/report to exports/.  Returns the file path or None."""
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    wallets = get_loaded_wallets()
    stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = os.path.join(EXPORTS_DIR, f'report_{stamp}.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write("TurnKey Auto Bot — Airdrop — Export\n")
        f.write("=" * 50 + "\n")
        f.write(f"Date: {datetime.now().isoformat()}\n")
        f.write(f"Wallets loaded: {len(wallets)}\n\n")
        for i, w in enumerate(wallets, 1):
            f.write(f"{i}. {w}\n")
    return path
