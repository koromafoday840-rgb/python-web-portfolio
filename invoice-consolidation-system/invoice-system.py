"""
Author: Foday Christopher Koroma
Date: 28 March, 2026.

Project Description:
I build this program to simulate a small business invoice processing system.

Raw sales records often arrive as repeated line entries where the
same item may appear multiple times under the same invoice.
This program groups those records into structured invoices,
merges duplicate items, calculates accurate totals,
and prints a clean financial summary.

Design Goals:
- Prevent duplicate item entries inside the same invoice
- Maintain accurate running totals
- Keep data grouped logically by invoice ID
- Make the output readable for business use
- Build structure that can later be extended to files, reports, or databases
"""


# -------------------------------
# Raw Sales Data (Input Layer)
# -------------------------------
# In real systems this data could come from:
# - CSV files
# - POS systems
# - Databases
# Here we simulate incoming sales transactions.

sales = [
("INV001", "Rice", 2, 20),
("INV002", "Oil", 3, 12),
("INV001", "Rice", 4, 20),
("INV003", "Salt", 1, 20),
("INV004", "Oil", 4, 12),
("INV002", "Rice", 5, 20),
("INV005", "Maggi", 7, 5),
("INV003", "Rice", 2, 20),
("INV004", "Garri", 3, 10)
]


# -------------------------------------
# Phase 1 — Build Structured Invoices
# -------------------------------------

# Dictionary chosen because:
# - Invoice IDs must be unique
# - We need fast lookup by invoice ID
# - Each invoice holds multiple items (one-to-many relationship)

invoices = {}

for invoice_id, item, qty, price in sales:

    # setdefault ensures each invoice ID
    # always points to a list of items.
    # If the invoice does not exist yet,
    # it creates an empty list automatically.

    invoices.setdefault(invoice_id, [])

    # This flag tracks whether the item
    # already exists inside the invoice.
    # Used to prevent duplicate entries.

    found = False

    # Search existing items in this invoice
    for record in invoices[invoice_id]:

        # Compare item names
        # If match found, merge quantities
        # instead of creating duplicate entries.

        if record["item"] == item:

            # Add quantity instead of overwriting.
            # This preserves history and creates
            # accurate totals.

            record["qty"] += qty

            found = True

            # Break stops unnecessary searching.
            # Once found, no need to continue.

            break


    # If item was not found,
    # create a brand new record.

    if not found:

        item_record = {

            # Dictionary chosen because:
            # - Item fields belong together
            # - Clear labeling improves readability

            "item": item,
            "qty": qty,
            "price": price

        }

        # Append adds new item
        # to the invoice list.

        invoices[invoice_id].append(item_record)



# -------------------------------------
# Phase 2 — Financial Calculations
# -------------------------------------

# Grand total placed OUTSIDE loops
# so it does not reset repeatedly.

grand_total = 0


for invoice_id, items in invoices.items():

    # Invoice total resets once
    # per invoice.

    invoice_total = 0

    # Additional statistics
    total_quantity = 0
    total_items = len(items)

    print("================================")
    print("Invoice:", invoice_id)
    print("================================")


    # Process each item
    for record in items:

        # Calculate item cost
        # Quantity × Price

        line_total = record["qty"] * record["price"]

        # Add to invoice total
        # inside item loop
        # because every item contributes.

        invoice_total += line_total

        # Track total quantity
        total_quantity += record["qty"]

        # Display clean item output

        print(
            record["item"],
            "| Qty:", record["qty"],
            "| Price:", record["price"],
            "| Line Total:", line_total
        )


    # After all items processed,
    # display invoice summary.

    print("--------------------------------")

    print("Invoice Total:", invoice_total)

    print("Unique Items:", total_items)

    print("Total Quantity:", total_quantity)

    print()


    # Add invoice total to grand total
    # AFTER finishing item loop.

    grand_total += invoice_total



# -------------------------------------
# Final Business Summary
# -------------------------------------

print("================================")
print("BUSINESS SUMMARY")
print("================================")

print("Grand Total:", grand_total)

print("Total Invoices Processed:", len(invoices))

print("================================")