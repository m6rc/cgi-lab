#!/usr/bin/env python3
import os
import json

print("Content-Type: text/html")
print()
#print(json.dumps(dict(os.environ), indent=2))
print(f"<p>HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}</p>")

# q2: query_string
# q3: http_user_agent
# q4: cgi.form
# q5: set-cookie
# q6: http_cookie
