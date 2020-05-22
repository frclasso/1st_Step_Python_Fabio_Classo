import csv
from faker import Faker
from time import time

RECORD_COUNT = 10000

fake = Faker()


def create_csv_file():
    with open('invoices.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'product_id',
                      'qty', 'amount','description', 'address', 'city',
                      'state', 'country']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': fake.name(),
                    'last_name':fake.name(),
                    'email':fake.email(),
                    'product_id':fake.random_int(min=100, max=1099),
                    'qty': fake.random_int(min=1, max=9),
                    'amount':fake.random_int(500, 10000) / 100,
                    'description':fake.sentence(),
                    'address':fake.street_address(),
                    'city':fake.city(),
                    'state':fake.state(),
                    'country': fake.country()

                }
            )

def get_totals():
    qty_total = 0
    amount_total = 0
    with open('invoices.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[4] != 'qty':
                qty = int(row[4])
                qty_total += qty

                amount = float(row[5])
                amount_total += amount
    return qty_total, amount_total


if __name__=="__main__":
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file - time: {}'.format(elapsed))

    start = time()
    qty_total, amount_total = get_totals()
    elapsed = time() - start
    print('Got totals - time {}'.format(elapsed))

    print('qty: {}'.format(qty_total))
    print('Amount: {}'.format(amount_total))



# utlizando a biblioteca Faker para gerar dados em .csv
# https://faker.readthedocs.io/