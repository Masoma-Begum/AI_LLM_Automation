def load_prompts(file_path="prompts/prompt_dataset.json"):
   with open(file_path, "r") as f:
       return json.load(f)

def get_prompt(topic):
   prompts = load_prompts()
   return prompts.get(topic, f"Explain {topic} in simple points.")
# Example prompt_dataset.json:

{
   "API testing": "Explain API testing in 3 bullet points.",
   "Selenium": "Explain Selenium WebDriver basics for beginners."
}
