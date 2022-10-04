EMPTY_STRING = "{{0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}, 0x00}, \\"
EMPTY_LIST = ["0x00"] * 8
STRENGTH_TO_STRING = [str(i) for i in range(10)] + ["a", "b", "c", "d", "e", "f"]

# {{0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}, 0x00}
#   row0, row1, row2, ...
# Betyr at nederst til høyre(?) er full styrke


def set_single_pixel(hexlist, coord, strength):
    # Coord is tuple on form (row (bottom = 0), left(0) or right(1))
    # Strength is int from 0 to 15
    list_ind = coord[0]
    right = coord[1]
    old_hex = hexlist[list_ind]
    new_hex = old_hex[:2+right] + STRENGTH_TO_STRING[strength] + old_hex[2+right+1:]
    hexlist[list_ind] = new_hex
    return hexlist


def set_all_pixels_in_list(hexlist, coord_strength_tups):
    for (coord, strength) in coord_strength_tups:
        hexlist = set_single_pixel(hexlist, coord, strength)
    return hexlist


def hexlist_to_string(hexlist):
    hexstr = ", ".join(hexlist)
    hexstr = "{{" + hexstr + "}, 0x00}, \\"
    return hexstr


if __name__ == "__main__":
    hxlist = set_all_pixels_in_list(EMPTY_LIST, [((2, 0), 12), ((3, 1), 12), ((4, 0), 12), ((4, 1), 2), ((2, 0), 13)])
    print(hxlist)
    print(hexlist_to_string(hxlist))