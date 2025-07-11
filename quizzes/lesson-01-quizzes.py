diff = [
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

QUIZZES = {"diff": diff}
