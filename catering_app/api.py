import frappe

@frappe.whitelist(allow_guest=True)
def get_items():
    # Fetch all items where 'show_in_website' is enabled
    items = frappe.get_all(
        'Item', 
        filters={'show_in_website': 1}, 
        fields=['item_name', 'description', 'item_code', 'standard_rate']
    )
    
    return items
