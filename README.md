# UA Stock Market Volume Data

This project processes CSV data containing volume information for UA stock market indexes and select US equities, and loads it into a PostgreSQL database.

## How to Use

- The CSV data format needs to be defined.
- The PostgreSQL schema needs to be defined.

To run the script:

```bash
python scripts/main.py
```

## Setting up the Environment

### Prerequisites

- Python
- PostgreSQL

### Installing Dependencies

To install the necessary Python libraries, run:

```bash
pip install pandas psycopg2-binary
```

## Contributing

We welcome contributions to improve this project! If you'd like to contribute, please follow these general guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes, ensuring to follow any existing coding style.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## License

This project is released under the MIT License.

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It puts only very limited restriction on reuse and has, therefore, an excellent license compatibility.

It is recommended to create a `LICENSE` file in the root of the project containing the full text of the MIT License.
