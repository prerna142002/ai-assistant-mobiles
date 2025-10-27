from supabase import create_client, Client
from typing import Dict, Any
import pandas as pd

class SupbaseHandler:
    """A conversational agent for mobile phone shopping assistance."""
    
    def __init__(self, csv_path: str = None):
        """Initialize the shopping chat agent with CSV data source.
        
        Args:
            csv_path: Optional path to the CSV file. If not provided, uses the default path.
        """
        # Initialize data loader with CSV
        self.url: str = "https://cspthyaokwivgxuyuknn.supabase.co"
        self.key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNzcHRoeWFva3dpdmd4dXl1a25uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE1NjAwNTAsImV4cCI6MjA3NzEzNjA1MH0.yhcN-I72Awfr4WQ8AK1pwBsmGWHpbJgvuTGU_hC8knc"
        self.supabase: Client = create_client(self.url, self.key)

    def insert_data(self, data: Dict[str, Any]):
        """Insert data into the database."""
        response = self.supabase.table("MobileDetails").insert(data).execute()
        print(data)
        
        df = pd.DataFrame([data])

        # # Overwrite CSV file completely
        df.to_csv("./data/sample_mobiles.csv", index=False, mode="a", header=False)
        # return response.data
        
    def fetch_data(self):
        response = self.supabase.table("MobileDetails").select("*").execute()
        df = pd.DataFrame(response.data)

        # # Overwrite CSV file completely
        df.to_csv("./data/sample_mobiles.csv", index=False, mode="a", header=False)
        return response.data    




