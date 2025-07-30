# Debt Management Website

This project is a simple web application for managing debts using Flask and Bootstrap. It allows users to add, view, and manage their debts efficiently.

## Project Structure

```
debt-website
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── css
│   │       └── bootstrap.min.css
│   └── templates
│       ├── base.html
│       ├── index.html
│       └── debts.html
├── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/debt-website.git
   cd debt-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to set up your database URI and other configurations as needed.

## Running the Application

To run the application, execute the following command:
```
flask run
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Features

- Add new debts with details such as amount, description, and due date.
- View a list of all debts in a structured format.
- Responsive design using Bootstrap for a better user experience.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.