
from core.prompt_builder import build_prompt

def handle_insights_generation(req_id: str, client_id: str, prompt_id: int, from_time: str, to_time: str) -> str:
    # build prompt
    prompt = build_prompt(
        req_id=req_id, 
        client_id=client_id, 
        prompt_id=prompt_id, 
        from_time=from_time, 
        to_time=to_time
        )
    
    print(prompt)
    
    # # generate insights
    # insights = generate_insights(req_id, client_id, prompt)
    # # save insights
    # save_insights(req_id, client_id, insights)
    # # inform clients
    # inform_clients(req_id, client_id)

if __name__ == "__main__":
    handle_insights_generation(
        req_id="req_1", 
        client_id="test_client", 
        prompt_id=1, 
        from_time="2019-12-29T06:39:22", 
        to_time="2019-12-29T23:49:22"
        )