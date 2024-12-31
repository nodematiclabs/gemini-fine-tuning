import json

with open("train_data.jsonl", "w") as training_file:
    for i in range(1, 7):
        with open(f"data/story-{i}.txt", "r") as file:
            story = "".join(file.readlines())
        with open(f"data/summary-{i}.txt", "r") as file:
            summary = "".join(file.readlines())
        prompt = f"""
Summarize the following text in my style.

{story}
""".strip()
        training_file.write(json.dumps(
            {"contents": [
                {
                    "role": "user",
                    "parts": [{
                        "text": prompt
                    }]
                },
                {
                    "role": "model",
                    "parts": [{
                        "text": summary,
                    }]
                }
            ]}
        ) + "\n")