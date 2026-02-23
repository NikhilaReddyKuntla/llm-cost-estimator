import json
import tiktoken

# pricing per token
pricing = {
    "gpt-3.5-turbo": 0.002 / 1000,
    "gpt-4": 0.03 / 1000
}

def handler(request):
    try:
        body = json.loads(request.body)
        text = body.get("text", "")
        model = body.get("model", "gpt-3.5-turbo")

        enc = tiktoken.encoding_for_model(model)
        tokens = len(enc.encode(text))
        cost = tokens * pricing[model]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "tokens": tokens,
                "cost": round(cost, 6)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
