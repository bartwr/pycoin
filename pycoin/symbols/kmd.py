from pycoin.networks.bitcoinish import create_bitcoinish_network

# Network prefix: 3C
# https://docs.komodoplatform.com/notary/generate-privkeys-third-party-coins-from-passphrase.html#example-output
network = create_bitcoinish_network(
    symbol="KMD", network_name="Komodo", subnet_name="mainnet",
    wif_prefix_hex="bc", address_prefix_hex="3C", pay_to_script_prefix_hex="1cbd",
    bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488b21e")
