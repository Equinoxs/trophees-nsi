import re

d = "m 35.711149,849.6469 -14.578377,-6.31016 -6.48999,-15.33759 -3.103816,-27.51973 6.107205,-56.36425 1.012344,-56.58767 -0.48687,-45.83242 3.211597,-13.50035 62.641006,-31.72915 29.044322,-18.70379 23.06683,-8.24611 42.73966,-4.35908 21.36675,11.64361 23.67049,13.76209 -1.58908,16.70984 -0.70764,32.98497 14.65623,24.21063 11.10866,6.5617 6.48443,13.71868 -1.39968,92.57437 -2.61322,49.83937 -29.85677,5.1062 -50.12615,5.28184 -68.21465,5.29125 z"

def read_next_nbr(cursor: int) -> int:
	match = re.search(r'-?\d+(\.\d+)?', d[cursor:])
	if match:
		number = float(match.group())
		cursor += match.end()
		return number, cursor
	return 0, cursor

def append(path: list, pos_x: int, pos_y: int) -> None:
	path.append([pos_x, pos_y])

def handle_M(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	pos_y, new_cursor_2 = read_next_nbr(new_cursor)
	append(path, pos_x, pos_y)
	return new_cursor_2

def handle_L(cursor: int, path: list[list[int]]) -> int:
	return handle_M(cursor, path)

def handle_V(cursor: int, path: list[list[int]]) -> int:
	pos_y, new_cursor = read_next_nbr(cursor)
	append(path, path[-1][0], pos_y)
	return new_cursor

def handle_H(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	append(path, pos_x, path[-1][1])
	return new_cursor

def handle_m(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	pos_y, new_cursor_2 = read_next_nbr(new_cursor)
	append(path, path[-1][0] + pos_x, path[-1][1] + pos_y)
	return new_cursor_2

def handle_l(cursor: int, path: list[list[int]]) -> int:
	return handle_m(cursor, path)

def handle_v(cursor: int, path: list[list[int]]) -> int:
	pos_y, new_cursor = read_next_nbr(cursor)
	append(path, path[-1][0], path[-1][1] + pos_y)
	return new_cursor

def handle_h(cursor: int, path: list[list[int]]) -> int:
	pos_x, new_cursor = read_next_nbr(cursor)
	append(path, path[-1][0] + pos_x, path[-1][1])
	return new_cursor

def main() -> int:
	cursor = 0
	path = [[0, 0]]

	last_letter = None
	while cursor < len(d):
		while d[cursor] == ' ':
			cursor += 1
		if last_letter is None:
			last_letter = d[cursor]
		cursor_copy = cursor
		match d[cursor]:
			case 'M':
				cursor = handle_M(cursor, path)
			case 'L':
				cursor = handle_L(cursor, path)
			case 'V':
				cursor = handle_V(cursor, path)
			case 'H':
				cursor = handle_H(cursor, path)
			case 'm':
				cursor = handle_m(cursor, path)
			case 'l':
				cursor = handle_l(cursor, path)
			case 'v':
				cursor = handle_v(cursor, path)
			case 'h':
				cursor = handle_h(cursor, path)
			case 'z':
				break
			case _:
				function_name = f'handle_{last_letter}'
				cursor = globals()[function_name](cursor, path)
		if d[cursor_copy] in 'MLVHmlvh':
			last_letter = d[cursor_copy]

	factor = 2.8
	for i in range(1, len(path)):
		path[i][0] = factor * path[i][0]
		path[i][1] = factor * path[i][1]

	print([[int(el[0]), int(el[1])] for el in path[1:]])
	return 0

if __name__ == '__main__':
	main()
