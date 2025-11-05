from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize router
router = APIRouter()

# Load API key from environment
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class UserQuery(BaseModel):
    query: str

@router.post("/respond")
async def ai_respond(payload: UserQuery):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")

    try:
        import asyncio, time
        start_time = time.time()

        # Asynchronous non-blocking API call
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert nutritionist and chef, an assistant that helps users with meal planning, nutrition, and recipe ideas. Return your output in MARKUP language only. You will always provide a list of ingredients and then the steps to make it."},
                {"role": "user", "content": payload.query},
            ],
            max_tokens=int(os.getenv("AI_MAX_TOKENS", "800")),
            timeout=30  # seconds
        )

        ai_text = response.choices[0].message.content.strip()

        print(f"[DEBUG] AI Response length: {len(ai_text)} characters")

        # Basic response type categorization
        content_lower = ai_text.lower()
        if any(word in content_lower for word in ["ingredient", "cook", "recipe"]):
            response_type = "recipe"
        elif any(word in content_lower for word in ["suggest", "recommend"]):
            response_type = "suggestion"
        else:
            response_type = "text"

        from fastapi.responses import JSONResponse
        import json

        latency = round(time.time() - start_time, 2)
        response_payload = {
            "type": response_type,
            "content": ai_text,
            "latency_seconds": latency,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Return beautified JSON
        return JSONResponse(
            content=json.loads(json.dumps(response_payload, indent=2, ensure_ascii=False)),
            media_type="application/json"
        )

    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="OpenAI request timed out")
    except Exception as e:
        import traceback
        print("=== AI Endpoint Error Debug Info ===")
        print("Error Type:", type(e).__name__)
        print("Error Message:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"AI generation failed: {type(e).__name__}: {str(e)}")