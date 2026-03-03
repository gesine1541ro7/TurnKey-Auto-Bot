# -*- coding: utf-8 -*-
"""
Network and bot configuration for TurnKey airdrop automation.

Provides typed defaults, environment-variable overrides, and validation
for Sepolia testnet interaction parameters.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional


SEPOLIA_CHAIN_ID = 11155111
SEPOLIA_RPC_DEFAULT = "https://ethereum-sepolia-rpc.publicnode.com"
SEPOLIA_EXPLORER = "https://sepolia.etherscan.io"

MIN_DELAY_FLOOR = 1
MAX_DELAY_CEILING = 300
RETRY_CEILING = 20


@dataclass
class NetworkConfig:
    """Sepolia network connection parameters."""
    rpc_url: str = SEPOLIA_RPC_DEFAULT
    chain_id: int = SEPOLIA_CHAIN_ID
    explorer_url: str = SEPOLIA_EXPLORER
    gas_limit: int = 21_000
    gas_price_gwei: float = 1.5
    request_timeout: int = 30

    @classmethod
    def from_env(cls) -> "NetworkConfig":
        """Build a NetworkConfig from environment variables (if set)."""
        return cls(
            rpc_url=os.environ.get("TURNKEY_RPC_URL", SEPOLIA_RPC_DEFAULT),
            chain_id=int(os.environ.get("TURNKEY_CHAIN_ID", str(SEPOLIA_CHAIN_ID))),
            gas_limit=int(os.environ.get("TURNKEY_GAS_LIMIT", "21000")),
            gas_price_gwei=float(os.environ.get("TURNKEY_GAS_PRICE", "1.5")),
            request_timeout=int(os.environ.get("TURNKEY_TIMEOUT", "30")),
        )


@dataclass
class BotConfig:
    """Timing and retry behaviour for the airdrop bot."""
    delay_min: int = 5
    delay_max: int = 15
    max_retries: int = 3
    wallets_path: str = "wallets.txt"

    def validate(self) -> None:
        """Raise ValueError on invalid field values."""
        if self.delay_min < MIN_DELAY_FLOOR:
            raise ValueError(f"delay_min must be >= {MIN_DELAY_FLOOR}")
        if self.delay_max > MAX_DELAY_CEILING:
            raise ValueError(f"delay_max must be <= {MAX_DELAY_CEILING}")
        if self.delay_min > self.delay_max:
            raise ValueError("delay_min must not exceed delay_max")
        if not 1 <= self.max_retries <= RETRY_CEILING:
            raise ValueError(f"max_retries must be between 1 and {RETRY_CEILING}")


@dataclass
class AppConfig:
    """Top-level configuration aggregating network and bot settings."""
    network: NetworkConfig = field(default_factory=NetworkConfig)
    bot: BotConfig = field(default_factory=BotConfig)

    @classmethod
    def default(cls) -> "AppConfig":
        return cls(
            network=NetworkConfig.from_env(),
            bot=BotConfig(),
        )

    def validate(self) -> None:
        self.bot.validate()
