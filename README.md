# python-order-calculator

Pada project ini tujuannya adalah membuat aplikasi sederhana untuk menghitung total pendapatan dan total pajak secara akurat menggunakan python

### Project ini menerapkan konsep OOP pada python, yaitu:
- Encapsulation : Membungkus atribut dan method dari class Order seperti atribut customer_name dan method calculate_tax. Tujuan utama adalah mengontrol bagaimana atribut diakses dari luar kelas. 
- Abstraction   : Mengurangi kompleksitas kode dan memberikan keterbacaan lebih dari kode yang dimiliki. 
- Separation of Concerns : Project ini memisahkan dua class Order untuk penyimpanan data individu dan class OrderProcessor untuk pengelolaan seluruh data Order

## Struktur Komponen
### Class Order
- **Tujuan**: Representasi dari data order per individu.
- **Fungsi**: Kalkulasi pajak otomatis per order dan formatting output baris transaksi.

### Class OrderProcessor
- **Tujuan**: Manajemen koleksi untuk objek Order.
- **Fitur**: Penambahan objek ke list_order, akumulasi total revenue, dan akumulasi total pajak.

## Skema Pengujian
Pengujian dilakukan melalui dua tahap untuk memastikan reliabilitas sistem:
1. **Instansiasi Manual**: Verifikasi fungsionalitas objek tunggal (pesanan1).
2. **Automated Batch Processing**: Memproses delapan data dari dictionary menggunakan perulangan untuk simulasi input data masal secara efisien.

## Cara Penggunaan
1. Pastikan versi Python 3.13 atau ke atas installed di sistem.
2. Clone repositori ini ke direktori lokal.
3. Jalankan file utama melalui terminal atau command prompt menggunakan 
   ```bash
   python main.py
    ```
    atau
   ```bash 
   python3 main.py
   ```
