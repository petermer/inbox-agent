import json
from config import USE_MODEL
from agents.inbox_summarizer import summarize_email

if USE_MODEL == "claude":
    from model_wrappers.bedrock_claude import get_claude_llm
    llm = get_claude_llm()
elif USE_MODEL == "gpt":
    from model_wrappers.openai_gpt import get_gpt_llm
    llm = get_gpt_llm()
else:
    raise ValueError("Invalid model specified in config.py")

# Load emails
with open("data/sample_emails.json", "r") as f:
    emails = json.load(f)

# Run agent on each email
for i, email in enumerate(emails, 1):
    print(f"\n--- Email #{i} from {email['from']} ---")
    text = f"Subject: {email['subject']}\n\n{email['body']}"
    result = summarize_email(llm, text)
    print(result)
