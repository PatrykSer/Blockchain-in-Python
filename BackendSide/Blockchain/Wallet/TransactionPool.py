class TransactionPool:
    def __init__(self):
        self.transcationMap = {}

    def setTransaction(self, transaction):
        """
        Set a transaction in the transacation Pool
        """
        self.transcationMap[transaction.id] = transaction

    def existingTransaction(self, address):
        """
        Find a transaction generated by the address in the transac pool

        Znajdź transakcję wygenerowaną przez adres w puli transakcji

        """
        for transaction in self.transcationMap.values():
            if transaction.input['address'] == address:
                return transaction

    def transactionData(self):
        """
       Return the transaction of the transaction pool represented in thier json serialized form.

       Zwraca transakcję puli transakcji reprezentowaną w postaci serializowanej JSON.
        """

        return list(map(lambda transaction: transaction.to_json(), self.transcationMap.values()))

    def clearTransaction(self, blockchain):
        """
        Delete blockchain transaction recorded transaction from the pool

        Usuń zarejestrowaną transakcję blockchain z puli
        """
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                    del self.transcationMap[transaction['id']]
                except KeyError:
                    pass
