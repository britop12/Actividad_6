import pandas as pd

def create_row(datos):

    print('Ingrese los datos del nuevo registro')

    nombre = input('Nombre: ')
    assert nombre != '' and nombre.isalpha(), 'El nombre no puede estar vacío y debe ser alfabético'

    apellido = input('Apellido: ')
    assert apellido != '' and apellido.isalpha(), 'El apellido no puede estar vacío y debe ser alfabético'

    edad = input('Edad: ')
    assert edad != '' and edad.isnumeric(), 'La edad no puede estar vacía y debe ser numérica'

    cedula = input('Cédula: ')
    assert cedula != '' and cedula.isnumeric(), 'La cédula no puede estar vacía y debe ser numérica'

    datos.loc[len(datos)] = [nombre, apellido, int(edad), int(cedula)]

    print('Registro creado exitosamente')

    return datos

def update_row(datos):

    print('Ingrese el número de cédula del registro a actualizar')

    cedula = input('Cédula: ')
    assert cedula != '' and cedula.isnumeric(), 'La cédula no puede estar vacía y debe ser numérica'

    if int(cedula) in datos['Cedula'].unique():
            
            print('Ingrese los nuevos datos del registro')
    
            nombre = input('Nombre: ')
            assert nombre != '' and nombre.isalpha(), 'El nombre no puede estar vacío y debe ser alfabético'
    
            apellido = input('Apellido: ')
            assert apellido != '' and apellido.isalpha(), 'El apellido no puede estar vacío y debe ser alfabético'
    
            edad = input('Edad: ')
            assert edad != '' and edad.isnumeric(), 'La edad no puede estar vacía y debe ser numérica'
    
            datos.loc[datos['Cedula'] == int(cedula)] = [nombre, apellido, int(edad), int(cedula)]
    
            print('Registro actualizado exitosamente')

    else:

        print('No se encontró el registro')

    return datos

def delete_row(datos):

    print('Ingrese el número de cédula del registro a eliminar')

    cedula = input('Cédula: ')
    assert cedula != '' and cedula.isnumeric(), 'La cédula no puede estar vacía y debe ser numérica'

    if int(cedula) in datos['Cedula'].unique():

        datos = datos[datos['Cedula'] != int(cedula)]
        print('Registro eliminado exitosamente')

    else:

        print('No se encontró el registro')

    return datos

def show_table(datos):
    print()
    print(datos.to_string())
    print()

def show_menu():

    print()
    print('1. Crear registro')
    print('2. Actualizar registro')
    print('3. Eliminar registro')
    print('4. Mostrar tabla')
    print('5. Salir')
    print()

    opcion = input('Opción: ')
    assert opcion != '' and opcion.isnumeric(), 'La opción no puede estar vacía y debe ser numérica'

    return opcion

def main():

    print('Bienvenido al sistema de gestión de datos')

    datos = pd.read_csv('datos.csv')

    opcion = show_menu()

    while opcion != '5':

        if opcion == '1':

            datos = create_row(datos)

        elif opcion == '2':

            datos = update_row(datos)

        elif opcion == '3':

            datos = delete_row(datos)

        elif opcion == '4':

            show_table(datos)

        else:

            print('Opción inválida')

        opcion = show_menu()

    datos.to_csv('datos.csv', index=False)

    print('Hasta luego')

if __name__ == '__main__':
    main()