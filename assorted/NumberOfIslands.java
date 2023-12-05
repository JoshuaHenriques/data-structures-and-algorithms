import java.awt.Point;

class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int numOfIslands = 0;
    
        for (int i = 0; i < grid.length; i++) {
             for(int j = 0; j < grid[i].length; j++){
                 if (grid[i][j] == '0') continue;
                 if (grid[i][j] == '1') {
                     numOfIslands += bfs(grid, i, j);
                     //bfsFill(grid, i, j);
                     //numOfIslands++;
                 } 
             }
         }
        
        return numOfIslands;
    }
                
    private int dfs(char[][] grid, int i, int j) {
        if (grid == null || i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0') {
            return 0;
        }
        
        grid[i][j] = '0';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
        return 1;
    }
    
    private int bfs(char[][] grid, int i, int j) {
        int m = grid.length;
        int n = grid[0].length;
        Queue<Point> queue = new LinkedList<>();
        grid[i][j] = '0';
        queue.offer(new Point(i, j));
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            int x = (int) point.getX();
            int y = (int) point.getY();
            if (x < m-1 && grid[x+1][y] == '1') {
                queue.offer(new Point(x+1,y));
                grid[x+1][y] = '0';
            }
            
            if (x > 0 && grid[x-1][y] == '1') {
                queue.offer(new Point(x-1,y));
                grid[x-1][y] = '0';
            }
            
            if (y < n-1 && grid[x][y+1] == '1') {
                queue.offer(new Point(x,y+1));
                grid[x][y+1] = '0';
            }
            
            if (y > 0 && grid[x][y-1] == '1') {
                queue.offer(new Point(x,y-1));
                grid[x][y-1] = '0';
            }
        }
        return 1;
    }
    
    private void bfsFill(char[][] grid, int x, int y){
        grid[x][y]='0';
        int n = grid.length;
        int m = grid[0].length;
        LinkedList<Integer> queue = new LinkedList<Integer>();  
        int code = x*m+y;  
        queue.offer(code);  
        while(!queue.isEmpty())  
        {  
            code = queue.poll();  
            int i = code/m;  
            int j = code%m;  
            if(i>0 && grid[i-1][j]=='1')    //search upward and mark adjacent '1's as '0'.
            {  
                queue.offer((i-1)*m+j);  
                grid[i-1][j]='0';  
            }  
            if(i<n-1 && grid[i+1][j]=='1')  //down
            {  
                queue.offer((i+1)*m+j);  
                grid[i+1][j]='0';  
            }  
            if(j>0 && grid[i][j-1]=='1')  //left
            {  
                queue.offer(i*m+j-1);  
                grid[i][j-1]='0';  
            }  
            if(j<m-1 && grid[i][j+1]=='1')  //right
            {  
                queue.offer(i*m+j+1);  
                grid[i][j+1]='0';  
            }
        } 
    }
}