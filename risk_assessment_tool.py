class RiskAssessmentTool:
    def __init__(self, data):
        self.data = data

    def assess_risk(self, phase, data_points):
        interventions = self.data["phases_of_birth"][phase]["interventions"]
        scores = {}

        for intervention, details in interventions.items():
            score = 0
            for factor, value in details.get("risk_factors", {}).items():
                if data_points.get(factor) in value:
                    score += 1
            scores[intervention] = score

        return sorted(scores.items(), key=lambda item: item[1], reverse=True)
