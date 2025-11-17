REST API endpoints for Markdown

Use the REST API to render a markdown document as an HTML page or as raw text.
Render a Markdown document

Depending on what is rendered in the Markdown, you may need to provide additional token scopes for labels, such as issues:read or pull_requests:read.
Fine-grained access tokens for "Render a Markdown document"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Render a Markdown document"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Body parameters
Name, Type, Description
text string Required

The Markdown text to render in HTML.
mode string

The rendering mode.

Default: markdown

Can be one of: markdown, gfm
context string

The repository context to use when creating references in gfm mode. For example, setting context to octo-org/octo-repo will change the text #42 into an HTML link to issue 42 in the octo-org/octo-repo repository.
HTTP response status codes for "Render a Markdown document"
Status code	Description
200	

OK
304	

Not modified
Code samples for "Render a Markdown document"
Request example
post/markdown

curl -L \
  -X POST \
  -H "Accept: text/html" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/markdown \
  -d '{"text":"Hello **world**"}'

Example response

Status: 200
"<p>Hello <strong>world</strong></p>"
Render a Markdown document in raw mode

You must send Markdown as plain text (using a Content-Type header of text/plain or text/x-markdown) to this endpoint, rather than using JSON format. In raw mode, GitHub Flavored Markdown is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.
Fine-grained access tokens for "Render a Markdown document in raw mode"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token does not require any permissions.

This endpoint can be used without authentication if only public resources are requested.
HTTP response status codes for "Render a Markdown document in raw mode"
Status code	Description
200	

OK
304	

Not modified
Code samples for "Render a Markdown document in raw mode"
Request examples
Select the example type
post/markdown/raw

curl -L \
  -X POST \
  -H "Accept: text/html" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/markdown/raw \
  -d '{"text":"Hello **world**"}'

Example response

Status: 200
"<p>Hello <strong>world</strong></p>"