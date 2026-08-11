# SmartGen Docs JavaScript / TypeScript SDK

The **SmartGen JavaScript SDK** enables frontend applications, Node.js microservices, and serverless functions to interact with SmartGen documentation services, search APIs, and theme switcher state [1].

## Client Integration Example

```typescript
export class SmartGenClient {
    private baseUrl: string;

    constructor(baseUrl: string = 'https://docs.smartgentools.com') {
        this.baseUrl = baseUrl.replace(/\/$/, '');
    }

    async fetchDocumentationIndex(): Promise<Response> {
        const response = await fetch(`${this.baseUrl}/sitemap.xml`);
        if (!response.ok) {
            throw new Error(`Failed to fetch sitemap: ${response.statusText}`);
        }
        return response;
    }
}
```

## References

- [1] JavaScript SDK Reference. [SmartGen Documentation](https://docs.smartgentools.com/sdk/javascript.html).
- [2] SmartGen API Reference. [SmartGen API Guides](https://docs.smartgentools.com/api/index.html).
