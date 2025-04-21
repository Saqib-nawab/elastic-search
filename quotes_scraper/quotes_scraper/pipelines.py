import json
import os
from elasticsearch import Elasticsearch
from datetime import datetime
import hashlib

class ElasticSearchPipeline:
    def __init__(self):
        # Get the absolute path to context.json
        base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of pipelines.py
        context_path = os.path.join(base_dir, '', 'context.json')  # go up one level

        with open(context_path) as f:
            context = json.load(f)

        self.es = Elasticsearch(
            [context["elastic_endpoint"]],
            api_key=context["elastic_api_key"],
            verify_certs=True
        )

    def process_item(self, item, spider):
        item_id = hashlib.md5(item['text'].encode('utf-8')).hexdigest()
        self.es.index(
            index="quotes-index",
            id=item_id,
            document={
                "text": item['text'],
                "author": item['author'],
                "tags": item['tags'],
                "scraped_at": datetime.utcnow()
            }
        )
        return item
