alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")

alien_1 = {}
print(f"Print alien_1: {alien_1}")
alien_1['color'] = 'green'
alien_1['points'] = 10
print(f"Print new alien_1:{alien_1}")

print("\n")
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}")

if alien_2['speed'] == 'low':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3

alien_2['x_position'] += x_increment
print(f"New position: {alien_2['x_position']}")

print("\n")
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original kvp:{alien_3}")
del alien_3['speed']
print(f"New kvp:{alien_3}")

print("\n")
point_value = alien_3.get('points', 'No point value assigned.')
print(point_value)