import os

from flask import Flask, render_template
from flask.ext.assets import Environment

app = Flask(__name__)
app.debug = True

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
  return {
    'asset_path': '/static/govuk-template/',
    'prototypes_asset_path': '/static/'
  }

@app.route('/')
def home():
  return render_template('index.html')

# Sprint 2, prototype 1: Passing a "token" -----------------------------------------
@app.route('/sprint-2/token')
def sprint_2_1():
  return render_template('sprint-2/citizen-1-register.html')

@app.route('/sprint-2/select-action')
def sprint_2_2():
  return render_template('sprint-2/citizen-2-select-action.html')

@app.route('/sprint-2/choose-method')
def sprint_2_3():
  return render_template('sprint-2/citizen-3-choose-method.html')

@app.route('/sprint-2/generate-token')
def sprint_2_4():
  return render_template('sprint-2/citizen-4-generate-token.html')

@app.route('/sprint-2/input-token')
def sprint_2_5():
  return render_template('sprint-2/conveyancer-1-input-token.html')

@app.route('/sprint-2/retrieve-token')
def sprint_2_6():
  return render_template('sprint-2/conveyancer-2-retrieve-details.html')


if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
