"""Initialize Flask app."""
from pathlib import Path
from flask import Flask, render_template
import covid.adapters.repository as repo
from covid.adapters.memory_repository import MemoryRepository, populate
# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from music.domainmodel.track import Track


# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!

def create_app(test_config=None):
    # Create the Flask App OBJECT 
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    # Data Path
    data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    # fill the content of the repository from the provided csv files
    populate(data_path, repo.repo_instance)

    @app.route('/')
    def home():
        some_track = create_some_track()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
        return render_template('simple_tr', track=some_track)

    return app
