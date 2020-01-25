# things to do, add in discounts
def create_price_dict(cart):
    price_dict = {
        total_price: 0,
        total_tax: 0,
        stripe_fees: 0,
        net: 0,
    }

    for item in cart.items:
        taxes = item.product.price * (item.product.tax_rate / 100)
        total_price = item.product.price + taxes
        # the man always gets his cut
        stripe_fees = total_price * (3/100)
        # we make only what we keep
        net = total_price - taxes - stripe_fees

        price_dict['total_tax'] += taxes
        price_dict['total_price'] += total_price
        price_dict['stripe_fees'] += stripe_fees
        price_dict['net'] += net

    return price_dict


def set_cart_price(cart):
    cart_price_dict = create_price_dict(cart)
    cart.price = cart_price_dict['total_price']
    cart.save()
