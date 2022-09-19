from DataStructures.Cost import Cost
from DataStructures.Member import Member


class CostManager:
    """
    Represent a mutable Cost manager
    Grant access to the balance sheet to see the interpersonal debt relationship
    Adding Cost event to update the balance sheet

    Attributes
    ----------
    balance : dict
        (k, dict) = (debtor, their relationship with others)
            inner dict (k, v) = (others, the amount they have to pay to the person)
    transactions: dict
        (k, v) = (ID of the cost, Cost object)
    """
    ID_count = 1

    def __init__(self):
        self.balance = {}
        self.transactions = {}

    # Test representation exposure here
    def get_balance(self) -> dict:
        return self.balance

    # Test representation exposure here
    def get_transactions(self) -> dict:
        return self.transactions

    def calculate_balance(self, cost: Cost) -> None:
        """
        Update the balance by calculating the upcoming cost

        This method should be kept private, updating balance sheet would be done by
        adding the cost event into the cost manager.

        Parameters
        ----------
        cost : Cost
            The upcoming cost to be calculated
        """
        single_cost = cost.calculate_debt()
        payer = cost.get_payer()
        for debtor in single_cost.keys():
            payer_to_debtor = self.balance[payer][debtor]
            debtor_to_payer = self.balance[debtor][payer] + single_cost[debtor]
            self.balance[payer][debtor] = payer_to_debtor - debtor_to_payer
            self.balance[debtor][payer] = debtor_to_payer - payer_to_debtor

    def add_member(self, member: Member) -> None:
        """
        Add a member into the cost manager
        """
        curr = self.balance.keys()
        self.balance[member] = {}
        for debtor in curr:
            self.balance[debtor][member] = 0.0
            self.balance[member][debtor] = 0.0

    def delete_member(self, member: Member) -> None:
        """
        Delete a current member from this cost manager, including the balance sheet
        No behavior if the member does not exist in this manager
        """
        if member in self.balance.keys():
            self.balance.pop(member)
            for debtor in self.balance.keys():
                self.balance[debtor].pop(member)

    def add_cost(self, cost: Cost) -> None:
        """
        Add a new cost into the transaction sheet
        Invoke updating the balance immediately
        """
        self.ID_count += 1
        self.transactions[self.ID_count] = cost
        self.calculate_balance(cost)

    def __str__(self) -> None:
        result = ""
        for debtor in self.balance.keys():
            result = result + debtor.get_name() + "\n" + "-------------\n"
            they_owe_you = "They Owe You: \n"
            you_owe_them = "You Owe Them: \n"
            for payer in self.balance[debtor].keys():
                if self.balance[debtor][payer] > 0:
                    you_owe_them = you_owe_them + "\t" + payer.get_name() + " : " + str(self.balance[debtor][payer]) + "\n"
                if self.balance[debtor][payer] < 0:
                    they_owe_you = they_owe_you + "\t" + payer.get_name() + " : " + str(-self.balance[debtor][payer]) + "\n"
            result = result + they_owe_you + you_owe_them + "\n"
        return result


