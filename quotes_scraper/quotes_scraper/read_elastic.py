from elasticsearch import Elasticsearch
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

res = es.search(index="quotes-index", query={"match_all": {}})
for hit in res["hits"]["hits"]:
    print(hit["_source"])
