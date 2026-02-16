from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
import yaml


@dataclass(frozen=True, slots=True)
class MqttConfig:
    host: str
    port: int
    tls: bool
    username: str | None
    password: str | None
    client_id_prefix: str
    keepalive_s: int
    base_topic: str


@dataclass(frozen=True, slots=True)
class AppConfig:
    mqtt: MqttConfig


def load_config(path: str | Path = "config.yaml") -> AppConfig:
    # Load a local .env if present (it is gitignored by default).
    # This makes workshop setup easier while keeping secrets out of git.
    load_dotenv(override=False)

    data = _load_yaml_dict(path)
    mqtt = data.get("mqtt") or {}

    host = str(mqtt.get("host") or "localhost")
    port = int(mqtt.get("port") or 1883)
    tls = bool(mqtt.get("tls") or False)

    username_env = mqtt.get("username_env")
    password_env = mqtt.get("password_env")
    username = os.getenv(str(username_env)) if username_env else None
    password = os.getenv(str(password_env)) if password_env else None

    client_id_prefix = str(mqtt.get("client_id_prefix") or "simcity")
    keepalive_s = int(mqtt.get("keepalive_s") or 60)
    base_topic = str(mqtt.get("base_topic") or "simulated-city")

    return AppConfig(
        mqtt=MqttConfig(
            host=host,
            port=port,
            tls=tls,
            username=username,
            password=password,
            client_id_prefix=client_id_prefix,
            keepalive_s=keepalive_s,
            base_topic=base_topic,
        )
    )


def _load_yaml_dict(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}

    content = p.read_text(encoding="utf-8")
    loaded = yaml.safe_load(content)
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(f"Config file {p} must contain a YAML mapping at top level")
    return loaded
