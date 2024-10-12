from datetime import datetime

class EnergyBill:
    def __init__(self, rechnungssumme, rechnungzeitraum_beginn, rechnungzeitraum_ende):
        self.rechnungssumme = rechnungssumme
        self.rechnungzeitraum_beginn = rechnungzeitraum_beginn
        self.rechnungzeitraum_ende = rechnungzeitraum_ende



def calculate_energy_bill(menge, preis,rechnungzeitraum_beginn,rechnungzeitraum_ende):
    """
    Calculates the total energy bill based on the given price and amount.

    Args:
        price (float): The price per unit of energy.
        amount (float): The amount of energy consumed.

    Returns:
        float: The total energy bill.

    """
    return EnergyBill(menge * preis, rechnungzeitraum_beginn, rechnungzeitraum_ende)

    
def pretty_print_energy_bill(energy_bill):
    """
    Pretty prints the given energy bill.

    Args:
        energy_bill (EnergyBill): The energy bill to print.

    """
    print(f"Rechnungssumme: {energy_bill.rechnungssumme}")

def main():
    energy_bill = calculate_energy_bill(2, 2)
    pretty_print_energy_bill(energy_bill)

if __name__ == '__main__':
    main()

