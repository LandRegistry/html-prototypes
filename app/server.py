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

# Sprint 3, prototype 1, conveyancer - buyer relationship --------------------------
@app.route('/sprint-3/conveyancer-register')
def sprint_3_conveyancer_register():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-3-register.html')

@app.route('/sprint-3/select-action')
def sprint_3_select_action():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-4-select-action.html')

@app.route('/sprint-3/add-buyers')
def sprint_3_add_buyers():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-5-add-buyers.html')

# Sprint 3, Execute Deed -reworked from sprint 2 -----------------------------------
@app.route('/sprint-3/execute-deed')
def sprint_3_execute_deed():
  return render_template('sprint-3/deed/buyer-1-execute-deed.html')

@app.route('/sprint-3/execution-complete')
def sprint_3_execution_complete():
  return render_template('sprint-3/deed/buyer-2-execution-complete.html')



# Sprint 2, prototype 1: Passing a "token" -----------------------------------------
@app.route('/sprint-2/token')
def sprint_2_token():
  return render_template('sprint-2/token/citizen-1-register.html')

@app.route('/sprint-2/select-action')
def sprint_2_select_action():
  return render_template('sprint-2/token/citizen-2-select-action.html')

@app.route('/sprint-2/choose-method')
def sprint_2_choose_method():
  return render_template('sprint-2/token/citizen-3-choose-method.html')

@app.route('/sprint-2/generate-token')
def sprint_2_generate_token():
  return render_template('sprint-2/token/citizen-4-generate-token.html')

@app.route('/sprint-2/show-change')
def sprint_2_show_change():
  return render_template('sprint-2/token/citizen-5-register-during-change.html')

@app.route('/sprint-2/input-token')
def sprint_2_input_token():
  return render_template('sprint-2/token/conveyancer-1-input-token.html')

@app.route('/sprint-2/retrieve-token')
def sprint_2_retrieve_token():
  return render_template('sprint-2/token/conveyancer-2-retrieve-details.html')

# Sprint 2, spike - Execute Deed -----------------------------------------
@app.route('/sprint-2/execute-deed')
def sprint_2_execute_deed():
  return render_template('sprint-2/deed/buyer-1-execute-deed.html')

@app.route('/sprint-2/execution-complete')
def sprint_2_execution_complete():
  return render_template('sprint-2/deed/buyer-2-execution-complete.html')


if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
