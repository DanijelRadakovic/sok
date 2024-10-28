from abc import ABC, abstractmethod
import hashlib


class Provider(ABC):
    @abstractmethod
    def get_network(self) -> str:
        pass

    @abstractmethod
    def get_block_number(self) -> int:
        pass


class Wallet(ABC):
    @abstractmethod
    def sign_transaction(self, tx) -> str:
        pass

    @abstractmethod
    def send_transaction(self, signed_tx):
        pass


class EthereumProvider(Provider):
    def __init__(self):
        self.block_number = 0

    def get_network(self) -> str:
        return "Ethereum"

    def get_block_number(self) -> int:
        self.block_number += 1
        return self.block_number


class EthereumWallet(Wallet):
    def __init__(self, provider: Provider):
        self.provider = provider

    def sign_transaction(self, tx: str) -> str:
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

    def get_network(self) -> str:
        return "Solana"

    def get_block_number(self) -> int:
        self.block_number += 1
        return self.block_number


class SolanaWallet(Wallet):
    def __init__(self, provider: Provider):
        self.provider = provider

    def sign_transaction(self, tx: str) -> str:
        network = self.provider.get_network()
        input_bytes = f"{network}{tx}".encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_bytes)
        return f"0x{sha256_hash.hexdigest()}"

    def send_transaction(self, signed_tx: str):
        print(f"Sending transaction: {signed_tx}")


class NearProvider(Provider):
    def __init__(self):
        self.block_number = 0

    def get_network(self) -> str:
        return "Near"

    def get_block_number(self) -> int:
        self.block_number += 1
        return self.block_number


class NearWallet(Wallet):
    def __init__(self, provider: Provider):
        self.provider = provider

    def sign_transaction(self, tx: str) -> str:
        network = self.provider.get_network()
        input_bytes = f"{network}{tx}".encode('utf-8')
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_bytes)
        return f"0x{sha256_hash.hexdigest()}"

    def send_transaction(self, signed_tx: str):
        print(f"Sending transaction: {signed_tx}")


class BlockchainFactory(ABC):
    @abstractmethod
    def create_provider(self) -> Provider:
        pass

    @abstractmethod
    def create_wallet(self) -> Wallet:
        pass


class EthereumFactory(BlockchainFactory):
    def create_provider(self) -> Provider:
        return EthereumProvider()

    def create_wallet(self) -> Wallet:
        return EthereumWallet(self.create_provider())


class SolanaFactory(BlockchainFactory):
    def create_provider(self) -> Provider:
        return SolanaProvider()

    def create_wallet(self) -> Wallet:
        return SolanaWallet(self.create_provider())


class NearFactory(BlockchainFactory):
    def create_provider(self) -> Provider:
        return NearProvider()

    def create_wallet(self) -> Wallet:
        return NearWallet(self.create_provider())


class Client:
    def __init__(self, factory: BlockchainFactory):
        self.factory = factory

    def factory(self, factory: BlockchainFactory):
        self.factory = factory

    def execute(self, msg):
        provider = self.factory.create_provider()
        wallet = self.factory.create_wallet()

        print(f"Network: {provider.get_network()}")
        print(f"Block number: {provider.get_block_number()}")

        signed_tx = wallet.sign_transaction(msg)
        wallet.send_transaction(signed_tx)

if __name__ == "__main__":
    message = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

    client = Client(EthereumFactory())
    client.execute(message)

    client.factory = SolanaFactory()
    client.execute(message)

    client.factory = NearFactory()
    client.execute(message)
