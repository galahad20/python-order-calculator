class Order:
    #input awal
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    #hitung pajak
    def calculate_tax(self, tax_rate = 0.1):
        return self.total_amount * tax_rate
    
    #tampilkan order
    def display_order(self):
        print(f"ID: {self.order_id} | Nama: {self.customer_name} | Total : Rp.{self.total_amount} | Pajak 10% : Rp.{self.calculate_tax()} | Total Bayar: Rp.{self.total_amount + self.calculate_tax()}") 

class OrderProcessor:
    def __init__(self):
        self.orders =[]
    
    def add_order(self, order):
        self.orders.append(order)
        #print(f"Sistem: Order atas nama {order.customer_name} berhasil disimpan")

    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total
        
    def calculate_total_tax(self):
        total_tax = 0
        for order in self.orders:
            total_tax += order.calculate_tax()
        return total_tax
    
    #tampilkan daftar order
    def display_orders(self):
        for order in self.orders:
            order.display_order()
        
        print("-" * 50)
        print(f"Total revenue yang didapatkan adalah Rp.{self.calculate_total_revenue()}")
        print(f"Total pajak Rp.{self.calculate_total_tax()}")

#objek
pesanan1 = Order ("001", "Budi", "2024-01-01", 100000)

#pengelola
prosesor = OrderProcessor()

#input data
prosesor.add_order(pesanan1)

#---------------------------------TEST DATA--------------------------------------#
#data lain untuk object baru
test_order = [
    {"order_id": "002", "customer_name": "Abe", "order_date": "2024-01-01", "total_amount": 143000},
    {"order_id": "003", "customer_name": "Doria", "order_date": "2024-01-01", "total_amount": 13000},
    {"order_id": "004", "customer_name": "Fani", "order_date": "2024-01-02", "total_amount": 15000},
    {"order_id": "005", "customer_name": "Ceri", "order_date": "2024-01-02", "total_amount": 53000},
    {"order_id": "006", "customer_name": "Kalia", "order_date": "2024-01-02", "total_amount": 70000},
    {"order_id": "007", "customer_name": "Dono", "order_date": "2024-01-05", "total_amount": 39000},
    {"order_id": "008", "customer_name": "Joko", "order_date": "2024-01-05", "total_amount": 113000},
    {"order_id": "009", "customer_name": "Sutejo", "order_date": "2024-01-06", "total_amount": 150000},
]

#perulangan untuk buat object dan simpan orders
for order in test_order:
    #buat object (order) lain
    pesanan = Order(order["order_id"], order["customer_name"], order["order_date"], order["total_amount"])

    #simpan ke list orders
    prosesor.add_order(pesanan)


#tampilkan hasil
prosesor.display_orders()
