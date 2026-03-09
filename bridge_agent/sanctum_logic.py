import requests # Sanctum usually exposes a local OpenAI-compatible API

class SanctumValidator:
    def __init__(self, local_url="http://localhost:1234/v1"):
        self.api_url = local_url

    def validate_vendor_p2p(self, tx_data):
        """
        Uses local Sanctum LLM to audit the vendor transaction details.
        """
        prompt = f"Audit this P2P vendor request: {tx_data}. Return 'RELEASE' or 'HALT'."
        
        response = requests.post(f"{self.api_url}/chat/completions", json={
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        })
        
        decision = response.json()['choices'][0]['message']['content']
        return "RELEASE" in decision.upper()