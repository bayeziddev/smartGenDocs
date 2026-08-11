# SmartGen Docs Java SDK

The **SmartGen Java SDK** provides enterprise Java and Spring Boot applications with programmatic access to SmartGen documentation repositories, search indexes, and metadata services [1].

## Java Client Example

```java
package com.smartgen.sdk;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class SmartGenClient {
    private final String baseUrl;
    private final HttpClient httpClient;

    public SmartGenClient(String baseUrl) {
        this.baseUrl = baseUrl;
        this.httpClient = HttpClient.newHttpClient();
    }

    public String fetchSitemap() throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(baseUrl + "/sitemap.xml"))
                .GET()
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        return response.body();
    }
}
```

## References

- [1] Java SDK Reference. [SmartGen Documentation](https://docs.smartgentools.com/sdk/java.html).
- [2] API Reference. [SmartGen API Guides](https://docs.smartgentools.com/api/index.html).
