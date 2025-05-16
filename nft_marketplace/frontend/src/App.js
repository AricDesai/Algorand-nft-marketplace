import { useEffect, useState } from "react"
import NFTCard from "./components/NFTCard"
import { algodClient } from "./utils/algod"

function App() {
  const [account, setAccount] = useState("")
  const [nfts, setNfts] = useState([])

  const fetchNFTs = async () => {
    const response = await fetch("https://testnet.algoexplorerapi.io/v2/assets?limit=10&unit=NFT")
    const data = await response.json()
    const assets = data.assets.map(a => ({
      id: a.index,
      name: a.params.name,
      unitName: a.params["unit-name"],
      url: a.params.url,
    }))
    setNfts(assets)
  }

  const connectWallet = async () => {
    const accounts = await window.algorand.enable()
    setAccount(accounts[0])
  }

  const buyNFT = async (assetId) => {
    console.log("Buy logic with escrow goes here")
  }

  useEffect(() => {
    fetchNFTs()
  }, [])

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">NFT Marketplace</h1>
      {account ? <p>Connected: {account}</p> : <button onClick={connectWallet} className="bg-green-500 px-4 py-2 text-white">Connect Wallet</button>}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
        {nfts.map(nft => (
          <NFTCard key={nft.id} nft={nft} onBuy={() => buyNFT(nft.id)} />
        ))}
      </div>
    </div>
  )
}

export default App
