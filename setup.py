import JH, pygame


class Map:
    def __init__(self, scale):
        

        wall_NS = pygame.Surface((5, 25)).convert_alpha()
        wall_NS.fill((0, 0, 0))

        wall_WE = pygame.Surface((25, 5)).convert_alpha()
        wall_WE.fill((0, 0, 0))
        

        wall_NS_WE = pygame.Surface((25, 25)).convert_alpha()
        wall_NS_WE.blit(wall_WE, (0, 0))
        wall_NS_WE.blit(wall_NS, (0, 0))
        self.wallsSurfs = {"wall_WE": wall_WE,
                           "wall_NS": wall_NS,
                           "wall_NS-WE": wall_NS_WE
                               }
        self.scale = scale
        self.folder = "data/json/map.json"
        self.Json = JH.JsonReader(self.folder)
        self.mapName = "Map 1"
        self.map = self.Json[self.mapName] 
        self.LoadedMap = None
    def loadMap(self, name="Map 1"):
        self.mapName = name
        self.map = self.Json[self.mapName] 
        self.LoadedMap = pygame.Surface((29*25*self.scale, 29*25*self.scale)).convert_alpha()
        Yint = 0
        for y in self.map:
            Xint = 0
            for x in y:
                if x == 0:
                    Xint+=1
                    continue
                if x == 1:
                    self.LoadedMap.blit(self.wallsSurfs["wall_NS"], (Xint*25*self.scale, Yint*25*self.scale))
                if x == 2:
                    self.LoadedMap.blit(self.wallsSurfs["wall_WE"], (Xint*25*self.scale, Yint*25*self.scale))
                if x == 3:
                    self.LoadedMap.blit(self.wallsSurfs["wall_NS-WE"], (Xint*25*self.scale, Yint*25*self.scale))
                Xint += 1
            Yint += 1
        return self.LoadedMap
    def draw(self, screen:pygame.Surface):
        if self.LoadedMap == None:
            print("No map Loaded")
            return 1
        screen.blit(self.LoadedMap, (0, 0))