import sqlite3
from models import Order, Metal, Style, Size

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
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT 
        o.id,
        o.time_stamp,
        o.metal_id,
        o.size_id,
        o.style_id,
        m.metal metal,
        m.price metal_price,
        sz.carets carets,
        sz.price carets_price,
        s.style style,
        s.price style_price
      FROM Orders o
      JOIN Metals m ON m.id = o.metal_id
      JOIN Sizes sz ON sz.id = o.size_id
      JOIN Styles s ON s.id = o.style_id;
      """)

      orders = []

      dataset = db_cursor.fetchall()

      for row in dataset:

        # Create an order instance from the current row
        order = Order(row['id'], row['time_stamp'], row['metal_id'], row['size_id'], row['style_id'])

        metal = Metal(row['id'], row['metal'], row['metal_price'])
        # Create a Size instance from the current row
        size = Size(row['id'], row['carets'], row['carets_price'])
        # Create a Style instance from the current row
        style = Style(row['id'], row['style'], row['style_price'])

        # Add the dictionary representation of related object to the order instance
        # Here what added the size would look like. You add the other two.
        added_metal = metal.__dict__
        added_metal.pop('id')
        order.metal = added_metal
        added_size = size.__dict__
        added_size.pop('id')
        order.size = added_size
        added_style = style.__dict__
        added_style.pop('id')
        order.style = added_style
        # Add the dictionary representation of the order to the list
        orders.append(order.__dict__)
      
      return orders


def get_single_order(id):
    """function to return a single dictionary from the list of orders"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT 
        o.id,
        o.time_stamp,
        o.metal_id,
        o.size_id,
        o.style_id
      FROM Orders o
      WHERE o.id = ?
      """, (id, ))

      data = db_cursor.fetchone()

      order = Order( data['id'], data['time_stamp'],
                        data['metal_id'], data['size_id'], data['style_id'])
          
      return order.__dict__


def create_order(new_order):
    """function to create a new order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
          INSERT INTO Orders
              ( time_stamp, metal_id, size_id, style_id )
          VALUES
              ( ?, ?, ?, ? );
          """, (new_order['time_stamp'], new_order['metal_id'], 
                new_order['size_id'], new_order['style_id']))
        
        id = db_cursor.lastrowid

        new_order['id'] = id
    
    return new_order

def delete_order(id):
    """function to delete an order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))

def update_order(id, order):
    """updates an existing order"""
    # connecting to the database with sqlite3.connect()
    # "with" 
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                time_stamp = ?,
                metal_id = ?,
                size_id = ?,
                style_id = ?
          WHERE id = ?
        """, (order['time_stamp'], order['metal_id'],
              order['size_id'], order['style_id'], id ))
        
        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True