# API Rate Limits

To ensure fair usage, maintain system stability, and protect against abuse, the SmartGen Docs API implements rate limiting. Rate limits restrict the number of requests a user or application can make to the API within a given time window. Understanding and adhering to these limits is crucial for building robust and reliable integrations.

## How Rate Limits Work

Rate limits are typically applied per API key or per IP address, depending on the endpoint and the authentication method used. When you exceed a rate limit, the API will return a `429 Too Many Requests` HTTP status code, along with a specific error message.

### Rate Limit Headers

API responses will often include HTTP headers that provide information about your current rate limit status. While the exact headers may vary, common ones include:

*   `X-RateLimit-Limit`: The maximum number of requests allowed in the current time window.
*   `X-RateLimit-Remaining`: The number of requests remaining in the current time window.
*   `X-RateLimit-Reset`: The time (in UTC epoch seconds or similar format) when the current rate limit window resets.

### Example (Conceptual)

```
HTTP/1.1 200 OK
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 58
X-RateLimit-Reset: 1678886400
Content-Type: application/json

{
  "status": "operational"
}
```

## Current Rate Limit Policies (Conceptual)

The following are conceptual rate limit policies. Actual limits may vary and will be communicated through the API documentation or developer portal.

| Endpoint Category | Limit (Requests/Minute) | Notes                                                              |
| :---------------- | :---------------------- | :----------------------------------------------------------------- |
| General Status    | 60                      | Applies to `/status` endpoint.                                     |
| Content Retrieval | 30                      | Applies to `/docs/{page_path}`.                                    |
| Content Upload    | 5                       | Applies to `/upload/doc`. Higher limits for authenticated users.   |
| Site Build        | 1                       | Applies to `/build`. Prevents excessive server load.               |

## Handling Rate Limit Exceedance

When your application receives a `429 Too Many Requests` response, it means you have temporarily exceeded the allowed request rate. To handle this gracefully, you should:

1.  **Read Rate Limit Headers**: Inspect the `X-RateLimit-Reset` header to determine when you can safely retry your request.
2.  **Implement Exponential Backoff**: Instead of immediately retrying, wait for an increasing amount of time between retries. This prevents overwhelming the API and helps your application recover.
3.  **Avoid Bursting**: Distribute your requests evenly over time rather than sending them all at once.

### Example with Exponential Backoff (Python)

```python
import requests
import time

API_KEY = "your_secret_api_key_here"
BASE_URL = "https://api.smartgendocs.com/v1"

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

def make_api_request(endpoint, max_retries=5):
    retries = 0
    while retries < max_retries:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)

        if response.status_code == 429:
            reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60)) # Default to 60 seconds if header missing
            wait_time = reset_time - int(time.time()) + 1 # Wait until reset time + 1 second
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(max(1, wait_time)) # Ensure at least 1 second wait
            retries += 1
        elif response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status() # Raise an exception for other HTTP errors
    raise Exception("Max retries exceeded for API request.")

try:
    status = make_api_request("status")
    print("API Status:", status)
except Exception as e:
    print("API Request Failed:", e)
```

## Best Practices

*   **Monitor Usage**: Keep track of your API usage to stay within the limits.
*   **Cache Responses**: Cache API responses where appropriate to reduce the number of requests you need to make.
*   **Batch Requests**: If possible, combine multiple operations into a single request to reduce your overall request count.
*   **Contact Support**: If you consistently hit rate limits and believe your use case requires higher limits, contact SmartGen Docs support to discuss potential solutions or custom limits.
