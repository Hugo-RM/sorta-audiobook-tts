# This module integrates with Piper TTS (https://github.com/rhasspy/piper)

from flask import (Flask, render_template, request, redirect, url_for)
from flask_bootstrap import Bootstrap5
from gtts import gTTS
import tts as tts

# The base app is run with bootstrap.
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# The initial route for the index page.
@app.route('/', methods=('GET', 'POST')) # assuming we'll pass info this way, added methods
def home():
   if request.method == 'POST':

        # This is to make sure that the button to head back to index works accurately
        topic = request.form.get('topic')
        content = request.form.get('content')
        
        if not topic:
            return redirect(url_for('home'))

        if not content:
            content = ''

        topic = tts.sanitize_filename(topic)

        return redirect(url_for('reader', topic=topic, content=content))
   
   return render_template('index.html')

# The code for the reader in order to also take you to the section page.
@app.route('/reader', methods=('GET', 'POST'))
def reader():      
   # This gains the topic, in order to search within the wikipedia api with the various information
   topic = request.args.get('topic', '')
   content = request.args.get('content', '')
      
   # This determines that if there's no information found, it will give a brief statement and audio file for it
   tts.convertText(topic, content)
   
   return render_template('reader.html', topic=topic, content=content)