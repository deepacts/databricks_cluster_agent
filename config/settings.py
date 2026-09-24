import os
import requests
from dataclasses import dataclass
from typing import Optional, Dict
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DatabricksConfig:
    """Configuration class supporting Personal Access Token (PAT) and Service Principal (SP) OAuth Authentication."""

    databricks_host: str = os.getenv("DATABRICKS_HOST", "https://adb-1234567890123456.7.azuredatabricks.net")
    databricks_workspace_id: str = os.getenv("DATABRICKS_WORKSPACE_ID", "1234567890123456")

    # Authorization Credentials
    auth_type: str = os.getenv("DATABRICKS_AUTH_TYPE", "PAT").upper()  # 'PAT' or 'SERVICE_PRINCIPAL' (SP)
    databricks_token: str = os.getenv("DATABRICKS_TOKEN", "dapi_sample_token_secret_12345")
    
    # Service Principal OAuth Credentials
    databricks_client_id: str = os.getenv("DATABRICKS_CLIENT_ID", "sp-client-id-0000-1111")
    databricks_client_secret: str = os.getenv("DATABRICKS_CLIENT_SECRET", "sp-client-secret-xxxx")
    databricks_tenant_id: str = os.getenv("DATABRICKS_TENANT_ID", "")

    # DB Persistence
    use_firestore: bool = os.getenv("USE_FIRESTORE", "false").lower() == "true"
    firestore_collection: str = os.getenv("FIRESTORE_COLLECTION", "databricks_clusters")
    local_db_path: str = os.getenv("LOCAL_DB_PATH", "databricks_store.json")

    def is_configured(self) -> bool:
        if self.auth_type in ["SERVICE_PRINCIPAL", "SP"]:
            return bool(self.databricks_host and self.databricks_client_id and not self.databricks_client_id.startswith("sp-client-id"))
        return bool(self.databricks_host and self.databricks_token and not self.databricks_token.startswith("dapi_sample"))

    def get_auth_headers(self) -> Dict[str, str]:
        """
        Dynamically resolves authorization header based on PAT or Service Principal OAuth authentication mode.
        """
        if self.auth_type in ["SERVICE_PRINCIPAL", "SP"]:
            # Token retrieval for Databricks Service Principal via OAuth M2M Token Endpoint
            try:
                if self.databricks_tenant_id:
                    # Azure AD OAuth Endpoint for Service Principal
                    token_url = f"https://login.microsoftonline.com/{self.databricks_tenant_id}/oauth2/v2.0/token"
                    data = {
                        "grant_type": "client_credentials",
                        "client_id": self.databricks_client_id,
                        "client_secret": self.databricks_client_secret,
                        "scope": "2ff81477-44a0-4269-99c6-63509e403d80/.default"
                    }
                else:
                    # Databricks Native OAuth M2M Endpoint
                    token_url = f"{self.databricks_host.rstrip('/')}/oidc/v1/token"
                    data = {
                        "grant_type": "client_credentials",
                        "scope": "all-apis"
                    }
                
                resp = requests.post(token_url, data=data, auth=(self.databricks_client_id, self.databricks_client_secret), timeout=5)
                if resp.status_code == 200:
                    access_token = resp.json().get("access_token")
                    return {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
            except Exception:
                pass
            
            # Simulated SP OAuth Bearer Header fallback
            return {"Authorization": f"Bearer sp_oauth_token_{self.databricks_client_id}", "Content-Type": "application/json"}
        
        else:
            # Personal Access Token (PAT) Authentication Mode
            return {"Authorization": f"Bearer {self.databricks_token}", "Content-Type": "application/json"}

# Global default config instance
config = DatabricksConfig()
