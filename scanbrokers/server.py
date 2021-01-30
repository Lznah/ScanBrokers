import flask
import os
from .db import reload_data, get_db, find_agents_by_name, find_agent_by_ic
import copy

app = flask.Flask(__name__)

@app.route('/')
def index():
    """Landing page."""
    return flask.render_template(
        'home.html',
        title="you love stalking, we love it too",
        description="ScanBrokers is a tool that fulfills your deepest dreams abotu stalking people."
    )

@app.route('/search')
def search():
    """Search page."""
    query = flask.request.args.get('query') or ''
    minimal_number_of_letters = 4
    number_of_letters = len(query.replace(' ',''))
    agents = []
    if number_of_letters >= minimal_number_of_letters:
        agents = find_agents_by_name(query)
    return flask.render_template('search.html',
        title=f"Výsledky hledání pro 'query'", \
        minimal_number_of_letters=minimal_number_of_letters, \
        number_of_letters=number_of_letters, \
        query=query, agents=agents, \
        len=len(agents))

@app.route('/broker/<string:ic>')
def broker_detail(ic):
    """Agent's detail page."""
    agent = find_agent_by_ic(ic)
    if agent is None:
        flask.abort(404)
    return flask.render_template('broker_detail.html', title=f"Detail makléře {agent['name']}", agent=agent)

@app.cli.command()
def reload_db():
    reload_data()

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('page_not_found.html', title="404")

def create_app(*args, **kwargs):
    app = flask.Flask(__name__)
    with app.app_context():
        reload_data()
    return app

if __name__ == '__main__':
    app = create_app()