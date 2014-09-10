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

# ---------------------------------------------------------------------------

# Transfer prototypes, login page
@app.route('/transfer/login')
def transfer_login():
  return render_template('transfer/login.html')

# Transfer prototypes, conveyancer-case-list page
@app.route('/transfer/conveyancer-case-list')
def conveyancer_case_list():
  return render_template('transfer/conveyancer-case-list.html')

# Transfer prototypes, conveyancer-case-list page
@app.route('/transfer/create-transfer')
def create_transfer():
  return render_template('transfer/create-transfer.html')

# Transfer prototypes, new provisions page
@app.route('/transfer/new-provisions')
def transfer_new_provisions():
  return render_template('transfer/new-provisions.html')

# Transfer prototypes, mortgage details page
@app.route('/transfer/mortgage-details')
def transfer_mortgage_details():
  return render_template('transfer/mortgage-details.html')

# Transfer prototypes, confirm page
@app.route('/transfer/confirm')
def transfer_confirm():
  return render_template('transfer/confirm.html')

# Transfer prototypes, done page
@app.route('/transfer/done')
def transfer_done():
  return render_template('transfer/done.html')

# ---------------------------------------------------------------------------

# Transaction flows, citizens sign transfer and charge v2.0 -----------------
@app.route('/transfer-and-charge/citizen-1-start')
def transfer_and_charge_citizen_1_start_2_0():
  return render_template('transfer-and-charge/citizen-1-start-2.0.html')

# Step 1 - login with GOV.UK Verify
@app.route('/transfer-and-charge/citizen-1-login')
def transfer_and_charge_citizen_1_login_2_0():
  return render_template('transfer-and-charge/citizen-1-login-2.0.html')

# Step 2 - Client 1 enters token
@app.route('/transfer-and-charge/citizen-1-enter-token')
def transfer_and_charge_citizen_1_enter_token_2_0():
  return render_template('transfer-and-charge/citizen-1-enter-token-2.0.html')

# Step 3 - Client 1 signs mortgage deed
@app.route('/transfer-and-charge/citizen-1-sign-mortgage')
def transfer_and_charge_citizen_1_sign_mortgage_2_0():
  return render_template('transfer-and-charge/citizen-1-sign-mortgage-2.0.html')

# Step 4 - Client 1 signs transfer
@app.route('/transfer-and-charge/citizen-1-sign-transfer')
def transfer_and_charge_citizen_1_sign_transfer_2_0():
  return render_template('transfer-and-charge/citizen-1-sign-transfer-2.0.html')

# Step 5 - Client 1 - semi confirmation
@app.route('/transfer-and-charge/citizen-1-semi-confirmed')
def transfer_and_charge_citizen_1_semi_confirmed_2_0():
  return render_template('transfer-and-charge/citizen-1-semi-confirmed-2.0.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, conveyancer initiates v2.0 --------
@app.route('/relationship-starts/conveyancer-start')
def conveyancer_start_2_0():
  return render_template('relationship-starts/conveyancer-start-2.0.html')

# Step 1 - login with GOV.UK Verify
@app.route('/relationship-starts/conveyancer-login')
def conveyancer_verify_2_0():
  return render_template('relationship-starts/conveyancer-login-2.0.html')

# Step 2 - find correct property
@app.route('/relationship-starts/conveyancer-find-property')
def conveyancer_find_property_2_0():
  return render_template('relationship-starts/conveyancer-find-property-2.0.html')

# Step 3 - results and select correct property
@app.route('/relationship-starts/conveyancer-select-property')
def conveyancer_select_property_2_0():
  return render_template('relationship-starts/conveyancer-select-property-2.0.html')

# Step 4 - select associated task
@app.route('/relationship-starts/conveyancer-select-task')
def conveyancer_select_task_2_0():
  return render_template('relationship-starts/conveyancer-select-task-2.0.html')

# Step 5 - set the number of clients
@app.route('/relationship-starts/conveyancer-add-clients')
def conveyancer_add_clients_2_0():
  return render_template('relationship-starts/conveyancer-add-clients-2.0.html')

# Step 6 - add 1st client
@app.route('/relationship-starts/conveyancer-add-client-1')
def conveyancer_add_client_1_2_0():
  return render_template('relationship-starts/conveyancer-add-client-1-2.0.html')

# Step 7 - add 2nd client
@app.route('/relationship-starts/conveyancer-add-client-2')
def conveyancer_add_client_2_2_0():
  return render_template('relationship-starts/conveyancer-add-client-2-2.0.html')

# Step 8 - confirmation
@app.route('/relationship-starts/conveyancer-confirm')
def conveyancer_confirm_2_0():
  return render_template('relationship-starts/conveyancer-confirm-2.0.html')

# Step 9 - generated token
@app.route('/relationship-starts/conveyancer-token')
def conveyancer_token_2_0():
  return render_template('relationship-starts/conveyancer-token-2.0.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, client(s) confirm v2.0 --------
@app.route('/relationship-starts/client-start')
def client_start_2_0():
  return render_template('relationship-starts/client-start-2.0.html')

# Step 1 - login with GOV.UK Verify
@app.route('/relationship-starts/client-login')
def client_verify_2_0():
  return render_template('relationship-starts/client-login-2.0.html')

# Step 2 - Client 1 enters token
@app.route('/relationship-starts/client-enter-token')
def client_enter_token_2_0():
  return render_template('relationship-starts/client-enter-token-2.0.html')

# Step 3 - Client 1 confirms
@app.route('/relationship-starts/client-confirm')
def client_confirm_2_0():
  return render_template('relationship-starts/client-confirm-2.0.html')

# Step 4 - Client 1 receives confirmation
@app.route('/relationship-starts/client-semi-confirmed')
def client_semi_confirmed_2_0():
  return render_template('relationship-starts/client-semi-confirmed-2.0.html')

# Step 5 - Client 2 visits start page
@app.route('/relationship-starts/client-2-start')
def client_2_start_2_0():
  return render_template('relationship-starts/client-2-start-2.0.html')

# Step 6 - Client 2 visits start page
@app.route('/relationship-starts/client-2-login')
def client_2_verify_2_0():
  return render_template('relationship-starts/client-2-login-2.0.html')

# Step 7 - Client 2 enters token
@app.route('/relationship-starts/client-2-enter-token')
def client_2_enter_token_2_0():
  return render_template('relationship-starts/client-2-enter-token-2.0.html')

# Step 8 - Client 2 confirms
@app.route('/relationship-starts/client-2-confirm')
def client_2_confirm_2_0():
  return render_template('relationship-starts/client-2-confirm-2.0.html')

# Step 9 - Client 2 receives (all parties) confirmation
@app.route('/relationship-starts/clients-confirmed')
def clients_confirmed_2_0():
  return render_template('relationship-starts/clients-confirmed-2.0.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, citizen confirms v2.0 --------
@app.route('/relationship-starts/citizen-confirms')
def citizen_confirms_2_0():
  return render_template('relationship-starts/citizen-confirms-2.0.html')

# ---------------------------------------------------------------------------

# Page prototypes, Register View --------------------------
@app.route('/register-view/register-2.0')
def register_2_0():
  return render_template('register-view/register-2.0.html')
@app.route('/register-view/register-2.1')
def register_2_1():
  return render_template('register-view/register-2.1.html')

# Page prototypes, Example mortgage agreement  --------------------------
@app.route('/legal-documents/mortgage-agreement-v1')
def mortgage_agreement_1():
  return render_template('legal-documents/mortgage-agreement-v1.html')

# Page prototypes, Example transfer agreement  --------------------------
@app.route('/legal-documents/transfer-agreement-v1')
def transfer_agreement_1():
  return render_template('legal-documents/transfer-agreement-v1.html')

# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------

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
