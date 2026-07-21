# Webhooks

Webhooks provide a way for SmartGen Docs to notify your application in real-time when certain events occur. Instead of continuously polling the API for changes, webhooks push information to your designated endpoint, making your integrations more efficient and responsive.

## What are Webhooks?

A webhook is an automated message sent from an app when something happens. It's an HTTP callback: an HTTP POST request that occurs when an event happens in SmartGen Docs. Webhooks are user-defined HTTP callbacks. They are usually triggered by some event, such as a new document being uploaded or a site build completing.

## How SmartGen Docs Webhooks Work

When a configured event occurs within SmartGen Docs (e.g., a document update, a successful site build), the system will send an HTTP POST request to a URL you specify. This request will contain a JSON payload describing the event.

### 1. Event Triggers

SmartGen Docs can trigger webhooks for various events. Common events might include (conceptual):

*   `document.created`: A new Markdown document has been added.
*   `document.updated`: An existing Markdown document has been modified.
*   `document.deleted`: A Markdown document has been removed.
*   `site.build_started`: A site build process has begun.
*   `site.build_completed`: A site build process has successfully finished.
*   `site.build_failed`: A site build process has failed.

### 2. Payload Structure

The JSON payload sent with each webhook request will typically include:

*   `event`: The type of event that occurred (e.g., `document.updated`).
*   `timestamp`: The time the event occurred (ISO 8601 format).
*   `data`: An object containing event-specific data. This might include:
    *   For `document` events: `file_path`, `author`, `commit_id`, `url`.
    *   For `site.build` events: `build_id`, `status`, `duration`, `site_url`.

#### Example Webhook Payload (Conceptual `document.updated`)

```json
{
  "event": "document.updated",
  "timestamp": "2026-07-21T14:30:00Z",
  "data": {
    "file_path": "getting-started/installation.md",
    "author": "bayeziddev",
    "commit_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "url": "https://yourdocs.com/getting-started/installation.html"
  }
}
```

### 3. Security Considerations

To ensure the authenticity and integrity of incoming webhooks, it's highly recommended to implement security measures:

*   **HTTPS**: Always use HTTPS for your webhook endpoint to encrypt the payload in transit.
*   **Secret Signing**: SmartGen Docs may optionally sign webhook payloads with a shared secret. Your application can then verify this signature to ensure the webhook originated from SmartGen Docs and has not been tampered with.
    *   Upon receiving a webhook, calculate the signature using the same secret and algorithm.
    *   Compare your calculated signature with the one provided in the `X-SmartGen-Signature` header (conceptual).
    *   If they don't match, reject the webhook.

## Setting Up Webhooks (Conceptual)

Setting up webhooks typically involves:

1.  **Creating an Endpoint**: Develop an HTTP endpoint in your application that can receive POST requests.
2.  **Configuring in SmartGen Docs**: Provide SmartGen Docs with your endpoint URL and select the events you want to subscribe to. This might be done via a configuration file (e.g., `smartgen.yml`), a web interface, or a CLI command.

#### Example `smartgen.yml` Webhook Configuration (Conceptual)

```yaml
webhooks:
  - url: https://your-app.com/smartgen-webhook-listener
    events:
      - document.created
      - document.updated
      - site.build_completed
    secret: your_webhook_secret_key
```

## Handling Webhooks in Your Application

When your application receives a webhook, it should:

1.  **Verify Signature (if applicable)**: Validate the webhook's authenticity using the shared secret.
2.  **Process Asynchronously**: Webhook requests are typically time-sensitive. Process the payload quickly and return a `200 OK` response. Any heavy processing should be offloaded to a background job.
3.  **Handle Retries**: SmartGen Docs may implement retry mechanisms for failed webhook deliveries. Ensure your endpoint is idempotent, meaning that processing the same webhook multiple times has the same effect as processing it once.

## Next Steps

For more information on how to configure webhooks within your specific SmartGen Docs deployment, consult the [Configuration Guide](../guides/configuration.md) or the relevant section in the SmartGen Platform documentation.
