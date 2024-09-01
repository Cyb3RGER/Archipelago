import typing
from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, Range, Choice, DeathLink, OptionDict, PerGameCommonOptions
from .Items import default_weights, default_junk_items_weights, default_trap_items_weights, collectible_items, \
    junk_items, trap_items


class TotalLocations(Range):
    """Number of location checks which are added."""
    display_name = "Total Locations"
    range_start = 10
    range_end = 500
    default = 125


class RequiredLocations(Range):
    # ToDo: make this a percentage? + Add warning for when these are actually required
    """Number of location checks required to beat the game."""
    display_name = "Required Locations"
    range_start = 1
    range_end = 500
    default = 75


class Goal(Choice):
    """Goal to finish the run. Note that note marks and full notes do not include the Cent Sign note mark as greed mode is
    not supported yet. """
    display_name = "Goal"
    option_mom = 0
    option_moms_heart = 1
    option_isaac_satan = 2
    option_isaac = 3
    option_satan = 4
    option_blue_baby_lamb = 5
    option_blue_baby = 6
    option_lamb = 7
    option_mega_satan = 8
    option_boss_rush = 9
    option_hush = 10
    option_dogma = 11
    option_beast = 12
    option_mother = 13
    option_delirium = 14
    option_required_locations = 15
    option_full_notes = 16
    option_note_marks = 17
    default = 5


class NoteMarkAmount(Range):
    """Number of note marks needed to beat the game (if goal is note marks). """
    display_name = "Note Mark Amount"
    range_start = 1
    range_end = 374
    default = 20


class FullNoteAmount(Range):
    """Number of full notes needed to beat the game (if goal is full notes).  """
    display_name = "Full Note Amount"
    range_start = 1
    range_end = 34
    default = 1


class NoteMarksRequireHardMode(Toggle):
    """If set on Note Marks are only considered complete if the run was on hard mode.
    Relevant for both full notes and note marks goal"""
    display_name = "Note Marks Require Hard Mode"


class ItemPickupStep(Range):
    """Number of items to pick up before an AP Check is completed.
    Setting to 1 means every pickup,
    Setting to 2 means every other pickup,
    Setting to 3 means every third pickup and so on..."""
    display_name = "Item Pickup Step"
    range_start = 1
    range_end = 5
    default = 1


class StageUnlocks(Choice):
    """
    Determine how stages are unlocked in AP.
    Not every stage has a unique
    None: Stages are not locked.
    Progressive: Stages are locked behind progressive unlock items.
    Unique: Stages can be unlocked out of order.
    """
    display_name = "Stage Unlocks"
    option_none = 0
    option_progressive = 1
    option_unique = 2
    default = 1


class IncludeAltStageUnlocks(Toggle):
    """
    Includes unlock items for alternative stage.
    Requires Logic Mode to be set to a stage unlock mode.
    """
    display_name = "Include Alternative Stage Unlocks"


class LocationsByStage(DefaultOnToggle):
    """
    Splits locations per stage so specific locations are mapped to a stage (i.e. Basement I, Basement II, etc.).
    """
    display_name = "Locations By Stage"


class IncludeAltStageLocations(DefaultOnToggle):
    """
    Should alternative stages (Downpour/Mines/Mausoleum/Corpse I/II) have separate locations to their counterparts.
    This brings the total number of stages from 15 to 23.
    """


class LocationsByRoomType(DefaultOnToggle):
    """
    Splits locations per room type so specific locations are mapped to a certain room type (i.e. Treasure room, Planetarium).
    """
    display_name = "Locations By Room Type"


class LocationAmountShop(Range):
    """
    Amount of locations in Shops.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Shop"
    range_start = 0
    range_end = 50
    default = 15


class LocationAmountTreasure(Range):
    """
    Amount of locations in Treasure Rooms.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Treasure Room"
    range_start = 0
    range_end = 50
    default = 25


class LocationAmountBoss(Range):
    """
    Amount of locations in Boss Rooms.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Boss Room"
    range_start = 0
    range_end = 50
    default = 20


class LocationAmountSecret(Range):
    """
    Amount of locations in Secret Rooms.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Secret Room"
    range_start = 0
    range_end = 50
    default = 3


class LocationAmountDevil(Range):
    """
    Amount of locations in Devil Deals.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Devil Deal"
    range_start = 0
    range_end = 50
    default = 15


class LocationAmountAngel(Range):
    """
    Amount of locations in Angel Deals.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Angel Deal"
    range_start = 0
    range_end = 50
    default = 15


class LocationAmountPlanetarium(Range):
    """
    Amount of locations in Planetariums.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Planetarium"
    range_start = 0
    range_end = 50
    default = 2


class LocationAmountOther(Range):
    """
    Amount of locations in all other rooms.
    When "Locations Per Stage" is non-0, this is not an absolute amount but rather a weight.
    Needs "Locations By Room Type" to be on.
    """
    display_name = "Location Amount: Other Rooms"
    range_start = 0
    range_end = 50
    default = 5


class AdditonalBossRewards(DefaultOnToggle):
    """If enabled all goal bosses will reward additional checks.
    The amount of checks if determined on how deep the boss in the run:
    Mom = 1
    Mom's Heart/Boss Rush = 2
    Isaac/Satan/Hush = 3
    Blue Baby/The Lamb = 4
    Mega Satan/Mother/Beast/Delirium = 5
    exception:
    Dogma = 0
    """
    display_name = "Additional Boss Rewards"


class CollectibleAmount(Range):
    """Amount of Collectibles to find. This will be capped by the total amount of locations available."""
    display_name = "Collectible Amount"
    range_start = 20
    range_end = 100
    default = 30


# class JunkPercentage(Range):
#     """Percentage of junk items (Non-Collectable Pickups like Coins, Bombs etc.)"""
#     display_name = "Junk Percentage"
#     range_start = 0
#     range_end = 100
#     default = 75


class TrapPercentage(Range):
    """Replaces a percentage of junk items with traps"""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class TeleportTrapCanError(DefaultOnToggle):
    """Can a Teleport Trap teleport to an Error Room?"""
    display_name = "Teleport Trap can teleport to Error Room"


class ItemWeights(Choice):
    """Preset choices for determining the weights of the item pool."""
    display_name = "Item Weights"
    option_default = 0
    option_custom = 99


class CustomItemWeightsBase(OptionDict):

    def __init__(self, value: typing.Dict[str, int]):
        if len(value) <= 0:
            value = self.default
        if any(value < 0 for value in value.values()):
            raise Exception("Cannot have negative value.")
        if sum(value.values()) <= 0:
            raise Exception("Sum of all values cannot be non-positive")
        super(CustomItemWeightsBase, self).__init__(value)


class CustomItemWeights(CustomItemWeightsBase):
    """
    Put your custom item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for progression items. For junk and trap items use Custom Junk Item Weights and Trap Item
    Weights.
    """
    display_name = "Custom Item Weights"
    default = default_weights
    valid_keys = {key for key in collectible_items.keys()}


class CustomJunkItemWeights(CustomItemWeightsBase):
    """
    Put your custom junk item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for junk items. For progression and trap items use Custom Item Weights and Trap Item
    Weights.
    """
    display_name = "Custom Junk Item Weights"
    default = default_junk_items_weights
    valid_keys = {key for key in junk_items.keys()}


class TrapItemWeights(CustomItemWeightsBase):
    """
    Put your custom trap item weights here. Format is item_name: weighting. Leave empty for default weighting. These
    weights are only for trap items. For progression and junk items use Custom Item Weights and Custom Junk Item
    Weights.
    """
    display_name = "Custom Trap Item Weights"
    default = default_trap_items_weights
    valid_keys = {key for key in trap_items.keys()}


class SplitStartItems(Choice):
    """
    Will split items already received on run start to be received over multiple floors.
    This is to avoid getting to many items early and make runs more interesting.
    Always 6 will always divide items over the first 6 floors.
    Furthest will base the division on your furthest run so far.
    """
    display_name = "Split Items received on start"
    option_off = 0
    option_on_always_6 = 1
    option_on_furthest = 2


@dataclass
class IsaacOptions(PerGameCommonOptions):
    stage_unlocks: StageUnlocks
    include_alt_stage_unlocks: IncludeAltStageUnlocks
    locations_by_stage: LocationsByStage
    include_alt_stage_locations: IncludeAltStageLocations
    locations_by_room_type: LocationsByRoomType
    location_amount_treasure: LocationAmountTreasure
    location_amount_shop: LocationAmountShop
    location_amount_boss: LocationAmountBoss
    location_amount_secret: LocationAmountSecret
    location_amount_angel: LocationAmountAngel
    location_amount_devil: LocationAmountDevil
    location_amount_planetarium: LocationAmountPlanetarium
    location_amount_other: LocationAmountOther
    total_locations: TotalLocations
    required_locations: RequiredLocations
    item_pickup_step: ItemPickupStep
    goal: Goal
    full_note_amount: FullNoteAmount
    note_marks_amount: NoteMarkAmount
    note_marks_require_hard_mode: NoteMarksRequireHardMode
    item_weights: ItemWeights
    custom_item_weights: CustomItemWeights
    collectible_amount: CollectibleAmount
    # junk_percentage: JunkPercentage
    custom_junk_item_weights: CustomJunkItemWeights
    trap_percentage: TrapPercentage
    trap_item_weights: TrapItemWeights
    teleport_trap_can_error: TeleportTrapCanError
    additional_boss_rewards: AdditonalBossRewards
    death_link: DeathLink
    split_start_items: SplitStartItems
