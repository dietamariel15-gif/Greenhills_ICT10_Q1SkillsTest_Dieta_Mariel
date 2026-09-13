from pyscript import document, display


def generate_receipt(event):

    # Get all selected menu items
    items = document.querySelectorAll(
        'input[type="checkbox"]:checked'
    )

    subtotal = 0
    order = []

    # Calculate the subtotal
    for item in items:
        price = float(item.value)
        name = item.nextElementSibling.textContent

        subtotal += price
        order.append(f"{name}")

    # Calculate the 12% VAT
    vat = subtotal * 0.12

    # Calculate the total amount
    total = subtotal + vat

    # Create the receipt
    receipt = "<h2>===== RECEIPT =====</h2>"

    if order:
        for item in order:
            receipt += f"<p>{item}</p>"
    else:
        receipt += "<p>No items selected.</p>"

    receipt += "<hr>"
    receipt += f"<p><strong>Subtotal:</strong> ₱{subtotal:.2f}</p>"
    receipt += f"<p><strong>VAT (12%):</strong> ₱{vat:.2f}</p>"
    receipt += f"<p><strong>Total Amount:</strong> ₱{total:.2f}</p>"

    # Display the receipt
    document.querySelector("#receipt").innerHTML = receipt