from simulated_city.config import load_config


def test_load_config_defaults_when_missing(tmp_path) -> None:
    cfg = load_config(tmp_path / "missing.yaml")
    assert cfg.mqtt.host
    assert cfg.mqtt.port


def test_load_config_reads_yaml(tmp_path) -> None:
    p = tmp_path / "config.yaml"
    p.write_text(
        """
        mqtt:
          host: example.com
          port: 1883
          tls: false
          client_id_prefix: demo
          keepalive_s: 30
          base_topic: test
        """.strip(),
        encoding="utf-8",
    )

    cfg = load_config(p)
    assert cfg.mqtt.host == "example.com"
    assert cfg.mqtt.port == 1883
    assert cfg.mqtt.tls is False
    assert cfg.mqtt.client_id_prefix == "demo"
    assert cfg.mqtt.keepalive_s == 30
    assert cfg.mqtt.base_topic == "test"
