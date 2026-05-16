import os
from typing import Optional
from groq import Groq
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

class LLMProvider:
    def __init__(self):
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.primary_model = "llama-3.1-70b-versatile"
        self.fallback_model = "claude-3-5-sonnet-20240620"

    def get_completion(self, prompt: str, system_prompt: str = ""):
        try:
            # Primary: Groq (Llama 3.1 70B)
            response = self.groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                model=self.primary_model,
                response_format={"type": "json_object"}
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Groq failed: {e}. Falling back to Anthropic.")
            try:
                # Fallback: Anthropic
                response = self.anthropic_client.messages.create(
                    model=self.fallback_model,
                    max_tokens=1024,
                    system=system_prompt,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
            except Exception as e2:
                print(f"Anthropic also failed: {e2}")
                return None

# Singleton instance
llm = LLMProvider()
