import pytest
from helper import del_envvar, set_envvar
from scanbrokers.db import reload_data, historize
import flask
import importlib


def _import_app():
    import scanbrokers
    importlib.reload(scanbrokers)  # force reload (config could change)
    if hasattr(scanbrokers, 'app'):
        return scanbrokers.app
    elif hasattr(scanbrokers, 'create_app'):
        return scanbrokers.create_app(None)
    else:
        raise RuntimeError(
            "Can't find a Flask app. "
            "Either instantiate `scanbrokers.app` variable "
            "or implement `scanbrokers.create_app(dummy)` function. "
            "See https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/"
            "for additional information."
        )

def test_db_missing_envvar():
    del_envvar('WEBSERVER_DATAPATH')
    app = _import_app()
    with app.app_context():
        with pytest.raises(SystemExit) as wrapped:
            reload_data()
        assert wrapped.type == SystemExit
        assert wrapped.value.code == 1

def test_db_nonexisting_path():
    set_envvar('WEBSERVER_DATAPATH', '/non-existing-path')
    app = _import_app()
    with pytest.raises(FileNotFoundError):
        reload_data()

def test_db_empty():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/empty_folder/')
    app = _import_app()
    with app.app_context():
        data = reload_data()
        assert len(data['json_files'].keys()) == 0

def test_db_not_empty():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.app_context():
        data = reload_data()
        assert len(data['json_files'].keys()) == 1
        assert '0000000000.json' in data['json_files'].keys()

def test_db_agents_not_empty_folder():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.app_context():
        data = reload_data()
        assert len(data['agents'].keys()) == 4

def test_db_agents_preprocessing_ignoring_ambigous_ic():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.app_context():
        data = reload_data()
        assert data['agents']['0000003']['name'] == 'Testing agent 4'

def test_db_agents_empty_if_data_with_missing_values():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/data_with_missing_values/')
    app = _import_app()
    with app.app_context():
        # flushing database with empty initialization
        data = reload_data({
            'json_files' : {},
            'agents': {}
        })
        assert '1234567890.json' in data['json_files'].keys()
        assert len(data['agents'].keys()) == 0

def test_db_reloading_adds_new_data():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.app_context():
        data = reload_data({
            'json_files' : {},
            'agents': {}
        })
        import shutil
        import os
        shutil.copyfile('tests/data/not_empty_folder/new_data/0000086400.json', 'tests/data/not_empty_folder/0000086400.json')
        data = reload_data(data)
        os.remove('tests/data/not_empty_folder/0000086400.json')

        assert len(data['json_files']) == 2
        assert '0000000000.json' in data['json_files'].keys()
        assert '0000086400.json' in data['json_files'].keys()
        assert 'new-agent' in data['agents'].keys()
        assert 'new-agent-2' in data['agents'].keys()



def historize(history_name, obj, key, historized_data):
    """Function that saves history of the object into history object by defined key.

    :param history_name: A key inside history object
    :type history_name: object

    :param obj: Object that needs to be historized.
    :type obj: object

    :param key: Key that will serve as and index
    :type key: string

    :param historized_data: Data that needs to be historized
    :type historized_data: string
    """
    if 'history' not in obj.keys():
        obj['history'] = {}
    if history_name not in obj['history'].keys():
        obj['history'][history_name] = {}
    if key not in obj['history'][history_name].keys():
        obj['history'][history_name][key] = []
    obj['history'][history_name][key].append(historized_data)


def test_db_historize():
    history_name = "my-sleeping-routine"
    some_obj = {}
    key = "some-key"
    some_data1 = "On Monday I woke up early"
    some_data2 = "On Tuesday I woke up pretty late"
    historize('my-sleeping-routine', some_obj, key, some_data1)
    assert 'history' in some_obj.keys()
    assert history_name in some_obj['history'].keys()
    assert key in some_obj['history'][history_name].keys()
    assert some_obj['history'][history_name][key][0] == some_data1

    historize('my-sleeping-routine', some_obj, key, some_data2)
    assert some_obj['history'][history_name][key][1] == some_data2
    assert len(some_obj['history'][history_name][key]) == 2
    
