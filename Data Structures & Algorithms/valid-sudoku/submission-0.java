class Pair {
    private int x;
    private int y;

    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return x;
    }

    public int getY(){
        return y;
    }

    public void setX(int newX){
        this.x = newX;
    }

    public void setY(int newY){
        this.y = newY;
    }
}

class Solution {
    public ArrayList<Pair> getGrid(Pair coor){
        int x = coor.getX();
        int y = coor.getY();

        Pair topLeft = new Pair((x / 3) * 3, (y / 3) * 3);
        Pair bottomRight = new Pair(topLeft.getX() + 2, topLeft.getY() + 2);

        ArrayList<Pair> coors = new ArrayList<>();
        coors.add(topLeft);
        coors.add(bottomRight);
        return coors;
    }
    public ArrayList<Pair> findAllLocations(int num, char[][] board){
        int m = board.length;
        int n = board[0].length;

        ArrayList<Pair> numList = new ArrayList<>();

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == (char) ('0' + num)){
                    numList.add(new Pair(i, j));
                }
            }
        }

        return numList;
    }

    public boolean isValidSudoku(char[][] board) {
        boolean result = true;

        for(int i = 1; i <= 9; i++){
            ArrayList<Pair> locations = findAllLocations(i, board);

            // Row Checking
            HashSet<Integer> visitedRow = new HashSet<>();
            for(Pair coor : locations){
                if(!visitedRow.contains(coor.getX())){
                    visitedRow.add(coor.getX());
                }
                else{
                    result = false;
                    return result;
                }
            }

            // Col Checking
            HashSet<Integer> visitedCol = new HashSet<>();
            for(Pair coor : locations){
                if(!visitedCol.contains(coor.getY())){
                    visitedCol.add(coor.getY());
                }
                else{
                    result = false;
                    return result;
                }
            }

            // Grid Checking
            HashSet<String> visitedGrids = new HashSet<>();
            for (Pair coor : locations) {
                
                ArrayList<Pair> grid = getGrid(coor);
                Pair topLeft = grid.get(0);
                Pair bottomRight = grid.get(1);

                
                if (coor.getX() >= topLeft.getX() && coor.getX() <= bottomRight.getX() &&
                    coor.getY() >= topLeft.getY() && coor.getY() <= bottomRight.getY()) {
                    
                    
                    String gridKey = topLeft.getX() + "-" + topLeft.getY();
                    if (!visitedGrids.contains(gridKey)) {
                        visitedGrids.add(gridKey);
                    } else {
                        result = false;
                        return result;
                    }
                }
            }
        }

    return result;
    }
}