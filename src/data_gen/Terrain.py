import random

class TerrainMaker(object):
    def __init__(self, width=100, height=100):
        self.Width = width
        self.Height = height
        self.StoredTerrainsDict = {}
    
    def makeRandomTerrain(self, floor=0, ceiling=100, terrainName=""):
        """
        Generates a 2D array of random 3-D topographic-style values
        """
        if terrainName == "":
            terrainName = f"random [{self.Width}, {self.Height}]"
        m = []

        for _ in range(self.Height):
            row = []
            for _ in range(self.Width):
                alt = random.random() * (ceiling - floor)
                row.append(alt)
            m.append(row)
        
        return Terrain(terrainName, m)
    
    def makePeakTerrain(self, floor=0, ceiling=100, terrainName=""):
        """
        Generates a 2-D array of 3-D topographic-style values with a center peak
        """
        if terrainName == "":
            terrainName = f"peak [{self.Width}, {self.Height}]"
        m = []
        halfH = (self.Height / 2)
        halfW = (self.Width / 2)
        for i in range(self.Height):
            row = []
            rowFactor = 1 - abs((halfH - i)) / halfH
            for j in range(self.Width):
                colFactor = 1 - abs((halfW - j)) / halfW
                peakFactor = colFactor * rowFactor
                alt = (ceiling - floor) * peakFactor
                row.append(alt)
            m.append(row)
        
        return Terrain(terrainName, m)

    def storeTerrain(self, Terrain):
        self.StoredTerrainsDict[Terrain.Name] = Terrain
    
    def writeToCSV(self, Terrain, filename=""):
        if filename == "":
            filename = f"terrain_gen[{self.Width}, {self.Height}]" + ".csv"
        elif filename[-4:] != ".csv":
            filename += ".csv"
        
        with open(filename, "w+") as file:
            for row in range(Terrain.Height):
                for col in range(Terrain.Width):
                    file.write(str(Terrain.TerrainMatrix[row][col]) + ", ")
                file.write('\n')


class Terrain(object):
    def __init__(self, name, terrainMatrix):
        self.Name = name
        self.TerrainMatrix = terrainMatrix
        self.Width = len(terrainMatrix[0])
        self.Height = len(terrainMatrix)
    
    def getPointForm(self):
        cols = []

        for i in range(self.Height):
            for j in range(self.Width):
                row = []
                row.append(j)
                row.append(i)
                row.append(self.TerrainMatrix[i][j])
                cols.append(row)
        
        return cols

    def preview(self, numRows=10, numCols=10):
        r = numRows if numRows < self.Width else self.Width
        c = numCols if numCols < self.Height else self.Height
        for i in range(r):
            print("[", end="")
            for j in range(c-1):
                print(round(self.TerrainMatrix[i][j]), end=", ")
            if i != r-1:
                print(f"{round(self.TerrainMatrix[i][c])}],\n", end="")
            else:
                print(f"{round(self.TerrainMatrix[i][c])}]")
