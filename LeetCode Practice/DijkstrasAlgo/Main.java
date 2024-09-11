package DijkstrasAlgo;

import java.util.*;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) {
        Graph graph = new Graph();

        graph.addNode("A");
        graph.addNode("B");
        graph.addNode("C");
        graph.addNode("D");

        graph.addEdge("A", "B", 1);
        graph.addEdge("B", "C", 2);
        graph.addEdge("A", "C", 4);
        graph.addEdge("C", "D", 1);

        String startNode = "A";

        Map<String, Long> shortestPaths = ShortestPathFinder.dijkstra(graph, startNode);

        System.out.println("Shortest paths from " + startNode);
        System.out.println("Shortest paths from " + startNode + ":");
        for (Entry<String, Long> entry : shortestPaths.entrySet()) {
            String node = entry.getKey();
            Long distance = entry.getValue();

            if (distance == Integer.MAX_VALUE) {
                System.out.println(node + ": Unreachable");
            } else {
                System.out.println(node + ": " + distance);
            }
        }
    }
    }

