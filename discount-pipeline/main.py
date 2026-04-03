from engine import get_discount_price, build_receipt

def run_pipeline():
    """
    Executes the discount calculation and receipt generation.
    """
    # 1. Input Data
    item_name = "Professional Clippers"
    retail_price = 50.0
    discount_rate = 15.0

    # 2. Logic Execution
    final_total = get_discount_price(retail_price, discount_rate)
    
    # 3. Output Generation
    receipt_message = build_receipt(item_name, final_total)
    print(receipt_message)

if __name__ == "__main__":
    run_pipeline()