from risk_assessment_tool import RiskAssessmentTool
from data import phases_of_birth
from output import Output

def main():
    tool = RiskAssessmentTool(data={"phases_of_birth": phases_of_birth})
    output = Output(data={"phases_of_birth": phases_of_birth})

    # Example data points
    data_points = {
        "pain_level": 8,
        "dilation": 4,
        "ctg": "non_reassuring"
    }

    assessed_interventions = tool.assess_risk("latent_phase", data_points)
    output.display(assessed_interventions)

if __name__ == "__main__":
    main()
