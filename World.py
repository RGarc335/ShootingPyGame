import Soldier
import ItemBox
import Decoration
import HealthBar
import Water
import Exit

class World():
    def __init__(self, TILE_SIZE, screen_scroll):
        self.obstacle_list = []
        self.TILE_SIZE = TILE_SIZE
        self.screen_scroll = screen_scroll

    def process_data(self, data, img_list, water_group, decoration_group, enemy_group, item_box_group, exit_group):
        self.level_length = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * self.TILE_SIZE
                    img_rect.y = y * self.TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * self.TILE_SIZE, y * self.TILE_SIZE)
                        water_group.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(img, x * self.TILE_SIZE, y * self.TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 15:  # create player
                        player = Soldier('player', x * self.TILE_SIZE, y * self.TILE_SIZE, 1.65, 5, 20, 5)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 16:  # create enemies
                        enemy = Soldier('enemy', x * self.TILE_SIZE, y * self.TILE_SIZE, 1.65, 2, 20, 0)
                        enemy_group.add(enemy)
                    elif tile == 17:  # create ammo box
                        item_box = ItemBox('Ammo', x * self.TILE_SIZE, y * self.TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 18:  # create grenade box
                        item_box = ItemBox('Grenade', x * self.TILE_SIZE, y * self.TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 19:  # create health box
                        item_box = ItemBox('Health', x * self.TILE_SIZE, y * self.TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 20:  # create exit
                        exit = Exit(img, x * self.TILE_SIZE, y * self.TILE_SIZE)
                        exit_group.add(exit)

        return player, health_bar

    def draw(self, screen):
        for tile in self.obstacle_list:
            tile[1][0] += self.screen_scroll
            screen.blit(tile[0], tile[1])
