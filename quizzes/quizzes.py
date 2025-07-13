num_q = [
    {
        "question": "Estimate the self‑diffusion coefficient of SPC/E water at 300 K (2 sig‑figs):",
        "type": "numeric",
        "precision": 2,
        "answers": [
            {"type": "range", "range": [0.20, 0.30], "correct": True,
             "feedback": "Experimental ≈ 0.23 Å² ps⁻¹."},
            {"type": "default", "feedback": "Check slope and units."}
        ]
    }
]

many_q = [
    {
        "question": "Which are valid units of energy? (select all)",
        "type": "many_choice",
        "answers": [
            {"answer": "kJ mol⁻¹", "correct": True, "feedback": "Yes—kilojoules per mole."},
            {"answer": "parsec", "correct": False, "feedback": "That is a distance."},
            {"answer": "eV", "correct": True, "feedback": "Electron‑volts are energy."}
        ]
    }
]

QUIZZES = {"num_q": num_q , "many_q": many_q}
