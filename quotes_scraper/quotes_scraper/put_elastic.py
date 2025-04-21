from elasticsearch import Elasticsearch
from datetime import datetime  # for storing the current date and time

import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of pipelines.py
context_path = os.path.join(base_dir, '', 'context.json')  # go up one level

with open(context_path) as f:
    context = json.load(f)

es = Elasticsearch(
    [context["elastic_endpoint"]],
    api_key=context["elastic_api_key"],
    verify_certs=True
)

# updating a certain field in a document by doc ID
# doc_id = '05f4668b21413b946fbb80df4c1d796e'
# es.update(
#     index="quotes-index",
#     id=doc_id,
#     doc={"author": "Updated Author",
#          "text": "Updated text",
#          "tags": ["updated", "tags"],
#          "scraped_at": datetime.utcnow()}
# )

# get document by ID
# doc_id = '3c96933b3a61a5510fae63d33a7ea6ad'
# res = es.get(index="quotes-index", id=doc_id)
# print(res["_source"])

# how to list all indixes
res = es.indices.get_alias().keys()
print(res)