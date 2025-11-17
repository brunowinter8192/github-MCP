Get a tree

Returns a single tree using the SHA1 value or ref name for that tree.

If truncated is true in the response then the number of items in the tree array exceeded our maximum limit. If you need to fetch more items, use the non-recursive method of fetching trees, and fetch one sub-tree at a time.

Note

The limit for the tree array is 100,000 entries with a maximum size of 7 MB when using the recursive parameter.
Differenzierte Zugriffstoken für "Get a tree"

Dieser Endpunkt funktioniert mit den folgenden differenzierten Tokentypen.:

    GitHub-App-Benutzerzugriffstoken
    Zugriffstoken für GitHub App-Installation
    Differenzierte persönliche Zugriffstoken

Das differenzierte Token muss einen der folgenden Berechtigungssätze aufweisen.:

    "Contents" repository permissions (read)

Dieser Endpunkt kann ohne Authentifizierung oder die zuvor erwähnten Berechtigungen verwendet werden, wenn nur öffentliche Ressourcen angefordert werden.
Parameter für „Get a tree“
Header
Name, type, BESCHREIBUNG
accept string

Setting to application/vnd.github+json is recommended.
Pfadparameter
Name, type, BESCHREIBUNG
owner string Erforderlich

The account owner of the repository. The name is not case sensitive.
repo string Erforderlich

The name of the repository without the .git extension. The name is not case sensitive.
tree_sha string Erforderlich

The SHA1 value or ref (branch or tag) name of the tree.
Abfrageparameter
Name, type, BESCHREIBUNG
recursive string

Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in :tree_sha. For example, setting recursive to any of the following will enable returning objects or subtrees: 0, 1, "true", and "false". Omit this parameter to prevent recursively returning objects or subtrees.
HTTP-Antwortstatuscodes für „Get a tree“
Statuscode	BESCHREIBUNG
200	

OK
404	

Resource not found
409	

Conflict
422	

Validation failed, or the endpoint has been spammed.
Codebeispiele für „Get a tree“
Beispiele für Anforderungen
Select the example type
get/repos/{owner}/{repo}/git/trees/{tree_sha}

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/git/trees/TREE_SHA

Default response

Status: 200
{
  "sha": "9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
  "url": "https://api.github.com/repos/octocat/Hello-World/trees/9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
  "tree": [
    {
      "path": "file.rb",
      "mode": "100644",
      "type": "blob",
      "size": 30,
      "sha": "44b4fc6d56897b048c772eb4087f854f46256132",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/44b4fc6d56897b048c772eb4087f854f46256132"
    },
    {
      "path": "subdir",
      "mode": "040000",
      "type": "tree",
      "sha": "f484d249c660418515fb01c2b9662073663c242e",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/f484d249c660418515fb01c2b9662073663c242e"
    },
    {
      "path": "exec_file",
      "mode": "100755",
      "type": "blob",
      "size": 75,
      "sha": "45b983be36b73c0788dc9cbcb76cbb80fc7bb057",
      "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/45b983be36b73c0788dc9cbcb76cbb80fc7bb057"
    }
  ],
  "truncated": false
}