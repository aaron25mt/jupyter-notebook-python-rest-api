# jupyter-notebook-python-rest-api


| Route | Input | Output | Description |
|---|---|---|---|
| GET /api/rec/jupyter?keyword={keyword} | keyword = search query | {"notebooks": [notebooks]} | Returns an object containing a list of relevant notebooks |
| POST /api/rec/jupyter | {"keyword": keyword} | {"notebooks": [notebooks] } | Returns an object containing a list of relevant notebooks |
