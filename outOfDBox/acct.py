class account:
    def __init__(self, owner, amount=0):
        self.owner         = owner
        self.amount        = amount
        self._transactions = [amount]
        
    def __repr__(self):
        return 'Account ({!r}, {!r})'.format(self.owner,self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(self.owner,self.amount)

    def add_transaction(self,amount):
        if not isinstance(amount,int):
            raise ValueError('Please use int for amount.')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self,position):
        if len(self._transactions) < position:
            raise ValueError('Position is more than transactions.')
##        if not position:
##            position -= 1
        return self._transactions[position]

    def __reversed__(self):
        return self._transactions[::-1] 
