# SmartGen Docs Go SDK

The **SmartGen Go SDK** provides high-performance Go microservices and tools with native client bindings for querying SmartGen documentation endpoints, verifying sitemaps, and interacting with developer portals [1].

## Go Client Example

```go
package smartgen

import (
	"fmt"
	"net/http"
)

type Client struct {
	BaseURL    string
	HTTPClient *http.Client
}

func NewClient(baseURL string) *Client {
	return &Client{
		BaseURL:    baseURL,
		HTTPClient: &http.Client{},
	}
}

func (c *Client) Ping() error {
	resp, err := c.HTTPClient.Get(c.BaseURL + "/robots.txt")
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}
	return nil
}
```

## References

- [1] Go SDK Reference. [SmartGen Documentation](https://docs.smartgentools.com/sdk/go.html).
- [2] API Reference. [SmartGen API Guides](https://docs.smartgentools.com/api/index.html).
