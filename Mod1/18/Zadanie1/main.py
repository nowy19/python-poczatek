from shop.orders import create_new_order


def run_shop():
    print("Witaj w naszym sklepie!")

    product_name = input("Jaki towar chcesz kupić? ")
    quantity = int(input("Ile sztuk chcesz kupić? "))

    result = create_new_order(product_name, quantity)

    if result is not None:
        total_price = result["total_price"]
        print(f"Lączny koszt wyniesie: {total_price} zł")


if __name__ == "__main__":
    run_shop()
