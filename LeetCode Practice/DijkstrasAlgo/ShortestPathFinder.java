package DijkstrasAlgo;
import java.util.*;

public class ShortestPathFinder {
    public static Map<String, Long> dijkstra(Graph graph, String start){
        Set<String> visited = new HashSet<>();
        Map<String, Long> distance = new HashMap<>();
        PriorityQueue<String> priorityQueue = new PriorityQueue<>(Comparator.comparingLong(distance::get));

        graph.getNodes().forEach(node ->{
            distance.put(node, node.equals(start) ? 0L : Long.MAX_VALUE);
            priorityQueue.add(node);
        });

        while(!priorityQueue.isEmpty()){
            String current = priorityQueue.poll();

            for(Map.Entry<String, Integer> neighborEntry : graph.getNeighbors(current).entrySet()){
                String neighbor = neighborEntry.getKey();
                long newDistance = distance.get(current) + neighborEntry.getValue();

                if(newDistance < distance.get(neighbor)){
                    distance.put(neighbor, newDistance);
                }
            }

            visited.add(current);
            priorityQueue.removeAll(visited);
        }

        return distance;
    }
    
}
