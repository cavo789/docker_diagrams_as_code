# Diagrams as code

![Banner](./banner.svg)

This repository is just a quick reference to how to use *Diagrams as code* ([https://github.com/mingrammer/diagrams](https://github.com/mingrammer/diagrams)), an Open source project that will convert Python code to diagrams.

The following example is based on [https://diagrams.mingrammer.com/docs/getting-started/examples#grouped-workers-on-aws](https://diagrams.mingrammer.com/docs/getting-started/examples#grouped-workers-on-aws) and, f.i., display a team of workers; very basic:

```python
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("PHP_Team", show=False, direction="TB"):
    ELB("Olivier") >> [
        EC2("Christophe"),
        EC2("Jason"),
        EC2("Niki"),
        EC2("Rudy"),
        EC2("Stijn") ] >> RDS("Évènements")
```

![PHP_Team](./images/php_team.png)

To run the conversion, you just need to have Docker installed on your machine then run the following command:

```bash
cat php_team.py | docker run -i --rm -v $(pwd)/images:/out gtramontina/diagrams:0.22.0
```

Note: if you're working Windows, replace `$(pwd)` by `%CD%`. And replace `cat` by `type`.

```bash
type php_team.py | docker run -i --rm -v %CD%/out:/out gtramontina/diagrams:0.22.0
```

*0.22.0 is the latest version available when writing this document. See [https://hub.docker.com/r/gtramontina/diagrams/tags](https://hub.docker.com/r/gtramontina/diagrams/tags) to retrieve the latest one.*

A more sophisticated diagram can be:

![Advanced Web Service with On-Premise (colored)](./images/advanced_web_service_with_on-premise_(colored).png)

More samples on [https://diagrams.mingrammer.com/docs/getting-started/examples](https://diagrams.mingrammer.com/docs/getting-started/examples)

The Docker image code base is here: [https://github.com/gtramontina/docker-diagrams](https://github.com/gtramontina/docker-diagrams).

## Icons (called Nodes)

A tremendous list of icons/nodes is available on multiple pages at [https://diagrams.mingrammer.com/docs/nodes/onprem](https://diagrams.mingrammer.com/docs/nodes/onprem). See [OnPrem](https://diagrams.mingrammer.com/docs/nodes/onprem), [AWS](https://diagrams.mingrammer.com/docs/nodes/aws), [Azure](https://diagrams.mingrammer.com/docs/nodes/azure), [GCP](https://diagrams.mingrammer.com/docs/nodes/gcp), [IBM](https://diagrams.mingrammer.com/docs/nodes/ibm), [K8S](https://diagrams.mingrammer.com/docs/nodes/k8s), ... and also how to create our owns (using local `.png` images): [Custom](https://diagrams.mingrammer.com/docs/nodes/custom).

## Other tools

* [DB Diagram](https://dbdiagram.io/home)
* [DBML-renderer](https://github.com/softwaretechnik-berlin/dbml-renderer), dbml-renderer renders DBML files to SVG images
* [Graphviz](https://www.graphviz.org/), Graphviz is open source graph visualization software
* [JSON Crack](https://jsoncrack.com/), seamlessly visualize your JSON data instantly into graphs
* [Kroki](https://kroki.io/), creates diagrams from textual descriptions
* [Mermaid](https://mermaid-js.github.io/mermaid/), his [live editor](https://mermaid.live/), the [preview addon for vscode](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview) and the [convert tool as a CLI tool](https://github.com/mermaid-js/mermaid-cli)
* [Nomnoml](https://www.nomnoml.com/), tool for drawing UML diagrams based on a simple syntax
* [Pikchr](https://pikchr.org/), Pikchr (pronounced "picture") is a PIC-like markup language for diagrams in technical documentation
* [Plantuml](https://github.com/plantuml/plantuml), generate diagrams from textual description
* [Sequence diagram](https://sequencediagram.org/) *(seems based on Mermaid)*
* [Structurizr](https://github.com/structurizr/dsl), a way to create Structurizr software architecture models based upon the C4 model using a textual domain specific language
* [svgbob](https://github.com/ivanceras/svgbob), convert your ascii diagram scribbles into happy little SVG
* [Vega](https://vega.github.io/vega/), a Visualization Grammar
* [yEd Graph Editor](https://www.yworks.com/products/yed), Graphical interface, you'll need to drag & drop objects, resize, ... It doesn't support text files like the other tools already mentioned here.
