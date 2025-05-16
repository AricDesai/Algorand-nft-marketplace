# Algorand ASA Airdrop Tool

## Description
A Python tool to airdrop a fixed amount of an Algorand Standard Asset (ASA) to multiple wallet addresses from a CSV file.

## Setup

1. Clone this repository or download the zip.
2. Install dependencies:
3. Replace the following placeholders in `airdrop.py`:
- `<Your PureStake API Key>` with your Algorand API key.
- `<Your 25-word mnemonic here>` with the mnemonic of your sender account.
- `ASA_ID` with your ASA's asset ID.
- Adjust `AMOUNT` as needed.

4. Prepare your CSV file `addresses.csv` with one column named `address` listing the recipient Algorand addresses.

## Usage

Run the airdrop script:

```bash
python airdrop.py
