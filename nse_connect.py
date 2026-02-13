import time
import requests

class IndianMarketGateway:
    def __init__(self, api_key, access_token):
        self.api_key = api_key
        self.access_token = access_token
        self.base_url = "https://api.dhan.co/v2" # Example endpoint
        
    def get_headers(self):
        return {
            "access-token": self.access_token,
            "Content-Type": "application/json"
        }

    def fetch_ltp(self, security_id, exchange="NSE"):
        """Fetch Last Traded Price (LTP) for a stock"""
        endpoint = f"{self.base_url}/marketquote/{exchange}/{security_id}"
        
        # In 2026, we must pass the unique Algo ID in headers or params
        response = requests.get(endpoint, headers=self.get_headers())
        
        if response.status_code == 200:
            data = response.json()
            return data['last_price']
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

# --- Simulation for RELIANCE (Security ID: 2885) ---
# Note: In a real scenario, you'd get the access_token after a 2FA login flow.
bot = IndianMarketGateway(api_key="YOUR_KEY", access_token="YOUR_TOKEN")

print("--- NSE Live Data Stream ---")
# NSE Trading Hours: 9:15 AM - 3:30 PM IST
for _ in range(5):
    price = bot.fetch_ltp(security_id="2885") # Reliance Industries
    if price:
        print(f"RELIANCE (NSE): ₹{price:,.2f}")
    time.sleep(1)