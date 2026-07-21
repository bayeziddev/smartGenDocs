# API Endpoints

This section provides detailed documentation for the various API endpoints available within the SmartGen Docs ecosystem. Each endpoint description includes its purpose, HTTP method, URL structure, request parameters, and example responses. Understanding these endpoints is crucial for integrating SmartGen Docs functionalities into your applications.

## General Endpoint Structure

SmartGen Docs API endpoints generally follow a RESTful convention, using standard HTTP methods to interact with resources. The base URL for the API is typically `https://api.smartgendocs.com/v1` (conceptual, may vary based on deployment).

All requests should include appropriate authentication headers. Refer to the [API Authentication](authentication.md) guide for details.

## Available Endpoints (Conceptual Examples)

### 1. Get Site Status

Retrieves the current operational status of the SmartGen Docs instance.

*   **URL**: `/status`
*   **Method**: `GET`
*   **Authentication**: Optional (may require API key for detailed status)
*   **Request Parameters**: None

#### Example Request

```bash
curl -X GET "https://api.smartgendocs.com/v1/status" \
     -H "X-API-Key: YOUR_API_KEY"
```

#### Example Response (200 OK)

```json
{
  "status": "operational",
  "message": "SmartGen Docs API is running smoothly.",
  "version": "1.2.0",
  "timestamp": "2026-07-21T10:30:00Z"
}
```

#### Example Response (500 Internal Server Error)

```json
{
  "error": "internal_server_error",
  "message": "An unexpected error occurred on the server."
}
```

### 2. Get Documentation Page Content

Retrieves the rendered HTML content of a specific documentation page.

*   **URL**: `/docs/{page_path}`
*   **Method**: `GET`
*   **Authentication**: Optional (public pages do not require authentication)
*   **Request Parameters**:
    *   `page_path` (path parameter, string, required): The relative path to the Markdown file (e.g., `getting-started/installation.md`).
    *   `format` (query parameter, string, optional): Desired output format. Default is `html`. Other options might include `markdown` (returns raw Markdown).

#### Example Request

```bash
curl -X GET "https://api.smartgendocs.com/v1/docs/getting-started/installation.md?format=html"
```

#### Example Response (200 OK)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Installation - SmartGen Docs</title>
    <!-- ... other head content ... -->
</head>
<body>
    <!-- Rendered HTML content of installation.md -->
</body>
</html>
```

#### Example Response (404 Not Found)

```json
{
  "error": "not_found",
  "message": "The requested documentation page was not found."
}
```

### 3. Upload Document (via Upload Manager API)

Uploads a new Markdown file or updates an existing one. This endpoint is typically used by the [Upload Manager](../docs/features.md#8-upload-manager-web-based-interface) or integrated tools.

*   **URL**: `/upload/doc`
*   **Method**: `POST`
*   **Authentication**: Required (API Key or Session-based)
*   **Request Parameters**:
    *   `file` (form-data, file, required): The Markdown file to upload.
    *   `path` (form-data, string, required): The target path within the `docs/` directory (e.g., `new-section/my-document.md`).
    *   `overwrite` (form-data, boolean, optional): If `true`, overwrites an existing file at the specified path. Default is `false`.

#### Example Request

```bash
curl -X POST "https://api.smartgendocs.com/v1/upload/doc" \
     -H "X-API-Key: YOUR_API_KEY" \
     -F "file=@/path/to/your/document.md" \
     -F "path=new-section/my-document.md" \
     -F "overwrite=true"
```

#### Example Response (201 Created)

```json
{
  "status": "success",
  "message": "Document uploaded successfully.",
  "file_path": "new-section/my-document.md"
}
```

#### Example Response (409 Conflict)

```json
{
  "error": "conflict",
  "message": "A file already exists at new-section/my-document.md. Use overwrite=true to replace it."
}
```

### 4. Trigger Site Build

Initiates a new build of the static documentation site. This is useful for CI/CD pipelines or after programmatic content updates.

*   **URL**: `/build`
*   **Method**: `POST`
*   **Authentication**: Required (API Key)
*   **Request Parameters**: None

#### Example Request

```bash
curl -X POST "https://api.smartgendocs.com/v1/build" \
     -H "X-API-Key: YOUR_API_KEY"
```

#### Example Response (202 Accepted)

```json
{
  "status": "accepted",
  "message": "Site build initiated successfully.",
  "build_id": "bld_xyz123abc"
}
```

#### Example Response (429 Too Many Requests)

```json
{
  "error": "rate_limit_exceeded",
  "message": "You have exceeded the rate limit for build requests."
}
```

## Next Steps

For a detailed understanding of possible errors and their meanings, refer to the [Error Codes](errors.md) section. To understand how to manage frequent requests, consult the [Rate Limits](rate-limits.md) documentation.
