from flask import Flask, render_template, request
from risk_assessment_tool import RiskAssessmentTool
from data import phases_of_birth

app = Flask(__name__)

tool = RiskAssessmentTool(data={"phases_of_birth": phases_of_birth})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pain_level = int(request.form['pain_level'])
        dilation = int(request.form['dilation'])
        ctg = request.form['ctg']

        data_points = {
            "pain_level": pain_level,
            "dilation": dilation,
            "ctg": ctg
        }

        assessed_interventions = tool.assess_risk("latent_phase", data_points)
        return render_template('index.html', interventions=assessed_interventions, data=phases_of_birth)
    return render_template('index.html', interventions=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
