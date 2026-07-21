# Python SDK Reference

The SmartGen Docs Python SDK provides a convenient and idiomatic way for Python developers to interact with the SmartGen Docs platform. This library simplifies common tasks such as managing documentation content, triggering site builds, and accessing platform information, allowing you to integrate SmartGen Docs functionalities directly into your Python applications or scripts.

## Installation

You can install the SmartGen Docs Python SDK using pip:

```bash
pip install smartgendocs-sdk-python
```

## Authentication

To use the Python SDK, you will typically need an API key for authentication. Ensure you have obtained your API key from the SmartGen Platform dashboard. The SDK will handle including this key in your requests.

```python
from smartgendocs_sdk import SmartGenDocsClient

# Initialize the client with your API key
api_key = "YOUR_SMARTGENDOCS_API_KEY"
client = SmartGenDocsClient(api_key=api_key)
```

For more details on authentication, refer to the [API Authentication](../api/authentication.md) guide.

## Usage Examples

### 1. Get Site Status

Check the operational status of your SmartGen Docs instance.

```python
from smartgendocs_sdk import SmartGenDocsClient

client = SmartGenDocsClient(api_key="YOUR_SMARTGENDOCS_API_KEY")

try:
    status = client.get_status()
    print("Site Status:", status)
except Exception as e:
    print("Error getting status:", e)
```

### 2. Upload a Document

Upload a new Markdown file or update an existing one. This is particularly useful for automating content updates.

```python
from smartgendocs_sdk import SmartGenDocsClient

client = SmartGenDocsClient(api_key="YOUR_SMARTGENDOCS_API_KEY")

file_path = "./my_new_document.md"
target_path = "new-section/my-new-document.md"

try:
    with open(file_path, "rb") as f:
        response = client.upload_document(file_content=f.read(), target_path=target_path, overwrite=True)
    print("Upload successful:", response)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print("Error uploading document:", e)
```

### 3. Trigger a Site Build

Initiate a new build of your static documentation site programmatically.

```python
from smartgendocs_sdk import SmartGenDocsClient

client = SmartGenDocsClient(api_key="YOUR_SMARTGENDOCS_API_KEY")

try:
    response = client.trigger_build()
    print("Build triggered:", response)
except Exception as e:
    print("Error triggering build:", e)
```

### 4. Get Document Content

Retrieve the raw Markdown or rendered HTML content of a specific documentation page.

```python
from smartgendocs_sdk import SmartGenDocsClient

client = SmartGenDocsClient(api_key="YOUR_SMARTGENDOCS_API_KEY")

try:
    # Get raw Markdown content
    markdown_content = client.get_document_content("getting-started/installation.md", format="markdown")
    print("Markdown Content:\n", markdown_content[:200], "...")

    # Get rendered HTML content
    html_content = client.get_document_content("getting-started/installation.md", format="html")
    print("HTML Content:\n", html_content[:200], "...")

except Exception as e:
    print("Error getting document content:", e)
```

## API Reference

The `SmartGenDocsClient` class provides the following methods:

### `__init__(self, api_key: str, base_url: str = "https://api.smartgendocs.com/v1")`

Initializes the SmartGen Docs client.

*   **`api_key`** (`str`): Your SmartGen Docs API key.
*   **`base_url`** (`str`, optional): The base URL for the SmartGen Docs API. Defaults to `https://api.smartgendocs.com/v1`.

### `get_status(self) -> dict`

Retrieves the current operational status of the SmartGen Docs instance.

*   **Returns** (`dict`): A dictionary containing the status information.
*   **Raises** (`requests.exceptions.RequestException`): If the API request fails.

### `upload_document(self, file_content: bytes, target_path: str, overwrite: bool = False) -> dict`

Uploads a Markdown document to the specified path.

*   **`file_content`** (`bytes`): The content of the Markdown file as bytes.
*   **`target_path`** (`str`): The relative path within the `docs/` directory where the file should be saved (e.g., `new-section/my-doc.md`).
*   **`overwrite`** (`bool`, optional): If `True`, overwrites the file if it already exists. Defaults to `False`.
*   **Returns** (`dict`): A dictionary containing the upload status.
*   **Raises** (`requests.exceptions.RequestException`): If the API request fails.

### `trigger_build(self) -> dict`

Initiates a new build of the static documentation site.

*   **Returns** (`dict`): A dictionary containing the build initiation status.
*   **Raises** (`requests.exceptions.RequestException`): If the API request fails.

### `get_document_content(self, page_path: str, format: str = "html") -> str`

Retrieves the content of a specific documentation page.

*   **`page_path`** (`str`): The relative path to the Markdown file (e.g., `getting-started/installation.md`).
*   **`format`** (`str`, optional): The desired output format (`html` or `markdown`). Defaults to `html`.
*   **Returns** (`str`): The content of the document in the specified format.
*   **Raises** (`requests.exceptions.RequestException`): If the API request fails.

## Error Handling

The SDK methods will raise `requests.exceptions.RequestException` for network-related errors or non-2xx HTTP responses. It is recommended to wrap your API calls in `try-except` blocks to handle these exceptions gracefully. For specific API error codes, refer to the [API Error Codes](../api/errors.md) documentation.

## Contributing

Contributions to the Python SDK are welcome! Please refer to the [Contributing Guide](../../contributing.md) for details on how to contribute.
