# QPTDat Knowledge Graph

This projects is the QPTDat knowledge graph. It utilizes docker to run all necessary services. 

## File structure
* Caddyfile: Directly mounted configuration file for the proxy server of the whole project.
* convert.py: The automatic initial toLoad function of Virtuoso requires the n3 RDF serialization format. This script can be used to convert the RDF data. 
* data: Directly mounted directory to store the Virtuoso RDF data. 
* docker-compose.yml: All configuration of the architecture.
* .env: Some sensible configurations. 
* example.env: An example file of the .env file, which contains sensible configuration and is not included in the git repository. 
* LodView: The LowView git repository used in this 
* README.md: The current file. 
* requirements.txt: The Python requriements for the convert.py file.
* resource: The resources that are utilized in the Knowledge Graph infrastructure in multiple containers. 
* static: The temporary location for all static resources that should be loaded into LodView. In most cases it should contain the same data as resource.

## Setup
The setup 

### Conada Set up
```
conda create -n qpt python=3.10
conda activate qpt
pip install -r requirements.txt
```


### Move resources from ontology to current project

```
cp ../ontology/*.ttl resource/.
```

### Convert resources 

```
python convert.py -i resource/core.ttl -o resource/core.nt
python convert.py -i resource/source.ttl -o resource/source.nt
python convert.py -i resource/diagnostic.ttl -o resource/diagnostic.nt
```

### Create graph files

```
echo "http://qptdat.plasma-mds.org/ontology/" > resource/core.nt.graph
echo "http://qptdat.plasma-mds.org/source_ontology/" > resource/source.nt.graph
echo "http://qptdat.plasma-mds.org/diagnostic_ontology/" > resource/diagnostic.nt.graph

```

### Copy to static resources

```
cp resource/*.ttl static/.
```

### Add static resources
The static resouces just need to be copied to `` 
The current setting forward `/raw` to a `data` folder. This folder needs to be created with `mkdir` in side the container
```
docker exec -it knowledge_graph_lodview_1 /bin/bash
```
After that the resources can be copied by using 
```
docker cp ./static/core.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
docker cp ./static/source.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
docker cp ./static/diagnostic.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
docker cp ./static/resource.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
```

### Lokal Test
Add `127.0.0.1 qptdat.plasma-mds.org` to `/etc/hosts`  

## Operations
### Load a RDF dump into the Virtuoso triple store

