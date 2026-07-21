# JavaScript SDK Reference

The SmartGen Docs JavaScript SDK provides a robust and easy-to-use interface for integrating SmartGen Docs functionalities into your web applications, Node.js scripts, or other JavaScript-based projects. This SDK simplifies interactions with the SmartGen Docs API, handling network requests, authentication, and data parsing, allowing you to focus on building your application.

## Installation

You can install the SmartGen Docs JavaScript SDK using npm or yarn:

### Using npm

```bash
npm install smartgendocs-sdk-js
```

### Using yarn

```bash
yarn add smartgendocs-sdk-js
```

## Authentication

To use the JavaScript SDK, you will typically need an API key for authentication. Ensure you have obtained your API key from the SmartGen Platform dashboard. The SDK will handle including this key in your requests.

```javascript
import { SmartGenDocsClient } from 'smartgendocs-sdk-js';

// Initialize the client with your API key
const apiKey = "YOUR_SMARTGENDOCS_API_KEY";
const client = new SmartGenDocsClient(apiKey);
```

For more details on authentication, refer to the [API Authentication](../api/authentication.md) guide.

## Usage Examples

### 1. Get Site Status

Check the operational status of your SmartGen Docs instance.

```javascript
import { SmartGenDocsClient } from 'smartgendocs-sdk-js';

const client = new SmartGenDocsClient("YOUR_SMARTGENDOCS_API_KEY");

async function getStatus() {
  try {
    const status = await client.getStatus();
    console.log("Site Status:", status);
  } catch (error) {
    console.error("Error getting status:", error);
  }
}

getStatus();
```

### 2. Upload a Document

Upload a new Markdown file or update an existing one. This is particularly useful for automating content updates from a Node.js environment or a web-based content management system.

```javascript
import { SmartGenDocsClient } from 'smartgendocs-sdk-js';
import fs from 'fs'; // For Node.js environment

const client = new SmartGenDocsClient("YOUR_SMARTGENDOCS_API_KEY");

const filePath = "./my_new_document.md";
const targetPath = "new-section/my-new-document.md";

async function uploadDocument() {
  try {
    const fileContent = fs.readFileSync(filePath); // Read file content as Buffer
    const response = await client.uploadDocument(fileContent, targetPath, true); // true for overwrite
    console.log("Upload successful:", response);
  } catch (error) {
    console.error("Error uploading document:", error);
  }
}

uploadDocument();
```

### 3. Trigger a Site Build

Initiate a new build of your static documentation site programmatically.

```javascript
import { SmartGenDocsClient } from 'smartgendocs-sdk-js';

const client = new SmartGenDocsClient("YOUR_SMARTGENDOCS_API_KEY");

async function triggerBuild() {
  try {
    const response = await client.triggerBuild();
    console.log("Build triggered:", response);
  } catch (error) {
    console.error("Error triggering build:", error);
  }
}

triggerBuild();
```

### 4. Get Document Content

Retrieve the raw Markdown or rendered HTML content of a specific documentation page.

```javascript
import { SmartGenDocsClient } from 'smartgendocs-sdk-js';

const client = new SmartGenDocsClient("YOUR_SMARTGENDOCS_API_KEY");

async function getDocumentContent() {
  try {
    // Get raw Markdown content
    const markdownContent = await client.getDocumentContent("getting-started/installation.md", "markdown");
    console.log("Markdown Content:\n", markdownContent.substring(0, 200), "...");

    // Get rendered HTML content
    const htmlContent = await client.getDocumentContent("getting-started/installation.md", "html");
    console.log("HTML Content:\n", htmlContent.substring(0, 200), "...");
  } catch (error) {
    console.error("Error getting document content:", error);
  }
}

getDocumentContent();
```

## API Reference

### `SmartGenDocsClient` Class

#### `constructor(apiKey: string, baseUrl: string = "https://api.smartgendocs.com/v1")`

Initializes the SmartGen Docs client.

*   **`apiKey`** (`string`): Your SmartGen Docs API key.
*   **`baseUrl`** (`string`, optional): The base URL for the SmartGen Docs API. Defaults to `https://api.smartgendocs.com/v1`.

#### `getStatus(): Promise<object>`

Retrieves the current operational status of the SmartGen Docs instance.

*   **Returns** (`Promise<object>`): A promise that resolves to an object containing the status information.
*   **Throws** (`Error`): If the API request fails.

#### `uploadDocument(fileContent: Buffer | string, targetPath: string, overwrite: boolean = false): Promise<object>`

Uploads a Markdown document to the specified path.

*   **`fileContent`** (`Buffer | string`): The content of the Markdown file as a Buffer (Node.js) or string.
*   **`targetPath`** (`string`): The relative path within the `docs/` directory where the file should be saved (e.g., `new-section/my-doc.md`).
*   **`overwrite`** (`boolean`, optional): If `true`, overwrites the file if it already exists. Defaults to `false`.
*   **Returns** (`Promise<object>`): A promise that resolves to an object containing the upload status.
*   **Throws** (`Error`): If the API request fails.

#### `triggerBuild(): Promise<object>`

Initiates a new build of the static documentation site.

*   **Returns** (`Promise<object>`): A promise that resolves to an object containing the build initiation status.
*   **Throws** (`Error`): If the API request fails.

#### `getDocumentContent(pagePath: string, format: "html" | "markdown" = "html"): Promise<string>`

Retrieves the content of a specific documentation page.

*   **`pagePath`** (`string`): The relative path to the Markdown file (e.g., `getting-started/installation.md`).
*   **`format`** (`"html" | "markdown"`, optional): The desired output format (`html` or `markdown`). Defaults to `html`.
*   **Returns** (`Promise<string>`): A promise that resolves to the content of the document in the specified format.
*   **Throws** (`Error`): If the API request fails.

## Error Handling

The SDK methods will throw `Error` objects for network-related issues or non-2xx HTTP responses. It is recommended to wrap your API calls in `try-catch` blocks to handle these exceptions gracefully. For specific API error codes, refer to the [API Error Codes](../api/errors.md) documentation.

## Contributing

Contributions to the JavaScript SDK are welcome! Please refer to the [Contributing Guide](../../contributing.md) for details on how to contribute.
