# MQTT

This template includes **paho-mqtt** by default and ships with a committed `config.yaml` that points at a HiveMQ-style broker configuration.

## Configure HiveMQ Cloud

1. Edit `config.yaml`:
   - Set `mqtt.host` to your HiveMQ cluster host (example: `xxxxxx.s1.eu.hivemq.cloud`)
   - Keep `mqtt.port: 8883` and `mqtt.tls: true`

2. Store credentials in a local `.env` file:

```bash
cp .env.example .env
# edit .env and set:
# HIVEMQ_USERNAME=...
# HIVEMQ_PASSWORD=...
```

## Connect from Python

```python
from simulated_city.config import load_config
from simulated_city.mqtt import connect_mqtt, topic

cfg = load_config().mqtt
handle = connect_mqtt(cfg, client_id_suffix="demo")
handle.client.loop_start()

handle.publish_json(topic(cfg, "metrics"), '{"step": 1, "agents": 25}')
```

## Using other brokers

Projects can switch brokers by editing `config.yaml` (host/port/tls) or by loading a different config file.
