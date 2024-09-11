package DijkstrasAlgo;

import java.util.*;

class Graph {
    private Map<String, Map<String, Integer>> adjacencyList;

    public Graph(){
        this.adjacencyList = new HashMap<>();
    }

    public void addNode(String node){
        adjacencyList.put(node, new HashMap<>());
    }

    public void addEdge(String src, String dst, int weight){
        adjacencyList.get(src).put(dst, weight);
        adjacencyList.get(dst).put(src, weight);
    }

    public Set<String> getNodes(){
        return adjacencyList.keySet();
    }

    public Map<String, Integer> getNeighbors(String node){
        return adjacencyList.get(node);
    }
}
