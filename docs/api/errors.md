# API Error Codes

When interacting with the SmartGen Docs API, it's important to understand the various error codes that may be returned. These codes provide valuable information for debugging and troubleshooting issues with your API requests. The API uses standard HTTP status codes to indicate the general nature of an error, accompanied by a JSON payload containing more specific details.

## General Error Structure

Most API errors will return a JSON object with the following structure:

```json
{
  "error": "error_code_string",
  "message": "A human-readable description of the error.",
  "details": {
    "field_name": "Specific issue with this field."
  }
}
```

*   `error`: A machine-readable string code representing the type of error.
*   `message`: A human-readable message providing more context about the error.
*   `details` (optional): An object containing specific validation errors or additional context, often mapping to problematic fields in the request.

## Common HTTP Status Codes and SmartGen Docs Errors

### 2xx Success

*   `200 OK`: The request was successful, and the response body contains the requested data.
*   `201 Created`: The request was successful, and a new resource was created as a result.
*   `202 Accepted`: The request was accepted for processing, but the processing is not yet complete.

### 4xx Client Errors

These errors indicate that the client (your application) has sent an invalid or malformed request.

*   **`400 Bad Request`**
    *   **Error Code**: `invalid_request_payload`, `validation_error`
    *   **Message**: The request body was malformed, or one or more parameters failed validation.
    *   **Details**: Often includes an object detailing which fields were invalid and why.
    *   **Common Causes**: Missing required parameters, incorrect data types, invalid JSON format.
    *   **Troubleshooting**: Check your request payload against the API documentation for the specific endpoint. Ensure all required fields are present and correctly formatted.

*   **`401 Unauthorized`**
    *   **Error Code**: `authentication_required`, `invalid_api_key`, `invalid_access_token`
    *   **Message**: Authentication credentials were missing or invalid.
    *   **Common Causes**: No API key provided, expired or revoked API key, incorrect OAuth token.
    *   **Troubleshooting**: Ensure you are including a valid API key or OAuth token in your request headers. Verify that your credentials have not expired or been revoked. Refer to [API Authentication](authentication.md).

*   **`403 Forbidden`**
    *   **Error Code**: `permission_denied`, `access_forbidden`
    *   **Message**: The authenticated user does not have the necessary permissions to perform this action.
    *   **Common Causes**: API key or token lacks the required scope or role for the requested resource/action.
    *   **Troubleshooting**: Check the permissions associated with your API key or OAuth token. You may need to request additional permissions or use a different set of credentials.

*   **`404 Not Found`**
    *   **Error Code**: `resource_not_found`, `page_not_found`, `endpoint_not_found`
    *   **Message**: The requested resource or endpoint could not be found.
    *   **Common Causes**: Incorrect URL path, resource has been deleted, or the endpoint does not exist.
    *   **Troubleshooting**: Verify the URL path and ensure the resource you are trying to access exists. Check for typos in the endpoint URL.

*   **`405 Method Not Allowed`**
    *   **Error Code**: `method_not_allowed`
    *   **Message**: The HTTP method used is not supported for this endpoint.
    *   **Common Causes**: Attempting to `POST` to an endpoint that only accepts `GET` requests, or vice-versa.
    *   **Troubleshooting**: Consult the [API Endpoints](endpoints.md) documentation to confirm the supported HTTP methods for the endpoint you are calling.

*   **`409 Conflict`**
    *   **Error Code**: `resource_already_exists`, `file_exists`
    *   **Message**: The request could not be completed due to a conflict with the current state of the resource.
    *   **Common Causes**: Attempting to create a resource that already exists without specifying an overwrite option.
    *   **Troubleshooting**: If creating a resource, check if it already exists. For operations like file uploads, consider using an `overwrite` parameter if available.

*   **`429 Too Many Requests`**
    *   **Error Code**: `rate_limit_exceeded`
    *   **Message**: You have sent too many requests in a given amount of time.
    *   **Common Causes**: Exceeding the API's rate limits.
    *   **Troubleshooting**: Implement exponential backoff and retry logic in your application. Refer to the [Rate Limits](rate-limits.md) documentation for details on current limits.

### 5xx Server Errors

These errors indicate a problem on the server side. While you cannot directly fix these, understanding them helps in reporting issues.

*   **`500 Internal Server Error`**
    *   **Error Code**: `internal_server_error`, `unexpected_error`
    *   **Message**: An unexpected condition was encountered on the server that prevented it from fulfilling the request.
    *   **Common Causes**: Bugs in the API server code, unhandled exceptions.
    *   **Troubleshooting**: This is a server-side issue. If it persists, report it to the SmartGen Docs support team with details of your request and the error message.

*   **`503 Service Unavailable`**
    *   **Error Code**: `service_unavailable`, `maintenance_mode`
    *   **Message**: The server is currently unable to handle the request due to temporary overloading or scheduled maintenance.
    *   **Common Causes**: Server undergoing maintenance, high traffic load.
    *   **Troubleshooting**: Wait for a short period and retry your request. Check the SmartGen Docs status page for any ongoing incidents or maintenance announcements.

By carefully reviewing the HTTP status codes and the accompanying JSON error payloads, you can efficiently diagnose and resolve issues when working with the SmartGen Docs API.
