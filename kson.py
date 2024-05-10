import requests

def get_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for user {user_id}")
        return None

def calculate_age(birthdate):
    # Suponiendo que la fecha de nacimiento está en el formato "YYYY-MM-DD"
    birth_year = int(birthdate.split("-")[0])
    current_year = datetime.datetime.now().year
    return current_year - birth_year

# Obtener datos de los usuarios con IDs 6 y 8
user6_data = get_user_data(6)
user8_data = get_user_data(8)

if user6_data and user8_data:
    # Calcular edades
    user6_age = calculate_age(user6_data["birthdate"])
    user8_age = calculate_age(user8_data["birthdate"])

    # Comparar edades
    if user6_age > user8_age:
        print(f"{user6_data['name']} es mayor que {user8_data['name']}.")
    elif user6_age < user8_age:
        print(f"{user8_data['name']} es mayor que {user6_data['name']}.")
    else:
        print(f"{user6_data['name']} y {user8_data['name']} tienen la misma edad.")
else:
    print("No se pudieron obtener los datos de los usuarios.")
