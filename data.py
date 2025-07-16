phases_of_birth = {
    "latent_phase": {
        "interventions": {
            "pain_relief": {
                "side_effects": ["drowsiness", "nausea"],
                "risk_factors": {
                    "pain_level": [7, 8, 9, 10]
                }
            },
            "amniotomy": {
                "side_effects": ["infection", "umbilical_cord_prolapse"],
                "risk_factors": {
                    "dilation": [4, 5, 6]
                }
            },
            "oxytocin": {
                "side_effects": ["uterine_hyperstimulation", "fetal_distress"],
                "risk_factors": {
                    "dilation": [4, 5, 6],
                    "ctg": ["non_reassuring"]
                }
            }
        }
    }
}
