# Online Shopping Store Django Project

This is a Django project that allows users to browse and purchase products from an online store. Users can create accounts, add items to their cart, and checkout securely using Stripe payment processing.

## Features

- Browse products by category and search for specific items
- Create user accounts and log in/out
- Add items to cart and adjust quantities
- Checkout securely using Stripe payment processing
- View order history and update account information

## Getting Started

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up the database by running `python manage.py migrate`.
4. Start the Django development server using `python manage.py runserver`.

## Usage

1. Navigate to `http://localhost:8000/` in your web browser.
2. Browse products by clicking on the category links or using the search bar.
3. Click on a product to view more details.
4. Add items to your cart by selecting the quantity and clicking "Add to Cart".
5. Click on the shopping cart icon to view your cart and adjust quantities or remove items.
6. Click "Checkout" to enter your shipping and payment information.
7. Confirm your order and click "Place Order" to complete the transaction.

## Stripe Setup

This project uses Stripe to process payments. To use Stripe, you'll need to set up a Stripe account and obtain your API keys. You can then add your API keys to a `.env` file in the root directory of the project:

- STRIPE_PUBLIC_KEY= <your public key
- STRIPE_SECRET_KEY= <your secret key


## Contributing

Contributions are always welcome! If you have any suggestions or found a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
## Note
This Project is not Complete