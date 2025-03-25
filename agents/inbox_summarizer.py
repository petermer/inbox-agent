import json

def summarize_email(llm, email_text):
    prompt = (
        "Summarize the following email and extract any action items:\n\n"
        f"{email_text}\n\n"
        "Respond in the format:\n"
        "**Summary:** ...\n"
        "**Action Items:** ... (or 'None')"
    )
    return llm(prompt)
