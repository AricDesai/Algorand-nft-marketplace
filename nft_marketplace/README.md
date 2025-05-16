# 🖼️ Algorand NFT Minting & Marketplace

A full-stack project for minting NFTs as Algorand Standard Assets (ASAs) and listing them on a smart-contract-based marketplace.

---

## 🔧 Technologies

- **Algorand**
- **PyTeal** (smart contract development)
- **Python** (for minting and backend scripting)
- **React + Tailwind CSS** (frontend UI)
- **Algod SDK** (algosdk)

---

## 📁 Project Structure

nft_marketplace/
├── mint_nft/
│ └── create_nft.py
├── contracts/
│ ├── escrow_buy.py
│ └── escrow_sell.py
├── scripts/
│ ├── compile.py
│ └── deploy.py
├── artifacts/
│ └── (compiled TEAL files)
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── App.js
│ │ ├── index.js
│ │ ├── index.css
│ │ ├── components/
│ │ │ └── NFTCard.js
│ │ └── utils/
│ │ └── algod.js
│ ├── package.json
│ └── tailwind.config.js
└── README.md
## 📄 License

MIT License. Use freely for learning and development.