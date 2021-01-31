import flask
import pytest
from helper import set_envvar
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

def _test_app():
    app = _import_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_app_imports():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/empty_folder/')
    app = _import_app()
    assert isinstance(app, flask.Flask)

def test_app_server_index():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/')
        assert res.status_code == 200

def test_app_server_not_found_page():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/non-existing-page')
        assert res.status_code == 404

def test_app_agent_not_found():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/broker/non-existing-ic')
        assert res.status_code == 404
        assert b'nenalezena' in res.data

def test_app_agent_found():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/broker/0000001')
        assert res.status_code == 200
        assert b'Testing agent 1' in res.data

def test_app_search_empty_input():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/search?query=')
        assert res.status_code == 200
        assert 'Hledané jméno musí obsahovat alespoň 4 znaky.' in res.data.decode('utf-8')

def test_app_search_query_contains_at_least_four_characters():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/search?query=a aa')
        assert res.status_code == 200
        assert 'Hledané jméno musí obsahovat alespoň 4 znaky.' in res.data.decode('utf-8')

def test_app_search_query_results():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/search?query=testing agent 1')
        assert res.status_code == 200
        assert b'Testing agent 1' in res.data
        assert b'Testing agent 2' not in res.data
        assert b'Testing agent 3' not in res.data
        assert b'Testing agent 4' not in res.data
        assert b'Testing agent 5' not in res.data

def test_app_search_query_case_insensitive():
    set_envvar('WEBSERVER_DATAPATH', 'tests/data/not_empty_folder/')
    app = _import_app()
    with app.test_client() as client:
        res = client.get('/search?query=Testing')
        res2 = client.get('/search?query=testing')

        assert b'Testing agent 1' in res.data
        assert b'Testing agent 2' not in res.data
        assert b'Testing agent 3' in res.data
        assert b'Testing agent 4' in res.data
        assert b'Testing agent 5' in res.data

        assert b'Testing agent 1' in res2.data
        assert b'Testing agent 2' not in res2.data
        assert b'Testing agent 3' in res2.data
        assert b'Testing agent 4' in res2.data
        assert b'Testing agent 5' in res2.data
