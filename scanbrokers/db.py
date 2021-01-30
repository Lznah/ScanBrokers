import errno
import os
import datetime
import json
import flask

ENVVAR_DATAPATH = 'WEBSERVER_DATAPATH'

def reload_data(path, data = {
        'json_files' : {},
        'agents': {}
    }):
    """Process new data into existing data object

    :param path: New json that needs to be applied on existing data
    :type path: dictionary

    :param data: Dictionary of already loaded json files
    :type data: dictionary

    :param app: Flask app
    :type app: Flask app object

    :raises FileNotFoundError: Raises exception if provided path does not exist

    :return: Returns dictionary of loadeded files and preprocessed cached data
    """
    abs_path = os.path.join(os.getcwd(), path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    previous_files = data['json_files'].keys()
    json_files = [json_file for json_file in os.listdir(abs_path) if json_file.endswith('.json')]
    new_files = [json_file for json_file in json_files if json_file not in previous_files]
    list_new_data, errors = load_json_files(new_files, path)
    for filename in list_new_data:
        data['json_files'][filename] = list_new_data[filename]
        preprocess_queries(data, filename)
        break
    for error in errors:
        flask.app.logger.warning(error)
    return data


def preprocess_queries(data, filename):
    """This function calls functions that process new incoming data onto already preprocessed data.

    :param data: Already existing data
    :type data: dictionary

    :param filename: A filename of the new incoming data.
    :type filename: string
    """
    new_data = data['json_files'][filename]
    preprocess_agents_history(data['agents'], new_data, filename)

def preprocess_agents_history(agents, new_data, filename):
    """Process new data into existing data object

    :param agents: Existing data object
    :type agents: dictionary

    :param new_data: New json that needs to be applied on existing data
    :type new_data: dictionary

    :param filename: original filename of the new data
    :type filename: string
    """
    unixtime = filename.replace('.json','')
    date = format_unixtime(unixtime)
    for agency_id in new_data:
        agency = new_data[agency_id]
        if 'branches' not in agency.keys():
            continue
        for franchize in agency['branches']:
            if 'agents' not in franchize.keys():
                continue
            for agent in franchize['agents']:
                ic = agent['ic']
                if ic not in agents:
                    agents[ic] = {}
                agents[ic]['ic'] = ic
                agents[ic]['name'] = agent['name'] or ''
                agents[ic]['estate_counts'] = agent['estates_count'] or 0
                historize('agency_history', agents[ic], agency['name'], format_unixtime(unixtime))

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

def load_json_files(filenames, path):
    """Loads and parses JSON files.
    
    :param filenames: JSON files that are going to be loaded
    :type filenames: list

    :param path: A relative path to files
    :type path: string

    :return: Returns tuple of loaded JSON files and list of errors
    :type: tuple(data, errors)
    """
    data = {}
    errors = {}
    for filename in filenames:
        abs_path = os.path.join(os.getcwd(), path)
        if filename not in data.keys():
            json_path = os.path.join(abs_path, filename)
            with open(json_path, 'r', encoding = 'utf-8') as f:
                try:
                    data[filename] = json.load(f)
                except ValueError:
                    errors.append(f'File {filename} is not valid JSON file')
                f.close()
    return (data, errors)

def find_agents_by_name(name):
    """Find agents by name

    :param name: Agent's name or it's subpart
    :type name: string

    :return: Returns list of found agents defined by their IČ
    """
    db = get_db()
    results = []
    for ic in db['agents']:
        agent = db['agents'][ic]
        if name.lower() in agent['name'].lower():
            results.append({
                'name': agent['name'],
                'ic': ic
            })
    return results


def find_agent_by_ic(ic):
    """Find agent by his/her (be inclusive) ic number

    :param name: Agent's ic number
    :type name: int

    :return: Returns agent objet
    """
    db = get_db()
    if ic not in db['agents'].keys():
        return None
    return db['agents'][ic]


def get_db():
    """Function to retrieve in-memory database

    :return: Database dictionary or loaded files and preprocessed queries
    :rtype: dictionary
    """
    if ENVVAR_DATAPATH not in os.environ:
        app.logger.critical(f'Missing path to data folder in environment value: {ENVVAR_DATAPATH}')
        exit(1)
    if 'db' not in flask.g:
        flask.g.db = reload_data(os.environ[ENVVAR_DATAPATH])
    return flask.g.db


def format_unixtime(unixtime):
    """Transforms unixtime to simple DATE format

    :param unixtime: Unixtime
    :type: string

    :return: Returns a formatted date string
    :rtype: string
    """
    return datetime.datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d')

def get_year(unixtime):
    """Tranforms unixtime to full year

    :param unixtime: Unixtime
    :type: string

    :return: Returns full year from unixtime
    :rtype: string    
    """
    return datetime.datetime.fromtimestamp(int(unixtime)).strftime('%Y')

if __name__ == '__main__':
    print(reload_data('./data/'))