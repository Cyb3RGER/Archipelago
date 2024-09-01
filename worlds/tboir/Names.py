import enum
from enum import Enum


class ItemNames(Enum):
    Collectible = "Progression Collectible"
    StageUnlock = "Progressive Stage Unlock"
    AltStageUnlock = "Progressive Alt. Stage Unlock"


class StageNames(Enum):
    Basement1 = "Basement I"
    Basement2 = "Basement II"
    Caves1 = "Caves I"
    Caves2 = "Caves II"
    Depths1 = "Depths I"
    Depths2 = "Depths II"
    Womb1 = "Womb I"
    Womb2 = "Womb II"
    BlueWomb = "Blue Womb"
    Sheol = "Sheol"
    Cathedral = "Cathedral"
    DarkRoom = "Dark Room"
    Chest = "Chest"
    TheVoid = "The Void"
    Home = "Home"
    Downpour1 = "Downpour I"
    Downpour2 = "Downpour II"
    Mines1 = "Mines I"
    Mines2 = "Mines II"
    Mausoleum1 = "Mausoleum I"
    Mausoleum2 = "Mausoleum II"
    Corpse1 = "Corpse I"
    Corpse2 = "Corpse II"


unlock_item_names: list[str] = [
    StageNames.Basement2,
    StageNames.Caves1,
    StageNames.Caves2,
    StageNames.Depths1,
    StageNames.Depths2,
    StageNames.Womb1,
    StageNames.Womb2,
    f"{StageNames.BlueWomb}/{StageNames.Sheol}/{StageNames.Cathedral}",
    f"{StageNames.DarkRoom}/{StageNames.Chest}",
    StageNames.TheVoid,
    StageNames.Home
]

stage_names: list[str] = [
    StageNames.Basement1,
    StageNames.Basement2,
    StageNames.Caves1,
    StageNames.Caves2,
    StageNames.Depths1,
    StageNames.Depths2,
    StageNames.Womb1,
    StageNames.Womb2,
    StageNames.BlueWomb,
    StageNames.Sheol,
    StageNames.Cathedral,
    StageNames.DarkRoom,
    StageNames.Chest,
    StageNames.TheVoid,
    StageNames.Home
]

alt_stage_names: list[str] = [
    StageNames.Downpour1,
    StageNames.Downpour2,
    StageNames.Mines1,
    StageNames.Mines2,
    StageNames.Mausoleum1,
    StageNames.Mausoleum2,
    StageNames.Corpse1,
    StageNames.Corpse2,
]

all_stage_names = [
    StageNames.Basement1,
    StageNames.Basement2,
    StageNames.Downpour1,
    StageNames.Caves1,
    StageNames.Downpour2,
    StageNames.Caves2,
    StageNames.Mines1,
    StageNames.Depths1,
    StageNames.Mines2,
    StageNames.Depths2,
    StageNames.Mausoleum1,
    StageNames.Womb1,
    StageNames.Mausoleum2,
    StageNames.Womb2,
    StageNames.Corpse1,
    StageNames.BlueWomb,
    StageNames.Corpse2,
    StageNames.Sheol,
    StageNames.Cathedral,
    StageNames.DarkRoom,
    StageNames.Chest,
    StageNames.TheVoid,
    StageNames.Home
]



class RoomTypes(Enum):
    Shop = "Shop"
    Treasure = "Treasure Room"
    Boss = "Boss Room"
    Secret = "Secret Room"
    Devil = "Devil Deal"
    Angel = "Angel Deal"
    Planetarium = "Planetarium"
    Other = "Other"
    # part of Treasure Room for now
    Vault = "Vault"
    # part of Boss for now
    Miniboss = "Miniboss Room"
    Bossrush = "Bossrush"
    # part of Secret for now
    SuperSecret = "Super Secret Room"
    UltraSecret = "Ultra Secret Room"
    Dungeon = "Crawlspace"
    BlackMarket = "Black Market"
    # part of Other for now
    # Default = "Default Room"
    Aracde = "Arcade"
    Curse = "Curse Room"
    Challenge = "Challenge Room"
    Library = "Library"
    CleanBedroom = "Clean Bedroom"
    DirtyBedroom = "Dirty Bedroom"
    Dice = "Dice Room"
    GreedExit = "Greed Exit"
    SecretExit = "SecretExit"
    Blue = "Blue Key Room"
    Sacrifice = "Sacrifice Room"


room_type_names: list[str] = [
    RoomTypes.Shop,
    RoomTypes.Treasure,
    RoomTypes.Boss,
    RoomTypes.Secret,
    RoomTypes.Devil,
    RoomTypes.Angel,
    RoomTypes.Planetarium,
    RoomTypes.Other
]

disallowed_room_types_per_stage: dict[str, list[str]] = {
    # do not expect the player to get deals or planetarium on first floor... unless we make them guaranteed somehow at
    # some point
    StageNames.Basement1: [RoomTypes.Devil, RoomTypes.Angel, RoomTypes.Planetarium],
    # no shops/treasure rooms/planetariums after this point
    StageNames.Womb1: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium],
    StageNames.Womb2: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium],
    StageNames.Corpse1: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium],
    StageNames.Corpse2: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium],
    # no deals after this point
    # exception Blue Womb: only Shops, Treasure Rooms and Other
    StageNames.BlueWomb: [RoomTypes.Boss, RoomTypes.Planetarium, RoomTypes.Secret, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.Sheol: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.Cathedral: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.DarkRoom: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.Chest: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.TheVoid: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
    StageNames.Home: [RoomTypes.Shop, RoomTypes.Treasure, RoomTypes.Planetarium, RoomTypes.Devil, RoomTypes.Angel],
}
