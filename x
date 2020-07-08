POST /graphql HTTP/1.1
Host: gql.tokopedia.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 746
X-Tkpd-Lite-Service: atreus
X-Source: tokopedia-lite
Origin: https://m.tokopedia.com
Referer: https://m.tokopedia.com/user/profile/name
Connection: close

{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}
