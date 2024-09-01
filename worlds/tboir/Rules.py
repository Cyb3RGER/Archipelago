import typing

from worlds.generic.Rules import CollectionRule
from worlds.tboir.Names import StageNames, ItemNames
from worlds.tboir.Options import Goal


class ConnectionData(typing.NamedTuple):
    target_region: str
    access_rules: typing.Optional[typing.Callable[[int], CollectionRule]]


goal_stage_mapping: dict[int, list[str]] = {
    Goal.option_mom: [StageNames.Depths1, StageNames.Mausoleum2],
    Goal.option_moms_heart: [StageNames.Womb2, StageNames.Mausoleum2],
    Goal.option_isaac_satan: [StageNames.Sheol, StageNames.Cathedral],
    Goal.option_isaac: [StageNames.Cathedral],
    Goal.option_satan: [StageNames.Sheol],
    Goal.option_blue_baby_lamb: [StageNames.DarkRoom, StageNames.Chest],
    Goal.option_blue_baby: [StageNames.Chest],
    Goal.option_lamb: [StageNames.DarkRoom],
    Goal.option_mega_satan: [StageNames.DarkRoom, StageNames.Chest],
    Goal.option_boss_rush: [StageNames.Depths2],
    Goal.option_hush: [StageNames.BlueWomb],
    Goal.option_dogma: [StageNames.Home],
    Goal.option_beast: [StageNames.Home],
    Goal.option_mother: [StageNames.Corpse2],
    Goal.option_delirium: [StageNames.TheVoid],
    # ToDo
    Goal.option_required_locations: [StageNames.Basement1],
    Goal.option_full_notes: [],
    Goal.option_note_marks: [],
}

# ToDo: add quest items as requirements?
stage_vanilla_connections = {
    StageNames.Basement1: [
        ConnectionData(StageNames.Basement2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 2))
    ],
    StageNames.Basement2: [
        ConnectionData(StageNames.Caves1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 4))
    ],
    StageNames.Caves1: [
        ConnectionData(StageNames.Caves2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 6))
    ],
    StageNames.Caves2: [
        ConnectionData(StageNames.Depths1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 8))
    ],
    StageNames.Depths1: [
        ConnectionData(StageNames.Depths2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 10))
    ],
    StageNames.Depths2: [
        ConnectionData(StageNames.Womb1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 12)),
        ConnectionData(StageNames.Home, lambda player: lambda state: state.has(ItemNames.Collectible, player, 20)),
    ],
    StageNames.Womb1: [
        ConnectionData(StageNames.Womb2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 14))
    ],
    StageNames.Womb2: [
        ConnectionData(StageNames.BlueWomb, lambda player: lambda state: state.has(ItemNames.Collectible, player, 20)),
        ConnectionData(StageNames.Sheol, lambda player: lambda state: state.has(ItemNames.Collectible, player, 16)),
        ConnectionData(StageNames.Cathedral, lambda player: lambda state: state.has(ItemNames.Collectible, player, 16)),
    ],
    StageNames.BlueWomb: [
        ConnectionData(StageNames.Sheol, lambda player: lambda state: state.has(ItemNames.Collectible, player, 16)),
        ConnectionData(StageNames.Cathedral, lambda player: lambda state: state.has(ItemNames.Collectible, player, 16)),
        ConnectionData(StageNames.TheVoid, lambda player: lambda state: state.has(ItemNames.Collectible, player, 20)),
    ],
    StageNames.Sheol: [
        ConnectionData(StageNames.DarkRoom, lambda player: lambda state: state.has(ItemNames.Collectible, player, 18)),
    ],
    StageNames.Cathedral: [
        ConnectionData(StageNames.Chest, lambda player: lambda state: state.has(ItemNames.Collectible, player, 18)),
    ],
}

stage_progressive_connections = {
    StageNames.Basement1: [
        ConnectionData(StageNames.Basement2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 1))
    ],
    StageNames.Basement2: [
        ConnectionData(StageNames.Caves1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 2))
    ],
    StageNames.Caves1: [
        ConnectionData(StageNames.Caves2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 3))
    ],
    StageNames.Caves2: [
        ConnectionData(StageNames.Depths1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 4))
    ],
    StageNames.Depths1: [
        ConnectionData(StageNames.Depths2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 5))
    ],
    StageNames.Depths2: [
        ConnectionData(StageNames.Womb1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 6)),
        ConnectionData(StageNames.Home, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 11)),
    ],
    StageNames.Womb1: [
        ConnectionData(StageNames.Womb2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 7))
    ],
    StageNames.Womb2: [
        ConnectionData(StageNames.BlueWomb, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 8)),
        ConnectionData(StageNames.Sheol, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 8)),
        ConnectionData(StageNames.Cathedral, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 8)),
    ],
    StageNames.BlueWomb: [
        ConnectionData(StageNames.Sheol, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 8)),
        ConnectionData(StageNames.Cathedral, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 8)),
        ConnectionData(StageNames.TheVoid, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 10)),
    ],
    StageNames.Sheol: [
        ConnectionData(StageNames.DarkRoom, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 9)),
    ],
    StageNames.Cathedral: [
        ConnectionData(StageNames.Chest, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 9)),
    ],
}

alt_stage_vanilla_connections = {
    StageNames.Basement1: [
        ConnectionData(StageNames.Downpour1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 2))
    ],
    StageNames.Basement2: [
        ConnectionData(StageNames.Downpour2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 4))
    ],
    StageNames.Caves1: [
        ConnectionData(StageNames.Mines1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 6))
    ],
    StageNames.Caves2: [
        ConnectionData(StageNames.Mines2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 8))
    ],
    StageNames.Depths1: [
        ConnectionData(StageNames.Mausoleum1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 10))
    ],
    StageNames.Downpour1: [
        ConnectionData(StageNames.Downpour2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 4))
    ],
    StageNames.Downpour2: [
        ConnectionData(StageNames.Mines1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 6))
    ],
    StageNames.Mines1: [
        ConnectionData(StageNames.Mines2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 8))
    ],
    StageNames.Mines2: [
        ConnectionData(StageNames.Mausoleum1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 10))
    ],
    StageNames.Mausoleum1: [
        ConnectionData(StageNames.Mausoleum2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 12))
    ],
    StageNames.Mausoleum2: [
        ConnectionData(StageNames.Corpse1, lambda player: lambda state: state.has(ItemNames.Collectible, player, 14))
    ],
    StageNames.Corpse1: [
        ConnectionData(StageNames.Corpse2, lambda player: lambda state: state.has(ItemNames.Collectible, player, 16))
    ]
}

alt_stage_non_progressive_connections = {
    StageNames.Downpour1: [
        ConnectionData(StageNames.Downpour2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 1))
    ],
    StageNames.Downpour2: [
        ConnectionData(StageNames.Mines1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 2))
    ],
    StageNames.Mines1: [
        ConnectionData(StageNames.Mines2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 3))
    ],
    StageNames.Mines2: [
        ConnectionData(StageNames.Mausoleum1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 4))
    ],
    StageNames.Mausoleum1: [
        ConnectionData(StageNames.Mausoleum2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 5))
    ],
    StageNames.Mausoleum2: [
        ConnectionData(StageNames.Corpse1, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 6))
    ],
    StageNames.Corpse1: [
        ConnectionData(StageNames.Corpse2, lambda player: lambda state: state.has(ItemNames.StageUnlock, player, 7))
    ]
}

alt_stage_progressive_connections = {
    StageNames.Basement1: [
        ConnectionData(StageNames.Downpour1,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 1))
    ],
    StageNames.Basement2: [
        ConnectionData(StageNames.Downpour2,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 2))
    ],
    StageNames.Caves1: [
        ConnectionData(StageNames.Mines1, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 3))
    ],
    StageNames.Caves2: [
        ConnectionData(StageNames.Mines2, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 4))
    ],
    StageNames.Depths1: [
        ConnectionData(StageNames.Mausoleum1,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 5))
    ],
    StageNames.Downpour1: [
        ConnectionData(StageNames.Downpour2,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 2))
    ],
    StageNames.Downpour2: [
        ConnectionData(StageNames.Mines1, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 3))
    ],
    StageNames.Mines1: [
        ConnectionData(StageNames.Mines2, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 4))
    ],
    StageNames.Mines2: [
        ConnectionData(StageNames.Mausoleum1,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 5))
    ],
    StageNames.Mausoleum1: [
        ConnectionData(StageNames.Mausoleum2,
                       lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 6))
    ],
    StageNames.Mausoleum2: [
        ConnectionData(StageNames.Corpse1, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 7))
    ],
    StageNames.Corpse1: [
        ConnectionData(StageNames.Corpse2, lambda player: lambda state: state.has(ItemNames.AltStageUnlock, player, 8))
    ]
}
