# ppcTelegramHalvingBot

## Documentation

For more information about the APIs used in this project, see the [Blockchain.com Explorer API documentation](https://www.blockchain.com/explorer/api/q).

## Setup and Installation

To set up and run this project, follow these steps:

1. **Create a Virtual Environment**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip3 install requests
  pip3 install python-telegram-bot
  pip3 list
  ```

2. **Run crontab**:
  ```
  0 * * * * /path/to/runhalving.sh >>/path/to/ppchalving_countdown.log 2>&1
  ```

