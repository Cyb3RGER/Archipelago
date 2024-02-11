import logging
import string

from BaseClasses import Region, Entrance, Item, MultiWorld, Tutorial, ItemClassification, CollectionState
from worlds.AutoWorld import World, WebWorld
from .Items import TheBindingOfIsaacRepentanceItem, item_table, default_weights, default_junk_items_weights, \
    default_trap_items_weights
from .Locations import location_table, TheBindingOfIsaacRepentanceLocation, base_location_table
from .Options import IsaacOptions, ItemWeights
from .Rules import set_rules


class TheBindingOfIsaacRepentanceWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the The Binding Of Isaac Repentance integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cyb3R"]
    )]


class TheBindingOfIsaacRepentanceWorld(World):
    """
    The Binding of Isaac: Rebirth is a randomly generated action RPG shooter with heavy Rogue-like elements.
    Following Isaac on his journey players will find bizarre treasures that change Isaac’s form giving him super
    human abilities and enabling him to fight off droves of mysterious creatures, discover secrets and fight his way
    to safety.
    """
    game = "The Binding of Isaac Repentance"
    options_dataclass = IsaacOptions
    options: IsaacOptions
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = location_table
    item_name_groups = {
        "Any Progression": [name for name, data in item_table.items() if data.is_progression() and data.id is not None]}

    web = TheBindingOfIsaacRepentanceWeb()

    progression_item_count: int = 0
    trap_item_count: int = 0
    junk_item_count: int = 0
    required_prog_item_factor: float = 0.6

    def generate_early(self) -> None:
        if not self.multiworld.player_name[self.player].isalnum():
            logging.warning(f"The name {self.multiworld.player_name[self.player]} for a TBoI world contains "
                            f"non-alphanumerical characters. You are not guaranteed to be able to enter the name "
                            f"ingame and may have to edit the games savefile to connect.")
        if self.options.required_locations.value > self.options.total_locations.value:
            self.options.total_locations.value = self.options.required_locations.value

        self.junk_item_count = round(
            self.options.total_locations.value * (self.options.junk_percentage.value / 100))
        self.progression_item_count = self.options.total_locations.value - self.junk_item_count

        self.trap_item_count = round(
            self.junk_item_count * (self.options.trap_percentage.value / 100))
        self.junk_item_count = self.junk_item_count - self.trap_item_count

    def create_items(self):
        # Generate item pool
        itempool = []

        if self.options.item_weights.value == ItemWeights.option_custom:
            item_weights = {name: val for name, val in self.options.custom_item_weights.value.items()}
        else:
            item_weights = default_weights

        # Fill non-junk items
        itempool += self.random.choices(list(item_weights.keys()), weights=list(item_weights.values()),
                                                   k=self.progression_item_count)

        trap_weights = {name: val for name, val in self.options.trap_item_weights.value.items()}
        junk_weights = {name: val for name, val in self.options.custom_junk_item_weights.value.items()}

        # Fill traps
        itempool += self.random.choices(list(trap_weights.keys()), weights=list(trap_weights.values()),
                                                   k=self.trap_item_count)

        # Fill remaining items with randomly generated junk
        itempool += self.random.choices(list(junk_weights.keys()), weights=list(junk_weights.values()),
                                                   k=self.junk_item_count)

        assert len(itempool) == self.options.total_locations.value

        # Convert itempool into real items
        itempool = list(map(lambda name: self.create_item(name), itempool))

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.progression_item_count, self.required_prog_item_factor)

    def create_regions(self):
        create_regions(self.multiworld, self.player, int(self.options.total_locations.value),
                       self.progression_item_count, self.required_prog_item_factor)

    def fill_slot_data(self):
        return {
            "itemPickupStep": self.options.item_pickup_step.value,
            "seed": "".join(self.random.choice(string.digits) for _ in range(16)),
            "totalLocations": self.options.total_locations.value,
            "requiredLocations": self.options.required_locations.value,
            "goal": self.options.goal.value,
            "additionalBossRewards": self.options.additional_boss_rewards.value,
            "deathLink": self.options.death_link.value,
            "teleportTrapCanError": self.options.teleport_trap_can_error.value,
            "fullNoteAmount": self.options.full_note_amount.value,
            "noteMarksAmount": self.options.note_marks_amount.value,
            "noteMarkRequireHardMode": self.options.note_marks_require_hard_mode.value,
            "splitStartItems": self.options.split_start_items.value
        }

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = TheBindingOfIsaacRepentanceItem(name, item_data.classification, item_data.id, self.player)
        return item

    def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False):
        if item.advancement and item.code:
            return "Progression Item"

        return super(TheBindingOfIsaacRepentanceWorld, self).collect_item(state, item, remove)


# generate locations based on player setting
def create_regions(world, player: int, total_locations: int, progression_item_count: int,
                   required_prog_item_factor: float):
    world.regions += [
        create_region(world, player, "Menu", None, ["New Run"]),
    ]
    # setup regions
    locations_per_section = 25
    num_of_sections = total_locations // locations_per_section
    if total_locations / locations_per_section == num_of_sections:
        num_of_sections -= 1
    num_of_sections += 1
    assert num_of_sections > 1
    for i in range(num_of_sections):
        locations = [f"ItemPickup{n}" for n in
                     range(i * locations_per_section + 1,
                           min(total_locations + 1, (i + 1) * locations_per_section + 1))]
        if i == num_of_sections - 1:
            locations += [location for location in base_location_table]
        world.regions.append(create_region(world, player, f"Run Section {i + 1}", locations))

    # setup connections
    world.get_entrance("New Run", player).connect(world.get_region("Run Section 1", player))
    for i in range(1, num_of_sections):
        source_region = world.get_region(f"Run Section {i}", player)
        target_region = world.get_region(f"Run Section {i + 1}", player)
        connection = Entrance(player, f"From Section {i} To Section {i + 1}", source_region)
        needed = round(i * ((progression_item_count * required_prog_item_factor) / (
                (2 - ((i - 1) / (num_of_sections - 1))) * num_of_sections)))
        connection.access_rule = lambda state, n=needed: state.has(f"Progression Item", player, n)
        source_region.exits.append(connection)
        connection.connect(target_region)

    world.get_location("Run End", player).place_locked_item(
        TheBindingOfIsaacRepentanceItem("Victory", ItemClassification.progression, None, player))


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    ret.world = world
    if locations:
        for location in locations:
            loc_id = location_table[location]
            location = TheBindingOfIsaacRepentanceLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for _exit in exits:
            ret.exits.append(Entrance(player, _exit, ret))

    return ret
