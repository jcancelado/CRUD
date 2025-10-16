import json
import os
from typing import Dict, Any, List

class JSONRepository:
    def __init__(self, filename='db.json'):
        self.filename = filename
        if not os.path.exists(self.filename):
            self._write({'customers': [], 'products': []})

    def _read(self) -> Dict[str, Any]:
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write(self, data: Dict[str, Any]):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # Customer methods
    def list_customers(self) -> List[Dict[str, Any]]:
        return self._read()['customers']

    def get_customer(self, customer_id: int) -> Dict[str, Any] | None:
        for c in self.list_customers():
            if c['id'] == customer_id:
                return c
        return None

    def add_customer(self, customer: Dict[str, Any]) -> Dict[str, Any]:
        data = self._read()
        customers = data['customers']
        customer['id'] = (max([c['id'] for c in customers]) + 1) if customers else 1
        customers.append(customer)
        self._write(data)
        return customer

    def update_customer(self, customer_id: int, fields: Dict[str, Any]) -> bool:
        data = self._read()
        for i, c in enumerate(data['customers']):
            if c['id'] == customer_id:
                data['customers'][i].update(fields)
                self._write(data)
                return True
        return False

    def delete_customer(self, customer_id: int) -> bool:
        data = self._read()
        before = len(data['customers'])
        data['customers'] = [c for c in data['customers'] if c['id'] != customer_id]
        self._write(data)
        return len(data['customers']) < before

    # Product methods
    def list_products(self) -> List[Dict[str, Any]]:
        return self._read()['products']

    def get_product(self, product_id: int) -> Dict[str, Any] | None:
        for p in self.list_products():
            if p['id'] == product_id:
                return p
        return None

    def add_product(self, product: Dict[str, Any]) -> Dict[str, Any]:
        data = self._read()
        products = data['products']
        product['id'] = (max([p['id'] for p in products]) + 1) if products else 1
        products.append(product)
        self._write(data)
        return product

    def update_product(self, product_id: int, fields: Dict[str, Any]) -> bool:
        data = self._read()
        for i, p in enumerate(data['products']):
            if p['id'] == product_id:
                data['products'][i].update(fields)
                self._write(data)
                return True
        return False

    def delete_product(self, product_id: int) -> bool:
        data = self._read()
        before = len(data['products'])
        data['products'] = [p for p in data['products'] if p['id'] != product_id]
        self._write(data)
        return len(data['products']) < before
