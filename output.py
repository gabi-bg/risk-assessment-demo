class Output:
    def __init__(self, data):
        self.data = data

    def display(self, interventions):
        print("Top 3 Most Likely Interventions:")
        for i, (intervention, score) in enumerate(interventions[:3]):
            side_effects = self.data["phases_of_birth"]["latent_phase"]["interventions"][intervention]["side_effects"]
            print(f"{i+1}. {intervention.replace('_', ' ').title()}")
            print(f"   - Side Effects: {', '.join(side_effects)}")
