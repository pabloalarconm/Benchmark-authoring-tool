from rdflib import Graph
import chevron
import os
from SPARQLWrapper import SPARQLWrapper, JSON, POST, BASIC

class Benchmark:

    def metric_from_benchmark(self, web_benchmark):

        g = Graph()
        g.parse(web_benchmark, format="turtle") 

        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        rdf_file_path = os.path.join(base_path, "templates", "benchmark-metrics.mustache")
        with open(rdf_file_path, 'r') as f:
            imported_query = chevron.render(f)

        results = g.query(imported_query)

        self.metrics_list=list()
        for row in results:
            metric = row.metric
            metric_string = f"{metric}"
            self.metrics_list.append(metric_string)

        return self.metrics_list
    
    
    def call_fdp_for_test_information(self,creator):
        #fdp connection:
        ENDPOINT = SPARQLWrapper("https://tools.ostrails.eu/repositories/fdpindex-fdp")
        ENDPOINT.setHTTPAuth(BASIC)
        ENDPOINT.setMethod(POST)

        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        self.test_list = list()

        for i, metric in enumerate(self.metrics_list, start=1):
            print(f"Calling FAIR Metric {i}/{len(self.metrics_list)}: {metric}")

            rdf_file_path = os.path.join(base_path, "templates", "query-fdp.mustache")
            with open(rdf_file_path, 'r') as f:
                imported_query = chevron.render(f, {'metric': metric, 'creator': creator})

            ENDPOINT.setQuery(imported_query)
            ENDPOINT.setReturnFormat(JSON)
            result = ENDPOINT.query().convert()

            if not result["results"]["bindings"]:
                print(f"No results found for metric: {metric}")
                continue

            test_string = result["results"]["bindings"][0]["test"]["value"]
            self.test_list.append(test_string)

        return self.test_list

# # Test
# test= Benchmark()
# metrics_obtained = test.metric_from_benchmark(web_bench="https://oeg-upm.github.io/fair_ontologies/doc/benchmark/ALL/ALL.ttl")
# test_final = test.call_fdp_for_test_information(creator="https://orcid.org/0000-0003-0454-7145")