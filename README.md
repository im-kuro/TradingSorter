# Kuros Trading Visualizer

Kuros Trading Visualizer is a web application that allows users to visualize their trade history stored in a CSV file. It provides a user-friendly interface to view and analyze trades, including order types, symbols, lot sizes, stop loss, take profit, and more.

## Features

- Converts CSV trade data into a JSON format for easy visualization.
- Displays trade history with relevant information, including order type, symbol, lot size, stop loss, take profit, opened and closed timestamps, swaps, commissions/fees, and profit/loss.
- Highlights trades with different colors based on their profit/loss status.
- Indicates trade events such as stop loss and take profit hits with visual markers.
- Responsive design for optimal viewing on different devices.

## Prerequisites

- Python 3.7 or above
- Flask web framework
- Jinja2 templating engine
- Bootstrap 4.5 CSS framework

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Change into the project directory: `cd kuros-trading-visualizer`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Prepare your trade history CSV file. Ensure that it follows the required format with the appropriate columns (order type, symbol, volume, sl, tp, openedAt, closedAt, swaps, commission, profitloss, comment).
2. Run the Flask application: `python app.py --filepath <path-to-csv-file>`
   - Replace `<path-to-csv-file>` with the actual file path of your trade history CSV.
   - This will start the application and make it accessible at `http://localhost:5000`.
3. Open a web browser and visit `http://localhost:5000` to view your trade history.

## Customization

- Styling: You can customize the CSS styles by modifying the `style` section in the HTML template (`templates/main.html`).
- Layout: To change the layout of the trade cards, you can modify the HTML structure in the template (`templates/main.html`).
- Additional Functionality: If you want to add more features or enhance the existing functionality, you can modify the Python code in `app.py` and the HTML templates in the `templates` directory.

## Contributing

Contributions are welcome! If you find any bugs, issues, or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, please feel free to reach out:

- Developer: [Kuros](https://github.com/im-kuro)
- Twitter: [@devkuro](https://twitter.com/devkuro)

