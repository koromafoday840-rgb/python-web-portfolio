# 🧾 Smart Invoice Consolidation System

**Author:** Foday Christopher Koroma  
**Date:** 28 March 2026  
**Project Type:** Backend Logic Simulation  
**Language:** Python  

---

# 📌 Project Overview

This project simulates a real-world invoice processing system used in small retail or trading businesses.

In many real business environments, raw sales records often contain repeated entries of the same item under a single invoice. Without proper consolidation, this leads to duplicate records, incorrect totals, and unreliable financial reporting.

This program solves that problem by:

- Grouping raw sales into structured invoices
- Detecting duplicate items
- Merging quantities correctly
- Calculating accurate financial totals
- Producing clean, readable invoice summaries

The logic implemented here reflects real backend workflows used in billing systems, inventory systems, and accounting tools.

---

# 🎯 Problem This Project Solves

In real businesses:

- A customer may buy the same item multiple times
- Sales records may be entered separately
- Duplicate entries cause incorrect billing
- Totals become unreliable

Without consolidation:

Example raw data:

INV001 Rice 2  
INV001 Rice 4  

Wrong result:

Rice Qty: 2  
Rice Qty: 4  

Correct result (after consolidation):

Rice Qty: 6  

This program performs that consolidation automatically.

---

# ⚙️ Core Features

✔ Groups transactions by **Invoice ID**  
✔ Merges duplicate items automatically  
✔ Calculates **Line Totals**  
✔ Calculates **Invoice Totals**  
✔ Calculates **Grand Total**  
✔ Tracks **Total Quantity per Invoice**  
✔ Displays clean financial summaries  
✔ Uses structured nested dictionaries  

---

# 🏗️ System Design

This project uses a **nested dictionary structure**:
