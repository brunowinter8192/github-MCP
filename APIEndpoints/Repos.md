REST API endpoints for repository autolinks

Use the REST API to add autolinks to external resources.
About repository autolinks

To help streamline your workflow, you can use the REST API to add autolinks to external resources like JIRA issues and Zendesk tickets. For more information, see Configuring autolinks to reference external resources.

GitHub Apps require repository administration permissions with read or write access to use these endpoints.
Get all autolinks of a repository

Gets all autolinks that are configured for a repository.

Information about autolinks are only available to repository administrators.
Fine-grained access tokens for "Get all autolinks of a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "Get all autolinks of a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Get all autolinks of a repository"
Status code	Description
200	

OK
Code samples for "Get all autolinks of a repository"
Request example
get/repos/{owner}/{repo}/autolinks

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/autolinks

Response

Status: 200
[
  {
    "id": 1,
    "key_prefix": "TICKET-",
    "url_template": "https://example.com/TICKET?query=<num>",
    "is_alphanumeric": true
  }
]
Create an autolink reference for a repository

Users with admin access to the repository can create an autolink.
Fine-grained access tokens for "Create an autolink reference for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Create an autolink reference for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
key_prefix string Required

This prefix appended by certain characters will generate a link any time it is found in an issue, pull request, or commit.
url_template string Required

The URL must contain <num> for the reference number. <num> matches different characters depending on the value of is_alphanumeric.
is_alphanumeric boolean

Whether this autolink reference matches alphanumeric characters. If true, the <num> parameter of the url_template matches alphanumeric characters A-Z (case insensitive), 0-9, and -. If false, this autolink reference only matches numeric characters.

Default: true
HTTP response status codes for "Create an autolink reference for a repository"
Status code	Description
201	

Created
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create an autolink reference for a repository"
Request example
post/repos/{owner}/{repo}/autolinks

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/autolinks \
  -d '{"key_prefix":"TICKET-","url_template":"https://example.com/TICKET?query=<num>","is_alphanumeric":true}'

response

Status: 201
{
  "id": 1,
  "key_prefix": "TICKET-",
  "url_template": "https://example.com/TICKET?query=<num>",
  "is_alphanumeric": true
}
Get an autolink reference of a repository

This returns a single autolink reference by ID that was configured for the given repository.

Information about autolinks are only available to repository administrators.
Fine-grained access tokens for "Get an autolink reference of a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "Get an autolink reference of a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
autolink_id integer Required

The unique identifier of the autolink.
HTTP response status codes for "Get an autolink reference of a repository"
Status code	Description
200	

OK
404	

Resource not found
Code samples for "Get an autolink reference of a repository"
Request example
get/repos/{owner}/{repo}/autolinks/{autolink_id}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/autolinks/AUTOLINK_ID

Response

Status: 200
{
  "id": 1,
  "key_prefix": "TICKET-",
  "url_template": "https://example.com/TICKET?query=<num>",
  "is_alphanumeric": true
}
Delete an autolink reference from a repository

This deletes a single autolink reference by ID that was configured for the given repository.

Information about autolinks are only available to repository administrators.
Fine-grained access tokens for "Delete an autolink reference from a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Delete an autolink reference from a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
autolink_id integer Required

The unique identifier of the autolink.
HTTP response status codes for "Delete an autolink reference from a repository"
Status code	Description
204	

No Content
404	

Resource not found
Code samples for "Delete an autolink reference from a repository"
Request example
delete/repos/{owner}/{repo}/autolinks/{autolink_id}

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/autolinks/AUTOLINK_ID

Response
Status: 204


REST API endpoints for repository contents

Use the REST API to create, modify, and delete Base64 encoded content in a repository.
Get repository content

Gets the contents of a file or directory in a repository. Specify the file path or directory with the path parameter. If you omit the path parameter, you will receive the contents of the repository's root directory.

This endpoint supports the following custom media types. For more information, see "Media types."

    application/vnd.github.raw+json: Returns the raw file contents for files and symlinks.
    application/vnd.github.html+json: Returns the file contents in HTML. Markup languages are rendered to HTML using GitHub's open-source Markup library.
    application/vnd.github.object+json: Returns the contents in a consistent object format regardless of the content type. For example, instead of an array of objects for a directory, the response will be an object with an entries attribute containing the array of objects.

If the content is a directory, the response will be an array of objects, one object for each item in the directory. When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value should be "submodule". This behavior exists for backwards compatibility purposes. In the next major version of the API, the type will be returned as "submodule".

If the content is a symlink and the symlink's target is a normal file in the repository, then the API responds with the content of the file. Otherwise, the API responds with an object describing the symlink itself.

If the content is a submodule, the submodule_git_url field identifies the location of the submodule repository, and the sha identifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit. If the submodule repository is not hosted on github.com, the Git URLs (git_url and _links["git"]) and the github.com URLs (html_url and _links["html"]) will have null values.

Notes:

    To get a repository's contents recursively, you can recursively get the tree.
    This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the Git Trees API.
    Download URLs expire and are meant to be used just once. To ensure the download URL does not expire, please use the contents API to obtain a fresh download URL for each download.
    If the requested file's size is:
        1 MB or smaller: All features of this endpoint are supported.
        Between 1-100 MB: Only the raw or object custom media types are supported. Both will work as normal, except that when using the object media type, the content field will be an empty string and the encoding field will be "none". To get the contents of these larger files, use the raw media type.
        Greater than 100 MB: This endpoint is not supported.

Fine-grained access tokens for "Get repository content"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get repository content"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
path string Required

path parameter
Query parameters
Name, Type, Description
ref string

The name of the commit/branch/tag. Default: the repository’s default branch.
HTTP response status codes for "Get repository content"
Status code	Description
200	

OK
302	

Found
304	

Not modified
403	

Forbidden
404	

Resource not found
Code samples for "Get repository content"
Request examples
Select the example type
get/repos/{owner}/{repo}/contents/{path}

curl -L \
  -H "Accept: application/vnd.github.object" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH

Response if content is a file

Status: 200
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "IyBZb2dhIEJvmsgaW4gcHJvZ3Jlc3MhIEZlZWwgdAoKOndhcm5pbmc6IFdvc\\nZnJlZSBmUgdG8gY0byBjaGVjayBvdXQgdGhlIGFwcCwgYnV0IGJlIHN1c29t\\nZSBiYWNrIG9uY2UgaXQgaXMgY29tcGxldGUuCgpBIHdlYiBhcHAgdGhhdCBs\\nZWFkcyB5b3UgdGhyb3VnaCBhIHlvZ2Egc2Vzc2lvbi4KCltXb3Jrb3V0IG5v\\ndyFdKGh0dHBzOi8vc2tlZHdhcmRzODguZ2l0aHViLmlvL3lvZ2EvKQoKPGlt\\nZyBzcmM9InNyYy9pbWFnZXMvbWFza2FibGVfaWNvbl81MTIucG5nIiBhbHQ9\\nImJvdCBsaWZ0aW5nIHdlaWdodHMiIHdpZHRoPSIxMDAiLz4KCkRvIHlvdSBo\\nYXZlIGZlZWRiYWNrIG9yIGlkZWFzIGZvciBpbXByb3ZlbWVudD8gW09wZW4g\\nYW4gaXNzdWVdKGh0dHBzOi8vZ2l0aHViLmNvbS9za2Vkd2FyZHM4OC95b2dh\\nL2lzc3Vlcy9uZXcpLgoKV2FudCBtb3JlIGdhbWVzPyBWaXNpdCBbQ25TIEdh\\nbWVzXShodHRwczovL3NrZWR3YXJkczg4LmdpdGh1Yi5pby9wb3J0Zm9saW8v\\nKS4KCiMjIERldmVsb3BtZW50CgpUbyBhZGQgYSBuZXcgcG9zZSwgYWRkIGFu\\nIGVudHJ5IHRvIHRoZSByZWxldmFudCBmaWxlIGluIGBzcmMvYXNhbmFzYC4K\\nClRvIGJ1aWxkLCBydW4gYG5wbSBydW4gYnVpbGRgLgoKVG8gcnVuIGxvY2Fs\\nbHkgd2l0aCBsaXZlIHJlbG9hZGluZyBhbmQgbm8gc2VydmljZSB3b3JrZXIs\\nIHJ1biBgbnBtIHJ1biBkZXZgLiAoSWYgYSBzZXJ2aWNlIHdvcmtlciB3YXMg\\ncHJldmlvdXNseSByZWdpc3RlcmVkLCB5b3UgY2FuIHVucmVnaXN0ZXIgaXQg\\naW4gY2hyb21lIGRldmVsb3BlciB0b29sczogYEFwcGxpY2F0aW9uYCA+IGBT\\nZXJ2aWNlIHdvcmtlcnNgID4gYFVucmVnaXN0ZXJgLikKClRvIHJ1biBsb2Nh\\nbGx5IGFuZCByZWdpc3RlciB0aGUgc2VydmljZSB3b3JrZXIsIHJ1biBgbnBt\\nIHN0YXJ0YC4KClRvIGRlcGxveSwgcHVzaCB0byBgbWFpbmAgb3IgbWFudWFs\\nbHkgdHJpZ2dlciB0aGUgYC5naXRodWIvd29ya2Zsb3dzL2RlcGxveS55bWxg\\nIHdvcmtmbG93Lgo=\\n",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
Create or update file contents

Creates a new file or replaces an existing file in a repository.

Note

If you use this endpoint and the "Delete a file" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.

OAuth app tokens and personal access tokens (classic) need the repo scope to use this endpoint. The workflow scope is also required in order to modify files in the .github/workflows directory.
Fine-grained access tokens for "Create or update file contents"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have at least one of the following permission sets:

    "Contents" repository permissions (write)
    "Contents" repository permissions (write) and "Workflows" repository permissions (write)

Parameters for "Create or update file contents"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
path string Required

path parameter
Body parameters
Name, Type, Description
message string Required

The commit message.
content string Required

The new file content, using Base64 encoding.
sha string

Required if you are updating a file. The blob SHA of the file being replaced.
branch string

The branch name. Default: the repository’s default branch.
committer object

The person that committed the file. Default: the authenticated user.
Properties of committer
author object

The author of the file. Default: The committer or the authenticated user if you omit committer.
Properties of author
HTTP response status codes for "Create or update file contents"
Status code	Description
200	

OK
201	

Created
404	

Resource not found
409	

Conflict
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create or update file contents"
Request examples
Select the example type
put/repos/{owner}/{repo}/contents/{path}

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH \
  -d '{"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM="}'

Response

Status: 201
{
  "content": {
    "name": "hello.txt",
    "path": "notes/hello.txt",
    "sha": "95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
    "size": 9,
    "url": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
    "html_url": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt",
    "git_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
    "download_url": "https://raw.githubusercontent.com/octocat/HelloWorld/master/notes/hello.txt",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
      "git": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
      "html": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt"
    }
  },
  "commit": {
    "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
    "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
    "html_url": "https://github.com/octocat/Hello-World/git/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
    "author": {
      "date": "2014-11-07T22:01:45Z",
      "name": "Monalisa Octocat",
      "email": "octocat@github.com"
    },
    "committer": {
      "date": "2014-11-07T22:01:45Z",
      "name": "Monalisa Octocat",
      "email": "octocat@github.com"
    },
    "message": "my commit message",
    "tree": {
      "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
      "sha": "691272480426f78a0138979dd3ce63b77f706feb"
    },
    "parents": [
      {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
      }
    ],
    "verification": {
      "verified": false,
      "reason": "unsigned",
      "signature": null,
      "payload": null,
      "verified_at": null
    }
  }
}
Delete a file

Deletes a file in a repository.

You can provide an additional committer parameter, which is an object containing information about the committer. Or, you can provide an author parameter, which is an object containing information about the author.

The author section is optional and is filled in with the committer information if omitted. If the committer information is omitted, the authenticated user's information is used.

You must provide values for both name and email, whether you choose to use author or committer. Otherwise, you'll receive a 422 status code.

Note

If you use this endpoint and the "Create or update file contents" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.
Fine-grained access tokens for "Delete a file"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have at least one of the following permission sets:

    "Contents" repository permissions (write)
    "Contents" repository permissions (write) and "Workflows" repository permissions (write)

Parameters for "Delete a file"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
path string Required

path parameter
Body parameters
Name, Type, Description
message string Required

The commit message.
sha string Required

The blob SHA of the file being deleted.
branch string

The branch name. Default: the repository’s default branch
committer object

object containing information about the committer.
Properties of committer
author object

object containing information about the author.
Properties of author
HTTP response status codes for "Delete a file"
Status code	Description
200	

OK
404	

Resource not found
409	

Conflict
422	

Validation failed, or the endpoint has been spammed.
503	

Service unavailable
Code samples for "Delete a file"
Request example
delete/repos/{owner}/{repo}/contents/{path}

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH \
  -d '{"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"sha":"329688480d39049927147c162b9d2deaf885005f"}'

Response

Status: 200
{
  "content": null,
  "commit": {
    "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
    "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
    "html_url": "https://github.com/octocat/Hello-World/git/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
    "author": {
      "date": "2014-11-07T22:01:45Z",
      "name": "Monalisa Octocat",
      "email": "octocat@github.com"
    },
    "committer": {
      "date": "2014-11-07T22:01:45Z",
      "name": "Monalisa Octocat",
      "email": "octocat@github.com"
    },
    "message": "my commit message",
    "tree": {
      "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
      "sha": "691272480426f78a0138979dd3ce63b77f706feb"
    },
    "parents": [
      {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
      }
    ],
    "verification": {
      "verified": false,
      "reason": "unsigned",
      "signature": null,
      "payload": null,
      "verified_at": null
    }
  }
}
Get a repository README

Gets the preferred README for a repository.

This endpoint supports the following custom media types. For more information, see "Media types."

    application/vnd.github.raw+json: Returns the raw file contents. This is the default if you do not specify a media type.
    application/vnd.github.html+json: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source Markup library.

Fine-grained access tokens for "Get a repository README"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get a repository README"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
ref string

The name of the commit/branch/tag. Default: the repository’s default branch.
HTTP response status codes for "Get a repository README"
Status code	Description
200	

OK
304	

Not modified
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Get a repository README"
Request example
get/repos/{owner}/{repo}/readme

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/readme

Response

Status: 200
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "encoded content ...",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
Get a repository README for a directory

Gets the README from a repository directory.

This endpoint supports the following custom media types. For more information, see "Media types."

    application/vnd.github.raw+json: Returns the raw file contents. This is the default if you do not specify a media type.
    application/vnd.github.html+json: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source Markup library.

Fine-grained access tokens for "Get a repository README for a directory"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get a repository README for a directory"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
dir string Required

The alternate path to look for a README file
Query parameters
Name, Type, Description
ref string

The name of the commit/branch/tag. Default: the repository’s default branch.
HTTP response status codes for "Get a repository README for a directory"
Status code	Description
200	

OK
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Get a repository README for a directory"
Request example
get/repos/{owner}/{repo}/readme/{dir}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/readme/DIR

Response

Status: 200
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "encoded content ...",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
Download a repository archive (tar)

Gets a redirect URL to download a tar archive for a repository. If you omit :ref, the repository’s default branch (usually main) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the Location header to make a second GET request.

Note

For private repositories, these links are temporary and expire after five minutes.
Fine-grained access tokens for "Download a repository archive (tar)"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Download a repository archive (tar)"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
ref string Required
HTTP response status codes for "Download a repository archive (tar)"
Status code	Description
302	

Found
Code samples for "Download a repository archive (tar)"
Request example
get/repos/{owner}/{repo}/tarball/{ref}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/tarball/REF

Response
Status: 302
Download a repository archive (zip)

Gets a redirect URL to download a zip archive for a repository. If you omit :ref, the repository’s default branch (usually main) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the Location header to make a second GET request.

Note

For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect.
Fine-grained access tokens for "Download a repository archive (zip)"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Download a repository archive (zip)"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
ref string Required
HTTP response status codes for "Download a repository archive (zip)"
Status code	Description
302	

Found
Code samples for "Download a repository archive (zip)"
Request example
get/repos/{owner}/{repo}/zipball/{ref}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/zipball/REF

Response
Status: 302



REST API endpoints for custom properties

Use the REST API to list the custom properties assigned to a repository by the organization.
About custom properties

You can use the REST API to view the custom properties that were assigned to a repository by the organization that owns the repository. For more information, see Managing custom properties for repositories in your organization. For more information about the REST API endpoints to manage custom properties, see REST API endpoints for custom properties.
Get all custom property values for a repository

Gets all custom property values that are set for a repository. Users with read access to the repository can use this endpoint.
Fine-grained access tokens for "Get all custom property values for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get all custom property values for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Get all custom property values for a repository"
Status code	Description
200	

OK
403	

Forbidden
404	

Resource not found
Code samples for "Get all custom property values for a repository"
Request example
get/repos/{owner}/{repo}/properties/values

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/properties/values

Response

Status: 200
[
  {
    "property_name": "environment",
    "value": "production"
  },
  {
    "property_name": "service",
    "value": "web"
  },
  {
    "property_name": "team",
    "value": "octocat"
  }
]
Create or update custom property values for a repository

Create new or update existing custom property values for a repository. Using a value of null for a custom property will remove or 'unset' the property value from the repository.

Repository admins and other users with the repository-level "edit custom property values" fine-grained permission can use this endpoint.
Fine-grained access tokens for "Create or update custom property values for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Custom properties" repository permissions (write)

Parameters for "Create or update custom property values for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
properties array of objects Required

A list of custom property names and associated values to apply to the repositories.
Properties of properties
HTTP response status codes for "Create or update custom property values for a repository"
Status code	Description
204	

No Content when custom property values are successfully created or updated
403	

Forbidden
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create or update custom property values for a repository"
Request example
patch/repos/{owner}/{repo}/properties/values

curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/properties/values \
  -d '{"properties":[{"property_name":"environment","value":"production"},{"property_name":"service","value":"web"},{"property_name":"team","value":"octocat"}]}'

No Content when custom property values are successfully created or updated
Status: 204


REST API endpoints for forks

Use the REST API to manage repository forks.
List forks
Fine-grained access tokens for "List forks"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List forks"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
sort string

The sort order. stargazers will sort by star count.

Default: newest

Can be one of: newest, oldest, stargazers, watchers
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List forks"
Status code	Description
200	

OK
400	

Bad Request
Code samples for "List forks"
Request example
get/repos/{owner}/{repo}/forks

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/forks

Response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": true,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "delete_branch_on_merge": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit",
      "node_id": "MDc6TGljZW5zZW1pdA=="
    }
  }
]
Create a fork

Create a fork for the authenticated user.

Note

Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact GitHub Support.

Note

Although this endpoint works with GitHub Apps, the GitHub App must be installed on the destination account with access to all repositories and on the source account with access to the source repository.
Fine-grained access tokens for "Create a fork"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write) and "Contents" repository permissions (read)

Parameters for "Create a fork"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
organization string

Optional parameter to specify the organization name if forking into an organization.
name string

When forking from an existing repository, a new name for the fork.
default_branch_only boolean

When forking from an existing repository, fork with only the default branch.
HTTP response status codes for "Create a fork"
Status code	Description
202	

Accepted
400	

Bad Request
403	

Forbidden
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create a fork"
Request example
post/repos/{owner}/{repo}/forks

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/forks \
  -d '{"organization":"octocat","name":"Hello-World","default_branch_only":true}'

Response

Status: 202
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "license": {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "spdx_id": "MIT",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "html_url": "https://github.com/licenses/mit"
  },
  "language": null,
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "web_commit_signoff_required": false,
  "subscribers_count": 42,
  "network_count": 0,
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
}




REST API endpoints for repositories

Use the REST API to manage repositories on GitHub.
List organization repositories

Lists repositories for the specified organization.

Note

In order to see the security_and_analysis block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "Managing security managers in your organization."
Fine-grained access tokens for "List organization repositories"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List organization repositories"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
org string Required

The organization name. The name is not case sensitive.
Query parameters
Name, Type, Description
type string

Specifies the types of repositories you want returned.

Default: all

Can be one of: all, public, private, forks, sources, member
sort string

The property to sort the results by.

Default: created

Can be one of: created, updated, pushed, full_name
direction string

The order to sort by. Default: asc when using full_name, otherwise desc.

Can be one of: asc, desc
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List organization repositories"
Status code	Description
200	

OK
Code samples for "List organization repositories"
Request example
get/orgs/{org}/repos

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/ORG/repos

Response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": false,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "has_discussions": false,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "security_and_analysis": {
      "advanced_security": {
        "status": "enabled"
      },
      "secret_scanning": {
        "status": "enabled"
      },
      "secret_scanning_push_protection": {
        "status": "disabled"
      },
      "secret_scanning_non_provider_patterns": {
        "status": "disabled"
      }
    }
  }
]
Create an organization repository

Creates a new repository in the specified organization. The authenticated user must be a member of the organization.

OAuth app tokens and personal access tokens (classic) need the public_repo or repo scope to create a public repository, and repo scope to create a private repository.
Fine-grained access tokens for "Create an organization repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Create an organization repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
org string Required

The organization name. The name is not case sensitive.
Body parameters
Name, Type, Description
name string Required

The name of the repository.
description string

A short description of the repository.
homepage string

A URL with more information about the repository.
private boolean

Whether the repository is private.

Default: false
visibility string

The visibility of the repository.

Can be one of: public, private
has_issues boolean

Either true to enable issues for this repository or false to disable them.

Default: true
has_projects boolean

Either true to enable projects for this repository or false to disable them. Note: If you're creating a repository in an organization that has disabled repository projects, the default is false, and if you pass true, the API returns an error.

Default: true
has_wiki boolean

Either true to enable the wiki for this repository or false to disable it.

Default: true
has_downloads boolean

Whether downloads are enabled.

Default: true
is_template boolean

Either true to make this repo available as a template repository or false to prevent it.

Default: false
team_id integer

The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.
auto_init boolean

Pass true to create an initial commit with empty README.

Default: false
gitignore_template string

Desired language or platform .gitignore template to apply. Use the name of the template without the extension. For example, "Haskell".
license_template string

Choose an open source license template that best suits your needs, and then use the license keyword as the license_template string. For example, "mit" or "mpl-2.0".
allow_squash_merge boolean

Either true to allow squash-merging pull requests, or false to prevent squash-merging.

Default: true
allow_merge_commit boolean

Either true to allow merging pull requests with a merge commit, or false to prevent merging pull requests with merge commits.

Default: true
allow_rebase_merge boolean

Either true to allow rebase-merging pull requests, or false to prevent rebase-merging.

Default: true
allow_auto_merge boolean

Either true to allow auto-merge on pull requests, or false to disallow auto-merge.

Default: false
delete_branch_on_merge boolean

Either true to allow automatically deleting head branches when pull requests are merged, or false to prevent automatic deletion. The authenticated user must be an organization owner to set this property to true.

Default: false
use_squash_pr_title_as_default boolean

Either true to allow squash-merge commits to use pull request title, or false to use commit message. **This property is closing down. Please use squash_merge_commit_title instead.

Default: false
squash_merge_commit_title string

Required when using squash_merge_commit_message.

The default value for a squash merge commit title:

    PR_TITLE - default to the pull request's title.
    COMMIT_OR_PR_TITLE - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).

Can be one of: PR_TITLE, COMMIT_OR_PR_TITLE
squash_merge_commit_message string

The default value for a squash merge commit message:

    PR_BODY - default to the pull request's body.
    COMMIT_MESSAGES - default to the branch's commit messages.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, COMMIT_MESSAGES, BLANK
merge_commit_title string

Required when using merge_commit_message.

The default value for a merge commit title.

    PR_TITLE - default to the pull request's title.
    MERGE_MESSAGE - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).

Can be one of: PR_TITLE, MERGE_MESSAGE
merge_commit_message string

The default value for a merge commit message.

    PR_TITLE - default to the pull request's title.
    PR_BODY - default to the pull request's body.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, PR_TITLE, BLANK
custom_properties object

The custom properties for the new repository. The keys are the custom property names, and the values are the corresponding custom property values.
HTTP response status codes for "Create an organization repository"
Status code	Description
201	

Created
403	

Forbidden
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create an organization repository"
Request example
post/orgs/{org}/repos

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/ORG/repos \
  -d '{"name":"Hello-World","description":"This is your first repository","homepage":"https://github.com","private":false,"has_issues":true,"has_projects":true,"has_wiki":true}'

Response

Status: 201
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "license": {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "spdx_id": "MIT",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "html_url": "https://github.com/licenses/mit"
  },
  "language": null,
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "web_commit_signoff_required": false,
  "subscribers_count": 42,
  "network_count": 0,
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
}
Get a repository

The parent and source objects are present when the repository is a fork. parent is the repository this repository was forked from, source is the ultimate source for the network.

Note

    In order to see the security_and_analysis block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "Managing security managers in your organization."
    To view merge-related settings, you must have the contents:read and contents:write permissions.

Fine-grained access tokens for "Get a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Get a repository"
Status code	Description
200	

OK
301	

Moved permanently
403	

Forbidden
404	

Resource not found
Code samples for "Get a repository"
Request example
get/repos/{owner}/{repo}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO

Default response

Status: 200
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "has_discussions": false,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "subscribers_count": 42,
  "network_count": 0,
  "license": {
    "key": "mit",
    "name": "MIT License",
    "spdx_id": "MIT",
    "url": "https://api.github.com/licenses/mit",
    "node_id": "MDc6TGljZW5zZW1pdA=="
  },
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1,
    "security_and_analysis": {
      "advanced_security": {
        "status": "enabled"
      },
      "secret_scanning": {
        "status": "enabled"
      },
      "secret_scanning_push_protection": {
        "status": "disabled"
      },
      "secret_scanning_non_provider_patterns": {
        "status": "disabled"
      }
    }
  }
}
Update a repository

Note: To edit a repository's topics, use the Replace all repository topics endpoint.
Fine-grained access tokens for "Update a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Update a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
name string

The name of the repository.
description string

A short description of the repository.
homepage string

A URL with more information about the repository.
private boolean

Either true to make the repository private or false to make it public. Default: false.
Note: You will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private.

Default: false
visibility string

The visibility of the repository.

Can be one of: public, private
security_and_analysis object or null

Specify which security and analysis features to enable or disable for the repository.

To use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "Managing security managers in your organization."

For example, to enable GitHub Advanced Security, use this data in the body of the PATCH request: { "security_and_analysis": {"advanced_security": { "status": "enabled" } } }.

You can check which security and analysis features are currently enabled by using a GET /repos/{owner}/{repo} request.
Properties of security_and_analysis
has_issues boolean

Either true to enable issues for this repository or false to disable them.

Default: true
has_projects boolean

Either true to enable projects for this repository or false to disable them. Note: If you're creating a repository in an organization that has disabled repository projects, the default is false, and if you pass true, the API returns an error.

Default: true
has_wiki boolean

Either true to enable the wiki for this repository or false to disable it.

Default: true
is_template boolean

Either true to make this repo available as a template repository or false to prevent it.

Default: false
default_branch string

Updates the default branch for this repository.
allow_squash_merge boolean

Either true to allow squash-merging pull requests, or false to prevent squash-merging.

Default: true
allow_merge_commit boolean

Either true to allow merging pull requests with a merge commit, or false to prevent merging pull requests with merge commits.

Default: true
allow_rebase_merge boolean

Either true to allow rebase-merging pull requests, or false to prevent rebase-merging.

Default: true
allow_auto_merge boolean

Either true to allow auto-merge on pull requests, or false to disallow auto-merge.

Default: false
delete_branch_on_merge boolean

Either true to allow automatically deleting head branches when pull requests are merged, or false to prevent automatic deletion.

Default: false
allow_update_branch boolean

Either true to always allow a pull request head branch that is behind its base branch to be updated even if it is not required to be up to date before merging, or false otherwise.

Default: false
use_squash_pr_title_as_default boolean

Either true to allow squash-merge commits to use pull request title, or false to use commit message. **This property is closing down. Please use squash_merge_commit_title instead.

Default: false
squash_merge_commit_title string

Required when using squash_merge_commit_message.

The default value for a squash merge commit title:

    PR_TITLE - default to the pull request's title.
    COMMIT_OR_PR_TITLE - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).

Can be one of: PR_TITLE, COMMIT_OR_PR_TITLE
squash_merge_commit_message string

The default value for a squash merge commit message:

    PR_BODY - default to the pull request's body.
    COMMIT_MESSAGES - default to the branch's commit messages.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, COMMIT_MESSAGES, BLANK
merge_commit_title string

Required when using merge_commit_message.

The default value for a merge commit title.

    PR_TITLE - default to the pull request's title.
    MERGE_MESSAGE - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).

Can be one of: PR_TITLE, MERGE_MESSAGE
merge_commit_message string

The default value for a merge commit message.

    PR_TITLE - default to the pull request's title.
    PR_BODY - default to the pull request's body.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, PR_TITLE, BLANK
archived boolean

Whether to archive this repository. false will unarchive a previously archived repository.

Default: false
allow_forking boolean

Either true to allow private forks, or false to prevent private forks.

Default: false
web_commit_signoff_required boolean

Either true to require contributors to sign off on web-based commits, or false to not require contributors to sign off on web-based commits.

Default: false
HTTP response status codes for "Update a repository"
Status code	Description
200	

OK
307	

Temporary Redirect
403	

Forbidden
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Update a repository"
Request example
patch/repos/{owner}/{repo}

curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO \
  -d '{"name":"Hello-World","description":"This is your first repository","homepage":"https://github.com","private":true,"has_issues":true,"has_projects":true,"has_wiki":true}'

Response

Status: 200
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "license": {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "spdx_id": "MIT",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "html_url": "https://github.com/licenses/mit"
  },
  "language": null,
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "web_commit_signoff_required": false,
  "subscribers_count": 42,
  "network_count": 0,
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
}
Delete a repository

Deleting a repository requires admin access.

If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a 403 Forbidden response.

OAuth app tokens and personal access tokens (classic) need the delete_repo scope to use this endpoint.
Fine-grained access tokens for "Delete a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Delete a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Delete a repository"
Status code	Description
204	

No Content
307	

Temporary Redirect
403	

If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, a member will get this response:
404	

Resource not found
409	

Conflict
Code samples for "Delete a repository"
Request example
delete/repos/{owner}/{repo}

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO

Response
Status: 204
List repository activities

Lists a detailed history of changes to a repository, such as pushes, merges, force pushes, and branch changes, and associates these changes with commits and users.

For more information about viewing repository activity, see "Viewing activity and data for your repository."
Fine-grained access tokens for "List repository activities"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repository activities"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
direction string

The direction to sort the results by.

Default: desc

Can be one of: asc, desc
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
before string

A cursor, as given in the Link header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
after string

A cursor, as given in the Link header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
ref string

The Git reference for the activities you want to list.

The ref for a branch can be formatted either as refs/heads/BRANCH_NAME or BRANCH_NAME, where BRANCH_NAME is the name of your branch.
actor string

The GitHub username to use to filter by the actor who performed the activity.
time_period string

The time period to filter by.

For example, day will filter for activity that occurred in the past 24 hours, and week will filter for activity that occurred in the past 7 days (168 hours).

Can be one of: day, week, month, quarter, year
activity_type string

The activity type to filter by.

For example, you can choose to filter by "force_push", to see all force pushes to the repository.

Can be one of: push, force_push, branch_creation, branch_deletion, pr_merge, merge_queue_merge
HTTP response status codes for "List repository activities"
Status code	Description
200	

OK
422	

Validation failed, or the endpoint has been spammed.
Code samples for "List repository activities"
Request example
get/repos/{owner}/{repo}/activity

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/activity

Response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "before": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
    "after": "827efc6d56897b048c772eb4087f854f46256132",
    "ref": "refs/heads/main",
    "pushed_at": "2011-01-26T19:06:43Z",
    "push_type": "normal",
    "pusher": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    }
  }
]
Create an attestation

Store an artifact attestation and associate it with a repository.

The authenticated user must have write permission to the repository and, if using a fine-grained access token, the attestations:write permission is required.

Artifact attestations are meant to be created using the attest action. For more information, see our guide on using artifact attestations to establish a build's provenance.
Fine-grained access tokens for "Create an attestation"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Attestations" repository permissions (write)

Parameters for "Create an attestation"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
bundle object Required

The attestation's Sigstore Bundle. Refer to the Sigstore Bundle Specification for more information.
Properties of bundle
HTTP response status codes for "Create an attestation"
Status code	Description
201	

Created
403	

Forbidden
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create an attestation"
Request example
post/repos/{owner}/{repo}/attestations

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/attestations \
  -d '{"value":{"bundle":{"mediaType":"application/vnd.dev.sigstore.bundle.v0.3+json","verificationMaterial":{"tlogEntries":[{"logIndex":"97913980","logId":{"keyId":"wNI9atQGlz+VWfO6LRygH4QUfY/8W4RFwiT5i5WRgB0="},"kindVersion":{"kind":"dsse","version":"0.0.1"},"integratedTime":"1716998992","inclusionPromise":{"signedEntryTimestamp":"MEYCIQCeEsQAy+qXtULkh52wbnHrkt2R2JQ05P9STK/xmdpQ2AIhANiG5Gw6cQiMnwvUz1+9UKtG/vlC8dduq07wsFOViwSL"},"inclusionProof":{"logIndex":"93750549","rootHash":"KgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=","treeSize":"93750551","hashes":["8LI21mzwxnUSo0fuZeFsUrz2ujZ4QAL+oGeTG+5toZg=","nCb369rcIytNhGwWoqBv+eV49X3ZKpo/HJGKm9V+dck=","hnNQ9mUdSwYCfdV21pd87NucrdRRNZATowlaRR1hJ4A=","MBhhK33vlD4Tq/JKgAaXUI4VjmosWKe6+7RNpQ2ncNM=","XKWUE3stvGV1OHsIGiCGfn047Ok6uD4mFkh7BaicaEc=","Tgve40VPFfuei+0nhupdGpfPPR+hPpZjxgTiDT8WNoY=","wV+S/7tLtYGzkLaSb6UDqexNyhMvumHK/RpTNvEZuLU=","uwaWufty6sn6XqO1Tb9M3Vz6sBKPu0HT36mStxJNd7s=","jUfeMOXQP0XF1JAnCEETVbfRKMUwCzrVUzYi8vnDMVs=","xQKjzJAwwdlQG/YUYBKPXxbCmhMYKo1wnv+6vDuKWhQ=","cX3Agx+hP66t1ZLbX/yHbfjU46/3m/VAmWyG/fhxAVc=","sjohk/3DQIfXTgf/5XpwtdF7yNbrf8YykOMHr1CyBYQ=","98enzMaC+x5oCMvIZQA5z8vu2apDMCFvE/935NfuPw8="],"checkpoint":{"envelope":"rekor.sigstore.dev - 2605736670972794746\\n93750551\\nKgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=\\n\\n— rekor.sigstore.dev wNI9ajBEAiBkLzdjY8A9HReU7rmtjwZ+JpSuYtEr9SmvSwUIW7FBjgIgKo+vhkW3tqc+gc8fw9gza3xLoncA8a+MTaJYCaLGA9c=\\n"}},"canonicalizedBody":"eyJhcGlWZXJzaW9uIjoiMC4wLjEiLCJraW5kIjoiZHNzZSIsInNwZWMiOnsiZW52ZWxvcGVIYXNoIjp7ImFsZ29yaXRobSI6InNoYTI1NiIsInZhbHVlIjoiM2I1YzkwNDk5MGFiYzE4NjI1ZWE3Njg4MzE1OGEwZmI4MTEwMjM4MGJkNjQwZjI5OWJlMzYwZWVkOTMxNjYwYiJ9LCJwYXlsb2FkSGFzaCI6eyJhbGdvcml0aG0iOiJzaGEyNTYiLCJ2YWx1ZSI6IjM4ZGNlZDJjMzE1MGU2OTQxMDViYjZiNDNjYjY3NzBiZTYzZDdhNGM4NjNiMTc2YTkwMmU1MGQ5ZTAyN2ZiMjMifSwic2lnbmF0dXJlcyI6W3sic2lnbmF0dXJlIjoiTUVRQ0lFR0lHQW03Z1pWTExwc3JQY2puZEVqaXVjdEUyL2M5K2o5S0d2YXp6M3JsQWlBZDZPMTZUNWhrelJNM0liUlB6bSt4VDQwbU5RWnhlZmQ3bGFEUDZ4MlhMUT09IiwidmVyaWZpZXIiOiJMUzB0TFMxQ1JVZEpUaUJEUlZKVVNVWkpRMEZVUlMwdExTMHRDazFKU1VkcVZFTkRRbWhUWjBGM1NVSkJaMGxWVjFsNGNVdHpjazFUTTFOMmJEVkphalZQUkdaQ1owMUtUeTlKZDBObldVbExiMXBKZW1vd1JVRjNUWGNLVG5wRlZrMUNUVWRCTVZWRlEyaE5UV015Ykc1ak0xSjJZMjFWZFZwSFZqSk5ValIzU0VGWlJGWlJVVVJGZUZaNllWZGtlbVJIT1hsYVV6RndZbTVTYkFwamJURnNXa2RzYUdSSFZYZElhR05PVFdwUmQwNVVTVFZOVkZsM1QxUlZlVmRvWTA1TmFsRjNUbFJKTlUxVVdYaFBWRlY1VjJwQlFVMUdhM2RGZDFsSUNrdHZXa2w2YWpCRFFWRlpTVXR2V2tsNmFqQkVRVkZqUkZGblFVVmtiV2RvVGs1M00yNVZMMHQxWlZGbmMzQkhTRmMzWjJnNVdFeEVMMWRrU1RoWlRVSUtLekJ3TUZZMGJ6RnJTRzgyWTAweGMwUktaM0pEWjFCUlZYcDRjSFZaZFc4cmVIZFFTSGxzTDJ0RWVXWXpSVXhxYTJGUFEwSlVUWGRuWjFWMlRVRTBSd3BCTVZWa1JIZEZRaTkzVVVWQmQwbElaMFJCVkVKblRsWklVMVZGUkVSQlMwSm5aM0pDWjBWR1FsRmpSRUY2UVdSQ1owNVdTRkUwUlVablVWVnhaa05RQ25aWVMwRjJVelJEWkdoUk1taGlXbGRLVTA5RmRsWnZkMGgzV1VSV1VqQnFRa0puZDBadlFWVXpPVkJ3ZWpGWmEwVmFZalZ4VG1wd1MwWlhhWGhwTkZrS1drUTRkMWRuV1VSV1VqQlNRVkZJTDBKR1FYZFViMXBOWVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREpPYzJGVE9XcGlSMnQyVEcxa2NBcGtSMmd4V1drNU0ySXpTbkphYlhoMlpETk5kbHBIVm5kaVJ6azFZbGRXZFdSRE5UVmlWM2hCWTIxV2JXTjVPVzlhVjBaclkzazVNR051Vm5WaGVrRTFDa0puYjNKQ1owVkZRVmxQTDAxQlJVSkNRM1J2WkVoU2QyTjZiM1pNTTFKMllUSldkVXh0Um1wa1IyeDJZbTVOZFZveWJEQmhTRlpwWkZoT2JHTnRUbllLWW01U2JHSnVVWFZaTWpsMFRVSTRSME5wYzBkQlVWRkNaemM0ZDBGUlNVVkZXR1IyWTIxMGJXSkhPVE5ZTWxKd1l6TkNhR1JIVG05TlJGbEhRMmx6UndwQlVWRkNaemM0ZDBGUlRVVkxSMXBvV2xkWmVWcEhVbXRQUkVacFRVUmplazVxWXpCUFJGRjRUVEpGTTFsNldUQk9iVTVyVFVkS2JWbDZTVEpaZWtGM0NsbFVRWGRIUVZsTFMzZFpRa0pCUjBSMmVrRkNRa0ZSUzFKSFZuZGlSemsxWWxkV2RXUkVRVlpDWjI5eVFtZEZSVUZaVHk5TlFVVkdRa0ZrYW1KSGEzWUtXVEo0Y0UxQ05FZERhWE5IUVZGUlFtYzNPSGRCVVZsRlJVaEtiRnB1VFhaaFIxWm9Xa2hOZG1SSVNqRmliWE4zVDNkWlMwdDNXVUpDUVVkRWRucEJRZ3BEUVZGMFJFTjBiMlJJVW5kamVtOTJURE5TZG1FeVZuVk1iVVpxWkVkc2RtSnVUWFZhTW13d1lVaFdhV1JZVG14amJVNTJZbTVTYkdKdVVYVlpNamwwQ2sxR2QwZERhWE5IUVZGUlFtYzNPSGRCVVd0RlZHZDRUV0ZJVWpCalNFMDJUSGs1Ym1GWVVtOWtWMGwxV1RJNWRFd3lUbk5oVXpscVlrZHJka3h0WkhBS1pFZG9NVmxwT1ROaU0wcHlXbTE0ZG1RelRYWmFSMVozWWtjNU5XSlhWblZrUXpVMVlsZDRRV050Vm0xamVUbHZXbGRHYTJONU9UQmpibFoxWVhwQk5BcENaMjl5UW1kRlJVRlpUeTlOUVVWTFFrTnZUVXRIV21oYVYxbDVXa2RTYTA5RVJtbE5SR042VG1wak1FOUVVWGhOTWtVeldYcFpNRTV0VG10TlIwcHRDbGw2U1RKWmVrRjNXVlJCZDBoUldVdExkMWxDUWtGSFJIWjZRVUpEZDFGUVJFRXhibUZZVW05a1YwbDBZVWM1ZW1SSFZtdE5RMjlIUTJselIwRlJVVUlLWnpjNGQwRlJkMFZJUVhkaFlVaFNNR05JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKT2MyRlRPV3BpUjJ0M1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWdwRVVWRnhSRU5vYlZsWFZtMU5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBGSENrTnBjMGRCVVZGQ1p6YzRkMEZSTkVWRlozZFJZMjFXYldONU9XOWFWMFpyWTNrNU1HTnVWblZoZWtGYVFtZHZja0puUlVWQldVOHZUVUZGVUVKQmMwMEtRMVJKZUUxcVdYaE5la0V3VDFSQmJVSm5iM0pDWjBWRlFWbFBMMDFCUlZGQ1FtZE5SbTFvTUdSSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhZ3BpUjJ0M1IwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWUlVVdEVRV2N4VDFSamQwNUVZM2hOVkVKalFtZHZja0puUlVWQldVOHZUVUZGVTBKRk5FMVVSMmd3Q21SSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhbUpIYTNaWk1uaHdUSGsxYm1GWVVtOWtWMGwyWkRJNWVXRXlXbk5pTTJSNlRESlNiR05IZUhZS1pWY3hiR0p1VVhWbFZ6RnpVVWhLYkZwdVRYWmhSMVpvV2toTmRtUklTakZpYlhOM1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWM1VYRkVRMmh0V1ZkV2JRcE5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBWSFEybHpSMEZSVVVKbk56aDNDa0ZTVVVWRmQzZFNaREk1ZVdFeVduTmlNMlJtV2tkc2VtTkhSakJaTW1kM1ZGRlpTMHQzV1VKQ1FVZEVkbnBCUWtaUlVTOUVSREZ2WkVoU2QyTjZiM1lLVERKa2NHUkhhREZaYVRWcVlqSXdkbGt5ZUhCTU1rNXpZVk01YUZrelVuQmlNalY2VEROS01XSnVUWFpQVkVrMFQxUkJNMDVVWXpGTmFUbG9aRWhTYkFwaVdFSXdZM2s0ZUUxQ1dVZERhWE5IUVZGUlFtYzNPSGRCVWxsRlEwRjNSMk5JVm1saVIyeHFUVWxIVEVKbmIzSkNaMFZGUVdSYU5VRm5VVU5DU0RCRkNtVjNRalZCU0dOQk0xUXdkMkZ6WWtoRlZFcHFSMUkwWTIxWFl6TkJjVXBMV0hKcVpWQkxNeTlvTkhCNVowTTRjRGR2TkVGQlFVZFFlRkl4ZW1KblFVRUtRa0ZOUVZORVFrZEJhVVZCS3pobmJGRkplRTlCYUZoQ1FVOVRObE1yT0ZweGQwcGpaSGQzVTNJdlZGZHBhSE16WkV4eFZrRjJiME5KVVVSaWVUbG9NUXBKWTNWRVJYSXJlbk5YYVV3NFVIYzFRMU5VZEd0c2RFbzBNakZ6UlRneFZuWjFOa0Z3VkVGTFFtZG5jV2hyYWs5UVVWRkVRWGRPYmtGRVFtdEJha0VyQ2tSSU4xQXJhR2cwVmtoWFprTlhXSFJ5UzFSdlFrdDFZa0pyUzNCbVYwTlpVWGhxV0UweWRsWXZibEJ4WWxwR1dVOVdXazlpWlRaQlRuSm5lV1J2V1VNS1RVWlZUV0l6ZUhwelJrNVJXWFp6UlZsUGFUSkxibkoyUmpCMFoyOXdiVmhIVm05NmJsb3JjUzh5UVVsRVZ6bEdNVVUzV1RaWk1EWXhaVzkxUVZsa1NBcFhkejA5Q2kwdExTMHRSVTVFSUVORlVsUkpSa2xEUVZSRkxTMHRMUzBLIn1dfX0="}],"timestampVerificationData":{},"certificate":{"rawBytes":"MIIGjTCCBhSgAwIBAgIUWYxqKsrMS3Svl5Ij5ODfBgMJO/IwCgYIKoZIzj0EAwMwNzEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MR4wHAYDVQQDExVzaWdzdG9yZS1pbnRlcm1lZGlhdGUwHhcNMjQwNTI5MTYwOTUyWhcNMjQwNTI5MTYxOTUyWjAAMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdmghNNw3nU/KueQgspGHW7gh9XLD/WdI8YMB+0p0V4o1kHo6cM1sDJgrCgPQUzxpuYuo+xwPHyl/kDyf3ELjkaOCBTMwggUvMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDAzAdBgNVHQ4EFgQUqfCPvXKAvS4CdhQ2hbZWJSOEvVowHwYDVR0jBBgwFoAU39Ppz1YkEZb5qNjpKFWixi4YZD8wWgYDVR0RAQH/BFAwToZMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA5BgorBgEEAYO/MAEBBCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMB8GCisGAQQBg78wAQIEEXdvcmtmbG93X2Rpc3BhdGNoMDYGCisGAQQBg78wAQMEKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwGAYKKwYBBAGDvzABBAQKRGVwbG95bWVudDAVBgorBgEEAYO/MAEFBAdjbGkvY2xpMB4GCisGAQQBg78wAQYEEHJlZnMvaGVhZHMvdHJ1bmswOwYKKwYBBAGDvzABCAQtDCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMFwGCisGAQQBg78wAQkETgxMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA4BgorBgEEAYO/MAEKBCoMKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwHQYKKwYBBAGDvzABCwQPDA1naXRodWItaG9zdGVkMCoGCisGAQQBg78wAQwEHAwaaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkwOAYKKwYBBAGDvzABDQQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCAGCisGAQQBg78wAQ4EEgwQcmVmcy9oZWFkcy90cnVuazAZBgorBgEEAYO/MAEPBAsMCTIxMjYxMzA0OTAmBgorBgEEAYO/MAEQBBgMFmh0dHBzOi8vZ2l0aHViLmNvbS9jbGkwGAYKKwYBBAGDvzABEQQKDAg1OTcwNDcxMTBcBgorBgEEAYO/MAESBE4MTGh0dHBzOi8vZ2l0aHViLmNvbS9jbGkvY2xpLy5naXRodWIvd29ya2Zsb3dzL2RlcGxveW1lbnQueW1sQHJlZnMvaGVhZHMvdHJ1bmswOAYKKwYBBAGDvzABEwQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCEGCisGAQQBg78wARQEEwwRd29ya2Zsb3dfZGlzcGF0Y2gwTQYKKwYBBAGDvzABFQQ/DD1odHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaS9hY3Rpb25zL3J1bnMvOTI4OTA3NTc1Mi9hdHRlbXB0cy8xMBYGCisGAQQBg78wARYECAwGcHVibGljMIGLBgorBgEEAdZ5AgQCBH0EewB5AHcA3T0wasbHETJjGR4cmWc3AqJKXrjePK3/h4pygC8p7o4AAAGPxR1zbgAABAMASDBGAiEA+8glQIxOAhXBAOS6S+8ZqwJcdwwSr/TWihs3dLqVAvoCIQDby9h1IcuDEr+zsWiL8Pw5CSTtkltJ421sE81Vvu6ApTAKBggqhkjOPQQDAwNnADBkAjA+DH7P+hh4VHWfCWXtrKToBKubBkKpfWCYQxjXM2vV/nPqbZFYOVZObe6ANrgydoYCMFUMb3xzsFNQYvsEYOi2KnrvF0tgopmXGVoznZ+q/2AIDW9F1E7Y6Y061eouAYdHWw=="}},"dsseEnvelope":{"payload":"eyJfdHlwZSI6Imh0dHBzOi8vaW4tdG90by5pby9TdGF0ZW1lbnQvdjEiLCJzdWJqZWN0IjpbeyJuYW1lIjoiZ2hfMi41MC4wX3dpbmRvd3NfYXJtNjQuemlwIiwiZGlnZXN0Ijp7InNoYTI1NiI6IjhhYWQxMjBiNDE2Mzg2YjQyNjllZjYyYzhmZGViY2FkMzFhNzA4NDcyOTc4MTdhMTQ5ZGFmOTI3ZWRjODU1NDgifX1dLCJwcmVkaWNhdGVUeXBlIjoiaHR0cHM6Ly9zbHNhLmRldi9wcm92ZW5hbmNlL3YxIiwicHJlZGljYXRlIjp7ImJ1aWxkRGVmaW5pdGlvbiI6eyJidWlsZFR5cGUiOiJodHRwczovL3Nsc2EtZnJhbWV3b3JrLmdpdGh1Yi5pby9naXRodWItYWN0aW9ucy1idWlsZHR5cGVzL3dvcmtmbG93L3YxIiwiZXh0ZXJuYWxQYXJhbWV0ZXJzIjp7IndvcmtmbG93Ijp7InJlZiI6InJlZnMvaGVhZHMvdHJ1bmsiLCJyZXBvc2l0b3J5IjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkiLCJwYXRoIjoiLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWwifX0sImludGVybmFsUGFyYW1ldGVycyI6eyJnaXRodWIiOnsiZXZlbnRfbmFtZSI6IndvcmtmbG93X2Rpc3BhdGNoIiwicmVwb3NpdG9yeV9pZCI6IjIxMjYxMzA0OSIsInJlcG9zaXRvcnlfb3duZXJfaWQiOiI1OTcwNDcxMSJ9fSwicmVzb2x2ZWREZXBlbmRlbmNpZXMiOlt7InVyaSI6ImdpdCtodHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaUByZWZzL2hlYWRzL3RydW5rIiwiZGlnZXN0Ijp7ImdpdENvbW1pdCI6ImZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAifX1dfSwicnVuRGV0YWlscyI6eyJidWlsZGVyIjp7ImlkIjoiaHR0cHM6Ly9naXRodWIuY29tL2FjdGlvbnMvcnVubmVyL2dpdGh1Yi1ob3N0ZWQifSwibWV0YWRhdGEiOnsiaW52b2NhdGlvbklkIjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvYWN0aW9ucy9ydW5zLzkyODkwNzU3NTIvYXR0ZW1wdHMvMSJ9fX19","payloadType":"application/vnd.in-toto+json","signatures":[{"sig":"MEQCIEGIGAm7gZVLLpsrPcjndEjiuctE2/c9+j9KGvazz3rlAiAd6O16T5hkzRM3IbRPzm+xT40mNQZxefd7laDP6x2XLQ=="}]}}}}'

response

Status: 201
{
  "id": 2
}
List attestations

List a collection of artifact attestations with a given subject digest that are associated with a repository.

The authenticated user making the request must have read access to the repository. In addition, when using a fine-grained access token the attestations:read permission is required.

Please note: in order to offer meaningful security benefits, an attestation's signature and timestamps must be cryptographically verified, and the identity of the attestation signer must be validated. Attestations can be verified using the GitHub CLI attestation verify command. For more information, see our guide on how to use artifact attestations to establish a build's provenance.
Fine-grained access tokens for "List attestations"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Attestations" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List attestations"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
subject_digest string Required

The parameter should be set to the attestation's subject's SHA256 digest, in the form sha256:HEX_DIGEST.
Query parameters
Name, Type, Description
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
before string

A cursor, as given in the Link header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
after string

A cursor, as given in the Link header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
predicate_type string

Optional filter for fetching attestations with a given predicate type. This option accepts provenance, sbom, release, or freeform text for custom predicate types.
HTTP response status codes for "List attestations"
Status code	Description
200	

OK
Code samples for "List attestations"
Request example
get/repos/{owner}/{repo}/attestations/{subject_digest}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/attestations/SUBJECT_DIGEST

Response

Status: 200
{
  "attestations": [
    {
      "bundle": {
        "mediaType": "application/vnd.dev.sigstore.bundle.v0.3+json",
        "verificationMaterial": {
          "tlogEntries": [
            {
              "logIndex": "97913980",
              "logId": {
                "keyId": "wNI9atQGlz+VWfO6LRygH4QUfY/8W4RFwiT5i5WRgB0="
              },
              "kindVersion": {
                "kind": "dsse",
                "version": "0.0.1"
              },
              "integratedTime": "1716998992",
              "inclusionPromise": {
                "signedEntryTimestamp": "MEYCIQCeEsQAy+qXtULkh52wbnHrkt2R2JQ05P9STK/xmdpQ2AIhANiG5Gw6cQiMnwvUz1+9UKtG/vlC8dduq07wsFOViwSL"
              },
              "inclusionProof": {
                "logIndex": "93750549",
                "rootHash": "KgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=",
                "treeSize": "93750551",
                "hashes": [
                  "8LI21mzwxnUSo0fuZeFsUrz2ujZ4QAL+oGeTG+5toZg=",
                  "nCb369rcIytNhGwWoqBv+eV49X3ZKpo/HJGKm9V+dck=",
                  "hnNQ9mUdSwYCfdV21pd87NucrdRRNZATowlaRR1hJ4A=",
                  "MBhhK33vlD4Tq/JKgAaXUI4VjmosWKe6+7RNpQ2ncNM=",
                  "XKWUE3stvGV1OHsIGiCGfn047Ok6uD4mFkh7BaicaEc=",
                  "Tgve40VPFfuei+0nhupdGpfPPR+hPpZjxgTiDT8WNoY=",
                  "wV+S/7tLtYGzkLaSb6UDqexNyhMvumHK/RpTNvEZuLU=",
                  "uwaWufty6sn6XqO1Tb9M3Vz6sBKPu0HT36mStxJNd7s=",
                  "jUfeMOXQP0XF1JAnCEETVbfRKMUwCzrVUzYi8vnDMVs=",
                  "xQKjzJAwwdlQG/YUYBKPXxbCmhMYKo1wnv+6vDuKWhQ=",
                  "cX3Agx+hP66t1ZLbX/yHbfjU46/3m/VAmWyG/fhxAVc=",
                  "sjohk/3DQIfXTgf/5XpwtdF7yNbrf8YykOMHr1CyBYQ=",
                  "98enzMaC+x5oCMvIZQA5z8vu2apDMCFvE/935NfuPw8="
                ],
                "checkpoint": {
                  "envelope": "rekor.sigstore.dev - 2605736670972794746\\n93750551\\nKgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=\\n\\n— rekor.sigstore.dev wNI9ajBEAiBkLzdjY8A9HReU7rmtjwZ+JpSuYtEr9SmvSwUIW7FBjgIgKo+vhkW3tqc+gc8fw9gza3xLoncA8a+MTaJYCaLGA9c=\\n"
                }
              },
              "canonicalizedBody": "eyJhcGlWZXJzaW9uIjoiMC4wLjEiLCJraW5kIjoiZHNzZSIsInNwZWMiOnsiZW52ZWxvcGVIYXNoIjp7ImFsZ29yaXRobSI6InNoYTI1NiIsInZhbHVlIjoiM2I1YzkwNDk5MGFiYzE4NjI1ZWE3Njg4MzE1OGEwZmI4MTEwMjM4MGJkNjQwZjI5OWJlMzYwZWVkOTMxNjYwYiJ9LCJwYXlsb2FkSGFzaCI6eyJhbGdvcml0aG0iOiJzaGEyNTYiLCJ2YWx1ZSI6IjM4ZGNlZDJjMzE1MGU2OTQxMDViYjZiNDNjYjY3NzBiZTYzZDdhNGM4NjNiMTc2YTkwMmU1MGQ5ZTAyN2ZiMjMifSwic2lnbmF0dXJlcyI6W3sic2lnbmF0dXJlIjoiTUVRQ0lFR0lHQW03Z1pWTExwc3JQY2puZEVqaXVjdEUyL2M5K2o5S0d2YXp6M3JsQWlBZDZPMTZUNWhrelJNM0liUlB6bSt4VDQwbU5RWnhlZmQ3bGFEUDZ4MlhMUT09IiwidmVyaWZpZXIiOiJMUzB0TFMxQ1JVZEpUaUJEUlZKVVNVWkpRMEZVUlMwdExTMHRDazFKU1VkcVZFTkRRbWhUWjBGM1NVSkJaMGxWVjFsNGNVdHpjazFUTTFOMmJEVkphalZQUkdaQ1owMUtUeTlKZDBObldVbExiMXBKZW1vd1JVRjNUWGNLVG5wRlZrMUNUVWRCTVZWRlEyaE5UV015Ykc1ak0xSjJZMjFWZFZwSFZqSk5ValIzU0VGWlJGWlJVVVJGZUZaNllWZGtlbVJIT1hsYVV6RndZbTVTYkFwamJURnNXa2RzYUdSSFZYZElhR05PVFdwUmQwNVVTVFZOVkZsM1QxUlZlVmRvWTA1TmFsRjNUbFJKTlUxVVdYaFBWRlY1VjJwQlFVMUdhM2RGZDFsSUNrdHZXa2w2YWpCRFFWRlpTVXR2V2tsNmFqQkVRVkZqUkZGblFVVmtiV2RvVGs1M00yNVZMMHQxWlZGbmMzQkhTRmMzWjJnNVdFeEVMMWRrU1RoWlRVSUtLekJ3TUZZMGJ6RnJTRzgyWTAweGMwUktaM0pEWjFCUlZYcDRjSFZaZFc4cmVIZFFTSGxzTDJ0RWVXWXpSVXhxYTJGUFEwSlVUWGRuWjFWMlRVRTBSd3BCTVZWa1JIZEZRaTkzVVVWQmQwbElaMFJCVkVKblRsWklVMVZGUkVSQlMwSm5aM0pDWjBWR1FsRmpSRUY2UVdSQ1owNVdTRkUwUlVablVWVnhaa05RQ25aWVMwRjJVelJEWkdoUk1taGlXbGRLVTA5RmRsWnZkMGgzV1VSV1VqQnFRa0puZDBadlFWVXpPVkJ3ZWpGWmEwVmFZalZ4VG1wd1MwWlhhWGhwTkZrS1drUTRkMWRuV1VSV1VqQlNRVkZJTDBKR1FYZFViMXBOWVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREpPYzJGVE9XcGlSMnQyVEcxa2NBcGtSMmd4V1drNU0ySXpTbkphYlhoMlpETk5kbHBIVm5kaVJ6azFZbGRXZFdSRE5UVmlWM2hCWTIxV2JXTjVPVzlhVjBaclkzazVNR051Vm5WaGVrRTFDa0puYjNKQ1owVkZRVmxQTDAxQlJVSkNRM1J2WkVoU2QyTjZiM1pNTTFKMllUSldkVXh0Um1wa1IyeDJZbTVOZFZveWJEQmhTRlpwWkZoT2JHTnRUbllLWW01U2JHSnVVWFZaTWpsMFRVSTRSME5wYzBkQlVWRkNaemM0ZDBGUlNVVkZXR1IyWTIxMGJXSkhPVE5ZTWxKd1l6TkNhR1JIVG05TlJGbEhRMmx6UndwQlVWRkNaemM0ZDBGUlRVVkxSMXBvV2xkWmVWcEhVbXRQUkVacFRVUmplazVxWXpCUFJGRjRUVEpGTTFsNldUQk9iVTVyVFVkS2JWbDZTVEpaZWtGM0NsbFVRWGRIUVZsTFMzZFpRa0pCUjBSMmVrRkNRa0ZSUzFKSFZuZGlSemsxWWxkV2RXUkVRVlpDWjI5eVFtZEZSVUZaVHk5TlFVVkdRa0ZrYW1KSGEzWUtXVEo0Y0UxQ05FZERhWE5IUVZGUlFtYzNPSGRCVVZsRlJVaEtiRnB1VFhaaFIxWm9Xa2hOZG1SSVNqRmliWE4zVDNkWlMwdDNXVUpDUVVkRWRucEJRZ3BEUVZGMFJFTjBiMlJJVW5kamVtOTJURE5TZG1FeVZuVk1iVVpxWkVkc2RtSnVUWFZhTW13d1lVaFdhV1JZVG14amJVNTJZbTVTYkdKdVVYVlpNamwwQ2sxR2QwZERhWE5IUVZGUlFtYzNPSGRCVVd0RlZHZDRUV0ZJVWpCalNFMDJUSGs1Ym1GWVVtOWtWMGwxV1RJNWRFd3lUbk5oVXpscVlrZHJka3h0WkhBS1pFZG9NVmxwT1ROaU0wcHlXbTE0ZG1RelRYWmFSMVozWWtjNU5XSlhWblZrUXpVMVlsZDRRV050Vm0xamVUbHZXbGRHYTJONU9UQmpibFoxWVhwQk5BcENaMjl5UW1kRlJVRlpUeTlOUVVWTFFrTnZUVXRIV21oYVYxbDVXa2RTYTA5RVJtbE5SR042VG1wak1FOUVVWGhOTWtVeldYcFpNRTV0VG10TlIwcHRDbGw2U1RKWmVrRjNXVlJCZDBoUldVdExkMWxDUWtGSFJIWjZRVUpEZDFGUVJFRXhibUZZVW05a1YwbDBZVWM1ZW1SSFZtdE5RMjlIUTJselIwRlJVVUlLWnpjNGQwRlJkMFZJUVhkaFlVaFNNR05JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKT2MyRlRPV3BpUjJ0M1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWdwRVVWRnhSRU5vYlZsWFZtMU5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBGSENrTnBjMGRCVVZGQ1p6YzRkMEZSTkVWRlozZFJZMjFXYldONU9XOWFWMFpyWTNrNU1HTnVWblZoZWtGYVFtZHZja0puUlVWQldVOHZUVUZGVUVKQmMwMEtRMVJKZUUxcVdYaE5la0V3VDFSQmJVSm5iM0pDWjBWRlFWbFBMMDFCUlZGQ1FtZE5SbTFvTUdSSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhZ3BpUjJ0M1IwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWUlVVdEVRV2N4VDFSamQwNUVZM2hOVkVKalFtZHZja0puUlVWQldVOHZUVUZGVTBKRk5FMVVSMmd3Q21SSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhbUpIYTNaWk1uaHdUSGsxYm1GWVVtOWtWMGwyWkRJNWVXRXlXbk5pTTJSNlRESlNiR05IZUhZS1pWY3hiR0p1VVhWbFZ6RnpVVWhLYkZwdVRYWmhSMVpvV2toTmRtUklTakZpYlhOM1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWM1VYRkVRMmh0V1ZkV2JRcE5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBWSFEybHpSMEZSVVVKbk56aDNDa0ZTVVVWRmQzZFNaREk1ZVdFeVduTmlNMlJtV2tkc2VtTkhSakJaTW1kM1ZGRlpTMHQzV1VKQ1FVZEVkbnBCUWtaUlVTOUVSREZ2WkVoU2QyTjZiM1lLVERKa2NHUkhhREZaYVRWcVlqSXdkbGt5ZUhCTU1rNXpZVk01YUZrelVuQmlNalY2VEROS01XSnVUWFpQVkVrMFQxUkJNMDVVWXpGTmFUbG9aRWhTYkFwaVdFSXdZM2s0ZUUxQ1dVZERhWE5IUVZGUlFtYzNPSGRCVWxsRlEwRjNSMk5JVm1saVIyeHFUVWxIVEVKbmIzSkNaMFZGUVdSYU5VRm5VVU5DU0RCRkNtVjNRalZCU0dOQk0xUXdkMkZ6WWtoRlZFcHFSMUkwWTIxWFl6TkJjVXBMV0hKcVpWQkxNeTlvTkhCNVowTTRjRGR2TkVGQlFVZFFlRkl4ZW1KblFVRUtRa0ZOUVZORVFrZEJhVVZCS3pobmJGRkplRTlCYUZoQ1FVOVRObE1yT0ZweGQwcGpaSGQzVTNJdlZGZHBhSE16WkV4eFZrRjJiME5KVVVSaWVUbG9NUXBKWTNWRVJYSXJlbk5YYVV3NFVIYzFRMU5VZEd0c2RFbzBNakZ6UlRneFZuWjFOa0Z3VkVGTFFtZG5jV2hyYWs5UVVWRkVRWGRPYmtGRVFtdEJha0VyQ2tSSU4xQXJhR2cwVmtoWFprTlhXSFJ5UzFSdlFrdDFZa0pyUzNCbVYwTlpVWGhxV0UweWRsWXZibEJ4WWxwR1dVOVdXazlpWlRaQlRuSm5lV1J2V1VNS1RVWlZUV0l6ZUhwelJrNVJXWFp6UlZsUGFUSkxibkoyUmpCMFoyOXdiVmhIVm05NmJsb3JjUzh5UVVsRVZ6bEdNVVUzV1RaWk1EWXhaVzkxUVZsa1NBcFhkejA5Q2kwdExTMHRSVTVFSUVORlVsUkpSa2xEUVZSRkxTMHRMUzBLIn1dfX0="
            }
          ],
          "timestampVerificationData": {},
          "certificate": {
            "rawBytes": "MIIGjTCCBhSgAwIBAgIUWYxqKsrMS3Svl5Ij5ODfBgMJO/IwCgYIKoZIzj0EAwMwNzEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MR4wHAYDVQQDExVzaWdzdG9yZS1pbnRlcm1lZGlhdGUwHhcNMjQwNTI5MTYwOTUyWhcNMjQwNTI5MTYxOTUyWjAAMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdmghNNw3nU/KueQgspGHW7gh9XLD/WdI8YMB+0p0V4o1kHo6cM1sDJgrCgPQUzxpuYuo+xwPHyl/kDyf3ELjkaOCBTMwggUvMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDAzAdBgNVHQ4EFgQUqfCPvXKAvS4CdhQ2hbZWJSOEvVowHwYDVR0jBBgwFoAU39Ppz1YkEZb5qNjpKFWixi4YZD8wWgYDVR0RAQH/BFAwToZMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA5BgorBgEEAYO/MAEBBCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMB8GCisGAQQBg78wAQIEEXdvcmtmbG93X2Rpc3BhdGNoMDYGCisGAQQBg78wAQMEKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwGAYKKwYBBAGDvzABBAQKRGVwbG95bWVudDAVBgorBgEEAYO/MAEFBAdjbGkvY2xpMB4GCisGAQQBg78wAQYEEHJlZnMvaGVhZHMvdHJ1bmswOwYKKwYBBAGDvzABCAQtDCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMFwGCisGAQQBg78wAQkETgxMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA4BgorBgEEAYO/MAEKBCoMKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwHQYKKwYBBAGDvzABCwQPDA1naXRodWItaG9zdGVkMCoGCisGAQQBg78wAQwEHAwaaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkwOAYKKwYBBAGDvzABDQQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCAGCisGAQQBg78wAQ4EEgwQcmVmcy9oZWFkcy90cnVuazAZBgorBgEEAYO/MAEPBAsMCTIxMjYxMzA0OTAmBgorBgEEAYO/MAEQBBgMFmh0dHBzOi8vZ2l0aHViLmNvbS9jbGkwGAYKKwYBBAGDvzABEQQKDAg1OTcwNDcxMTBcBgorBgEEAYO/MAESBE4MTGh0dHBzOi8vZ2l0aHViLmNvbS9jbGkvY2xpLy5naXRodWIvd29ya2Zsb3dzL2RlcGxveW1lbnQueW1sQHJlZnMvaGVhZHMvdHJ1bmswOAYKKwYBBAGDvzABEwQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCEGCisGAQQBg78wARQEEwwRd29ya2Zsb3dfZGlzcGF0Y2gwTQYKKwYBBAGDvzABFQQ/DD1odHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaS9hY3Rpb25zL3J1bnMvOTI4OTA3NTc1Mi9hdHRlbXB0cy8xMBYGCisGAQQBg78wARYECAwGcHVibGljMIGLBgorBgEEAdZ5AgQCBH0EewB5AHcA3T0wasbHETJjGR4cmWc3AqJKXrjePK3/h4pygC8p7o4AAAGPxR1zbgAABAMASDBGAiEA+8glQIxOAhXBAOS6S+8ZqwJcdwwSr/TWihs3dLqVAvoCIQDby9h1IcuDEr+zsWiL8Pw5CSTtkltJ421sE81Vvu6ApTAKBggqhkjOPQQDAwNnADBkAjA+DH7P+hh4VHWfCWXtrKToBKubBkKpfWCYQxjXM2vV/nPqbZFYOVZObe6ANrgydoYCMFUMb3xzsFNQYvsEYOi2KnrvF0tgopmXGVoznZ+q/2AIDW9F1E7Y6Y061eouAYdHWw=="
          }
        },
        "dsseEnvelope": {
          "payload": "eyJfdHlwZSI6Imh0dHBzOi8vaW4tdG90by5pby9TdGF0ZW1lbnQvdjEiLCJzdWJqZWN0IjpbeyJuYW1lIjoiZ2hfMi41MC4wX3dpbmRvd3NfYXJtNjQuemlwIiwiZGlnZXN0Ijp7InNoYTI1NiI6IjhhYWQxMjBiNDE2Mzg2YjQyNjllZjYyYzhmZGViY2FkMzFhNzA4NDcyOTc4MTdhMTQ5ZGFmOTI3ZWRjODU1NDgifX1dLCJwcmVkaWNhdGVUeXBlIjoiaHR0cHM6Ly9zbHNhLmRldi9wcm92ZW5hbmNlL3YxIiwicHJlZGljYXRlIjp7ImJ1aWxkRGVmaW5pdGlvbiI6eyJidWlsZFR5cGUiOiJodHRwczovL3Nsc2EtZnJhbWV3b3JrLmdpdGh1Yi5pby9naXRodWItYWN0aW9ucy1idWlsZHR5cGVzL3dvcmtmbG93L3YxIiwiZXh0ZXJuYWxQYXJhbWV0ZXJzIjp7IndvcmtmbG93Ijp7InJlZiI6InJlZnMvaGVhZHMvdHJ1bmsiLCJyZXBvc2l0b3J5IjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkiLCJwYXRoIjoiLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWwifX0sImludGVybmFsUGFyYW1ldGVycyI6eyJnaXRodWIiOnsiZXZlbnRfbmFtZSI6IndvcmtmbG93X2Rpc3BhdGNoIiwicmVwb3NpdG9yeV9pZCI6IjIxMjYxMzA0OSIsInJlcG9zaXRvcnlfb3duZXJfaWQiOiI1OTcwNDcxMSJ9fSwicmVzb2x2ZWREZXBlbmRlbmNpZXMiOlt7InVyaSI6ImdpdCtodHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaUByZWZzL2hlYWRzL3RydW5rIiwiZGlnZXN0Ijp7ImdpdENvbW1pdCI6ImZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAifX1dfSwicnVuRGV0YWlscyI6eyJidWlsZGVyIjp7ImlkIjoiaHR0cHM6Ly9naXRodWIuY29tL2FjdGlvbnMvcnVubmVyL2dpdGh1Yi1ob3N0ZWQifSwibWV0YWRhdGEiOnsiaW52b2NhdGlvbklkIjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvYWN0aW9ucy9ydW5zLzkyODkwNzU3NTIvYXR0ZW1wdHMvMSJ9fX19",
          "payloadType": "application/vnd.in-toto+json",
          "signatures": [
            {
              "sig": "MEQCIEGIGAm7gZVLLpsrPcjndEjiuctE2/c9+j9KGvazz3rlAiAd6O16T5hkzRM3IbRPzm+xT40mNQZxefd7laDP6x2XLQ=="
            }
          ]
        }
      },
      "repository_id": 1
    },
    {
      "bundle": {
        "mediaType": "application/vnd.dev.sigstore.bundle.v0.3+json",
        "verificationMaterial": {
          "tlogEntries": [
            {
              "logIndex": "97913980",
              "logId": {
                "keyId": "wNI9atQGlz+VWfO6LRygH4QUfY/8W4RFwiT5i5WRgB0="
              },
              "kindVersion": {
                "kind": "dsse",
                "version": "0.0.1"
              },
              "integratedTime": "1716998992",
              "inclusionPromise": {
                "signedEntryTimestamp": "MEYCIQCeEsQAy+qXtULkh52wbnHrkt2R2JQ05P9STK/xmdpQ2AIhANiG5Gw6cQiMnwvUz1+9UKtG/vlC8dduq07wsFOViwSL"
              },
              "inclusionProof": {
                "logIndex": "93750549",
                "rootHash": "KgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=",
                "treeSize": "93750551",
                "hashes": [
                  "8LI21mzwxnUSo0fuZeFsUrz2ujZ4QAL+oGeTG+5toZg=",
                  "nCb369rcIytNhGwWoqBv+eV49X3ZKpo/HJGKm9V+dck=",
                  "hnNQ9mUdSwYCfdV21pd87NucrdRRNZATowlaRR1hJ4A=",
                  "MBhhK33vlD4Tq/JKgAaXUI4VjmosWKe6+7RNpQ2ncNM=",
                  "XKWUE3stvGV1OHsIGiCGfn047Ok6uD4mFkh7BaicaEc=",
                  "Tgve40VPFfuei+0nhupdGpfPPR+hPpZjxgTiDT8WNoY=",
                  "wV+S/7tLtYGzkLaSb6UDqexNyhMvumHK/RpTNvEZuLU=",
                  "uwaWufty6sn6XqO1Tb9M3Vz6sBKPu0HT36mStxJNd7s=",
                  "jUfeMOXQP0XF1JAnCEETVbfRKMUwCzrVUzYi8vnDMVs=",
                  "xQKjzJAwwdlQG/YUYBKPXxbCmhMYKo1wnv+6vDuKWhQ=",
                  "cX3Agx+hP66t1ZLbX/yHbfjU46/3m/VAmWyG/fhxAVc=",
                  "sjohk/3DQIfXTgf/5XpwtdF7yNbrf8YykOMHr1CyBYQ=",
                  "98enzMaC+x5oCMvIZQA5z8vu2apDMCFvE/935NfuPw8="
                ],
                "checkpoint": {
                  "envelope": "rekor.sigstore.dev - 2605736670972794746\\n93750551\\nKgKiXoOl8rM5d4y6Xlbm2QLftvj/FYvTs6z7dJlNO60=\\n\\n— rekor.sigstore.dev wNI9ajBEAiBkLzdjY8A9HReU7rmtjwZ+JpSuYtEr9SmvSwUIW7FBjgIgKo+vhkW3tqc+gc8fw9gza3xLoncA8a+MTaJYCaLGA9c=\\n"
                }
              },
              "canonicalizedBody": "eyJhcGlWZXJzaW9uIjoiMC4wLjEiLCJraW5kIjoiZHNzZSIsInNwZWMiOnsiZW52ZWxvcGVIYXNoIjp7ImFsZ29yaXRobSI6InNoYTI1NiIsInZhbHVlIjoiM2I1YzkwNDk5MGFiYzE4NjI1ZWE3Njg4MzE1OGEwZmI4MTEwMjM4MGJkNjQwZjI5OWJlMzYwZWVkOTMxNjYwYiJ9LCJwYXlsb2FkSGFzaCI6eyJhbGdvcml0aG0iOiJzaGEyNTYiLCJ2YWx1ZSI6IjM4ZGNlZDJjMzE1MGU2OTQxMDViYjZiNDNjYjY3NzBiZTYzZDdhNGM4NjNiMTc2YTkwMmU1MGQ5ZTAyN2ZiMjMifSwic2lnbmF0dXJlcyI6W3sic2lnbmF0dXJlIjoiTUVRQ0lFR0lHQW03Z1pWTExwc3JQY2puZEVqaXVjdEUyL2M5K2o5S0d2YXp6M3JsQWlBZDZPMTZUNWhrelJNM0liUlB6bSt4VDQwbU5RWnhlZmQ3bGFEUDZ4MlhMUT09IiwidmVyaWZpZXIiOiJMUzB0TFMxQ1JVZEpUaUJEUlZKVVNVWkpRMEZVUlMwdExTMHRDazFKU1VkcVZFTkRRbWhUWjBGM1NVSkJaMGxWVjFsNGNVdHpjazFUTTFOMmJEVkphalZQUkdaQ1owMUtUeTlKZDBObldVbExiMXBKZW1vd1JVRjNUWGNLVG5wRlZrMUNUVWRCTVZWRlEyaE5UV015Ykc1ak0xSjJZMjFWZFZwSFZqSk5ValIzU0VGWlJGWlJVVVJGZUZaNllWZGtlbVJIT1hsYVV6RndZbTVTYkFwamJURnNXa2RzYUdSSFZYZElhR05PVFdwUmQwNVVTVFZOVkZsM1QxUlZlVmRvWTA1TmFsRjNUbFJKTlUxVVdYaFBWRlY1VjJwQlFVMUdhM2RGZDFsSUNrdHZXa2w2YWpCRFFWRlpTVXR2V2tsNmFqQkVRVkZqUkZGblFVVmtiV2RvVGs1M00yNVZMMHQxWlZGbmMzQkhTRmMzWjJnNVdFeEVMMWRrU1RoWlRVSUtLekJ3TUZZMGJ6RnJTRzgyWTAweGMwUktaM0pEWjFCUlZYcDRjSFZaZFc4cmVIZFFTSGxzTDJ0RWVXWXpSVXhxYTJGUFEwSlVUWGRuWjFWMlRVRTBSd3BCTVZWa1JIZEZRaTkzVVVWQmQwbElaMFJCVkVKblRsWklVMVZGUkVSQlMwSm5aM0pDWjBWR1FsRmpSRUY2UVdSQ1owNVdTRkUwUlVablVWVnhaa05RQ25aWVMwRjJVelJEWkdoUk1taGlXbGRLVTA5RmRsWnZkMGgzV1VSV1VqQnFRa0puZDBadlFWVXpPVkJ3ZWpGWmEwVmFZalZ4VG1wd1MwWlhhWGhwTkZrS1drUTRkMWRuV1VSV1VqQlNRVkZJTDBKR1FYZFViMXBOWVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREpPYzJGVE9XcGlSMnQyVEcxa2NBcGtSMmd4V1drNU0ySXpTbkphYlhoMlpETk5kbHBIVm5kaVJ6azFZbGRXZFdSRE5UVmlWM2hCWTIxV2JXTjVPVzlhVjBaclkzazVNR051Vm5WaGVrRTFDa0puYjNKQ1owVkZRVmxQTDAxQlJVSkNRM1J2WkVoU2QyTjZiM1pNTTFKMllUSldkVXh0Um1wa1IyeDJZbTVOZFZveWJEQmhTRlpwWkZoT2JHTnRUbllLWW01U2JHSnVVWFZaTWpsMFRVSTRSME5wYzBkQlVWRkNaemM0ZDBGUlNVVkZXR1IyWTIxMGJXSkhPVE5ZTWxKd1l6TkNhR1JIVG05TlJGbEhRMmx6UndwQlVWRkNaemM0ZDBGUlRVVkxSMXBvV2xkWmVWcEhVbXRQUkVacFRVUmplazVxWXpCUFJGRjRUVEpGTTFsNldUQk9iVTVyVFVkS2JWbDZTVEpaZWtGM0NsbFVRWGRIUVZsTFMzZFpRa0pCUjBSMmVrRkNRa0ZSUzFKSFZuZGlSemsxWWxkV2RXUkVRVlpDWjI5eVFtZEZSVUZaVHk5TlFVVkdRa0ZrYW1KSGEzWUtXVEo0Y0UxQ05FZERhWE5IUVZGUlFtYzNPSGRCVVZsRlJVaEtiRnB1VFhaaFIxWm9Xa2hOZG1SSVNqRmliWE4zVDNkWlMwdDNXVUpDUVVkRWRucEJRZ3BEUVZGMFJFTjBiMlJJVW5kamVtOTJURE5TZG1FeVZuVk1iVVpxWkVkc2RtSnVUWFZhTW13d1lVaFdhV1JZVG14amJVNTJZbTVTYkdKdVVYVlpNamwwQ2sxR2QwZERhWE5IUVZGUlFtYzNPSGRCVVd0RlZHZDRUV0ZJVWpCalNFMDJUSGs1Ym1GWVVtOWtWMGwxV1RJNWRFd3lUbk5oVXpscVlrZHJka3h0WkhBS1pFZG9NVmxwT1ROaU0wcHlXbTE0ZG1RelRYWmFSMVozWWtjNU5XSlhWblZrUXpVMVlsZDRRV050Vm0xamVUbHZXbGRHYTJONU9UQmpibFoxWVhwQk5BcENaMjl5UW1kRlJVRlpUeTlOUVVWTFFrTnZUVXRIV21oYVYxbDVXa2RTYTA5RVJtbE5SR042VG1wak1FOUVVWGhOTWtVeldYcFpNRTV0VG10TlIwcHRDbGw2U1RKWmVrRjNXVlJCZDBoUldVdExkMWxDUWtGSFJIWjZRVUpEZDFGUVJFRXhibUZZVW05a1YwbDBZVWM1ZW1SSFZtdE5RMjlIUTJselIwRlJVVUlLWnpjNGQwRlJkMFZJUVhkaFlVaFNNR05JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKT2MyRlRPV3BpUjJ0M1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWdwRVVWRnhSRU5vYlZsWFZtMU5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBGSENrTnBjMGRCVVZGQ1p6YzRkMEZSTkVWRlozZFJZMjFXYldONU9XOWFWMFpyWTNrNU1HTnVWblZoZWtGYVFtZHZja0puUlVWQldVOHZUVUZGVUVKQmMwMEtRMVJKZUUxcVdYaE5la0V3VDFSQmJVSm5iM0pDWjBWRlFWbFBMMDFCUlZGQ1FtZE5SbTFvTUdSSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhZ3BpUjJ0M1IwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWUlVVdEVRV2N4VDFSamQwNUVZM2hOVkVKalFtZHZja0puUlVWQldVOHZUVUZGVTBKRk5FMVVSMmd3Q21SSVFucFBhVGgyV2pKc01HRklWbWxNYlU1MllsTTVhbUpIYTNaWk1uaHdUSGsxYm1GWVVtOWtWMGwyWkRJNWVXRXlXbk5pTTJSNlRESlNiR05IZUhZS1pWY3hiR0p1VVhWbFZ6RnpVVWhLYkZwdVRYWmhSMVpvV2toTmRtUklTakZpYlhOM1QwRlpTMHQzV1VKQ1FVZEVkbnBCUWtWM1VYRkVRMmh0V1ZkV2JRcE5iVkpyV2tSbmVGbHFRVE5OZWxrelRrUm5NRTFVVG1oT01rMHlUa1JhYWxwRVFtbGFiVTE1VG0xTmQwMUhSWGROUTBWSFEybHpSMEZSVVVKbk56aDNDa0ZTVVVWRmQzZFNaREk1ZVdFeVduTmlNMlJtV2tkc2VtTkhSakJaTW1kM1ZGRlpTMHQzV1VKQ1FVZEVkbnBCUWtaUlVTOUVSREZ2WkVoU2QyTjZiM1lLVERKa2NHUkhhREZaYVRWcVlqSXdkbGt5ZUhCTU1rNXpZVk01YUZrelVuQmlNalY2VEROS01XSnVUWFpQVkVrMFQxUkJNMDVVWXpGTmFUbG9aRWhTYkFwaVdFSXdZM2s0ZUUxQ1dVZERhWE5IUVZGUlFtYzNPSGRCVWxsRlEwRjNSMk5JVm1saVIyeHFUVWxIVEVKbmIzSkNaMFZGUVdSYU5VRm5VVU5DU0RCRkNtVjNRalZCU0dOQk0xUXdkMkZ6WWtoRlZFcHFSMUkwWTIxWFl6TkJjVXBMV0hKcVpWQkxNeTlvTkhCNVowTTRjRGR2TkVGQlFVZFFlRkl4ZW1KblFVRUtRa0ZOUVZORVFrZEJhVVZCS3pobmJGRkplRTlCYUZoQ1FVOVRObE1yT0ZweGQwcGpaSGQzVTNJdlZGZHBhSE16WkV4eFZrRjJiME5KVVVSaWVUbG9NUXBKWTNWRVJYSXJlbk5YYVV3NFVIYzFRMU5VZEd0c2RFbzBNakZ6UlRneFZuWjFOa0Z3VkVGTFFtZG5jV2hyYWs5UVVWRkVRWGRPYmtGRVFtdEJha0VyQ2tSSU4xQXJhR2cwVmtoWFprTlhXSFJ5UzFSdlFrdDFZa0pyUzNCbVYwTlpVWGhxV0UweWRsWXZibEJ4WWxwR1dVOVdXazlpWlRaQlRuSm5lV1J2V1VNS1RVWlZUV0l6ZUhwelJrNVJXWFp6UlZsUGFUSkxibkoyUmpCMFoyOXdiVmhIVm05NmJsb3JjUzh5UVVsRVZ6bEdNVVUzV1RaWk1EWXhaVzkxUVZsa1NBcFhkejA5Q2kwdExTMHRSVTVFSUVORlVsUkpSa2xEUVZSRkxTMHRMUzBLIn1dfX0="
            }
          ],
          "timestampVerificationData": {},
          "certificate": {
            "rawBytes": "MIIGjTCCBhSgAwIBAgIUWYxqKsrMS3Svl5Ij5ODfBgMJO/IwCgYIKoZIzj0EAwMwNzEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MR4wHAYDVQQDExVzaWdzdG9yZS1pbnRlcm1lZGlhdGUwHhcNMjQwNTI5MTYwOTUyWhcNMjQwNTI5MTYxOTUyWjAAMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdmghNNw3nU/KueQgspGHW7gh9XLD/WdI8YMB+0p0V4o1kHo6cM1sDJgrCgPQUzxpuYuo+xwPHyl/kDyf3ELjkaOCBTMwggUvMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDAzAdBgNVHQ4EFgQUqfCPvXKAvS4CdhQ2hbZWJSOEvVowHwYDVR0jBBgwFoAU39Ppz1YkEZb5qNjpKFWixi4YZD8wWgYDVR0RAQH/BFAwToZMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA5BgorBgEEAYO/MAEBBCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMB8GCisGAQQBg78wAQIEEXdvcmtmbG93X2Rpc3BhdGNoMDYGCisGAQQBg78wAQMEKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwGAYKKwYBBAGDvzABBAQKRGVwbG95bWVudDAVBgorBgEEAYO/MAEFBAdjbGkvY2xpMB4GCisGAQQBg78wAQYEEHJlZnMvaGVhZHMvdHJ1bmswOwYKKwYBBAGDvzABCAQtDCtodHRwczovL3Rva2VuLmFjdGlvbnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tMFwGCisGAQQBg78wAQkETgxMaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWxAcmVmcy9oZWFkcy90cnVuazA4BgorBgEEAYO/MAEKBCoMKGZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAwHQYKKwYBBAGDvzABCwQPDA1naXRodWItaG9zdGVkMCoGCisGAQQBg78wAQwEHAwaaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkwOAYKKwYBBAGDvzABDQQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCAGCisGAQQBg78wAQ4EEgwQcmVmcy9oZWFkcy90cnVuazAZBgorBgEEAYO/MAEPBAsMCTIxMjYxMzA0OTAmBgorBgEEAYO/MAEQBBgMFmh0dHBzOi8vZ2l0aHViLmNvbS9jbGkwGAYKKwYBBAGDvzABEQQKDAg1OTcwNDcxMTBcBgorBgEEAYO/MAESBE4MTGh0dHBzOi8vZ2l0aHViLmNvbS9jbGkvY2xpLy5naXRodWIvd29ya2Zsb3dzL2RlcGxveW1lbnQueW1sQHJlZnMvaGVhZHMvdHJ1bmswOAYKKwYBBAGDvzABEwQqDChmYWVmMmRkZDgxYjA3MzY3NDg0MTNhN2M2NDZjZDBiZmMyNmMwMGEwMCEGCisGAQQBg78wARQEEwwRd29ya2Zsb3dfZGlzcGF0Y2gwTQYKKwYBBAGDvzABFQQ/DD1odHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaS9hY3Rpb25zL3J1bnMvOTI4OTA3NTc1Mi9hdHRlbXB0cy8xMBYGCisGAQQBg78wARYECAwGcHVibGljMIGLBgorBgEEAdZ5AgQCBH0EewB5AHcA3T0wasbHETJjGR4cmWc3AqJKXrjePK3/h4pygC8p7o4AAAGPxR1zbgAABAMASDBGAiEA+8glQIxOAhXBAOS6S+8ZqwJcdwwSr/TWihs3dLqVAvoCIQDby9h1IcuDEr+zsWiL8Pw5CSTtkltJ421sE81Vvu6ApTAKBggqhkjOPQQDAwNnADBkAjA+DH7P+hh4VHWfCWXtrKToBKubBkKpfWCYQxjXM2vV/nPqbZFYOVZObe6ANrgydoYCMFUMb3xzsFNQYvsEYOi2KnrvF0tgopmXGVoznZ+q/2AIDW9F1E7Y6Y061eouAYdHWw=="
          }
        },
        "dsseEnvelope": {
          "payload": "eyJfdHlwZSI6Imh0dHBzOi8vaW4tdG90by5pby9TdGF0ZW1lbnQvdjEiLCJzdWJqZWN0IjpbeyJuYW1lIjoiZ2hfMi41MC4wX3dpbmRvd3NfYXJtNjQuemlwIiwiZGlnZXN0Ijp7InNoYTI1NiI6IjhhYWQxMjBiNDE2Mzg2YjQyNjllZjYyYzhmZGViY2FkMzFhNzA4NDcyOTc4MTdhMTQ5ZGFmOTI3ZWRjODU1NDgifX1dLCJwcmVkaWNhdGVUeXBlIjoiaHR0cHM6Ly9zbHNhLmRldi9wcm92ZW5hbmNlL3YxIiwicHJlZGljYXRlIjp7ImJ1aWxkRGVmaW5pdGlvbiI6eyJidWlsZFR5cGUiOiJodHRwczovL3Nsc2EtZnJhbWV3b3JrLmdpdGh1Yi5pby9naXRodWItYWN0aW9ucy1idWlsZHR5cGVzL3dvcmtmbG93L3YxIiwiZXh0ZXJuYWxQYXJhbWV0ZXJzIjp7IndvcmtmbG93Ijp7InJlZiI6InJlZnMvaGVhZHMvdHJ1bmsiLCJyZXBvc2l0b3J5IjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkiLCJwYXRoIjoiLmdpdGh1Yi93b3JrZmxvd3MvZGVwbG95bWVudC55bWwifX0sImludGVybmFsUGFyYW1ldGVycyI6eyJnaXRodWIiOnsiZXZlbnRfbmFtZSI6IndvcmtmbG93X2Rpc3BhdGNoIiwicmVwb3NpdG9yeV9pZCI6IjIxMjYxMzA0OSIsInJlcG9zaXRvcnlfb3duZXJfaWQiOiI1OTcwNDcxMSJ9fSwicmVzb2x2ZWREZXBlbmRlbmNpZXMiOlt7InVyaSI6ImdpdCtodHRwczovL2dpdGh1Yi5jb20vY2xpL2NsaUByZWZzL2hlYWRzL3RydW5rIiwiZGlnZXN0Ijp7ImdpdENvbW1pdCI6ImZhZWYyZGRkODFiMDczNjc0ODQxM2E3YzY0NmNkMGJmYzI2YzAwYTAifX1dfSwicnVuRGV0YWlscyI6eyJidWlsZGVyIjp7ImlkIjoiaHR0cHM6Ly9naXRodWIuY29tL2FjdGlvbnMvcnVubmVyL2dpdGh1Yi1ob3N0ZWQifSwibWV0YWRhdGEiOnsiaW52b2NhdGlvbklkIjoiaHR0cHM6Ly9naXRodWIuY29tL2NsaS9jbGkvYWN0aW9ucy9ydW5zLzkyODkwNzU3NTIvYXR0ZW1wdHMvMSJ9fX19",
          "payloadType": "application/vnd.in-toto+json",
          "signatures": [
            {
              "sig": "MEQCIEGIGAm7gZVLLpsrPcjndEjiuctE2/c9+j9KGvazz3rlAiAd6O16T5hkzRM3IbRPzm+xT40mNQZxefd7laDP6x2XLQ=="
            }
          ]
        }
      },
      "repository_id": 1
    }
  ]
}
Check if Dependabot security updates are enabled for a repository

Shows whether Dependabot security updates are enabled, disabled or paused for a repository. The authenticated user must have admin read access to the repository. For more information, see "Configuring Dependabot security updates".
Fine-grained access tokens for "Check if Dependabot security updates are enabled for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "Check if Dependabot security updates are enabled for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Check if Dependabot security updates are enabled for a repository"
Status code	Description
200	

Response if Dependabot is enabled
404	

Not Found if Dependabot is not enabled for the repository
Code samples for "Check if Dependabot security updates are enabled for a repository"
Request example
get/repos/{owner}/{repo}/automated-security-fixes

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/automated-security-fixes

Response if Dependabot is enabled

Status: 200
{
  "enabled": true,
  "paused": false
}
Enable Dependabot security updates

Enables Dependabot security updates for a repository. The authenticated user must have admin access to the repository. For more information, see "Configuring Dependabot security updates".
Fine-grained access tokens for "Enable Dependabot security updates"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Enable Dependabot security updates"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Enable Dependabot security updates"
Status code	Description
204	

No Content
Code samples for "Enable Dependabot security updates"
Request example
put/repos/{owner}/{repo}/automated-security-fixes

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/automated-security-fixes

Response
Status: 204
Disable Dependabot security updates

Disables Dependabot security updates for a repository. The authenticated user must have admin access to the repository. For more information, see "Configuring Dependabot security updates".
Fine-grained access tokens for "Disable Dependabot security updates"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Disable Dependabot security updates"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Disable Dependabot security updates"
Status code	Description
204	

No Content
Code samples for "Disable Dependabot security updates"
Request example
delete/repos/{owner}/{repo}/automated-security-fixes

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/automated-security-fixes

Response
Status: 204
List CODEOWNERS errors

List any syntax errors that are detected in the CODEOWNERS file.

For more information about the correct CODEOWNERS syntax, see "About code owners."
Fine-grained access tokens for "List CODEOWNERS errors"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List CODEOWNERS errors"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
ref string

A branch, tag or commit name used to determine which version of the CODEOWNERS file to use. Default: the repository's default branch (e.g. main)
HTTP response status codes for "List CODEOWNERS errors"
Status code	Description
200	

OK
404	

Resource not found
Code samples for "List CODEOWNERS errors"
Request example
get/repos/{owner}/{repo}/codeowners/errors

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/codeowners/errors

Response

Status: 200
{
  "errors": [
    {
      "line": 3,
      "column": 1,
      "kind": "Invalid pattern",
      "source": "***/*.rb @monalisa",
      "suggestion": "Did you mean `**/*.rb`?",
      "message": "Invalid pattern on line 3: Did you mean `**/*.rb`?\n\n  ***/*.rb @monalisa\n  ^",
      "path": ".github/CODEOWNERS"
    },
    {
      "line": 7,
      "column": 7,
      "kind": "Invalid owner",
      "source": "*.txt docs@",
      "suggestion": null,
      "message": "Invalid owner on line 7:\n\n  *.txt docs@\n        ^",
      "path": ".github/CODEOWNERS"
    }
  ]
}
List repository contributors

Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API caches contributor data to improve performance.

GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.
Fine-grained access tokens for "List repository contributors"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repository contributors"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
anon string

Set to 1 or true to include anonymous contributors in results.
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List repository contributors"
Status code	Description
200	

If repository contains content
204	

Response if repository is empty
403	

Forbidden
404	

Resource not found
Code samples for "List repository contributors"
Request example
get/repos/{owner}/{repo}/contributors

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/contributors

If repository contains content

Status: 200
[
  {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false,
    "contributions": 32
  }
]
Create a repository dispatch event

You can use this endpoint to trigger a webhook event called repository_dispatch when you want activity that happens outside of GitHub to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the repository_dispatch event occurs. For an example repository_dispatch webhook payload, see "RepositoryDispatchEvent."

The client_payload parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the client_payload can include a message that a user would like to send using a GitHub Actions workflow. Or the client_payload can be used as a test to debug your workflow.

This input example shows how you can use the client_payload as a test to debug your workflow.

OAuth app tokens and personal access tokens (classic) need the repo scope to use this endpoint.
Fine-grained access tokens for "Create a repository dispatch event"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Contents" repository permissions (write)

Parameters for "Create a repository dispatch event"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
event_type string Required

A custom webhook event name. Must be 100 characters or fewer.
client_payload object

JSON payload with extra information about the webhook event that your action or workflow may use. The maximum number of top-level properties is 10. The total size of the JSON payload must be less than 64KB.
HTTP response status codes for "Create a repository dispatch event"
Status code	Description
204	

No Content
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create a repository dispatch event"
Request example
post/repos/{owner}/{repo}/dispatches

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/dispatches \
  -d '{"event_type":"on-demand-test","client_payload":{"unit":false,"integration":true}}'

Response
Status: 204
Check if immutable releases are enabled for a repository

Shows whether immutable releases are enabled or disabled. Also identifies whether immutability is being enforced by the repository owner. The authenticated user must have admin read access to the repository.
Fine-grained access tokens for "Check if immutable releases are enabled for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "Check if immutable releases are enabled for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Check if immutable releases are enabled for a repository"
Status code	Description
200	

Response if immutable releases are enabled
404	

Not Found if immutable releases are not enabled for the repository
Code samples for "Check if immutable releases are enabled for a repository"
Request example
get/repos/{owner}/{repo}/immutable-releases

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/immutable-releases

Response if immutable releases are enabled

Status: 200
{
  "enabled": true,
  "enforced_by_owner": false
}
Enable immutable releases

Enables immutable releases for a repository. The authenticated user must have admin access to the repository.
Fine-grained access tokens for "Enable immutable releases"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Enable immutable releases"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Enable immutable releases"
Status code	Description
204	

A header with no content is returned.
409	

Conflict
Code samples for "Enable immutable releases"
Request example
put/repos/{owner}/{repo}/immutable-releases

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/immutable-releases

A header with no content is returned.
Status: 204
Disable immutable releases

Disables immutable releases for a repository. The authenticated user must have admin access to the repository.
Fine-grained access tokens for "Disable immutable releases"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Disable immutable releases"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Disable immutable releases"
Status code	Description
204	

A header with no content is returned.
409	

Conflict
Code samples for "Disable immutable releases"
Request example
delete/repos/{owner}/{repo}/immutable-releases

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/immutable-releases

A header with no content is returned.
Status: 204
List repository languages

Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.
Fine-grained access tokens for "List repository languages"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repository languages"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "List repository languages"
Status code	Description
200	

OK
Code samples for "List repository languages"
Request example
get/repos/{owner}/{repo}/languages

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/languages

Response

Status: 200
{
  "C": 78769,
  "Python": 7769
}
Check if private vulnerability reporting is enabled for a repository

Returns a boolean indicating whether or not private vulnerability reporting is enabled for the repository. For more information, see "Evaluating the security settings of a repository".
Fine-grained access tokens for "Check if private vulnerability reporting is enabled for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Check if private vulnerability reporting is enabled for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Check if private vulnerability reporting is enabled for a repository"
Status code	Description
200	

Private vulnerability reporting status
422	

Bad Request
Code samples for "Check if private vulnerability reporting is enabled for a repository"
Request example
get/repos/{owner}/{repo}/private-vulnerability-reporting

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/private-vulnerability-reporting

Private vulnerability reporting status

Status: 200
{
  "enabled": true
}
Enable private vulnerability reporting for a repository

Enables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "Privately reporting a security vulnerability."
Fine-grained access tokens for "Enable private vulnerability reporting for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Enable private vulnerability reporting for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Enable private vulnerability reporting for a repository"
Status code	Description
204	

A header with no content is returned.
422	

Bad Request
Code samples for "Enable private vulnerability reporting for a repository"
Request example
put/repos/{owner}/{repo}/private-vulnerability-reporting

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/private-vulnerability-reporting

A header with no content is returned.
Status: 204
Disable private vulnerability reporting for a repository

Disables private vulnerability reporting for a repository. The authenticated user must have admin access to the repository. For more information, see "Privately reporting a security vulnerability".
Fine-grained access tokens for "Disable private vulnerability reporting for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Disable private vulnerability reporting for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Disable private vulnerability reporting for a repository"
Status code	Description
204	

A header with no content is returned.
422	

Bad Request
Code samples for "Disable private vulnerability reporting for a repository"
Request example
delete/repos/{owner}/{repo}/private-vulnerability-reporting

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/private-vulnerability-reporting

A header with no content is returned.
Status: 204
List repository tags
Fine-grained access tokens for "List repository tags"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repository tags"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List repository tags"
Status code	Description
200	

OK
Code samples for "List repository tags"
Request example
get/repos/{owner}/{repo}/tags

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/tags

Response

Status: 200
[
  {
    "name": "v0.1",
    "commit": {
      "sha": "c5b97d5ae6c19d5c5df71a34c7fbeeda2479ccbc",
      "url": "https://api.github.com/repos/octocat/Hello-World/commits/c5b97d5ae6c19d5c5df71a34c7fbeeda2479ccbc"
    },
    "zipball_url": "https://github.com/octocat/Hello-World/zipball/v0.1",
    "tarball_url": "https://github.com/octocat/Hello-World/tarball/v0.1",
    "node_id": "MDQ6VXNlcjE="
  }
]
List repository teams

Lists the teams that have access to the specified repository and that are also visible to the authenticated user.

For a public repository, a team is listed only if that team added the public repository explicitly.

OAuth app tokens and personal access tokens (classic) need the public_repo or repo scope to use this endpoint with a public repository, and repo scope to use this endpoint with a private repository.
Fine-grained access tokens for "List repository teams"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "List repository teams"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List repository teams"
Status code	Description
200	

OK
404	

Resource not found
Code samples for "List repository teams"
Request example
get/repos/{owner}/{repo}/teams

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/teams

Response

Status: 200
[
  {
    "id": 1,
    "node_id": "MDQ6VGVhbTE=",
    "url": "https://api.github.com/teams/1",
    "html_url": "https://github.com/orgs/github/teams/justice-league",
    "name": "Justice League",
    "slug": "justice-league",
    "description": "A great team.",
    "privacy": "closed",
    "notification_setting": "notifications_enabled",
    "permission": "admin",
    "members_url": "https://api.github.com/teams/1/members{/member}",
    "repositories_url": "https://api.github.com/teams/1/repos",
    "parent": null
  }
]
Get all repository topics
Fine-grained access tokens for "Get all repository topics"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "Get all repository topics"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Query parameters
Name, Type, Description
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
HTTP response status codes for "Get all repository topics"
Status code	Description
200	

OK
404	

Resource not found
Code samples for "Get all repository topics"
Request example
get/repos/{owner}/{repo}/topics

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/topics

Response

Status: 200
{
  "names": [
    "octocat",
    "atom",
    "electron",
    "api"
  ]
}
Replace all repository topics
Fine-grained access tokens for "Replace all repository topics"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Replace all repository topics"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
names array of strings Required

An array of topics to add to the repository. Pass one or more topics to replace the set of existing topics. Send an empty array ([]) to clear all topics from the repository. Note: Topic names will be saved as lowercase.
HTTP response status codes for "Replace all repository topics"
Status code	Description
200	

OK
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Replace all repository topics"
Request example
put/repos/{owner}/{repo}/topics

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/topics \
  -d '{"names":["octocat","atom","electron","api"]}'

Response

Status: 200
{
  "names": [
    "octocat",
    "atom",
    "electron",
    "api"
  ]
}
Transfer a repository

A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original owner, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see about repository transfers.
Fine-grained access tokens for "Transfer a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Transfer a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
new_owner string Required

The username or organization name the repository will be transferred to.
new_name string

The new name to be given to the repository.
team_ids array of integers

ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories.
HTTP response status codes for "Transfer a repository"
Status code	Description
202	

Accepted
Code samples for "Transfer a repository"
Request example
post/repos/{owner}/{repo}/transfer

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/transfer \
  -d '{"new_owner":"github","team_ids":[12,345],"new_name":"octorepo"}'

Response

Status: 202
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "language": null,
  "forks_count": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "admin": false,
    "push": false,
    "pull": true
  },
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "allow_forking": true,
    "subscribers_count": 42,
    "network_count": 0
  }
}
Check if vulnerability alerts are enabled for a repository

Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin read access to the repository. For more information, see "About security alerts for vulnerable dependencies".
Fine-grained access tokens for "Check if vulnerability alerts are enabled for a repository"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (read)

Parameters for "Check if vulnerability alerts are enabled for a repository"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Check if vulnerability alerts are enabled for a repository"
Status code	Description
204	

Response if repository is enabled with vulnerability alerts
404	

Not Found if repository is not enabled with vulnerability alerts
Code samples for "Check if vulnerability alerts are enabled for a repository"
Request example
get/repos/{owner}/{repo}/vulnerability-alerts

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/vulnerability-alerts

Response if repository is enabled with vulnerability alerts
Status: 204
Enable vulnerability alerts

Enables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "About security alerts for vulnerable dependencies".
Fine-grained access tokens for "Enable vulnerability alerts"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Enable vulnerability alerts"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Enable vulnerability alerts"
Status code	Description
204	

No Content
Code samples for "Enable vulnerability alerts"
Request example
put/repos/{owner}/{repo}/vulnerability-alerts

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/vulnerability-alerts

Response
Status: 204
Disable vulnerability alerts

Disables dependency alerts and the dependency graph for a repository. The authenticated user must have admin access to the repository. For more information, see "About security alerts for vulnerable dependencies".
Fine-grained access tokens for "Disable vulnerability alerts"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Disable vulnerability alerts"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
owner string Required

The account owner of the repository. The name is not case sensitive.
repo string Required

The name of the repository without the .git extension. The name is not case sensitive.
HTTP response status codes for "Disable vulnerability alerts"
Status code	Description
204	

No Content
Code samples for "Disable vulnerability alerts"
Request example
delete/repos/{owner}/{repo}/vulnerability-alerts

curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/vulnerability-alerts

Response
Status: 204
Create a repository using a template

Creates a new repository using a repository template. Use the template_owner and template_repo route parameters to specify the repository to use as the template. If the repository is not public, the authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository's information using the Get a repository endpoint and check that the is_template key is true.

OAuth app tokens and personal access tokens (classic) need the public_repo or repo scope to create a public repository, and repo scope to create a private repository.
Fine-grained access tokens for "Create a repository using a template"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write) and "Contents" repository permissions (read)

Parameters for "Create a repository using a template"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
template_owner string Required

The account owner of the template repository. The name is not case sensitive.
template_repo string Required

The name of the template repository without the .git extension. The name is not case sensitive.
Body parameters
Name, Type, Description
owner string

The organization or person who will own the new repository. To create a new repository in an organization, the authenticated user must be a member of the specified organization.
name string Required

The name of the new repository.
description string

A short description of the new repository.
include_all_branches boolean

Set to true to include the directory structure and files from all branches in the template repository, and not just the default branch. Default: false.

Default: false
private boolean

Either true to create a new private repository or false to create a new public one.

Default: false
HTTP response status codes for "Create a repository using a template"
Status code	Description
201	

Created
Code samples for "Create a repository using a template"
Request example
post/repos/{template_owner}/{template_repo}/generate

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/TEMPLATE_OWNER/TEMPLATE_REPO/generate \
  -d '{"owner":"octocat","name":"Hello-World","description":"This is your first repository","include_all_branches":false,"private":false}'

Response

Status: 201
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "license": {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "spdx_id": "MIT",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "html_url": "https://github.com/licenses/mit"
  },
  "language": null,
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "web_commit_signoff_required": false,
  "subscribers_count": 42,
  "network_count": 0,
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
}
List public repositories

Lists all public repositories in the order that they were created.

Note:

    For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise.
    Pagination is powered exclusively by the since parameter. Use the Link header to get the URL for the next page of repositories.

Fine-grained access tokens for "List public repositories"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List public repositories"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Query parameters
Name, Type, Description
since integer

A repository ID. Only return repositories with an ID greater than this ID.
HTTP response status codes for "List public repositories"
Status code	Description
200	

OK
304	

Not modified
422	

Validation failed, or the endpoint has been spammed.
Code samples for "List public repositories"
Request example
get/repositories

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repositories

Response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  }
]
List repositories for the authenticated user

Lists repositories that the authenticated user has explicit permission (:read, :write, or :admin) to access.

The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.
Fine-grained access tokens for "List repositories for the authenticated user"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repositories for the authenticated user"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Query parameters
Name, Type, Description
visibility string

Limit results to repositories with the specified visibility.

Default: all

Can be one of: all, public, private
affiliation string

Comma-separated list of values. Can include:

    owner: Repositories that are owned by the authenticated user.
    collaborator: Repositories that the user has been added to as a collaborator.
    organization_member: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.

Default: owner,collaborator,organization_member
type string

Limit results to repositories of the specified type. Will cause a 422 error if used in the same request as visibility or affiliation.

Default: all

Can be one of: all, owner, public, private, member
sort string

The property to sort the results by.

Default: full_name

Can be one of: created, updated, pushed, full_name
direction string

The order to sort by. Default: asc when using full_name, otherwise desc.

Can be one of: asc, desc
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
since string

Only show repositories updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
before string

Only show repositories updated before the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
HTTP response status codes for "List repositories for the authenticated user"
Status code	Description
200	

OK
304	

Not modified
401	

Requires authentication
403	

Forbidden
422	

Validation failed, or the endpoint has been spammed.
Code samples for "List repositories for the authenticated user"
Request example
get/user/repos

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos

Default response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "template_repository": null,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
]
Create a repository for the authenticated user

Creates a new repository for the authenticated user.

OAuth app tokens and personal access tokens (classic) need the public_repo or repo scope to create a public repository, and repo scope to create a private repository.
Fine-grained access tokens for "Create a repository for the authenticated user"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Administration" repository permissions (write)

Parameters for "Create a repository for the authenticated user"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Body parameters
Name, Type, Description
name string Required

The name of the repository.
description string

A short description of the repository.
homepage string

A URL with more information about the repository.
private boolean

Whether the repository is private.

Default: false
has_issues boolean

Whether issues are enabled.

Default: true
has_projects boolean

Whether projects are enabled.

Default: true
has_wiki boolean

Whether the wiki is enabled.

Default: true
has_discussions boolean

Whether discussions are enabled.

Default: false
team_id integer

The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.
auto_init boolean

Whether the repository is initialized with a minimal README.

Default: false
gitignore_template string

The desired language or platform to apply to the .gitignore.
license_template string

The license keyword of the open source license for this repository.
allow_squash_merge boolean

Whether to allow squash merges for pull requests.

Default: true
allow_merge_commit boolean

Whether to allow merge commits for pull requests.

Default: true
allow_rebase_merge boolean

Whether to allow rebase merges for pull requests.

Default: true
allow_auto_merge boolean

Whether to allow Auto-merge to be used on pull requests.

Default: false
delete_branch_on_merge boolean

Whether to delete head branches when pull requests are merged

Default: false
squash_merge_commit_title string

Required when using squash_merge_commit_message.

The default value for a squash merge commit title:

    PR_TITLE - default to the pull request's title.
    COMMIT_OR_PR_TITLE - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).

Can be one of: PR_TITLE, COMMIT_OR_PR_TITLE
squash_merge_commit_message string

The default value for a squash merge commit message:

    PR_BODY - default to the pull request's body.
    COMMIT_MESSAGES - default to the branch's commit messages.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, COMMIT_MESSAGES, BLANK
merge_commit_title string

Required when using merge_commit_message.

The default value for a merge commit title.

    PR_TITLE - default to the pull request's title.
    MERGE_MESSAGE - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).

Can be one of: PR_TITLE, MERGE_MESSAGE
merge_commit_message string

The default value for a merge commit message.

    PR_TITLE - default to the pull request's title.
    PR_BODY - default to the pull request's body.
    BLANK - default to a blank commit message.

Can be one of: PR_BODY, PR_TITLE, BLANK
has_downloads boolean

Whether downloads are enabled.

Default: true
is_template boolean

Whether this repository acts as a template that can be used to generate new repositories.

Default: false
HTTP response status codes for "Create a repository for the authenticated user"
Status code	Description
201	

Created
304	

Not modified
400	

Bad Request
401	

Requires authentication
403	

Forbidden
404	

Resource not found
422	

Validation failed, or the endpoint has been spammed.
Code samples for "Create a repository for the authenticated user"
Request example
post/user/repos

curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos \
  -d '{"name":"Hello-World","description":"This is your first repo!","homepage":"https://github.com","private":false,"is_template":true}'

Response

Status: 201
{
  "id": 1296269,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "name": "Hello-World",
  "full_name": "octocat/Hello-World",
  "owner": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/octocat/Hello-World",
  "description": "This your first repo!",
  "fork": false,
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "homepage": "https://github.com",
  "license": {
    "key": "mit",
    "name": "MIT License",
    "url": "https://api.github.com/licenses/mit",
    "spdx_id": "MIT",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "html_url": "https://github.com/licenses/mit"
  },
  "language": null,
  "forks_count": 9,
  "forks": 9,
  "stargazers_count": 80,
  "watchers_count": 80,
  "watchers": 80,
  "size": 108,
  "default_branch": "master",
  "open_issues_count": 0,
  "open_issues": 0,
  "is_template": false,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "has_pages": false,
  "has_downloads": true,
  "archived": false,
  "disabled": false,
  "visibility": "public",
  "pushed_at": "2011-01-26T19:06:43Z",
  "created_at": "2011-01-26T19:01:12Z",
  "updated_at": "2011-01-26T19:14:43Z",
  "permissions": {
    "pull": true,
    "push": false,
    "admin": false
  },
  "allow_rebase_merge": true,
  "template_repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World-Template",
    "full_name": "octocat/Hello-World-Template",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World-Template",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World-Template",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World-Template.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World-Template.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
    "homepage": "https://github.com",
    "language": null,
    "forks": 9,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues": 0,
    "open_issues_count": 0,
    "is_template": true,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "allow_squash_merge": true,
  "allow_auto_merge": false,
  "delete_branch_on_merge": true,
  "allow_merge_commit": true,
  "allow_forking": true,
  "web_commit_signoff_required": false,
  "subscribers_count": 42,
  "network_count": 0,
  "organization": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "parent": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  },
  "source": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": true,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "allow_rebase_merge": true,
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "subscribers_count": 42,
    "network_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://api.github.com/licenses/mit"
    },
    "forks": 1,
    "open_issues": 1,
    "watchers": 1
  }
}
List repositories for a user

Lists public repositories for the specified user.
Fine-grained access tokens for "List repositories for a user"

This endpoint works with the following fine-grained token types:

    GitHub App user access tokens
    GitHub App installation access tokens
    Fine-grained personal access tokens

The fine-grained token must have the following permission set:

    "Metadata" repository permissions (read)

This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.
Parameters for "List repositories for a user"
Headers
Name, Type, Description
accept string

Setting to application/vnd.github+json is recommended.
Path parameters
Name, Type, Description
username string Required

The handle for the GitHub user account.
Query parameters
Name, Type, Description
type string

Limit results to repositories of the specified type.

Default: owner

Can be one of: all, owner, member
sort string

The property to sort the results by.

Default: full_name

Can be one of: created, updated, pushed, full_name
direction string

The order to sort by. Default: asc when using full_name, otherwise desc.

Can be one of: asc, desc
per_page integer

The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30
page integer

The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
HTTP response status codes for "List repositories for a user"
Status code	Description
200	

OK
Code samples for "List repositories for a user"
Request example
get/users/{username}/repos

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/users/USERNAME/repos

Response

Status: 200
[
  {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
    "owner": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "private": false,
    "html_url": "https://github.com/octocat/Hello-World",
    "description": "This your first repo!",
    "fork": false,
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "is_template": false,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "has_discussions": false,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "admin": false,
      "push": false,
      "pull": true
    },
    "security_and_analysis": {
      "advanced_security": {
        "status": "enabled"
      },
      "secret_scanning": {
        "status": "enabled"
      },
      "secret_scanning_push_protection": {
        "status": "disabled"
      },
      "secret_scanning_non_provider_patterns": {
        "status": "disabled"
      }
    }
  }
] 


