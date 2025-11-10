from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

def start_campaign_background(campaign_id: str):
    print(f"Starting campaign in background: {campaign_id}")

@router.post("/sales/start_campaign")
async def start_sales_campaign(payload: dict, background_tasks: BackgroundTasks):
    campaign_id = payload.get("campaign_id", "test_campaign")
    background_tasks.add_task(start_campaign_background, campaign_id)
    return {"status": "queued", "campaign_id": campaign_id}
