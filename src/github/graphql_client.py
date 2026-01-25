# INFRASTRUCTURE
import os
import requests

GITHUB_GRAPHQL = "https://api.github.com/graphql"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


# FUNCTIONS

# Execute GraphQL query against GitHub API
def graphql_query(query: str, variables: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        GITHUB_GRAPHQL,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        raise Exception(f"GraphQL Error: {data['errors']}")
    return data["data"]
