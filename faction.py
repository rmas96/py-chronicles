from configs import game


class Faction:
    def __init__(self):
        self.__name = self.get_name()
        self.__stage = 0
        self.__region = self.get_region()

    @property
    def stage(self):
        return self.__stage

    @stage.setter
    def stage(self, value):
        self.__stage = value

    @property
    def name(self):
        return self.__name

    def get_name(self):
        return "none"

    def get_region(self):
        return [0, 0]

    def advance_stage(self, dt, factions):
        pass

class Druid(Faction):
    def __init__(self):
        super().__init__()
        self.__resources_taken = {
            "player": 0,
            "exiled": 0,
        }
        self.__kill_count = 0

    def get_name(self):
        return "druid"

    def get_region(self):
        return [1451.0, 1311.0]

    def advance_stage(self, dt, factions):
        match self.stage:
            case 0: self.observe(factions["corrupted"])
            case 1: self.observe(factions["corrupted"])
            case 2: self.assess_kills()

    def observe(self, corrupted):
        if corrupted.stage > self.stage:
            self.stage += 1
        else:
            for faction in self.__resources_taken:
                if self.__resources_taken[faction] > game.DRUID_RESOURCE_LIMIT * (self.stage + 1):
                    self.stage += 1

    def assess_kills(self):
        if self.__kill_count >= game.DRUID_MAX_KILLS:
            self.stage = 3

    def increment_kill_count(self):
        self.__kill_count += 1

class Exiled(Faction):
    def __init__(self):
        super().__init__()
        self.__resources_qt = 0
        self.__build_timer = 0
        self.__wall_exploded = False

    def increment_resource_qt(self):
        self.__resources_qt += 1

    def wall_exploded(self):
        self.__wall_exploded = True

    def get_name(self):
        return "exiled"

    def get_region(self):
        return [1387.0, 469.0]

    def advance_stage(self, dt, factions):
        match self.stage:
            case 0: self.count_resources()
            case 1: self.build_bomb(dt)
            case 2: self.assess_wall_explosion()

    def count_resources(self):
        if self.__resources_qt >= game.EXILED_RESOURCE_OBJECTIVE:
            self.stage = 1
            print("Exilados começam a construir uma bomba")

    def build_bomb(self, dt):
        self.__build_timer += dt
        if self.__build_timer >= game.EXILED_BUILD_TIME * 60 * 1000:
            self.stage = 2
            print("Exilados vão para a cidade")

    def assess_wall_explosion(self):
        if self.__wall_exploded:
            self.stage = 3

class Corrupted(Faction):
    def __init__(self):
        super().__init__()
        self.__corruption_timer = 0
        self.__kill_count = 0

    def get_name(self):
        return "corrupted"

    def get_region(self):
        return [211.0, 135.0]

    def advance_stage(self, dt, factions):
        match self.stage:
            case 0: self.update_corruption(dt)
            case 1: self.assess_kills()
            case 2: self.assess_kills()

    def update_corruption(self, dt):
        self.__corruption_timer += dt

        if self.__corruption_timer >= game.CORRUPTION_TIME * 60 * 1000:
            self.stage = 1
            print("Os corrompidos avançaram para a fase 2")

    def assess_kills(self):
        if self.stage == 1:
            if self.__kill_count >= game.CORRUPTED_KILL_TRIGGER:
                self.stage = 2
                self.__kill_count = 0
        elif self.stage == 2:
            if self.__kill_count >= game.CORRUPTED_MAX_KILLS:
                self.stage = 3
                self.__kill_count = 0

    def increment_kill_count(self):
        self.__kill_count += 1