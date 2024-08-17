from solana.rpc.api import Client, Pubkey

# Initialize the Solana client
solana_client = Client("https://api.mainnet-beta.solana.com")

# Replace with the specific wallet address you want to check
wallet_address = "CMeb68prsa7HmmVurnFLYQztAtgERsFNthvjddYJCJXa"
public_key = Pubkey.from_string(wallet_address)

# res = solana_client.get_signatures_for_address(
#     Pubkey.from_string(wallet_address),
#     limit = 1 # Specify how much last transactions to fetch
# )
# response = solana_client.get_transaction(
#     res.value[0].signature, 
#     max_supported_transaction_version=0
# )

# print(response)

import asyncio
from solders.keypair import Keypair
from solana.rpc.websocket_api import connect

async def main():
    async with connect("wss://api.mainnet-beta.solana.com") as websocket:
        # Create a Test Wallet
        wallet = Pubkey.from_string(wallet_address)
        # Subscribe to the Test wallet to listen for events
        await websocket.account_subscribe(wallet)
        # Capture response from account subscription 
        first_resp = await websocket.recv()
        # print("Subscription successful with id {}, listening for events \n".format(first_resp))
        for data in first_resp:
            print("block {}".format(data))

        updated_account_info = await websocket.recv()
        print(updated_account_info)
        
asyncio.run(main())
# print(f"Signature: {tx['signature']}, Slot: {tx['slot']}, Timestamp: {tx['blockTime']}, Status: {tx['confirmationStatus']}")




# # Fetch recent transactions
# def fetch_recent_transactions(pubkey):
#     # Fetch recent confirmed transactions for the wallet
#     response = solana_client.solana_client.get_signatures_for_address(pubkey, limit=10)
#     if response['result']:
#         return response['result']
#     else:
#         return "No transactions found or there was an error."

# transactions = fetch_recent_transactions(public_key)

# # Print out the recent transactions
# for tx in transactions:
#     print(f"Signature: {tx['signature']}, Slot: {tx['slot']}, Timestamp: {tx['blockTime']}, Status: {tx['confirmationStatus']}")