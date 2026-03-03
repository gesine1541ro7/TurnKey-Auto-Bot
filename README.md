# TurnKey-Auto-Bot
TurnKey Auto Bot Airdrop — CLI automation for TurnKey testnet airdrop tasks with multi-wallet support, configurable execution delays, transaction export reports, Sepolia network integration, batch processing, and Rich terminal interface for Web3 wallet infrastructure testing
<div align="center">

```
 ______  __ __  ____   ____   __  _    ___  __ __          ____  __ __  ______   ___          ____    ___   ______ 
|      ||  |  ||    \ |    \ |  |/ ]  /  _]|  |  |        /    ||  |  ||      | /   \        |    \  /   \ |      |
|      ||  |  ||  D  )|  _  ||  ' /  /  [_ |  |  | _____ |  o  ||  |  ||      ||     | _____ |  o  )|     ||      |
|_|  |_||  |  ||    / |  |  ||    \ |    _]|  ~  ||     ||     ||  |  ||_|  |_||  O  ||     ||     ||  O  ||_|  |_|
  |  |  |  :  ||    \ |  |  ||     \|   [_ |___, ||_____||  _  ||  :  |  |  |  |     ||_____||  O  ||     |  |  |  
  |  |  |     ||  .  \|  |  ||  .  ||     ||     |       |  |  ||     |  |  |  |     |       |     ||     |  |  |  
  |__|   \__,_||__|\_||__|__||__|\_||_____||____/        |__|__| \__,_|  |__|   \___/        |_____| \___/   |__|
```

# TurnKey Auto Bot — Airdrop

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![TurnKey](https://img.shields.io/badge/TurnKey-Sepolia-purple?style=for-the-badge)](https://turnkey.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)](https://github.com)

**CLI automation for TurnKey testnet airdrop tasks — multi-wallet support, configurable delays, export reports.**

[Features](#-features) • [Getting Started](#-getting-started) • [Configuration](#-configuration) • [Usage](#-usage) • [FAQ](#-faq)

</div>

---

## Official Links

| Resource | URL |
|----------|-----|
| TurnKey Website | https://turnkey.com |
| TurnKey Documentation | https://docs.turnkey.com |
| TurnKey Dashboard | https://app.turnkey.com |
| Demo Embedded Wallet | https://wallet.tx.xyz |
| Sepolia Testnet Explorer | https://sepolia.etherscan.io |
| Sepolia Faucet (Alchemy) | https://www.alchemy.com/faucets/ethereum-sepolia |

---

## Features

<table>
<tr>
<td width="50%">

**Automation**
- Multi-wallet batch processing
- Configurable delay ranges (min/max seconds)
- Retry logic with max attempts
- Automated daily transaction cycles

</td>
<td width="50%">

**Infrastructure**
- JSON-based configuration
- Wallet file import (wallets.txt)
- Results export to reports
- Cyberpunk-style CMD interface

</td>
</tr>
<tr>
<td>

- [x] Load wallets from file
- [x] Run bot cycle (simulation/real)
- [x] Export results to exports/
- [x] Settings UI (RPC, delays, paths)

</td>
<td>

- [x] Install dependencies from menu
- [x] ANSI color output (colorama)
- [x] Cross-platform (Windows/Linux/macOS)
- [x] Python 3.10+ support

</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

- **Python 3.10+**
- pip (Python package manager)

### Install

**Option 1 — Quick start**

```bash
git clone <repository-url>
cd "TurnKey Auto Bot - Airdrop"
pip install -r requirements.txt
python main.py
```

**Option 2 — From menu**

```bash
python main.py
# Select [1] Install Dependencies
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| colorama | >=0.4.6 | ANSI color support on Windows CMD |
| requests | >=2.31.0 | HTTP requests for RPC/API calls |

---

## Configuration

Configuration is stored in `config.json` (created via **Settings** menu or manually).

**Example `config.json`:**

```json
{
  "rpc_url": "https://ethereum-sepolia-rpc.publicnode.com",
  "delay_min": 5,
  "delay_max": 15,
  "wallets_path": "wallets.txt",
  "max_retries": 3
}
```

| Field | Type | Description |
|-------|------|-------------|
| `rpc_url` | string | Ethereum Sepolia RPC endpoint (leave empty for default) |
| `delay_min` | int | Minimum delay between actions (seconds) |
| `delay_max` | int | Maximum delay between actions (seconds) |
| `wallets_path` | string | Path to wallet file (relative or absolute) |
| `max_retries` | int | Max retry attempts on failure |

> **Tip:** Use a public Sepolia RPC (e.g. `https://rpc.sepolia.org`) or Alchemy/Infura for reliability.

**Example `wallets.txt`:**

```
# One address per line (private key or address depending on implementation)
0x1234567890abcdef1234567890abcdef12345678
0xabcdef1234567890abcdef1234567890abcdef
```

---

## Usage

**Start the bot:**

```bash
python main.py
```

**CLI menu mockup:**

```
╔════════════════════════════════════════╗
║              MAIN MENU                 ║
╠════════════════════════════════════════╣
║  [1] Install Dependencies             ║
║  [2] Settings                         ║
║  [3] About                            ║
║  [4] Load Wallets                     ║
║  [5] Run Bot                          ║
║  [6] Export Results                   ║
║  [0] Exit                             ║
╚════════════════════════════════════════╝

► Enter option number (0-6):
```

**Typical workflow:**

1. **[1]** Install Dependencies — first-time setup
2. **[2]** Settings — configure RPC URL, delays, wallets path
3. **[4]** Load Wallets — load from `wallets.txt`
4. **[5]** Run Bot — execute airdrop cycle
5. **[6]** Export Results — save report to `exports/`

---

## Project Structure

```
TurnKey Auto Bot - Airdrop/
├── main.py              # Entry point, CLI menu, cyberpunk UI
├── config.json          # Runtime config (created via Settings)
├── wallets.txt          # Wallet list (one per line)
├── requirements.txt     # Python dependencies
├── Insiders.md          # Internal documentation
├── src/
│   ├── __init__.py      # Package init
│   ├── bot.py           # Bot logic, wallet loading, cycle execution
│   ├── settings.py      # config.json load/save, Settings UI
│   └── export.py        # Export results to exports/
└── exports/             # Generated reports (report_YYYYMMDD_HHMMSS.txt)
```

---

## FAQ

<details>
<summary><b>What is TurnKey?</b></summary>

TurnKey is a secure wallet infrastructure platform. Its testnet (Ethereum Sepolia) offers airdrop opportunities for users who participate in protocol interactions. This bot automates transaction cycles to streamline participation.
</details>

<details>
<summary><b>Do I need real ETH?</b></summary>

No. Use Sepolia testnet ETH only. Get free Sepolia ETH from faucets (e.g. Alchemy, Sepolia Faucet). Never use mainnet funds for testing.
</details>

<details>
<summary><b>How do I add wallets?</b></summary>

Create or edit `wallets.txt` in the project root. Add one wallet address (or private key, depending on your setup) per line. Lines starting with `#` are ignored. Then use **Load Wallets** from the menu.
</details>

<details>
<summary><b>Where are results exported?</b></summary>

Reports are saved to `exports/` as `report_YYYYMMDD_HHMMSS.txt`. Use **Export Results** from the menu after running the bot.
</details>

<details>
<summary><b>How do I increase the wallet batch size?</b></summary>

The bot processes wallets sequentially with built-in rate limiting to avoid API throttling. Batch size and delay intervals are configurable in `src/bot.py`.
</details>

<details>
<summary><b>Is this affiliated with TurnKey?</b></summary>

No. This is an independent community tool for educational and testnet purposes. Not officially endorsed or affiliated with TurnKey.
</details>

<details>
<summary><b>Security: should I share my private keys?</b></summary>

Never. Use testnet-only wallets. Keep `.env` and `wallets.txt` out of version control. This tool is for testing; never expose mainnet keys.
</details>

---

## Disclaimer

This software is provided **for educational and testnet use only**. Use at your own risk. The authors are not responsible for any loss of funds. Always verify you are on Sepolia testnet. This project is not affiliated with, endorsed by, or connected to TurnKey or any official TurnKey entity.

---

<div align="center">

**If this project helped you, consider starring the repo.**

ETH donation: `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb1`

</div>
