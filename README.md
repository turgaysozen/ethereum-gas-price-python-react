# Gas Price Calculation 
You can run gas price calculation project by following command `docker-compose up --build` and then visit [Localhost](http://localhost:3000).

For server side development Python-Django, for client side development React.js were used.

For estimating gas price below MetaMask logic was used along with web3.py library.

The following MetaMask algorithm was used with web3.py to estimate gas price.

1. Get the details of the 5 most recent blocks.
2. Get the base fee of the latest block.
3. Adjust the base fee according to the high, medium and low user priority.
4. From each block, collect the priority fee for transactions at the 10th, 20th, and 30th percentiles.
5. Sort the priority fees according to the percentile and get the medians of each of the sorted list of priority fees.
6. Adjust the medians according to the high, medium and low user priority.
7. Get the gas estimates of your transaction.
8. Calculate the fee using the following formula,  

`fee = (gas estimates) * (adjustedBaseFee + adjustedPriorityFeeMedian)`

Below articles and examples were used to get inspiration:
1. https://ethereum.org/en/developers/docs/
2. https://web3py.readthedocs.io/en/stable/
3. https://docs.metamask.io/guide/
4. https://paxful.com/university/ethereum-gas-price-explained/
5. https://chainstack.com/a-developers-guide-to-the-transactions-in-mempool-metamask-edition/
6. https://chainstack.com/a-developers-guide-to-the-transactions-in-mempool-code-edition/
7. https://infura.io/dashboard/ethereum/07531cf4e16147c5ae9b7d617b870e09/settings
8. https://etherscan.io/gastracker
9. https://ethereum.org/en/developers/docs/gas/
10. https://www.blocknative.com/gas-platform
11. https://github.com/MetaMask/controllers/blob/db34740520a9a873c3371d80066a474d427e440b/src/gas/fetchGasEstimatesViaEthFeeHistory/calculateGasFeeEstimatesForPriorityLevels.ts
