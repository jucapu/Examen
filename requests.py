const fetch = require('node-fetch'); // Si estás trabajando en Node.js
// O si estás en un navegador, simplemente usa 'fetch'

const getUsersData = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const users = await response.json();

        // Filtrar los usuarios con IDs 6 y 8
        const user6 = users.find(user => user.id === 6);
        const user8 = users.find(user => user.id === 8);

        // Calcular las edades (suponiendo que tenemos la fecha de nacimiento)
        const currentDate = new Date();
        const birthDate6 = new Date(user6.birthdate); // Reemplaza 'birthdate' con el campo real
        const birthDate8 = new Date(user8.birthdate); // Reemplaza 'birthdate' con el campo real
        const age6 = currentDate.getFullYear() - birthDate6.getFullYear();
        const age8 = currentDate.getFullYear() - birthDate8.getFullYear();

        // Mostrar en consola
        console.log(`Usuario ${user6.name} tiene ${age6} años.`);
        console.log(`Usuario ${user8.name} tiene ${age8} años.`);

        // Comparar edades
        if (age6 > age8) {
            console.log(`${user6.name} es mayor que ${user8.name}.`);
        } else if (age8 > age6) {
            console.log(`${user8.name} es mayor que ${user6.name}.`);
        } else {
            console.log(`${user6.name} y ${user8.name} tienen la misma edad.`);
        }
    } catch (error) {
        console.error('Error al obtener datos de usuarios:', error);
    }
};

getUsersData();
