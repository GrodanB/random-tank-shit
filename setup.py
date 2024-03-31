import JH, pygame


class Map:
    def __init__(self, scale):
        

        wall_NS = pygame.Surface((4, 32))
        wall_NS.fill((0, 0, 0))

        wall_WE = pygame.Surface((32, 4))
        wall_WE.fill((0, 0, 0))
        

        wall_NS_WE = pygame.Surface((32, 32)).convert_alpha()
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
        self.LoadedMap = []
        Yindex = 0
        for y in self.map:
            self.LoadedMap.append([])
            for x in y:
                if x == 0:
                    self.LoadedMap[Yindex].append(0)
                if x == 1:
                    self.LoadedMap[Yindex].append(self.wallsSurfs["wall_NS"])
                if x == 2:
                    self.LoadedMap[Yindex].append(self.wallsSurfs["wall_WE"])
                if x == 3:
                    self.LoadedMap[Yindex].append(self.wallsSurfs["wall_NS-WE"])
            Yindex += 1
        return self.LoadedMap
    def draw(self, screen:pygame.Surface):
        if self.LoadedMap == None:
            print("No map Loaded")
            return 1
        Yint = 0
        for y in self.LoadedMap:
            Xint = 0
            for x in y:
                if x != 0:
                    screen.blit(x, (Xint*32*self.scale,Yint*32*self.scale))
                Xint += 1
            Yint += 1