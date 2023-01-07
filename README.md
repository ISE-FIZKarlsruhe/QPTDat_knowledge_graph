This projects is the QPTDat knowledge graph. It utilizes docker to run all necessary services. 

# Add static resources
The static resouces just need to be copied to `` 
The current setting forward `/raw` to a `data` folder. This folder needs to be created with `mkdir` in side the container
```
docker exec -it knowledge_graph_lodview_1 /bin/bash
```
After that the resources can be copied by using 
```
docker cp ./static/core.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
docker cp ./static/source.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
docker cp ./static/resource.ttl knowledge_graph_lodview_1:/usr/local/tomcat/webapps/lodview/resources/data/.
```


# Test
Add `127.0.0.1 qptdat.plasma-mds.org` to `/etc/hosts`  
