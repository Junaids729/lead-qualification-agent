import os
from groq import Groq

# 1. Initialize the AI Client 
# (We will get a free API key in the next step)
client = Groq(api_key="YOUR_API_KEY_HERE")

def qualify_lead(lead_text):
    # 2. The System Prompt (This tells the AI exactly what its job is)
    system_prompt = """
    You are an expert B2B Sales Lead Qualification Agent. 
    Your job is to read inbound lead inquiries and score them.
    
    You must classify the lead as one of the following:
    - HOT (Ready to buy, high urgency, large scale)
    - WARM (Interested, but asking for information or pricing)
    - COLD (Spam, irrelevant, or absolutely no intent to buy)
    
    Output a short explanation for your classification.
    """

    # 3. Route the data to the LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": lead_text}
        ]
    )
    
    return response.choices[0].message.content

# 4. A Test Lead to see if it works
sample_inquiry = "Hi, I need to purchase 500 enterprise licenses for my team by next Tuesday. Please call me ASAP."

print("Analyzing Lead...")
print("-" * 30)
print(qualify_lead(sample_inquiry))