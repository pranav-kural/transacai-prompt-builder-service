from prompts.primary_prompt_templates_db import PrimaryPromptTemplatesDB
# In memory prompt templates database
class InMemoryPromptTemplatesDB(PrimaryPromptTemplatesDB):

  def __init__(self):
    # load data
    self.data = [
  {
		"id": 1,
		"name": "Employee Payment Card Transactions Prompt",
		"description": "Prompt to provide insights on card transactions by employees.",
		"version": "1.0",
		"language": "en-US",
		"client_id": "test_client",
		"text": """You are an expert in analyzing card transactions and providing useful insights. Below you will find a list of card transactions made by employees. 
Analyze this data and generate useful and actionable insights, like overall spending trends across categories, overall spending habits across employees, possible optimizations, anomalies, etc., that will help business owners better understand employee spending and identify areas of opportunities. Keep the response concise and use bullet points and appropriate headings to organize your response. For providing overall insights, no need to be too descriptive and no need to provide details on specific transactions.
Your response maybe used by another large language model, so at the end of insights, provide a brief summary optimized for analysis by a large language model.

Organize your insights under below headings:
1. Category-wise Spending Insights
2. Employee-Specific Insights
3. Anomalies
4. Overall Spending Trends
5. Optimization Suggestions
6. Summary

Flag transactions as anomalies if they violate below category-wise thresholds:
```
Category, Threshold (CAD)
grocery_pos,150
food_dining,80
personal_care,100
entertainment,50
```

Transactions data (in JSON format) given below:
```
{transactions}
```
"""
  }
]

  # method to get prompt template by id
  def get_prompt_template_by_id(self, req_id, client_id, prompt_id) -> str:
    """
    Method to get prompt template by id. Client ID must also be provided and match, i.e., prompt template must belong to the client.

    Args:
    req_id (string): Request ID
    client_id (string): Client ID
    prompt_id (int): Prompt ID

    Returns:
    prompt_template (Dict): Prompt template
    """
    print(f"Getting prompt template for request {req_id} with client {client_id} and prompt {prompt_id}")
    # return prompt template with given id
    for prompt in self.data:
      if prompt["id"] == prompt_id and prompt["client_id"] == client_id:
        return prompt["text"]
    return None