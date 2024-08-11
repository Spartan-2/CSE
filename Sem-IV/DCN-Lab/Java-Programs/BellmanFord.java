// Bellman Ford Algorithm with adjacency matrix as inputs

import java.util.*;

public class BellmanFord {
    public static final int maxVal = 999;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of vertices ");
        int V = sc.nextInt();
        int[][] graph = new int[V+1][V+1];
        for (int i=0;i<=V;i++){
            for(int j=0;j<=V;j++){
                graph[i][j] = maxVal;
            }
        }
        System.out.println("Enter the number of edges ");
        int E = sc.nextInt();
        System.out.println("Enter the edges (u,v) and weight of edge,Enter 0 if there is no edge ");
        for(int i=0;i<E;i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            int wt = sc.nextInt();
            graph[u][v] = wt;
        }
        System.out.println("Enter the source ");
        int src = sc.nextInt();

        int[] dist = new int[V+1];
        Arrays.fill(dist,maxVal);
        dist[src] = 0;

        for(int i =1;i<V-1;i++){
            for(int u =1;u<=V;u++){
                for(int v=1;v<=V;v++){
                    if(dist[v] > dist[u] + graph[u][v]){
                        dist[v] = dist[u] + graph[u][v]; 
                    }
                }
            }
        }
        for(int u =1;u<=V;u++){
            for(int v=1;v<=V;v++){
                if(dist[v] > dist[u] + graph[u][v]){
                    System.out.println("Negative Cycle exists");
                    return;
                }
            }
        }

        System.out.println("Vertex\tDistance from source");
        for(int i=1;i<=V;i++){
            System.out.println(i+"\t"+dist[i]);
        }
        sc.close();   
    }
    
}
