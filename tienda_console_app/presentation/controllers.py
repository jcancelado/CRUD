class Controller:
    def __init__(self, repo, ui):
        self.repo = repo
        self.ui = ui

    def run(self):
        while True:
            self.ui.show_menu('Menu principal', [
                ('1','Clientes'),
                ('2','Productos'),
                ('0','Salir')
            ])
            choice = self.ui.input('> ').strip()
            if choice == '1':
                self.customers_menu()
            elif choice == '2':
                self.products_menu()
            elif choice == '0':
                print('Adiós!')
                break
            else:
                print('Opción no válida')

    # Customers
    def customers_menu(self):
        while True:
            self.ui.show_menu('Clientes', [
                ('1','Listar clientes'),
                ('2','Agregar cliente'),
                ('3','Editar cliente'),
                ('4','Eliminar cliente'),
                ('5','Ver deuda de un cliente'),
                ('0','Volver')
            ])
            choice = self.ui.input('> ').strip()
            if choice == '1':
                self.list_customers()
            elif choice == '2':
                self.add_customer()
            elif choice == '3':
                self.edit_customer()
            elif choice == '4':
                self.delete_customer()
            elif choice == '5':
                self.show_debt()
            elif choice == '0':
                break
            else:
                print('Opción no válida')

    def list_customers(self):
        customers = self.repo.list_customers()
        if not customers:
            print('No hay clientes.')
        else:
            for c in customers:
                print(f"ID:{c['id']} - {c.get('name')} - Deuda: {c.get('debt',0)}")
        self.ui.pause()

    def add_customer(self):
        name = self.ui.input('Nombre: ').strip()
        debt = float(self.ui.input('Deuda inicial (0): ') or 0)
        customer = {'name': name, 'debt': debt}
        self.repo.add_customer(customer)
        print('Cliente agregado.')
        self.ui.pause()

    def edit_customer(self):
        try:
            cid = int(self.ui.input('ID cliente a editar: '))
        except:
            print('ID inválido')
            return
        c = self.repo.get_customer(cid)
        if not c:
            print('Cliente no encontrado')
            return
        name = self.ui.input(f"Nombre ({c.get('name')}): ").strip() or c.get('name')
        debt = self.ui.input(f"Deuda ({c.get('debt',0)}): ").strip()
        debt = float(debt) if debt != '' else c.get('debt',0)
        self.repo.update_customer(cid, {'name': name, 'debt': debt})
        print('Cliente actualizado.')
        self.ui.pause()

    def delete_customer(self):
        try:
            cid = int(self.ui.input('ID cliente a eliminar: '))
        except:
            print('ID inválido')
            return
        ok = self.repo.delete_customer(cid)
        print('Eliminado.' if ok else 'No encontrado.')
        self.ui.pause()

    def show_debt(self):
        try:
            cid = int(self.ui.input('ID cliente: '))
        except:
            print('ID inválido')
            return
        c = self.repo.get_customer(cid)
        if not c:
            print('No encontrado')
            return
        print(f"Cliente {c.get('name')} debe: {c.get('debt',0)}")
        self.ui.pause()

    # Products
    def products_menu(self):
        while True:
            self.ui.show_menu('Productos', [
                ('1','Listar productos'),
                ('2','Agregar producto'),
                ('3','Editar producto'),
                ('4','Eliminar producto'),
                ('0','Volver')
            ])
            choice = self.ui.input('> ').strip()
            if choice == '1':
                self.list_products()
            elif choice == '2':
                self.add_product()
            elif choice == '3':
                self.edit_product()
            elif choice == '4':
                self.delete_product()
            elif choice == '0':
                break
            else:
                print('Opción no válida')

    def list_products(self):
        products = self.repo.list_products()
        if not products:
            print('No hay productos.')
        else:
            for p in products:
                print(f"ID:{p['id']} - {p.get('name')} - Precio: {p.get('price',0)} - Stock: {p.get('stock',0)}")
        self.ui.pause()

    def add_product(self):
        name = self.ui.input('Nombre producto: ').strip()
        price = float(self.ui.input('Precio: ') or 0)
        stock = int(self.ui.input('Stock: ') or 0)
        self.repo.add_product({'name': name, 'price': price, 'stock': stock})
        print('Producto agregado.')
        self.ui.pause()

    def edit_product(self):
        try:
            pid = int(self.ui.input('ID producto a editar: '))
        except:
            print('ID inválido')
            return
        p = self.repo.get_product(pid)
        if not p:
            print('Producto no encontrado')
            return
        name = self.ui.input(f"Nombre ({p.get('name')}): ").strip() or p.get('name')
        price = self.ui.input(f"Precio ({p.get('price',0)}): ").strip()
        price = float(price) if price != '' else p.get('price',0)
        stock = self.ui.input(f"Stock ({p.get('stock',0)}): ").strip()
        stock = int(stock) if stock != '' else p.get('stock',0)
        self.repo.update_product(pid, {'name': name, 'price': price, 'stock': stock})
        print('Producto actualizado.')
        self.ui.pause()

    def delete_product(self):
        try:
            pid = int(self.ui.input('ID producto a eliminar: '))
        except:
            print('ID inválido')
            return
        ok = self.repo.delete_product(pid)
        print('Eliminado.' if ok else 'No encontrado.')
        self.ui.pause()
