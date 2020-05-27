
                 # tinuu-url
Shorten the given URL

1. [POST] /api/create/
JSON-Data: {'url': 'www.google.com', 'expire': '2019-07-30 00:00:00'}
Response: {'short-url': '127.0.0.1:8080/s/(identifier)'}
Note 1: Short URL should expire after expiry and 404 should be returned after expiry.

2. [GET] /s/(identifier)
Redirect To Correct URL
Note 2: A 302 redirect is a must.
                 