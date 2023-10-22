from abc import ABC, abstractmethod
import hashlib

class Provider(ABC):
    @abstractmethod
    def get_network(self):
        pass

    @abstractmethod
    def get_block_number(self):
        pass

class Wallet(ABC):
    @abstractmethod
    def sign_transaction(self, tx):
        pass

    @abstractmethod
    def send_transaction(self, signed_tx):
        pass

# Ethereum Provider
class EthereumProvider(Provider):
    def __init__(self):
        self.block_number = 0

    def get_network(self):
        return "Ethereum"

    def get_block_number(self):
        self.block_number += 1
        return self.block_number

class EthereumWallet(Wallet):

    def __init__(self, provider: Provider):
        self.provider = provider

    def sign_transaction(self, tx: str):
        network = self.provider.get_network()
        input_bytes = f"{network}{tx}".encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_bytes)
        return f"0x{sha256_hash.hexdigest()}"

    def send_transaction(self, signed_tx: str):
        print(f"Sending transaction: {signed_tx}")

class SolanaProvider(Provider):
    def __init__(self):
        self.block_number = 0

    def get_network(self):
        return "Solana"

    def get_block_number(self):
        self.block_number += 1
        return self.block_number

class SolanaWallet(Wallet):

    def __init__(self, provider: Provider):
        self.provider = provider
    def sign_transaction(self, tx: str):
        network = "Solana"
        input_bytes = f"{network}{tx}".encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_bytes)
        return f"0x{sha256_hash.hexdigest()}"

    def send_transaction(self, signed_tx: str):
        print(f"Sending transaction: {signed_tx}")

class NearProvider(Provider):
    def __init__(self):
        self.block_number = 0

    def get_network(self):
        return "Near"

    def get_block_number(self):
        self.block_number += 1
        return self.block_number

class NearWallet(Wallet):

    def __init__(self, provider: Provider):
        self.provider = provider
    def sign_transaction(self, tx: str):
        network = "Near"
        input_bytes = f"{network}{tx}".encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_bytes)
        return f"0x{sha256_hash.hexdigest()}"

    def send_transaction(self, signed_tx: str):
        print(f"Sending transaction: {signed_tx}")

class BlockchainFactory(ABC):
    @abstractmethod
    def create_provider(self):
        pass

    @abstractmethod
    def create_wallet(self):
        pass

class EthereumFactory(BlockchainFactory):
    def create_provider(self):
        return EthereumProvider()

    def create_wallet(self):
        return EthereumWallet(self.create_provider())

class SolanaFactory(BlockchainFactory):
    def create_provider(self):
        return SolanaProvider()

    def create_wallet(self):
        return SolanaWallet(self.create_provider())

class NearFactory(BlockchainFactory):
    def create_provider(self):
        return NearProvider()

    def create_wallet(self):
        return NearWallet(self.create_provider())


if __name__ == "__main__":
    message = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

    eth_factory = EthereumFactory()
    eth_provider = eth_factory.create_provider()
    eth_wallet = eth_factory.create_wallet()
    print(f"Network: {eth_provider.get_network()}")
    print(f"Block number: {eth_provider.get_block_number()}")
    signed_tx = eth_wallet.sign_transaction(message)
    eth_wallet.send_transaction(signed_tx)

    sol_factory = SolanaFactory()
    sol_provider = sol_factory.create_provider()
    sol_wallet = sol_factory.create_wallet()
    print(f"Network: {sol_provider.get_network()}")
    print(f"Block number: {sol_provider.get_block_number()}")
    signed_tx = sol_wallet.sign_transaction(message)
    sol_wallet.send_transaction(signed_tx)


    near_factory = NearFactory()
    near_provider = near_factory.create_provider()
    near_wallet = near_factory.create_wallet()
    print(f"Network: {near_provider.get_network()}")
    print(f"Block number: {near_provider.get_block_number()}")
    signed_tx = near_wallet.sign_transaction(message)
    near_wallet.send_transaction(signed_tx)
