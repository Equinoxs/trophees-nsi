import json
import os


map_target = 'bletchley_park'
file_path = os.path.join(os.path.dirname(__file__), '..', 'backups', 'new_game_backup.json')

def get_backup():
	with open(file_path, "r") as file:
		data = json.load(file)
	return data

def divide_by(divider, backup):
    for element in backup['maps'][map_target]['elements']:
        if element['type'] not in ['Wall', 'GroundSurface']:
            continue
        for i in range(len(element['boundaries'])):
            element['boundaries'][i][0] /= divider
            element['boundaries'][i][1] /= divider
            element['boundaries'][i][0] = int(element['boundaries'][i][0])
            element['boundaries'][i][1] = int(element['boundaries'][i][1])

def register_data(data):
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)


def main():
    backup = get_backup()
    divide_by(1, backup)
    print(backup)
    # register_data(backup)


if __name__ == '__main__':
	main()

