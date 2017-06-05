import pytest
import os
import logging
from lago import sdk


@pytest.fixture(scope='module')
def test_results(request):
    current_dir = os.path.abspath(os.getcwd())
    results_path = os.path.join(
        current_dir, 'test_results', str(request.module.__name__)
    )
    return results_path


@pytest.fixture(scope='module')
def env(test_results, config='init-myapp.yaml', workdir='/tmp/lago-workdir'):
    lago_env = sdk.init(
        config=config,
        workdir=workdir,
    )
    lago_env.start()
    yield lago_env
    collect_path = os.path.join(test_results, 'collect')
    lago_env.collect_artifacts(output_dir=collect_path, ignore_nopath=True)
    lago_env.destroy()


def test_myapp_deploy(env):
    env.deploy()


def test_my_app_clean_import(env):
    client = env.get_vms()['myapp-client']
    res = client.ssh(['python3', '-c', '"import myapp"'])
    assert res.code == 0
