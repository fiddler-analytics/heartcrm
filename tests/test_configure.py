import heartcrm.conf as conf


def test_conf_writes_to_heartrc(monkeypatch, tmpdir):
    monkeypatch.setattr(conf, 'PROJECT_DIR', tmpdir.dirname)
    monkeypatch.setattr(conf, 'CURRENT_DIR', tmpdir.dirname)
    desired_config = {'redirect_uri': 'https://parrots.com',
                      'client_id': 'super',
                      'client_secret': 'secret',
                      'sandbox': True}
    conf.configure(**desired_config)
    config = conf.read_heartrc()
    assert config == desired_config
