from __future__ import annotations

from dataclasses import dataclass
import socket
import ssl
import time

import paho.mqtt.client as mqtt

from .config import MqttConfig


@dataclass(frozen=True, slots=True)
class MqttClientHandle:
    client: mqtt.Client

    def publish_json(self, topic: str, payload: str, qos: int = 0, retain: bool = False) -> None:
        # Keep it string-based by default to avoid forcing a JSON dependency.
        result = self.client.publish(topic, payload=payload, qos=qos, retain=retain)
        result.wait_for_publish()


def connect_mqtt(cfg: MqttConfig, *, client_id_suffix: str | None = None, timeout_s: float = 10.0) -> MqttClientHandle:
    """Create and connect an MQTT client using configuration.

    Notes:
    - This function does not run a loop for you; call `client.loop_start()` or `client.loop_forever()`.
    - Credentials are optional; for HiveMQ Cloud you'll typically set env vars.
    """

    client_id = _make_client_id(cfg.client_id_prefix, client_id_suffix)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)

    if cfg.username is not None:
        client.username_pw_set(cfg.username, password=cfg.password)

    if cfg.tls:
        context = ssl.create_default_context()
        client.tls_set_context(context)

    # Connect (blocking) with a simple timeout.
    started = time.time()
    last_err: Exception | None = None
    while time.time() - started < timeout_s:
        try:
            client.connect(cfg.host, cfg.port, keepalive=cfg.keepalive_s)
            return MqttClientHandle(client=client)
        except (OSError, socket.gaierror, ssl.SSLError) as e:
            last_err = e
            time.sleep(0.25)

    raise TimeoutError(f"Failed to connect to MQTT broker {cfg.host}:{cfg.port} within {timeout_s}s") from last_err


def topic(cfg: MqttConfig, suffix: str) -> str:
    suffix = suffix.lstrip("/")
    return f"{cfg.base_topic}/{suffix}" if suffix else cfg.base_topic


def _make_client_id(prefix: str, suffix: str | None) -> str:
    safe_prefix = prefix.strip() or "simcity"
    if suffix:
        return f"{safe_prefix}-{suffix}"
    return safe_prefix
