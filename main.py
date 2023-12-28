import pygame
import os

pygame.init()
BLOCK_SIZE = 50

grass_images = {
    'G1':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'grassblock1.png')),
    'G2':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'grassblock2.png')),
    'RL':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadCornerLL.png')),
    'RR':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadCornerLR.png')),
    'UL':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadCornerUL.png')),
    'UR':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadCornerUR.png')),
    'RC':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadCrossing.png')),
    'RR1':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass',
                     'roadCrossingRound.png')),
    'RE':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadEast.png')),
    'RN':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadNorth.png')),
    'RK':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadSplitE.png')),
    'R+':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadSplitN.png')),
    'RS':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadSplitS.png')),
    'RW':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'grass', 'roadSplitW.png'))
}

element_images = {
    'barrelBlack_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelBlack_side.png')),
    'barrelBlack_top':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelBlack_top.png')),
    'barrelGreen_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelGreen_side.png')),
    'barrelGreen_top':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelGreen_top.png')),
    'barrelRed_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelRed_side.png')),
    'barrelRed_top':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelRed_top.png')),
    'barrelRust_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelRust_side.png')),
    'barrelRust_top':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barrelRust_top.png')),
    'barricadeMetal':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barricadeMetal.png')),
    'barricadeWood':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'barricadeWood.png')),
    'crateMetal':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements', 'crateMetal.png')),
    'crateMetal_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'crateMetal_side.png')),
    'crateWood':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements', 'crateWood.png')),
    'crateWood_side':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'crateWood_side.png')),
    'fenceRedHoriz':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'fenceRedHoriz.png')),
    'fenceYellowHoriz':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'fenceYellowHoriz.png')),
    'fenceRedVert':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'fenceRedVert.png')),
    'fenceYellowVert':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'fenceYellowVert.png')),
    'oilSpill_large':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'oilSpill_large.png')),
    'oilSpill_small':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'oilSpill_small.png')),
    'sandbagBeige':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'sandbagBeige.png')),
    'sandbagBeige_open':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'sandbagBeige_open.png')),
    'sandbagBrown':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'sandbagBrown.png')),
    'sandbagBrown_open':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'sandbagBrown_open.png')),
    'treeBrown_large':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeBrown_large.png')),
    'treeBrown_leaf':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeBrown_leaf.png')),
    'treeBrown_small':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeBrown_small.png')),
    'treeBrown_twigs':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeBrown_twigs.png')),
    'treeGreen_large':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeGreen_large.png')),
    'treeGreen_leaf':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeGreen_leaf.png')),
    'treeGreen_small':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeGreen_small.png')),
    'treeGreen_twigs':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'treeGreen_twigs.png')),
    'wireCrooked':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'wireCrooked.png')),
    'wireStraight':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'elements',
                     'wireStraight.png')),
}

sand_images = {
    'S1':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'sandblock1.png')),
    'S2':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'sandblock2.png')),
    'RL':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadCornerLL.png')),
    'RR':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadCornerLR.png')),
    'UL':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadCornerUL.png')),
    'UR':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadCornerUR.png')),
    'RC':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadCrossing.png')),
    'RR1':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand',
                     'roadCrossingRound.png')),
    'RE':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadEast.png')),
    'RN':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadNorth.png')),
    'RK':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadSplitE.png')),
    'R+':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadSplitN.png')),
    'RS':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadSplitS.png')),
    'RW':
    pygame.image.load(
        os.path.join('src', 'assets', 'locale', 'sand', 'roadSplitW.png'))
}

levels = [
    [
        [
            'G1', 'G1', 'G1', 'G1', 'G1', 'G1', 'G1', 'G1', 'G2', 'G1', 'G1',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G1', 'G1', 'G1', 'G1'
        ],
        [
            'G1', 'RR', 'RE', 'RE', 'RS', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE',
            'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RS', 'RE', 'RE', 'RE',
            'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RL', 'G1'
        ],
        [
            'G1', 'RN', 'G2', 'G1', 'RN', 'G2', 'G1', 'G2', 'G1', 'G1', 'G1',
            'G2', 'G1', 'G2', 'G2', 'G1', 'G1', 'G2', 'RN', 'G1', 'G2', 'G2',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'RN', 'G1'
        ],
        [
            'G1', 'RN', 'G1', 'G1', 'RN', 'G1', 'G2', 'G1', 'G1', 'G1', 'G2',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G2', 'G1', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G1'
        ],
        [
            'G2', 'RN', 'G1', 'G2', 'RN', 'G2', 'G2', 'G1', 'G1', 'G2', 'G1',
            'G1', 'G2', 'G2', 'G2', 'G2', 'G1', 'G1', 'RN', 'G1', 'G1', 'G1',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G2', 'RN', 'G1'
        ],
        [
            'G1', 'RN', 'G2', 'G1', 'RN', 'G1', 'G2', 'G2', 'G2', 'G1', 'G1',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G2', 'G2', 'RN', 'G1', 'G2', 'G1',
            'G1', 'G1', 'G2', 'G2', 'G1', 'G2', 'RN', 'G1'
        ],
        [
            'G1', 'RN', 'G1', 'G1', 'RN', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G2', 'G1', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G1'
        ],
        [
            'G2', 'RN', 'G1', 'G2', 'RN', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'RK', 'RE', 'RE', 'RE',
            'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RW', 'G2'
        ],
        [
            'G1', 'RN', 'G2', 'G1', 'UR', 'RE', 'RE', 'RE', 'RE', 'RE', 'RL',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'RN', 'G1', 'G2', 'G1',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'RN', 'G1'
        ],
        [
            'G1', 'RN', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'RN',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G2', 'G1', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G1'
        ],
        [
            'G2', 'RN', 'G1', 'G2', 'G1', 'G1', 'G2', 'G2', 'G2', 'G2', 'RN',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'RN', 'G1', 'G1', 'G1',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'RN', 'G2'
        ],
        [
            'G1', 'RN', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'RN', 'G1', 'G2', 'G1',
            'G1', 'G1', 'G2', 'G1', 'G2', 'G2', 'RN', 'G2'
        ],
        [
            'G2', 'RN', 'G2', 'G1', 'G2', 'G1', 'G1', 'G2', 'G2', 'G2', 'RN',
            'G2', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G2', 'G1', 'G1',
            'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'RN', 'G1'
        ],
        [
            'G2', 'UR', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'R+',
            'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'R+', 'RE', 'RE', 'RE',
            'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'UL', 'G2'
        ],
        [
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1',
            'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1',
            'G1', 'G1', 'G2', 'G1', 'G1', 'G2', 'G1', 'G1'
        ],
    ],
]

new = [[
    'S1' if elem == 'G1' else 'S2' if elem == 'G2' else elem for elem in row
] for row in levels[0]]

object_coords_sand = [
    (2, 1.1, 'fenceRedHoriz'),
    (5, 4.1, 'fenceRedHoriz'),
    (13.1, 3.9, 'fenceRedVert'),
    (8.1, 7.9, 'fenceRedVert'),
    (1, 15, 'fenceYellowVert'),
    (1, 27, 'fenceYellowVert'),
    (7, 24, 'fenceYellowVert'),
    (9, 14, 'treeBrown_large'),
    (10, 15, 'treeBrown_small'),
    (8.8, 15, 'treeBrown_twigs'),
    (10.3, 14, 'treeBrown_twigs'),
]
object_coords_grass = [
    (2, 1.1, 'fenceRedHoriz'),
    (5, 4.1, 'fenceRedHoriz'),
    (13.1, 3.9, 'fenceRedVert'),
    (8.1, 7.9, 'fenceRedVert'),
    (1, 15, 'fenceYellowVert'),
    (1, 27, 'fenceYellowVert'),
    (7, 24, 'fenceYellowVert'),
    (9, 14, 'treeGreen_large'),
    (10, 15, 'treeGreen_small'),
    (8.8, 15, 'treeGreen_twigs'),
    (10.3, 14, 'treeGreen_twigs'),
]


def draw_objects_sand(screen, object_coords_sand):
  for row, col, object_key in object_coords_sand:
    if object_key in element_images:
      x = col * BLOCK_SIZE
      y = row * BLOCK_SIZE
      screen.blit(element_images[object_key], (x, y))


def draw_objects_grass(screen, object_coords_grass):
  for row, col, object_key in object_coords_grass:
    if object_key in element_images:
      x = col * BLOCK_SIZE
      y = row * BLOCK_SIZE
      screen.blit(element_images[object_key], (x, y))


def draw_level_grass(level, screen):
  for row_index, row in enumerate(level):
    for col_index, cell in enumerate(row):
      x = col_index * BLOCK_SIZE
      y = row_index * BLOCK_SIZE
      if cell in grass_images:
        screen.blit(grass_images[cell], (x, y))


def draw_level_sand(level, screen):
  for row_index, row in enumerate(level):
    for col_index, cell in enumerate(row):
      x = col_index * BLOCK_SIZE
      y = row_index * BLOCK_SIZE
      if cell in sand_images:
        screen.blit(sand_images[cell], (x, y))


screen = pygame.display.set_mode((BLOCK_SIZE * 30, BLOCK_SIZE * 15))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((0, 0, 0))
  #draw_level_grass(levels[0], screen)
  #draw_objects_sand(screen, object_coords_grass)
  draw_level_sand(new, screen)
  draw_objects_sand(screen, object_coords_sand)

  pygame.display.flip()

pygame.quit()
