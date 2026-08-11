# SmartGen Docs PHP Integration & Client SDK

The **SmartGen PHP Integration Guide** outlines how PHP-based web applications, Laravel services, and content management systems can interact with SmartGen documentation portals, consume REST APIs, and integrate webhooks [1].

## Consuming SmartGen APIs in PHP

You can interact with SmartGen services using standard HTTP clients like Guzzle or native cURL [2]:

```php
<?php

namespace SmartGen\Client;

class DocumentationClient {
    private string $baseUrl;

    public function __construct(string $baseUrl = 'https://docs.smartgentools.com') {
        $this->baseUrl = rtrim($baseUrl, '/');
    }

    public function getPage(string $path): ?string {
        $url = $this->baseUrl . '/' . ltrim($path, '/');
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        return $httpCode === 200 ? $response : null;
    }
}
```

## References

- [1] PHP SDK Documentation. [SmartGen Documentation](https://docs.smartgentools.com/sdk/php.html).
- [2] SmartGen API Reference. [SmartGen API Guides](https://docs.smartgentools.com/api/index.html).
