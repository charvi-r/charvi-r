print()
print('**UNIT CONVERTER**')
print()

conversions_available = [(1, 'km', 'mi'),
                        (2, 'mi', 'km'),
                        (3, 'kg', 'lbs'),
                        (4, 'lbs', 'kg'),
                        (5, '°F', '°C'),
                        (6, '°C', '°F'),
                        ]

                        


conversion_number = int(input('Enter the number you want to get converted: '))

for conv_number, from_unit_name, to_unit_name in conversions_available:
    print(f'{conv_number}) {from_unit_name} -> {to_unit_name}')


from_unit = int(input('Enter the conversion you want to get converted: '))

print()
selected_conversion = input('Enter the number of the conversion to use --> ')
conversion_index = int(selected_conversion) - 1

selected_conversion_number, from_unit_name, to_unit_name = conversions_available[conversion_index]
print()
from_value = float(input(f'Enter {from_unit_name} --> '))
print()

if selected_conversion_number == 1:
    to_value = from_value * 0.62
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')
    
elif selected_conversion_number == 2:
    to_value = from_value * 1.61
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')
 
elif selected_conversion_number == 3:
    to_value = from_value * 0.45
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')

elif selected_conversion_number == 4:
    to_value = from_value * 2.22
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')

elif selected_conversion_number == 5:
    to_value = (from_value - 32) / 1.8 
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')
elif selected_conversion_number == 6:
    to_value = from_value * 1.8 + 32
    print(f'{from_value} {from_unit_name} -> {to_value} {to_unit_name}')
