import requests
import json

def describe_disease(disease_name, treatments):
    #Converted Array to a single String
    treatments_str = ", ".join(treatments)
    
    #Defines the prompt given to the LLM
    prompt = (
        f"You are analyzing a plant disease based on an image the user provided. "
        f"The detected disease is '{disease_name}', and known treatments are: {treatments_str}.\n\n"
        "Return exactly one well‑formed JSON object with these keys: causes, treatments, and precautions.\n"
        "Each value must be a non‑empty string in full sentences. Do NOT use any bullet points, numbering, lists, or markdown.\n"
        "If you cannot identify applicable precautions from the provided treatments or data, write a general precaution paragraph that errs on the cautious side for plant care.\n\n"
        "Output **only** JSON, in this format:\n"
        "- causes (string)\n"
        "- treatments (string)\n"
        "- precautions (string)\n\n"
        "**Formatting rules:**\n"
        "1. Do NOT include any bullet points, numbers, or markdown.\n"
        "2. Each value must be written as a single, well-formed paragraph.\n"
        "3. Do NOT include extra explanation or preamble—only the JSON.\n"
        "4. Make sure every field has a clear and informative sentence.\n\n"
        "Begin:"
    )

    #Defines which model to use and the structure in which it should reply
    body = {
        "model": "qwen:7b",
        "prompt": prompt,
        "stream": False,
        "format": {
            "type": "object",
            "properties": {
                "causes": {"type": "string"},
                "treatments": {"type": "string"},
                "precautions": {"type": "string"}
            },
            "required": ["causes", "treatments", "precautions"]
        }
    }

    resp = requests.post("http://localhost:11434/api/generate",
                         json=body,
                         headers={"Content-Type": "application/json"})
    # Gives error if API call fails
    resp.raise_for_status()
    
    #The response is weird so you take the data out of JSON first and you find another JSON inside from which you take out the required info
    outer = resp.json()

    raw_json = outer.get("response")
    if raw_json is None:
        raise ValueError(f"No 'response' field in API reply: {outer}")

    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON from 'response': {raw_json}") from e
    # print(data) #remove comment to check reply sent by LLM
    causes = data.get("causes")
    treatments_out = data.get("treatments")
    precautions = data.get("precautions")

    return causes, treatments_out, precautions