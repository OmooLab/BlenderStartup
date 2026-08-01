SELECTOR_TILE_WIDTH = 160.0
SELECTOR_TILE_HEIGHT = 90.0
SELECTOR_TILE_GAP = 8.0
SELECTOR_MARGIN = 12.0
SELECTOR_MAX_COLUMNS = 4


def selector_tile_rects(
    count,
    region_width,
    region_height,
    anchor_x,
    anchor_y,
):
    if count <= 0:
        return []

    columns = min(SELECTOR_MAX_COLUMNS, count)
    rows = (count + columns - 1) // columns
    content_width = (
        columns * SELECTOR_TILE_WIDTH
        + (columns - 1) * SELECTOR_TILE_GAP
    )
    content_height = (
        rows * SELECTOR_TILE_HEIGHT
        + (rows - 1) * SELECTOR_TILE_GAP
    )
    available_width = max(1.0, region_width - SELECTOR_MARGIN * 2.0)
    available_height = max(1.0, region_height - SELECTOR_MARGIN * 2.0)
    scale = min(
        1.0,
        available_width / content_width,
        available_height / content_height,
    )
    tile_width = SELECTOR_TILE_WIDTH * scale
    tile_height = SELECTOR_TILE_HEIGHT * scale
    gap = SELECTOR_TILE_GAP * scale
    panel_width = columns * tile_width + (columns - 1) * gap
    panel_height = rows * tile_height + (rows - 1) * gap

    left = min(
        max(SELECTOR_MARGIN, anchor_x - panel_width / 2.0),
        region_width - SELECTOR_MARGIN - panel_width,
    )
    bottom = min(
        max(SELECTOR_MARGIN, anchor_y - panel_height / 2.0),
        region_height - SELECTOR_MARGIN - panel_height,
    )

    rects = []
    for index in range(count):
        column = index % columns
        row = index // columns
        x_min = left + column * (tile_width + gap)
        y_max = bottom + panel_height - row * (tile_height + gap)
        rects.append(
            (
                x_min,
                y_max - tile_height,
                x_min + tile_width,
                y_max,
            )
        )
    return rects
