import statistics
from web3 import Web3
import os
from backend.settings import *


class GasPrice:
    def __init__(self):
        self.node_endpoint = os.getenv('NODE_ENDPOINT')
        self.base_fee_percentage_factor = BASEFEE_PERCENTAGE_FACTOR
        self.priority_fee_percentage_factor = PRIORITY_FEE_PERCENTAGE_FACTOR
        self.minimum_fee = MINIMUM_FEE
        self.fee_by_priority = {
            'low': [],
            'medium': [],
            'high': []
        }
        self.gas_usage = 21000 # minumum gas usage of a simple transaction
        self.gas_price = {}

    def estimate_gas_price(self):
        try:
            w3 = Web3(Web3.HTTPProvider(self.node_endpoint)) 

            # get last 5 fees based with priority
            fee_history = w3.eth.fee_history(5, 'latest', [10, 20, 30])
            latest_base_fee = fee_history["baseFeePerGas"][-1]

            # store all base fees depending on priority
            for fees in fee_history['reward']:
                self.fee_by_priority['low'].append(fees[0])
                self.fee_by_priority['medium'].append(fees[1])
                self.fee_by_priority['high'].append(fees[2])

            # adjust base fees depending on priority
            for key in self.fee_by_priority:
                median_of_fees = statistics.median(self.fee_by_priority[key])

                #calculate median fee for each priority and if its lower than minimum fee use minimum fee
                adjusted_median_fee = median_of_fees * self.priority_fee_percentage_factor[key]
                adjusted_median_fee = adjusted_median_fee if adjusted_median_fee > self.minimum_fee[key] else self.minimum_fee[key]
                sugg_max_pri_fee_per_gas_in_gwei = round(w3.fromWei(adjusted_median_fee, 'gwei'), 4)

                adjusted_base_fee = latest_base_fee * self.base_fee_percentage_factor[key]
                adjusted_base_fee_in_gwei = round(w3.fromWei(adjusted_base_fee, 'gwei'), 4)

                suggested_max_fee_per_gas = adjusted_base_fee + adjusted_median_fee
                suggested_max_fee_per_gas_in_gwei = round(w3.fromWei(suggested_max_fee_per_gas, 'gwei'), 4)

                total_gas_fee = suggested_max_fee_per_gas_in_gwei * self.gas_usage
                total_gas_fee = round(w3.fromWei(total_gas_fee, 'gwei'), 4)

                self.gas_price[key] = {
                    'max_priority_fee': sugg_max_pri_fee_per_gas_in_gwei,
                    'adjusted_base_fee_in_gwei': adjusted_base_fee_in_gwei,
                    'max_fee': suggested_max_fee_per_gas_in_gwei,
                    'gas_price': total_gas_fee
                }

            return self.gas_price
        except Exception as e:
            print(f"An error occured while estimating gas price, error: {e}")
            return None