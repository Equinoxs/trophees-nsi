import re

d = "M285 841.5V689V685.5L286.5 686.5L290 689L294 693L301.5 697L308.5 701.5L316 705L324 708L332 711.5L342 714L350 716L358.5 718L368 719.5L376.5 721L385 722L392.5 723.5H400H407.5H414.5H526.5L534.5 723L541.5 720.5L549 718L555 715.5L560 713.5L565 711L570 709L575 705L580 701L585.5 697L590.5 692.5L594 688L598 682.5L600.5 678.5L603.5 673L606.5 667L608.5 662L611 656L613 651L615 645.5L617 640.5L618 634V578H710L719.5 579L726 581.5L733 585L740.5 588.5L747.5 592.5L753 595.5L759.5 598.5L765.5 601L771.5 605L777.5 608.5L782.5 612L787.5 615.5L791.5 619L794.5 623L797.5 628L800 633L802 638.5L803.5 644.5V650.5V787.5L802 794L799.5 800L796.5 806L793 812L789.5 817.5L786.5 822.5L782 828.5L777 834L771.5 838L764.5 840L285 841.5Z"


def read_next_nbr(cursor: int) -> int:
	match = re.search(r'\d+(\.\d+)?', d[cursor:])
	if match:
		number = int(float(match.group()))
		cursor += match.end()
		return number, cursor


def handle_M(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	pos_y, new_cursor_2 = read_next_nbr(new_cursor)
	path.append([pos_x, pos_y])
	return new_cursor_2

def handle_L(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	pos_y, new_cursor_2 = read_next_nbr(new_cursor)
	path.append([pos_x, pos_y])
	return new_cursor_2

def handle_V(cursor: int, path: list[list[int]]) -> int:
	pos_y, new_cursor  = read_next_nbr(cursor)
	path.append([path[-1][0], pos_y])
	return new_cursor

def handle_H(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor  = read_next_nbr(cursor)
	path.append([pos_x, path[-1][1]])
	return new_cursor


def main() -> int:
	cursor: int = 0
	path = []

	while cursor < len(d):
		if d[cursor] == ' ':
			cursor += 1
		match d[cursor]:
			case 'M':
				cursor = handle_M(cursor, path)
			case 'L':
				cursor = handle_L(cursor, path)
			case 'V':
				cursor = handle_V(cursor, path)
			case 'H':
				cursor = handle_H(cursor, path)
			case _:
				break
	print(path)
	return 0

if __name__ == '__main__':
	main()
