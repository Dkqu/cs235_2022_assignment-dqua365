"""Initialize Flask app."""

from flask import Flask, render_template

# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!
from music.domainmodel.track import Track


# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!

def create_app():
    # Create the Flask App OBJECT 
    app = Flask(__name__)

    @app.route('/')
    def home():
        some_track = create_some_track()
        # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
        return render_template('simple_tr', track=some_track)

    return app
