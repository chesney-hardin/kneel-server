ORDERS = [
    {
      "metalId": 3,
      "sizeId": 2,
      "styleId": 2,
      "id": 1
    },
    {
      "metalId": 1,
      "sizeId": 5,
      "styleId": 1,
      "id": 2
    },
    {
      "metalId": 5,
      "sizeId": 4,
      "styleId": 1,
      "id": 3
    },
    {
      "metalId": 2,
      "sizeId": 2,
      "styleId": 2,
      "id": 4
    },
    {
      "metalId": 4,
      "sizeId": 5,
      "styleId": 1,
      "id": 5
    },
    {
      "metalId": 4,
      "sizeId": 4,
      "styleId": 2,
      "id": 6
    },
    {
      "metalId": 2,
      "sizeId": 3,
      "styleId": 3,
      "id": 7
    },
    {
      "metalId": 4,
      "sizeId": 5,
      "styleId": 1,
      "id": 8
    }
]

def get_all_orders():
    """function to return the whole list of dictionaries for orders"""
    return ORDERS


def get_single_order(id):
    """function to return a single dictionary from the list of orders"""
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(new_order):
    """function to create a new order"""
    
    #find the last id in the ORDERS list
    last_id = ORDERS[-1]["id"]

    new_order["id"] = last_id + 1

    ORDERS.append(new_order)

    return new_order

def delete_order(id):
    """function to delete an order"""
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
          order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)
