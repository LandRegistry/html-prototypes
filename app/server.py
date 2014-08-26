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

# Page prototypes, Register View --------------------------
@app.route('/register-view/register-2.0')
def register_2_0():
  return render_template('register-view/register-2.0.html')

# Sprint 4, Relationship verifier flow --------------------------
@app.route('/sprint-4/citizen-reference')
def sprint_4_reference():
  return render_template('sprint-4/relationship/citizen-reference.html')

@app.route('/sprint-4/citizen-login')
def sprint_4_citizen_login():
  return render_template('sprint-4/relationship/citizen-login.html')

@app.route('/sprint-4/citizen-confirm')
def sprint_4_citizen_confirm():
  return render_template('sprint-4/relationship/citizen-confirm.html')

@app.route('/sprint-4/citizen-complete')
def sprint_4_citizen_complete():
  return render_template('sprint-4/relationship/citizen-complete.html')

@app.route('/sprint-4/citizen-register')
def sprint_4_citizen_register():
  return render_template('sprint-4/relationship/citizen-register.html')

# Sprint 3, Register view --------------------------
@app.route('/sprint-3/register-v1')
def sprint_3_register_v1():
  return render_template('sprint-3/register-view/register-v1.html')

@app.route('/sprint-3/register-v1a-history')
def sprint_3_register_v1a_history():
  return render_template('sprint-3/register-view/register-v1a-history.html')

@app.route('/sprint-3/register-v1a-history-1')
def sprint_3_register_v1a_history_1():
  return render_template('sprint-3/register-view/register-v1a-history-1.html')

# Sprint 3, prototype 1, conveyancer - buyer relationship --------------------------
@app.route('/sprint-3/conveyancer-start')
def sprint_3_conveyancer_start():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-0-start.html')

@app.route('/sprint-3/conveyancer-login')
def sprint_3_conveyancer_login():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-1-login.html')

@app.route('/sprint-3/conveyancer-enter-title')
def sprint_3_conveyancer_enter_title():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-2-enter-title.html')

@app.route('/sprint-3/conveyancer-add-buyers')
def sprint_3_conveyancer_add_buyers():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-5-add-buyers.html')

@app.route('/sprint-3/relationship-reference')
def sprint_3_relationship_reference():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-6-ref-for-buyers.html')

# Sprint 3, prototype 1, buyer -> conveyancer relationship --------------------------
@app.route('/sprint-3/buyer-login')
def sprint_3_buyer_login():
  return render_template('sprint-3/buyer-conveyancer/buyer-1-login.html')

@app.route('/sprint-3/buyer-ref-code')
def sprint_3_buyer_ref_code():
  return render_template('sprint-3/buyer-conveyancer/buyer-2-reference-code.html')

@app.route('/sprint-3/buyer-register')
def sprint_3_buyer_register():
  return render_template('sprint-3/buyer-conveyancer/buyer-3-register.html')


# Sprint 3, Execute Deed - reworked from sprint 2 -----------------------------------
@app.route('/sprint-3/buyer-signing-start')
def sprint_3_buyer_signing_start():
  return render_template('sprint-3/deed/buyer-0-start.html')

@app.route('/sprint-3/buyer-signing-login')
def sprint_3_buyer_signing_login():
  return render_template('sprint-3/deed/buyer-0a-login.html')

@app.route('/sprint-3/display-charge-for-signing')
def sprint_3_execute_deed():
  return render_template('sprint-3/deed/buyer-1-sign-charge.html')

@app.route('/sprint-3/display-transfer-for-signing')
def sprint_3_execute_transfer():
  return render_template('sprint-3/deed/buyer-1a-sign-transfer.html')


@app.route('/sprint-3/two-factor')
def sprint_3_two_factor():
  return render_template('sprint-3/deed/buyer-2-two-factor.html')

@app.route('/sprint-3/signing-complete')
def sprint_3_signing_complete():
  return render_template('sprint-3/deed/buyer-3-signing-complete.html')



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


# Example pages - for designers -----------------------------------------
@app.route('/examples/example-1')
def example_1():
  return render_template('examples/example-page.html')



if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
