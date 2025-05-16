export default function NFTCard({ nft, onBuy }) {
  return (
    <div className="border p-4 rounded-lg shadow-lg">
      <img src={nft.url} className="w-full h-48 object-cover mb-2" />
      <h2 className="text-lg font-semibold">{nft.name}</h2>
      <p>{nft.unitName}</p>
      <button onClick={onBuy} className="mt-2 bg-blue-600 text-white px-4 py-2 rounded">Buy</button>
    </div>
  )
}
