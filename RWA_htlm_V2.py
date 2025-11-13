# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:04:49 2025

@author: molin
"""
import pandas as pd


data = {
    'Solution': [ 'Abaxx (ID++/FDT)', 'Securitize NYSE (via ICE)', 'Chainlink CCIP', 'BlackRock BUIDL', 'JPMorgan Onyx', 'Polkadot', 'Corda', 'Polymesh', 'Lightning Network', 'Coinbase', 'COTI V2', 'Ondo Finance', 'Centrifuge', 'SWIFT Blockchain', 'Solana', 'Ethereum', 'WisdomTree tokenization initiatives', 'Franklin Templeton BENJI', 'DTCC Collateral Pilot', 'Ripple', 'Deutsche Boerse Seturion', 'ICE Digital Assets', 'Circle', 'Tether', 'Visa tokenization initiatives', 'Hyperliquid', 'Bakkt', 'OpenEden', 'Nasdaq Tokenized Securities', 'Provenance Foundation', 'LSE DMI', 'MakerDAO/FRAX', '0x Protocol', 'CME GCUL', 'Realio Network', 'Augur', 'Openverse Global Layer0', 'idOS Network', 'Rayls Labs', 'TSE/JPX Digital Securities', 'Novastro', 'B3 Digitas/ACXRWA', 'LME Modernization', 'Kalshi', 'Polymarket', 'Crypto.com', 'RobinHood', 'PredictIt', 'SHFE Initiatives', ],
    'End-to-End Privacy and Security Mechanisms': [ 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Identity and Ownership Verification with Legal Finality': [ 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Private T+0 Settlement for Domestic and Cross-Border RWA Trading': [ 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'TradFi Integration Costs': [ 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Decentralization Risk Management': [ 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Seamless Onboarding of Large RWA Traders': [ 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Liquidity Fragmentation Risks': [ 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Hacking/Manipulation Risks': [ 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Regulatory Adaptability': [ 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'DeFI Transition Path': [ 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Leverage of Existing Ecosystem Advantages': [ 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'KYC/AML Integration': [ 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Scalability and Throughput': [ 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'High', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Custody and Asset Verification Mechanisms': [ 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Interoperability Across Chains/Systems': [ 'High', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Ongoing Operational Cost Efficiency': [ 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Auditability and Third-Party Verification': [ 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', ],
    'Points': [ 120, 120, 117, 115, 118, 115, 118, 107, 102, 101, 99, 98, 98, 98, 93, 93, 96, 96, 96, 95, 94, 94, 94, 94, 93, 93, 91, 91, 91, 91, 91, 90, 87, 90, 90, 87, 84, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83 ]
}

# Convert to DataFrame for sorting and consistency
df = pd.DataFrame(data)

tooltip_header = {
    "Solution": {
        "Description": "Represents various blockchain and traditional platforms evaluated for RWA tokenization, ranked by aggregated points reflecting their performance across criteria.",
        "Impact": None,
        "Inverse Ranking": None},
    "End-to-End Privacy and Security Mechanisms": {
        "Description": "Ensures encrypted P2P workflows for communications, storage, and signatures in RWA trading, preventing reverse-engineering or leaks. Necessary for trust among privacy-focused institutional traders; high impact on success by safeguarding positions and flows, enabling high-volume adoption without competitive risks.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Identity and Ownership Verification with Legal Finality": {
        "Description": "Implements DID/VCs and private digital titles for legally enforceable ownership under standards like MLETR. Crucial for real-world asset validity and dispute resolution; high impact on success by bridging digital and legal realms, facilitating secure, scalable RWA onboarding globally.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Private T+0 Settlement for Domestic and Cross-Border RWA Trading": {
        "Description": "Facilitates instant, private settlements for RWAs within and across borders, minimizing delays and counterparty risks. Essential for efficient global markets; high impact on success by boosting liquidity and reducing costs, attracting TradFi players to digital platforms.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "TradFi Integration Costs": {
        "Description": "Assesses implementation friction and costs for integrating with existing TradFi systems like clearing and settlement. Low costs vital for quick, low-risk RWA onboarding; medium impact on success as it speeds market entry without disrupting operations, though not core to functionality.",
        "Impact": "Medium",
        "Inverse Ranking": True
    },
    "Decentralization Risk Management": {
        "Description": "Balances centralization for control and decentralization for resilience, minimizing oracle/bridge vulnerabilities. Important for hybrid system reliability; medium impact on success by reducing failure points, enhancing stability for RWA trading without over-relying on either paradigm.",
        "Impact": "Medium",
        "Inverse Ranking": False
    },
    "Seamless Onboarding of Large RWA Traders": {
        "Description": "Enables easy integration with existing platforms and back-offices for major traders, reducing legal/IT barriers. Critical for adoption by incumbents; high impact on success by lowering uncertainty and costs, accelerating volume migration to new RWA solutions.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Liquidity Fragmentation Risks": {
        "Description": "Evaluates potential for splitting trading volumes across platforms/chains, reducing efficiency. Low risks necessary to consolidate liquidity; high impact on success by ensuring deep markets, attracting participants, and preventing the pitfalls seen in fragmented DeFi ecosystems.",
        "Impact": "High",
        "Inverse Ranking": True
    },
    "Hacking/Manipulation Risks": {
        "Description": "Measures susceptibility to attacks like hacking, DDoS, or manipulation. Low risks essential for security in high-stakes RWA trading; high impact on success by building institutional confidence, preventing losses, and ensuring platform longevity amid cyber threats.",
        "Impact": "High",
        "Inverse Ranking": True
    },
    "Regulatory Adaptability": {
        "Description": "Gauges flexibility to comply with evolving regulations favoring centralized or decentralized models. Vital for legal operation across jurisdictions; medium impact on success by enabling sustained growth and avoiding bans, adapting to frameworks like MiCA or SEC rules.",
        "Impact": "Medium",
        "Inverse Ranking": False
    },
    "DeFI Transition Path": {
        "Description": "Provides a roadmap to evolve toward fully decentralized finance over time. Useful for long-term innovation; low impact on immediate success as current focus is hybrid adoption, but supports future-proofing RWA platforms against shifting paradigms.",
        "Impact": "Low",
        "Inverse Ranking": False
    },
    "Leverage of Existing Ecosystem Advantages": {
        "Description": "Utilizes incumbents' networks for faster RWA transfer to new platforms. Beneficial for quick scaling; high impact on success by leveraging established relationships and infrastructure, giving an edge to solutions backed by traditional finance players.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "KYC/AML Integration": {
        "Description": "Incorporates built-in verification for user identity and anti-money laundering compliance. Essential for regulatory approval and fraud prevention; high impact on success by enabling institutional participation, reducing legal risks, and fostering trust in RWA ecosystems.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Scalability and Throughput": {
        "Description": "Handles high transaction volumes and loads efficiently, supporting massive RWA inflows. Critical for performance under growth; high impact on success by preventing bottlenecks, ensuring smooth operations, and accommodating trillions in assets without degradation.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Custody and Asset Verification Mechanisms": {
        "Description": "Offers secure custody and proofs linking tokens to real assets, preventing fraud. Necessary for trust in tokenization; high impact on success by verifying ownership, reducing double-spending risks, and attracting cautious investors to RWA platforms.",
        "Impact": "High",
        "Inverse Ranking": False
    },
    "Interoperability Across Chains/Systems": {
        "Description": "Enables seamless connections between blockchains, protocols, and TradFi APIs for composability. Important to avoid silos; medium impact on success by enhancing liquidity and flexibility, allowing RWAs to flow across ecosystems without fragmentation.",
        "Impact": "Medium",
        "Inverse Ranking": False
    },
    "Ongoing Operational Cost Efficiency": {
        "Description": "Minimizes fees, maintenance, and energy costs for sustained RWA trading. Low costs crucial for competitiveness; medium impact on success by improving profitability and accessibility, encouraging long-term use by high-volume traders over costly alternatives.",
        "Impact": "Medium",
        "Inverse Ranking": True
    },
    "Auditability and Third-Party Verification": {
        "Description": "Supports regular audits and transparent reporting while preserving privacy. Essential for credibility; medium impact on success by mitigating risks through independent checks, building investor confidence, and complying with standards in RWA onboarding.",
        "Impact": "Medium",
        "Inverse Ranking": False
    },
    "Points": {
        "Description": "Calculation methodology: Award 3 points for HIGH, 2 for MEDIUM, 1 for LOW on each criterion. For Inverse Ranking criteria, reverse to 1 for HIGH, 2 for MEDIUM, 3 for LOW. Multiply by 3x for HIGH Impact, 2x for MEDIUM, 1x for LOW. Sum points across criteria for total score, ranking solutions by aggregated attractiveness for RWA onboarding.",
        "Impact": None,
        "Inverse Ranking": None
    }
}



# #
solution_types = {
    'Abaxx':        {"type": "DeFi_TradFi", 'color'    :'#FFFF00',
                     'display'  : True},    # Yellow for Abaxx row
    'Perm_Chain':   {"type": "DeFi_TradFi", 'color'    : '#1E90FF',
                     'display'  : True},    # Blue: Permissioned Blockchain/Enterprise
    'DeFi_TradFi':  {"type": "DeFi_TradFi", 'color'    : '#90EE90',
                     'display'  : True},    # Green: Hybrid DeFi/TradFi
    'Pub_Chain':    {'color'    : '#FFA07A',
                     'display'  : True},    # Orange: Public Blockchain
    'Trad_Exch':    {"type": "Trad_Exch", 'color'    : '#D3D3D3',
                     'display'  : True},    # Gray: Traditional Exchange
    'Pred_Mkt':     {"type": "Pred_Mkt", 'color'    : '#800080',
                     'display'  : True},    # Purple for prediction markets
    'Other':        {"type": "Other", 'color'    : '#FFF',
                     'display'  : True}    # Default white if no match
}

solution_map = {
    "Abaxx (ID++/FDT)": "Abaxx",
    "Securitize NYSE (via ICE)": "DeFi_TradFi",
    "Chainlink CCIP": "Pub_Chain",
    "BlackRock BUIDL": "DeFi_TradFi",
    "JPMorgan Onyx": "Perm_Chain",
    "Polkadot": "Pub_Chain",
    "Corda": "Perm_Chain",
    "Polymesh": "Pub_Chain",
    "Lightning Network": "Pub_Chain",
    "Coinbase": "DeFi_TradFi",
    "COTI V2": "Pub_Chain",
    "Ondo Finance": "DeFi_TradFi",
    "Centrifuge": "Pub_Chain",
    "SWIFT Blockchain": "Perm_Chain",
    "Solana": "Pub_Chain",
    "Ethereum": "Pub_Chain",
    "WisdomTree tokenization initiatives": "DeFi_TradFi",
    "Franklin Templeton BENJI": "DeFi_TradFi",
    "DTCC Collateral Pilot": "Perm_Chain",
    "Ripple": "Pub_Chain",
    "Deutsche Boerse Seturion": "Trad_Exch",
    "ICE Digital Assets": "Trad_Exch",
    "Circle": "DeFi_TradFi",
    "Tether": "DeFi_TradFi",
    "Visa tokenization initiatives": "Perm_Chain",
    "Hyperliquid": "Pub_Chain",
    "Bakkt": "Trad_Exch",
    "OpenEden": "DeFi_TradFi",
    "Nasdaq Tokenized Securities": "Trad_Exch",
    "Provenance Foundation": "Pub_Chain",
    "LSE DMI": "Trad_Exch",
    "MakerDAO/FRAX": "Pub_Chain",
    "0x Protocol": "Pub_Chain",
    "CME GCUL": "Trad_Exch",
    "Realio Network": "Pub_Chain",
    "Augur": "Pred_Mkt",
    "Openverse Global Layer0": "Pub_Chain",
    "idOS Network": "Pub_Chain",
    "Rayls Labs": "Pub_Chain",
    "TSE/JPX Digital Securities": "Trad_Exch",
    "Novastro": "Pub_Chain",
    "B3 Digitas/ACXRWA": "Trad_Exch",
    "LME Modernization": "Trad_Exch",
    "Kalshi": "Pred_Mkt",
    "Polymarket": "Pred_Mkt",
    "Crypto.com": "DeFi_TradFi",
    "RobinHood": "Trad_Exch",
    "PredictIt": "Pred_Mkt",
    "SHFE Initiatives": "Trad_Exch"
}

cell_hover_text = {
    'End-to-End Privacy and Security Mechanisms': {
        'Abaxx (ID++/FDT)': 'High: 5-layer P2P cryptographic stack with ZK-selective disclosure, FDT metadata shielding, and encrypted workflows. Zero public exposure of positions, flows, or intent. Prevents reverse-engineering even under regulatory audit. Designed for $100M+ commodity desks requiring full confidentiality.',
        'Securitize NYSE (via ICE)': 'Medium: Uses regulated custody and atomic swaps. NYSE/DTC integration adds compliance but no P2P encryption. Position flows visible to brokers; medium anti-reverse engineering.',
        'Chainlink CCIP': 'Medium: Encrypted messaging, but public calldata and chain patterns enable flow analysis. ZK helps verify, not hide. Not safe for large private strategies.',
        'BlackRock BUIDL': 'Medium: On-chain mint/burn visible. Custody centralized; yield accrual public. Strong compliance, but no position privacy.',
        'JPMorgan Onyx': 'High: Fully homomorphic encryption (FHE) enables confidential computation on tokenized assets. Permissioned ledger ensures no public graph. Bank-grade P2P privacy; ideal for institutional cross-border flows.',
        'Polkadot': 'Medium: Parachain isolation helps, but XCM and public validators expose frequency, volume. No native P2P encryption.',
        'Corda': 'High: Private bilateral flows with need-to-know access. No public ledger. Legal prose binding. Zero risk of flow reconstruction or adversarial inference.',
        'Polymesh': 'Medium: Identity-bound tokens prevent Sybil, but public chain exposes transfer patterns. Compliance metadata visible. Better than Ethereum, but not confidential.',
        'Lightning Network': 'Medium: Onion routing hides path, but channel liquidity and rebalancing inferable. Not suitable for non-fungible RWAs.',
        'Coinbase': 'Medium: Centralized custody with encryption in transit/rest. No public ledger, but internal logs accessible. Medium privacy; not P2P confidential.',
        'COTI V2': 'High: Garbled circuits enable confidential smart contracts. Selective disclosure hides amounts and counterparties. True private DeFi with anti-reverse engineering.',
        'Ondo Finance': 'Medium: Public vaults on Ethereum L2s. Yield accrual and token flows visible. ZK helps amounts, but patterns exposed. Medium institutional privacy.',
        'Centrifuge': 'Medium: SPVs add legal privacy, but on-chain pool activity public. Tinlake flows visible on Ethereum/Cosmos. Medium protection via legal wrappers.',
        'SWIFT Blockchain': 'Medium: Permissioned DLT with bank nodes. Private within consortium, but not end-to-end encrypted P2P. Audit trail visible to members.',
        'Solana': 'Low: Fully public, high-throughput ledger = maximum surveillance. Even ZK compression leaves metadata. Highest reverse-engineering risk.',
        'Ethereum': 'Low: Public L1/L2 exposes sender, receiver, amount (unless ZK), and dApp patterns. High risk of wallet clustering, MEV, and strategy reverse-engineering. Unsuitable for confidential institutional RWAs.',
        'WisdomTree tokenization initiatives': 'Medium: Fund-level privacy via custodians, but on-chain token transfers public. Yield and NAV visible. Medium confidentiality.',
        'Franklin Templeton BENJI': 'Medium: MMF shares tokenized on public chain. Yield accrual visible. Custodian controls access, but no P2P encryption.',
        'DTCC Collateral Pilot': 'Medium: Permissioned AppChain with member-only access. Repo flows private within consortium, but not P2P encrypted. Medium institutional privacy.',
        'Ripple': 'Medium: XRP Ledger public. ODL flows visible. ILP enables private routing, but default is transparent. Medium privacy.',
        'Deutsche Boerse Seturion': 'Medium: EU-regulated permissioned chain. Securities flows private within CSDs, but not end-to-end encrypted. Medium confidentiality.',
        'ICE Digital Assets': 'Medium: Exchange-controlled custody. Futures and spot flows private within ICE, but no P2P encryption. Medium privacy.',
        'Circle': 'Medium: USDC on public chains. Transfers visible. Circle controls mint/burn, but no transaction privacy. Medium institutional use.',
        'Tether': 'Medium: USDT on public chains. High volume but full transparency. Central attestation, no P2P privacy. Medium confidentiality.',
        'Visa tokenization initiatives': 'Medium: VTAP enables tokenized deposits, but bank-issued and visible on permissioned rails. No P2P encryption. Medium privacy.',
        'Hyperliquid': 'Low: Public L1 order book. All trades visible. No privacy; high front-running and inference risk.',
        'Bakkt': 'Medium: ICE-backed custody. Futures flows private within exchange, but no P2P encryption. Medium confidentiality.',
        'OpenEden': 'Medium: Treasury tokens on public Ethereum. KYC-gated, but flows visible. Yield accrual public. Medium privacy.',
        'Nasdaq Tokenized Securities': 'Medium: DTC-integrated. Share tokens private within broker network, but no P2P encryption. Medium confidentiality.',
        'Provenance Foundation': 'Medium: Cosmos-based. Loan pools public. SPVs add legal privacy, but on-chain flows visible. Medium protection.',
        'LSE DMI': 'Medium: Azure-based fund tokens. Private within LSE ecosystem, but no P2P encryption. Medium institutional privacy.',
        'MakerDAO/FRAX': 'Low: Public vaults. Collateral, debt, liquidations all visible. High inference risk.',
        '0x Protocol': 'Low: Public atomic swaps. Full transparency. No confidentiality.',
        'CME GCUL': 'Medium: CME clearing ensures privacy within members. Programmable futures visible on-chain only to participants. Medium confidentiality.',
        'Realio Network': 'Medium: Multi-chain real estate tokens. SPVs add legal privacy, but transfers public. Medium protection.',
        'Augur': 'Low: Public prediction markets on Ethereum. Bets and outcomes visible. No privacy.',
        'Openverse Global Layer0': 'Medium: ZK bridges hide cross-chain details, but underlying flows public. Medium privacy via obfuscation.',
        'idOS Network': 'Medium: Identity layer with encryption. No direct asset privacy. Medium user-level protection.',
        'Rayls Labs': 'High: Dual-layer architecture: private bank chain + public settlement. Confidential compute prevents leakage. Institutional-grade privacy.',
        'TSE/JPX Digital Securities': 'Medium: Japan exchange-controlled. Stock tokens private within TSE, but no P2P encryption. Medium confidentiality.',
        'Novastro': 'Medium: AI-optimized yield on public L3. Strategies visible. No P2P privacy.',
        'B3 Digitas/ACXRWA': 'Medium: Brazil-regulated. Asset tokens private within B3, but no P2P encryption. Medium confidentiality.',
        'LME Modernization': 'Medium: Metal warrants on exchange DLT. Flows private within LME, but not P2P encrypted. Medium privacy.',
        'Kalshi': 'Medium: CFTC-regulated event contracts. Private within platform, but no blockchain P2P privacy. Medium confidentiality.',
        'Polymarket': 'Low: Public prediction markets on Polygon. Bets and resolutions visible. No privacy.',
        'Crypto.com': 'Medium: Centralized exchange with wallet. Flows private internally, but no P2P encryption. Medium privacy.',
        'RobinHood': 'Medium: Broker-controlled wallet. Crypto flows private within Robinhood, but no P2P encryption. Medium confidentiality.',
        'PredictIt': 'Medium: CFTC-capped academic platform. No blockchain; flows private. Medium privacy (non-DLT).',
        'SHFE Initiatives': 'Medium: China commodity exchange. Tokenized assets private within SHFE, but no P2P encryption. Medium confidentiality.'
    },
    'Identity and Ownership Verification with Legal Finality': {
        'Abaxx (ID++/FDT)': 'High: Abaxx’s ID++ uses decentralized identifiers (DIDs) and verifiable credentials (VCs) to bind real-world identities to on-chain wallets with cryptographic proof. FDT ensures legal finality under MLETR, making digital documents enforceable in courts. This eliminates disputes over ownership in tokenized commodities, supports KYC/AML compliance, and enables institutional-grade onboarding with full audit trails and regulatory alignment.',
        'Securitize NYSE (via ICE)': 'High: Securitize integrates KYC-verified identities into ERC-1400 tokens, linking ownership to legal entities via NYSE/ICE custody. SEC-compliant transfers ensure finality, identical to traditional shares. This provides institutional-grade legal enforceability, seamless TradFi onboarding, and third-party verification through regulated brokers and DTC settlement.',
        'Chainlink CCIP': 'Medium: CCIP enables cross-chain ownership transfer with oracle-verified data, but identity is chain-dependent. No native KYC or legal finality framework; relies on underlying chains. Useful for interoperability, but lacks enforceable ownership rights without additional compliance layers.',
        'BlackRock BUIDL': 'High: BUIDL tokenizes fund shares with on-chain ownership verified through regulated custodians and KYC. Legal finality via SEC filings and DTC integration ensures tokenized units are identical to traditional shares. Enables institutional redemption and auditability with full compliance.',
        'JPMorgan Onyx': 'High: Onyx uses permissioned blockchain with embedded KYC and smart legal contracts to verify identity and ownership. Tokenized deposits and assets have bank-grade finality. Supports enforceable settlements in private equity and collateral, fully integrated with JPM’s compliance systems.',
        'Polkadot': 'High: Polkadot supports on-chain identity via Identity Pallet and governance-verified attestations. Parachain sovereignty enables legally compliant asset modules. Ownership finality achieved through relay chain consensus; supports regulatory frameworks for tokenized securities.',
        'Corda': 'High: Corda’s CorDapps embed legal prose in smart contracts, linking on-chain states to off-chain legal agreements. Notary services ensure uniqueness and finality. Identity managed via X.509 certificates; ideal for regulated financial assets with enforceable ownership.',
        'Polymesh': 'High: Polymesh requires mandatory identity for all participants via on-chain KYC. Asset tokens include compliance rules ensuring only verified holders can own. Settlement finality and legal enforceability built into protocol; designed for regulated securities.',
        'Lightning Network': 'Medium: Lightning supports Taproot Assets for tokenized ownership off-chain, but no native identity or legal framework. Relies on Bitcoin finality; suitable for bearer assets, not regulated RWAs requiring KYC or court enforceability.',
        'Coinbase': 'Medium: Coinbase enforces KYC for all users and supports tokenized assets, but ownership is custodial. Legal finality depends on exchange policies, not on-chain. Regulatory compliance strong, but not decentralized or self-sovereign.',
        'COTI V2': 'Medium: COTI V2 supports selective disclosure for identity and confidential asset verification. No built-in legal finality or KYC; ownership provable on-chain but not court-enforceable without external frameworks.',
        'Ondo Finance': 'Medium: Ondo verifies collateral ownership via smart contracts and oracles, with KYC at entry. Legal finality limited to DeFi liquidation rules. Suitable for yield-bearing RWAs, but not regulated securities with legal recourse.',
        'Centrifuge': 'Medium: Centrifuge uses Tinlake pools to verify real-world asset ownership via legal SPVs and KYC. On-chain claims enforceable via smart contracts, but finality depends on off-chain legal agreements and jurisdiction.',
        'SWIFT Blockchain': 'Medium: SWIFT’s permissioned ledger supports KYC-verified participants and digital asset transfers. Ownership tracked securely, but legal finality relies on existing banking law, not blockchain-native enforceability.',
        'Solana': 'Medium: Solana supports SPL tokens with metadata for ownership, but no native identity or legal layer. KYC must be added via dApps. High throughput enables fast settlement, but not institutional legal finality.',
        'Ethereum': 'Medium: Ethereum supports ERC-721/ERC-20 for ownership, with ENS and KYC dApps. Legal finality requires off-chain agreements or oracles. Strong for DeFi, but not natively compliant with securities law.',
        'WisdomTree tokenization initiatives': 'Medium: WisdomTree verifies ownership in tokenized funds via regulated custodians and KYC. Legal finality through traditional fund structures. Blockchain used for efficiency, not native enforceability.',
        'Franklin Templeton BENJI': 'Medium: BENJI tokens represent MMF shares with on-chain ownership and KYC. Legal finality via existing fund prospectus. Compliant and auditable, but ownership tied to traditional legal entity.',
        'DTCC Collateral Pilot': 'Medium: DTCC’s pilot tokenizes collateral with digital certificates and KYC. Ownership verified via AppChain, finality through existing settlement systems. Strong regulatory alignment, but not fully decentralized.',
        'Ripple': 'Medium: Ripple enables tokenized asset transfer with partner KYC, but no native legal finality. Ownership provable on ledger; enforceability depends on bilateral agreements and local law.',
        'Deutsche Boerse Seturion': 'Medium: Seturion supports tokenized securities with KYC and regulatory oversight. Ownership tracked on permissioned chain; finality via existing clearing systems. Compliant, but not self-sovereign.',
        'ICE Digital Assets': 'Medium: ICE verifies ownership in tokenized commodities via regulated platform and KYC. Legal finality through exchange rules. Strong for institutional trading, but centralized control.',
        'Circle': 'Medium: Circle’s USDC supports KYC and blacklisting for compliance. Ownership tracked on-chain, but finality enforced by issuer. Not suitable for non-fungible or complex RWAs.',
        'Tether': 'Medium: Tether enables tokenized asset issuance with KYC via partners. Ownership on-chain, but legal finality limited by reserve transparency and issuer control.',
        'Visa tokenization initiatives': 'Medium: VTAP enables banks to issue tokenized deposits with KYC. Ownership verified via Visa network; finality through banking law. Strong compliance, but not blockchain-native.',
        'Hyperliquid': 'Medium: Hyperliquid supports synthetic assets with on-chain ownership, but no KYC or legal framework. Finality via smart contracts; suitable for derivatives, not regulated RWAs.',
        'Bakkt': 'Medium: Bakkt verifies ownership in regulated futures and custody. KYC enforced; legal finality via CFTC rules. Strong for institutional crypto, but not decentralized.',
        'OpenEden': 'Medium: OpenEden verifies treasury ownership via KYC and on-chain yields. Legal finality through SPV and fund documents. Compliant, but not self-custodied.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq proposes fungible tokenized shares with DTC settlement. Ownership verified via brokers; legal finality identical to traditional stocks. Regulatory-focused.',
        'Provenance Foundation': 'Medium: Provenance uses Hash token for governance and KYC. Ownership in loan pools verifiable; finality via legal agreements and Cosmos SDK.',
        'LSE DMI': 'Medium: LSE’s DMI tokenizes funds on Azure with KYC. Ownership tracked digitally; finality via existing fund settlement. Regulatory compliant, but centralized.',
        'MakerDAO/FRAX': 'Medium: Maker verifies collateral ownership via vaults; over-collateralized. No KYC or legal finality. Ownership enforceable only via liquidation, not law.',
        '0x Protocol': 'Medium: 0x enables atomic swaps with on-chain ownership proof. No identity or legal layer. Finality via Ethereum; suitable for DEX, not regulated assets.',
        'CME GCUL': 'Medium: GCUL tokenizes assets with programmable logic and KYC. Ownership verified via Google Cloud; finality through CME clearing. Compliant, but centralized.',
        'Realio Network': 'Medium: Realio supports multi-chain RWAs with KYC dApps. Ownership on-chain; finality depends on jurisdiction and SPV structure.',
        'Augur': 'Medium: Augur verifies outcome ownership via REP staking. No KYC or legal finality. Ownership in prediction shares; enforceable only on-chain.',
        'Openverse Global Layer0': 'Medium: Layer0 supports cross-chain identity and asset bridging. Ownership verifiable via ZK proofs; no native legal finality.',
        'idOS Network': 'Medium: idOS enables decentralized identity with selective disclosure. Ownership linked to DID; no legal finality without external frameworks.',
        'Rayls Labs': 'Medium: Rayls supports bank-grade identity and tokenization. Ownership verified via dual-layer; finality through compliance, not blockchain-native.',
        'TSE/JPX Digital Securities': 'Medium: TSE tokenizes stocks with regulatory KYC. Ownership identical to traditional shares; finality via exchange settlement.',
        'Novastro': 'Medium: Novastro uses AI and SPVs for RWA tokenization. Ownership verified off-chain; finality via legal structure, not blockchain.',
        'B3 Digitas/ACXRWA': 'Medium: B3 tokenizes assets with digital twins and KYC. Ownership tracked on-chain; finality via Brazilian regulation.',
        'LME Modernization': 'Medium: LME tokenizes warrants with exchange oversight. Ownership verified via membership; finality through delivery rules.',
        'Kalshi': 'Medium: Kalshi verifies event contract ownership via CFTC compliance. No blockchain identity; finality via regulated settlement.',
        'Polymarket': 'Medium: Polymarket verifies outcome shares on-chain. No KYC; finality via USDC settlement, not legal enforceability.',
        'Crypto.com': 'Medium: Crypto.com enforces KYC and supports tokenized assets. Ownership custodial; finality via exchange policy, not law.',
        'RobinHood': 'Medium: Robinhood verifies ownership via broker-dealer KYC. Tokenized assets custodial; finality through SEC rules.',
        'PredictIt': 'Medium: PredictIt caps contract ownership with CFTC approval. No blockchain; finality via platform rules, not legal ownership.',
        'SHFE Initiatives': 'Medium: SHFE tokenizes commodities under exchange rules. Ownership verified via membership; finality through traditional clearing, not blockchain.'
    },
    'Private T+0 Settlement for Domestic and Cross-Border RWA Trading': {
        'Abaxx (ID++/FDT)': 'High: Abaxx enables private T+0 settlement via FDT and Adaptive Clearing, ensuring atomic delivery-vs-payment (DvP) for tokenized commodities. Cross-border trades settle instantly with legal finality under MLETR. Privacy preserved through encrypted P2P workflows; no central counterparty exposure. Ideal for institutional RWAs requiring confidentiality, speed, and global enforceability without liquidity fragmentation.',
        'Securitize NYSE (via ICE)': 'High: Securitize supports T+0 settlement on NYSE/ICE infrastructure using atomic swaps and tokenized securities. Private DvP with KYC-verified participants ensures confidentiality. Cross-border enabled via regulated brokers; legal finality identical to traditional shares. Eliminates T+1 delays, reduces counterparty risk, and integrates seamlessly with existing market plumbing.',
        'Chainlink CCIP': 'High: CCIP enables private T+0 cross-chain settlement with encrypted messaging and verifiable finality. Supports tokenized RWAs across ecosystems (e.g., Ethereum to Polygon) with atomic execution. Privacy via ZK proofs; no intermediary exposure. Regulatory-compliant bridges reduce fragmentation, ideal for institutional cross-border flows.',
        'BlackRock BUIDL': 'High: BUIDL offers T+0 intraday redemption and yield accrual on tokenized treasuries. Private settlement via on-chain mint/burn with institutional custody. Cross-border access through regulated platforms; legal finality via fund shares. Eliminates T+1 delays, enhances capital efficiency, and supports 24/7 global liquidity.',
        'JPMorgan Onyx': 'High: Onyx (Kinexys) enables T+0 settlement of tokenized deposits and assets on permissioned blockchain. Private DvP with FHE ensures confidentiality. Cross-border pilots (e.g., Singapore, Japan) demonstrate global reach. Legal finality via bank-grade smart contracts; reduces settlement risk and operational cost.',
        'Polkadot': 'High: Polkadot’s XCM enables T+0 cross-chain settlement with finality in ~12 seconds. Private channels and parachain isolation ensure confidentiality. Supports regulated asset parachains with KYC. Eliminates fragmentation; ideal for multi-jurisdictional RWA trading with enforceable finality.',
        'Corda': 'Medium: Corda supports T+0 settlement via notaries and private flows, but cross-border requires interoperability layers. Legal finality strong within consortiums. Privacy excellent for bilateral trades; scalable for enterprise RWAs but limited public chain access.',
        'Polymesh': 'Medium: Polymesh enables T+0 settlement with on-chain compliance and atomic transfers. Private via identity-bound tokens. Cross-border limited by ecosystem size; strong for regulated securities but not yet global-scale liquidity.',
        'Lightning Network': 'High: Lightning enables T+0 micropayments and asset swaps off-chain with Bitcoin finality. Private via onion routing. Cross-border instant; ideal for micro-RWAs (e.g., stablecoins), but limited smart contract support for complex assets.',
        'Coinbase': 'Medium: Coinbase supports T+0 crypto settlement, but RWAs are custodial. Cross-border via USDC; privacy limited by exchange oversight. No on-chain finality for tokenized securities; suitable for retail, not institutional-grade DvP.',
        'COTI V2': 'Medium: COTI V2 enables T+0 confidential payments on DAG L2. Cross-chain via MultiDAG; privacy via garbled circuits. Supports RWAs but lacks native securities compliance; strong for DeFi, medium for regulated cross-border.',
        'Ondo Finance': 'High: Ondo enables T+0 yield accrual and redemption in tokenized treasuries (OUSG). Private settlement via vaults; cross-border via USDC. Institutional-grade with KYC; legal finality via fund structure. Eliminates T+1 delays and enhances liquidity.',
        'Centrifuge': 'High: Centrifuge enables T+0 settlement in Tinlake pools via atomic mint/burn. Cross-border via Cosmos IBC; privacy via SPVs. Legal finality through off-chain agreements; strong for private credit RWAs with institutional onboarding.',
        'SWIFT Blockchain': 'High: SWIFT’s DLT trials enable T+0 cross-border settlement with 100+ banks. Private via permissioned ledger; legal finality via existing corridors. Reduces FX and counterparty risk; bridges TradFi and blockchain seamlessly.',
        'Solana': 'High: Solana achieves T+0 settlement in ~400ms with parallel execution. Cross-chain via Wormhole; privacy via ZK compression. Supports high-frequency RWAs; scalable but validator centralization limits institutional trust.',
        'Ethereum': 'High: Ethereum L2s (e.g., Arbitrum, Base) enable T+0 settlement with rollup finality. Cross-chain via bridges; privacy via ZK. Gas costs reduced; strong DeFi ecosystem, but base layer congestion affects reliability.',
        'WisdomTree tokenization initiatives': 'Medium: WisdomTree enables T+0 intraday access to tokenized funds. Settlement via traditional systems; cross-border limited. Privacy via custody; legal finality strong but not blockchain-native T+0 DvP.',
        'Franklin Templeton BENJI': 'Medium: BENJI offers T+0 yield but settlement via fund NAV. Cross-border via brokers; privacy through custody. Legal finality via prospectus; not atomic on-chain settlement.',
        'DTCC Collateral Pilot': 'Medium: DTCC enables T+0 collateral mobilization on AppChain. Private settlement within pilot; cross-border potential. Legal finality via existing systems; strong for repo but not full RWA trading.',
        'Ripple': 'High: Ripple enables T+0 cross-border settlement with XRP or stablecoins. Private via payment channels; 150+ countries. Legal finality via banking partners; reduces nostro costs and settlement risk.',
        'Deutsche Boerse Seturion': 'Medium: Seturion unifies T+0 settlement across assets. Private via permissioned chain; cross-border in EU. Legal finality via CSDR; strong for Europe, limited global reach.',
        'ICE Digital Assets': 'Medium: ICE supports T+0 crypto settlement; RWAs via custody. Cross-border via Bakkt; privacy regulated. Legal finality via exchange rules; not blockchain-native DvP.',
        'Circle': 'Medium: Circle enables T+0 USDC transfers globally. Private via wallets; cross-border strong. No native RWA settlement; legal finality via issuer, not on-chain.',
        'Tether': 'Medium: Tether enables T+0 USDT transfers; RWAs via Hadron. Cross-border strong; privacy via compliance. Legal finality limited by reserves; not institutional-grade.',
        'Visa tokenization initiatives': 'Medium: VTAP enables T+0 tokenized deposit settlement via banks. Private via network; cross-border potential. Legal finality via banking law; not blockchain-native.',
        'Hyperliquid': 'Medium: Hyperliquid enables T+0 perp settlement on L1. Cross-chain via bridges; privacy on-chain. No KYC or legal finality; strong for derivatives, not RWAs.',
        'Bakkt': 'Medium: Bakkt enables T+0 crypto futures settlement. RWAs via custody; cross-border limited. Legal finality via CFTC; not private blockchain settlement.',
        'OpenEden': 'Medium: OpenEden enables T+0 treasury yield access. Settlement via fund; cross-border via USDC. Privacy via KYC; legal finality via SPV, not atomic.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq proposes T+0 tokenized share settlement. Cross-border via DTC; privacy regulated. Legal finality strong; not yet live on-chain.',
        'Provenance Foundation': 'Medium: Provenance enables T+0 loan settlement via Hash. Cross-border via Cosmos; privacy via governance. Legal finality via SPV; strong for credit.',
        'LSE DMI': 'Medium: LSE DMI enables T+0 fund access. Settlement via Azure; cross-border limited. Privacy via custody; legal finality via fund rules.',
        'MakerDAO/FRAX': 'Medium: Maker enables T+0 DAI mint/burn. Settlement on Ethereum; cross-border via DEXs. No legal finality; strong for stablecoins, not RWAs.',
        '0x Protocol': 'Medium: 0x enables T+0 atomic swaps. Cross-chain via bridges; privacy on-chain. No legal finality; strong for DEX liquidity.',
        'CME GCUL': 'Medium: GCUL enables T+0 programmable settlement. Cross-border via Google Cloud; privacy compliant. Legal finality via CME; not fully decentralized.',
        'Realio Network': 'Medium: Realio enables T+0 RWA settlement multi-chain. Cross-border via IBC; privacy via Cosmos. Legal finality via SPV; growing ecosystem.',
        'Augur': 'Medium: Augur enables T+0 outcome settlement. Cross-chain limited; privacy on-chain. No legal finality; strong for prediction markets.',
        'Openverse Global Layer0': 'Medium: Layer0 enables T+0 cross-chain settlement. Privacy via ZK; legal finality limited. Strong interoperability; early stage.',
        'idOS Network': 'Medium: idOS enables identity-linked T+0 transfers. Cross-chain potential; privacy strong. No native settlement finality.',
        'Rayls Labs': 'Medium: Rayls enables T+0 bank-grade settlement. Private dual-layer; cross-border strong. Legal finality via compliance.',
        'TSE/JPX Digital Securities': 'Medium: TSE enables T+0 tokenized stock settlement. Cross-border limited; privacy regulated. Legal finality via exchange.',
        'Novastro': 'Medium: Novastro enables T+0 AI-optimized RWA settlement. Cross-chain via L3; privacy via SPVs. Legal finality via structure.',
        'B3 Digitas/ACXRWA': 'Medium: B3 enables T+0 digital twin settlement. Cross-border in Brazil; privacy compliant. Legal finality via regulation.',
        'LME Modernization': 'Medium: LME enables T+0 warrant settlement. Cross-border via exchange; privacy regulated. Legal finality via delivery.',
        'Kalshi': 'Medium: Kalshi enables T+0 event contract settlement. Cross-border limited; privacy compliant. Legal finality via CFTC.',
        'Polymarket': 'Medium: Polymarket enables T+0 outcome settlement on Polygon. Cross-border via USDC; privacy on-chain. No legal finality.',
        'Crypto.com': 'Medium: Crypto.com enables T+0 crypto settlement. RWAs custodial; cross-border via app. No on-chain RWA finality.',
        'RobinHood': 'Medium: Robinhood enables T+0 crypto settlement. RWAs via broker; cross-border limited. Legal finality via SEC.',
        'PredictIt': 'Medium: PredictIt enables T+0 contract settlement. Cross-border no; privacy capped. Legal finality via CFTC.',
        'SHFE Initiatives': 'Medium: SHFE enables T+0 commodity futures settlement. RWAs via exchange; cross-border limited. Legal finality via regulation.'
    },
    'TradFi Integration Costs': {
        'Abaxx (ID++/FDT)':'Low: Abaxx minimizes TradFi integration costs via modular ID++ and FDT, leveraging existing exchange APIs and clearing systems. No new infrastructure required; uses standard KYC/AML rails. Pilots with MineHub and ICE demonstrate seamless onboarding at low cost. Ideal for institutions avoiding high capex for blockchain adoption.',
        'Securitize NYSE (via ICE)':'Low: Securitize integrates directly with NYSE/ICE and DTC, using existing broker-dealer networks. No custom middleware needed; leverages regulated token standards (ERC-1400). Low cost for issuers and investors; eliminates T+1 reconciliation and reduces operational overhead.',
        'Chainlink CCIP':'Low: CCIP requires minimal integration—just oracle feeds and bridge contracts. Uses standard EVM tooling; no new custody or KYC systems. Low cost for cross-chain RWAs; enables TradFi via existing smart contract frameworks.',
        'BlackRock BUIDL':'Low: BUIDL integrates with existing fund platforms and custodians. No new tech stack; uses Ethereum L2s and standard APIs. Low cost for institutional onboarding; leverages BlackRock’s existing investor base and compliance infrastructure.',
        'JPMorgan Onyx':'Low: Onyx runs on permissioned Quorum; integrates with JPM’s core banking systems. No external gateways needed; uses existing KYC and treasury rails. Low cost for internal and partner adoption; reduces settlement and FX costs.',
        'Polkadot':'Medium: Polkadot requires parachain deployment and relay chain integration. Uses Substrate; moderate dev cost. TradFi integration via bridges and oracles; higher cost than EVM but lower than full custom DLT.',
        'Corda':'Low: Corda integrates with enterprise systems via CorDapps and APIs. Uses existing identity and messaging standards. Low cost for banks and corporates; proven in R3 consortiums with minimal retraining.',
        'Polymesh':'Medium: Polymesh requires migration to custom chain with built-in compliance. Moderate cost for issuers; uses standard tooling. Lower long-term cost due to on-chain KYC/AML; initial setup higher than EVM.',
        'Lightning Network':'Medium: Lightning requires channel setup and liquidity management. Integrates with Bitcoin; moderate cost for payment-focused RWAs. Low for retail, higher for institutional custody and compliance.',
        'Coinbase':'Medium: Coinbase offers API integration but custodial. Moderate cost for KYC and compliance; no blockchain dev needed. Higher cost for self-custody or on-chain settlement; suitable for retail onboarding.',
        'COTI V2':'Medium: COTI V2 uses DAG L2; requires smart contract deployment. Moderate cost for DeFi integration; low for payments. TradFi onboarding via partners; not plug-and-play with legacy systems.',
        'Ondo Finance':'Medium: Ondo integrates via Ethereum and USDC; uses standard DeFi tooling. Moderate cost for vault setup and oracles. Low for yield products; higher for full TradFi custody integration.',
        'Centrifuge':'Medium: Centrifuge requires SPV setup and legal structuring. Moderate cost for asset onboarding; uses Cosmos SDK. Low operational cost post-setup; ideal for private credit but not instant integration.',
        'SWIFT Blockchain':'Low: SWIFT leverages existing member banks and messaging (ISO 20022). No new infrastructure; uses APIs for DLT trials. Low cost for global banks; bridges TradFi and blockchain seamlessly.',
        'Solana':'Medium: Solana requires RPC and wallet integration. Low gas but custom tooling. Moderate cost for high-throughput RWAs; higher for compliance and KYC layers.',
        'Ethereum':'Medium: Ethereum uses standard ERC tokens and wallets. Moderate gas and L2 costs. High ecosystem support; integration cost low for DeFi, higher for regulated assets.',
        'WisdomTree tokenization initiatives':'Medium: WisdomTree uses existing fund platforms and custodians. Moderate cost for blockchain layer; leverages traditional rails. Low long-term cost; high initial regulatory alignment.',
        'Franklin Templeton BENJI':'Medium: BENJI integrates with fund admin and custody. Moderate cost for on-chain mint/burn. Uses existing investor KYC; low operational cost post-launch.',
        'DTCC Collateral Pilot':'Medium: DTCC uses AppChain with existing members. Moderate cost for node deployment; leverages current clearing. Low reconciliation cost; high value for repo and collateral.',
        'Ripple':'Medium: Ripple integrates via payment APIs and ILP. Moderate cost for bank onboarding; uses existing corridors. Low FX cost; higher for full RWA tokenization.',
        'Deutsche Boerse Seturion':'Medium: Seturion uses permissioned chain with existing CSDs. Moderate cost for EU integration; leverages T2S. Low settlement cost; high regulatory alignment.',
        'ICE Digital Assets':'Medium: ICE integrates with exchange and custody. Moderate cost for tokenization layer. Uses existing members; low trading cost but high compliance setup.',
        'Circle':'Medium: Circle integrates via USDC and APIs. Low cost for stablecoin flows; moderate for RWA minting. Uses existing KYC; not full asset tokenization.',
        'Tether':'Medium: Tether uses APIs for USDT; moderate cost for RWA platforms. Low for transfers; higher for compliance and reserve proofing.',
        'Visa tokenization initiatives':'Medium: VTAP integrates with bank core systems. Moderate cost for token issuance; uses existing card rails. Low transaction cost; high regulatory overhead.',
        'Hyperliquid':'Medium: Hyperliquid uses L1 DEX; low cost for perps. No KYC or TradFi integration; high cost for institutional compliance.',
        'Bakkt':'Medium: Bakkt integrates with ICE and custody. Moderate cost for regulated futures; uses existing members. Low trading cost; high compliance setup.',
        'OpenEden':'Medium: OpenEden uses Ethereum and USDC. Moderate cost for treasury vaults; low for yield distribution. Requires KYC partner; not direct TradFi plug-in.',
        'Nasdaq Tokenized Securities':'Medium: Nasdaq uses DTC and broker networks. Moderate cost for token layer; leverages existing settlement. Low long-term cost; high initial approval.',
        'Provenance Foundation':'Medium: Provenance uses Cosmos; moderate cost for loan pools. Low for credit RWAs; requires SPV and legal setup.',
        'LSE DMI':'Medium: DMI uses Azure and fund admin. Moderate cost for token issuance; leverages existing investors. Low distribution cost; high regulatory alignment.',
        'MakerDAO/FRAX':'Medium: Maker uses Ethereum; low cost for DAI minting. No TradFi integration; high cost for collateral and oracles.',
        '0x Protocol':'Medium: 0x uses standard DEX APIs. Low cost for swaps; no KYC or compliance. High cost for regulated asset integration.',
        'CME GCUL':'Low: GCUL uses Google Cloud and CME clearing. Low cost for members; leverages existing futures infrastructure. High efficiency; minimal new tech.',
        'Realio Network':'Medium: Realio uses Cosmos and EVM; moderate cost for multi-chain RWAs. Low for real estate; requires SPV and KYC.',
        'Augur':'Medium: Augur uses Ethereum; low cost for prediction markets. No TradFi integration; high cost for oracles and resolution.',
        'Openverse Global Layer0':'Medium: Layer0 uses ZK bridges; moderate cost for cross-chain. Low for interoperability; high for full RWA compliance.',
        'idOS Network':'Medium: idOS uses decentralized identity; moderate cost for integration. Low for user control; high for TradFi KYC mapping.',
        'Rayls Labs':'Medium: Rayls uses dual-layer for banks; moderate cost for private chains. Low for confidentiality; high for global scale.',
        'TSE/JPX Digital Securities':'Medium: TSE uses existing exchange systems. Moderate cost for token layer; leverages current members. Low trading cost.',
        'Novastro':'Medium: Novastro uses L3 and AI; moderate cost for optimization. Low for yield; high for SPV and compliance.',
        'B3 Digitas/ACXRWA':'Medium: B3 uses digital twins; moderate cost for Brazil market. Low for local assets; high for cross-border.',
        'LME Modernization':'Medium: LME uses exchange warrants; moderate cost for tokenization. Low for delivery; high for global reach.',
        'Kalshi':'Medium: Kalshi uses CFTC framework; moderate cost for event contracts. Low for U.S.; high for international.',
        'Polymarket':'Medium: Polymarket uses Polygon; low cost for predictions. No TradFi integration; high cost for resolution.',
        'Crypto.com':'Medium: Crypto.com uses APIs and custody. Moderate cost for KYC; low for retail. High for institutional RWA.',
        'RobinHood':'Medium: Robinhood uses broker-dealer rails. Moderate cost for crypto; high for tokenized securities.',
        'PredictIt':'Medium: PredictIt uses CFTC cap; moderate cost for platform. No blockchain; high for scale.',
        'SHFE Initiatives':'Medium: SHFE uses exchange systems. Moderate cost for tokenization; low for members. High for global integration.'
    },
    'Decentralization Risk Management': {
        'Abaxx (ID++/FDT)':'Medium: Abaxx uses permissioned P2P workflows with cryptographic decentralization (ID++), but clearing and legal finality rely on regulated entities. Reduces single-point failure via encrypted mesh, but governance is consortium-led. Mitigates risks through MLETR compliance and audit trails; not fully trustless, yet avoids centralization vulnerabilities.',
        'Securitize NYSE (via ICE)':'Medium: Securitize operates on public chains but integrates with centralized ICE/NYSE custody and DTC. Decentralized token standards (ERC-1400), but settlement finality depends on regulated intermediaries. Risk managed via compliance and redundancy; not resilient to TradFi outages.',
        'Chainlink CCIP':'High: CCIP uses decentralized oracle networks and multi-chain validation to eliminate single points of failure. Risk management committees and rate limits prevent manipulation. Fully trust-minimized cross-chain messaging; ideal for resilient RWA bridging without central control.',
        'BlackRock BUIDL':'Medium: BUIDL runs on Ethereum with decentralized mint/burn, but custody and KYC are centralized (BNY Mellon). Smart contract risks mitigated via audits; governance by BlackRock. Balances DeFi access with TradFi risk controls; not fully decentralized.',
        'JPMorgan Onyx':'Medium: Onyx is permissioned Quorum with known validators (banks). No public participation; decentralization limited to consortium. Risk managed via SLA and redundancy; resilient within network, but vulnerable to member coordination failures.',
        'Polkadot':'High: Polkadot uses NPoS with 1000+ validators and relay chain finality. Parachain sovereignty prevents single-chain failure. Governance on-chain and forkless upgrades; highly resilient to censorship and attacks.',
        'Corda':'Medium: Corda is permissioned with notary clusters for finality. Decentralization limited to consortium members. Risk managed via legal agreements and redundancy; no public attack surface, but not trustless.',
        'Polymesh':'Medium: Polymesh uses PoS with governance by token holders and node operators. Identity-bound; prevents Sybil attacks. Decentralized within regulated scope; resilient to spam, but validator set is curated.',
        'Lightning Network':'High: Lightning is fully decentralized with thousands of nodes and onion routing. No central coordinator; resistant to censorship. Risks (channel griefing, liquidity) managed via watchtowers and routing fees; trustless for payments.',
        'Coinbase':'High: Coinbase is fully centralized; single point of failure. Risk managed via insurance, audits, and compliance. No decentralization benefits; vulnerable to hacks, seizures, or operational downtime.',
        'COTI V2':'High: COTI V2 uses DAG with cluster-based consensus; no miners. Decentralized validation and garbled circuits prevent central control. Risk of cluster collusion low; resilient and scalable for confidential transactions.',
        'Ondo Finance':'High: Ondo uses public Ethereum and L2s; fully decentralized smart contracts. Risks (oracle, liquidation) managed via over-collateralization and governance. No central admin key; trustless yield for RWAs.',
        'Centrifuge':'High: Centrifuge runs on public chains (Ethereum, Centrifuge Chain) with open participation. Tinlake pools are permissionless post-onboarding. SPV legal risk isolated; on-chain logic fully decentralized and auditable.',
        'SWIFT Blockchain':'Medium: SWIFT trials use permissioned DLT with bank nodes. Decentralized among members; no public access. Risk managed via existing governance; resilient within consortium, but not globally decentralized.',
        'Solana':'High: Solana uses PoH and 2000+ validators; highly decentralized. Risks (outages) due to high throughput design, but recovery via coordination. No central control; resistant to censorship.',
        'Ethereum':'High: Ethereum has 1M+ validators post-Merge; maximally decentralized. Risks (MEV, congestion) managed via L2s and protocol upgrades. Gold standard for trustless RWA settlement.',
        'WisdomTree tokenization initiatives':'Medium: WisdomTree uses public chains but custody and issuance centralized. Smart contracts decentralized; off-chain processes not. Risk managed via regulation; partial resilience.',
        'Franklin Templeton BENJI':'Medium: BENJI on public chains; mint/burn logic decentralized. Fund operations and KYC centralized. Risk isolated to on-chain components; not fully trustless.',
        'DTCC Collateral Pilot':'Medium: DTCC AppChain is permissioned with member nodes. Decentralized within pilot; no public access. Risk managed via existing clearing; resilient but not open.',
        'Ripple':'High: Ripple ledger has 150+ validators; no central control. UNL reduces collusion risk. Resistant to censorship; ideal for cross-border without intermediaries.',
        'Deutsche Boerse Seturion':'Medium: Seturion uses permissioned chain with CSD nodes. Decentralized among members; risk managed via regulation. Not public; resilient within EU framework.',
        'ICE Digital Assets':'Medium: ICE platform centralized with exchange oversight. Blockchain layer may be permissioned. Risk managed via regulation; no decentralization benefits.',
        'Circle':'Medium: Circle controls USDC mint/burn and blacklisting. Chain-level decentralized; issuer centralized. Risk of freeze or seizure; not trustless.',
        'Tether':'Medium: Tether controls mint/burn and reserves. On-chain transparent; issuer centralized. High freeze risk; not resilient to regulatory action.',
        'Visa tokenization initiatives':'Medium: VTAP relies on bank-issued tokens; decentralized on-chain, controlled off-chain. Risk managed via banking regulation; not trustless.',
        'Hyperliquid':'High: Hyperliquid L1 is public with open validation. No central admin; fully decentralized order book. Risk of front-running managed via batching; trustless trading.',
        'Bakkt':'Medium: Bakkt is centralized exchange and custody. No decentralization; risk managed via insurance and CFTC oversight. Vulnerable to single-point failure.',
        'OpenEden':'Medium: OpenEden uses public chains; vaults decentralized. Treasury backing and KYC centralized. On-chain risk low; off-chain risk high.',
        'Nasdaq Tokenized Securities':'Medium: Nasdaq proposes public chain use; settlement via DTC (centralized). Token layer decentralized; clearing not. Risk managed via regulation.',
        'Provenance Foundation':'Medium: Provenance Chain is public; governance via Hash token. Decentralized validation; SPVs introduce legal centralization. Balanced risk profile.',
        'LSE DMI':'Medium: DMI uses Azure (centralized) with possible public chain. Fund operations centralized; token logic may be open. Risk managed via custody.',
        'MakerDAO/FRAX':'High: Maker is fully decentralized with MKR governance. No admin keys; liquidations automated. Oracle and collateral risks managed via community; trustless stability.',
        '0x Protocol':'High: 0x is open protocol on Ethereum; no central operator. Relayers decentralized; matches peer-to-peer. No censorship; fully resilient.',
        'CME GCUL':'Medium: GCUL uses Google Cloud (centralized) with possible permissioned chain. CME controls access; risk managed via clearing. Not decentralized.',
        'Realio Network':'High: Realio is multi-chain (Cosmos, Ethereum); public validation. No central control; SPVs for legal structure. On-chain fully decentralized.',
        'Augur':'High: Augur is fully decentralized on Ethereum. REP staking and outcome reporting distributed. No central resolution; trustless prediction markets.',
        'Openverse Global Layer0':'Medium: Layer0 uses ZK proofs and public validation. Decentralized bridging; risk of hub collusion low. Early stage; resilience building.',
        'idOS Network':'Medium: idOS is decentralized identity on public chains. No central issuer; risk of key loss. Resilient to censorship; user-controlled.',
        'Rayls Labs':'Medium: Rayls uses dual-layer with private and public components. Banks control private layer; public layer open. Risk isolated; not fully trustless.',
        'TSE/JPX Digital Securities':'Medium: TSE uses exchange-controlled systems. Possible permissioned chain; no public decentralization. Risk managed via regulation.',
        'Novastro':'Medium: Novastro uses L3 on EVM/Aptos; public but SPV-controlled. On-chain decentralized; legal layer centralized. Balanced risk.',
        'B3 Digitas/ACXRWA':'Medium: B3 uses exchange infrastructure; possible permissioned DLT. Decentralization limited to members. Risk managed via Brazilian regulation.',
        'LME Modernization':'Medium: LME uses exchange warrants; possible blockchain layer permissioned. No public decentralization; risk via membership control.',
        'Kalshi':'Medium: Kalshi is centralized platform under CFTC. No blockchain decentralization; risk managed via compliance and caps.',
        'Polymarket':'Medium: Polymarket uses Polygon; smart contracts decentralized. Outcome reporting via UMA; some centralization risk in resolution.',
        'Crypto.com':'High: Crypto.com is centralized exchange. Single point of failure; risk managed via insurance. No decentralization benefits.',
        'RobinHood':'High: Robinhood is centralized broker. Full control over assets; risk of outages or freezes. No blockchain decentralization.',
        'PredictIt':'High: PredictIt is centralized academic platform. CFTC-capped; full admin control. No decentralization; high operational risk.',
        'SHFE Initiatives':'Medium: SHFE uses exchange systems; possible permissioned blockchain. Decentralization limited to members. Risk managed via state oversight.'
    },
    'Seamless Onboarding of Large RWA Traders': {
        'Abaxx (ID++/FDT)':'High: Abaxx streamlines onboarding via ID++ digital identity and FDT legal templates, reducing KYC from weeks to minutes. Integrates with existing exchange accounts; no new wallets or custody. Pilots show 90% faster onboarding for commodity traders; supports high-volume institutional flows with full compliance.',
        'Securitize NYSE (via ICE)':'High: Securitize uses broker-dealer networks and DTC for instant onboarding. KYC/AML pre-verified via existing accounts. Tokenized securities mirror traditional shares; no retraining needed. Ideal for large traders already in NYSE ecosystem.',
        'Chainlink CCIP':'High: CCIP enables plug-and-play cross-chain access; no new onboarding. Uses existing wallets and oracles. Large traders integrate via APIs; supports institutional-grade RWAs with minimal friction.',
        'BlackRock BUIDL':'High: BUIDL leverages BlackRock’s investor base; onboarding via existing fund accounts. KYC pre-cleared; instant access to tokenized treasuries. Seamless for institutions already in traditional funds.',
        'JPMorgan Onyx':'High: Onyx uses JPM client relationships; onboarding via existing banking KYC. No new systems; instant access to tokenized deposits. Perfect for large corporate treasuries and banks.',
        'Polkadot':'High: Polkadot supports identity pallets; onboarding via existing wallets. Large traders use parachain dApps; no new custody. Scalable for institutional volumes.',
        'Corda':'High: Corda uses enterprise identity; onboarding via consortium membership. No public key management; instant for existing bank clients. Strong for private RWAs.',
        'Polymesh':'High: Polymesh requires on-chain KYC; streamlined via identity providers. Large traders onboard once; reusable across assets. Designed for institutional securities.',
        'Lightning Network':'Medium: Lightning requires channel setup; onboarding via Bitcoin wallets. Large traders need liquidity providers; suitable for payments, not complex RWAs.',
        'Coinbase':'Medium: Coinbase offers fast KYC; onboarding via app. Large traders face custodial limits; not self-custody. Retail-focused; medium for institutions.',
        'COTI V2':'Medium: COTI V2 uses wallet-based onboarding; no KYC. Large traders integrate via APIs; medium friction for confidential payments, not regulated assets.',
        'Ondo Finance':'Medium: Ondo requires KYC via partners; onboarding via USDC. Large traders access vaults; medium setup for yield products, not full custody.',
        'Centrifuge':'Medium: Centrifuge requires SPV and KYC; onboarding via legal process. Large traders face setup time; strong post-onboarding for private credit.',
        'SWIFT Blockchain':'High: SWIFT uses existing member banks; onboarding instant via ISO 20022. Large traders access via current accounts; no new systems.',
        'Solana':'Medium: Solana uses wallet onboarding; no KYC. Large traders integrate via RPC; high throughput but compliance friction.',
        'Ethereum':'Medium: Ethereum uses wallet and ENS; onboarding via dApps. Large traders face gas and KYC via partners; medium for DeFi RWAs.',
        'WisdomTree tokenization initiatives':'High: WisdomTree uses existing fund investors; onboarding via current accounts. No new KYC; instant access to tokenized products.',
        'Franklin Templeton BENJI':'High: BENJI leverages fund clients; onboarding via existing KYC. Instant access to MMF tokens; seamless for institutions.',
        'DTCC Collateral Pilot':'High: DTCC uses member firms; onboarding via existing clearing. No new systems; instant for repo and collateral traders.',
        'Ripple':'Medium: Ripple uses bank partnerships; onboarding via existing corridors. Large traders access via ILP; medium for payments, not full RWAs.',
        'Deutsche Boerse Seturion':'High: Seturion uses CSD members; onboarding instant. Large traders access via existing accounts; seamless in EU.',
        'ICE Digital Assets':'High: ICE uses exchange members; onboarding via current accounts. Instant for commodity traders; no new systems.',
        'Circle':'Medium: Circle uses wallet KYC; onboarding via app. Large traders access USDC; medium for stablecoins, not complex RWAs.',
        'Tether':'Medium: Tether uses exchange KYC; onboarding via platforms. Large traders access USDT; medium for transfers, not institutional RWAs.',
        'Visa tokenization initiatives':'High: VTAP uses bank clients; onboarding instant. Large traders access via existing accounts; seamless for tokenized deposits.',
        'Hyperliquid':'Medium: Hyperliquid uses wallet; no KYC. Large traders access perps; medium for derivatives, not regulated RWAs.',
        'Bakkt':'High: Bakkt uses ICE members; onboarding via existing accounts. Instant for futures traders; seamless integration.',
        'OpenEden':'Medium: OpenEden uses KYC partners; onboarding via USDC. Large traders access treasuries; medium setup time.',
        'Nasdaq Tokenized Securities':'High: Nasdaq uses broker networks; onboarding via DTC. Large traders access instantly; seamless for securities.',
        'Provenance Foundation':'Medium: Provenance uses KYC and SPV; onboarding via legal process. Large lenders face setup; strong post-onboarding.',
        'LSE DMI':'High: DMI uses fund investors; onboarding via existing accounts. Instant access to tokenized funds; seamless.',
        'MakerDAO/FRAX':'Medium: Maker uses wallet; no KYC. Large traders access vaults; medium for stablecoins, not regulated RWAs.',
        '0x Protocol':'Medium: 0x uses wallet; no KYC. Large traders integrate via API; medium for DEX liquidity.',
        'CME GCUL':'High: GCUL uses CME members; onboarding instant. Large traders access via existing clearing; seamless.',
        'Realio Network':'Medium: Realio uses KYC dApps; onboarding via SPV. Large real estate investors face setup; medium friction.',
        'Augur':'Medium: Augur uses wallet; no KYC. Large bettors access markets; medium for predictions, not RWAs.',
        'Openverse Global Layer0':'Medium: Layer0 uses wallet; onboarding via bridge. Large traders access cross-chain; medium setup.',
        'idOS Network':'Medium: idOS uses DID; onboarding via identity. Large users control data; medium for compliance mapping.',
        'Rayls Labs':'High: Rayls uses bank KYC; onboarding instant. Large institutions access private layer; seamless.',
        'TSE/JPX Digital Securities':'High: TSE uses exchange members; onboarding via accounts. Instant for stock traders; seamless.',
        'Novastro':'Medium: Novastro uses SPV; onboarding via legal. Large investors face setup; medium for AI-optimized RWAs.',
        'B3 Digitas/ACXRWA':'High: B3 uses member firms; onboarding instant. Large Brazilian traders access seamlessly.',
        'LME Modernization':'High: LME uses exchange members; onboarding via accounts. Instant for metal traders; seamless.',
        'Kalshi':'Medium: Kalshi uses CFTC KYC; onboarding via app. Large event bettors access; medium for U.S. only.',
        'Polymarket':'Medium: Polymarket uses wallet; no KYC. Large bettors access via USDC; medium for global predictions.',
        'Crypto.com':'Medium: Crypto.com uses app KYC; onboarding fast. Large traders access custodial; medium for retail RWAs.',
        'RobinHood':'Medium: Robinhood uses broker KYC; onboarding via app. Large traders access custodial; medium for securities.',
        'PredictIt':'Medium: PredictIt uses CFTC cap; onboarding via platform. Large bettors limited; medium for U.S. predictions.',
        'SHFE Initiatives':'High: SHFE uses exchange members; onboarding instant. Large commodity traders access seamlessly.'
    },
    'Liquidity Fragmentation Risks': {
        'Abaxx (ID++/FDT)':'Low: Abaxx unifies liquidity via Adaptive Clearing and FDT, preventing fragmentation across venues. Cross-border RWAs trade in single pool; legal finality ensures trust. Reduces search costs and slippage; ideal for institutional commodity flows.',
        'Securitize NYSE (via ICE)':'Low: Securitize pools liquidity on NYSE with DTC settlement. Tokenized securities trade alongside traditional shares; no fragmentation. Institutional depth ensures tight spreads; seamless for large orders.',
        'Chainlink CCIP':'Low: CCIP aggregates liquidity across chains via standardized messaging. Prevents silos; enables atomic cross-chain trades. Reduces fragmentation risk; strong for multi-chain RWAs.',
        'BlackRock BUIDL':'Low: BUIDL accesses BlackRock’s $10T+ treasury market. Liquidity unified via fund structure; no chain fragmentation. Institutional inflows ensure depth; minimal slippage.',
        'JPMorgan Onyx':'Low: Onyx pools liquidity within permissioned network. No public chain fragmentation; bank-grade depth. Reduces search costs; strong for tokenized deposits.',
        'Polkadot':'Low: Polkadot aggregates liquidity via XCM and parachains. Prevents chain silos; unified order books possible. Reduces fragmentation; ideal for multi-asset RWAs.',
        'Corda':'Low: Corda pools liquidity within consortiums. Bilateral trades prevent public fragmentation. Strong for private RWAs; no venue competition.',
        'Polymesh':'Low: Polymesh unifies regulated securities liquidity. On-chain compliance prevents silos. Growing but focused depth; low fragmentation risk.',
        'Lightning Network':'Medium: Lightning fragments liquidity across channels. Routing reduces but doesn’t eliminate search costs. Strong for payments; medium for complex RWAs.',
        'Coinbase':'Medium: Coinbase centralizes liquidity but isolates from DeFi pools. No chain fragmentation; retail depth only. Medium for institutional RWAs.',
        'COTI V2':'Medium: COTI V2 pools liquidity on DAG L2. Cross-chain via MultiDAG; medium fragmentation. Strong for payments; medium for RWAs.',
        'Ondo Finance':'Medium: Ondo pools liquidity in vaults; USDC-based. No chain silos; medium depth for treasuries. Growing institutional inflows.',
        'Centrifuge':'Medium: Centrifuge pools liquidity in Tinlake; Cosmos-based. No EVM fragmentation; medium depth for private credit. Strong niche liquidity.',
        'SWIFT Blockchain':'Low: SWIFT unifies liquidity across 11,000+ banks. No fragmentation; global depth. Reduces FX and search costs; ideal for cross-border.',
        'Solana':'Medium: Solana pools liquidity on single chain. No cross-chain fragmentation; high throughput. Validator centralization risk; medium for RWAs.',
        'Ethereum':'Medium: Ethereum fragments liquidity across L2s. Bridges reduce but don’t eliminate silos. High total depth; medium fragmentation risk.',
        'WisdomTree tokenization initiatives':'Low: WisdomTree pools liquidity in fund structure. No chain fragmentation; traditional depth. Strong for tokenized funds.',
        'Franklin Templeton BENJI':'Low: BENJI unifies MMF liquidity. No fragmentation; fund-based depth. Strong for yield products.',
        'DTCC Collateral Pilot':'Low: DTCC pools collateral liquidity. No fragmentation; repo depth. Strong for institutional finance.',
        'Ripple':'Low: Ripple pools liquidity via ODL and stablecoins. No fragmentation across corridors. Strong for cross-border payments.',
        'Deutsche Boerse Seturion':'Low: Seturion unifies EU liquidity. No fragmentation; CSD depth. Strong for securities.',
        'ICE Digital Assets':'Low: ICE pools commodity liquidity. No fragmentation; exchange depth. Strong for futures.',
        'Circle':'Medium: Circle pools USDC liquidity. No chain silos; medium depth for stablecoins. Growing but not RWA-specific.',
        'Tether':'Medium: Tether pools USDT liquidity. No fragmentation; high depth. Reserve risk; medium for RWAs.',
        'Visa tokenization initiatives':'Low: VTAP pools bank liquidity. No fragmentation; global depth. Strong for tokenized deposits.',
        'Hyperliquid':'Medium: Hyperliquid pools perp liquidity on L1. No fragmentation; high throughput. No KYC; medium for derivatives.',
        'Bakkt':'Low: Bakkt pools futures liquidity. No fragmentation; regulated depth. Strong for crypto.',
        'OpenEden':'Medium: OpenEden pools treasury liquidity. USDC-based; medium depth. Growing institutional access.',
        'Nasdaq Tokenized Securities':'Low: Nasdaq pools share liquidity. No fragmentation; DTC depth. Strong for securities.',
        'Provenance Foundation':'Medium: Provenance pools loan liquidity. Cosmos-based; medium depth. Strong for credit.',
        'LSE DMI':'Low: DMI pools fund liquidity. No fragmentation; traditional depth. Strong for funds.',
        'MakerDAO/FRAX':'Medium: Maker pools DAI liquidity. Ethereum-based; medium depth. Strong for stablecoins.',
        '0x Protocol':'Medium: 0x aggregates DEX liquidity. Reduces fragmentation; medium depth. Strong for swaps.',
        'CME GCUL':'Low: GCUL pools futures liquidity. No fragmentation; CME depth. Strong for programmable assets.',
        'Realio Network':'Medium: Realio pools real estate liquidity. Multi-chain; medium depth. Growing ecosystem.',
        'Augur':'Medium: Augur pools prediction liquidity. Ethereum-based; medium depth. Niche market focus.',
        'Openverse Global Layer0':'Low: Layer0 aggregates cross-chain liquidity. Prevents silos; low fragmentation. Early stage.',
        'idOS Network':'Medium: idOS enables identity-linked liquidity. No direct pooling; medium impact.',
        'Rayls Labs':'Low: Rayls pools bank liquidity. Private layer; low fragmentation. Strong for institutions.',
        'TSE/JPX Digital Securities':'Low: TSE pools stock liquidity. No fragmentation; exchange depth. Strong for securities.',
        'Novastro':'Medium: Novastro pools AI-optimized liquidity. L3-based; medium depth. Growing yield focus.',
        'B3 Digitas/ACXRWA':'Low: B3 pools Brazilian liquidity. No fragmentation; local depth. Strong for region.',
        'LME Modernization':'Low: LME pools metal liquidity. No fragmentation; exchange depth. Strong for commodities.',
        'Kalshi':'Medium: Kalshi pools event liquidity. CFTC-regulated; medium depth. U.S.-focused.',
        'Polymarket':'Medium: Polymarket pools prediction liquidity. Polygon-based; medium depth. Global but niche.',
        'Crypto.com':'Medium: Crypto.com pools retail liquidity. Custodial; medium depth. Not institutional-grade.',
        'RobinHood':'Medium: Robinhood pools broker liquidity. Custodial; medium depth. Retail-focused.',
        'PredictIt':'Medium: PredictIt caps liquidity. CFTC-limited; medium depth. Academic focus.',
        'SHFE Initiatives':'Low: SHFE pools commodity liquidity. No fragmentation; exchange depth. Strong for China.'
    },
    'Hacking/Manipulation Risks': {
        'Abaxx (ID++/FDT)':'Low: Abaxx uses 5-layer cryptography, ZK proofs, and P2P encryption to prevent reverse-engineering. FDT ensures legal finality; no central hack surface. Auditable workflows reduce manipulation; ideal for institutional RWAs.',
        'Securitize NYSE (via ICE)':'Low: Securitize uses regulated custody and atomic swaps. ICE infrastructure prevents manipulation; SEC oversight. Smart contract audits; low risk for tokenized securities.',
        'Chainlink CCIP':'Low: CCIP uses decentralized oracles and risk committees. Manipulation prevented via aggregation; ZK proofs. No single point of failure; low risk for cross-chain.',
        'BlackRock BUIDL':'Low: BUIDL uses audited smart contracts and institutional custody. Manipulation prevented via fund rules; low risk for treasuries.',
        'JPMorgan Onyx':'Low: Onyx uses FHE and permissioned access. Bank-grade security; no public attack surface. Low manipulation risk; strong for private assets.',
        'Polkadot':'Low: Polkadot uses NPoS and relay chain security. Manipulation prevented via slashing; low risk for parachains.',
        'Corda':'Low: Corda uses private flows and notaries. No public attack; manipulation prevented via legal agreements. Low risk for enterprise.',
        'Polymesh':'Low: Polymesh uses identity-bound tokens and governance. Manipulation prevented via compliance; low risk for securities.',
        'Lightning Network':'Low: Lightning uses onion routing and watchtowers. Manipulation risk low; channel griefing mitigated. Strong for payments.',
        'Coinbase':'Medium: Coinbase has insurance and audits. Centralized; hack risk exists (e.g., phishing). Medium for custodial RWAs.',
        'COTI V2':'Low: COTI V2 uses garbled circuits and DAG. Manipulation prevented via clusters; low risk for confidential transactions.',
        'Ondo Finance':'Medium: Ondo uses over-collateralization and oracles. Manipulation risk via price feeds; mitigated via governance. Medium for yield RWAs.',
        'Centrifuge':'Medium: Centrifuge uses SPVs and oracles. Manipulation risk in legal layer; on-chain low. Medium for private credit.',
        'SWIFT Blockchain':'Low: SWIFT uses permissioned DLT and bank security. No public attack; low manipulation risk.',
        'Solana':'Medium: Solana has high throughput; outage risk. Manipulation via validators; medium risk despite security.',
        'Ethereum':'Medium: Ethereum has MEV and congestion risk. Manipulation via flash loans; mitigated via L2s. Medium for base layer.',
        'WisdomTree tokenization initiatives':'Low: WisdomTree uses regulated custody. Manipulation prevented via fund rules; low risk.',
        'Franklin Templeton BENJI':'Low: BENJI uses fund security. Manipulation prevented via NAV; low risk for MMFs.',
        'DTCC Collateral Pilot':'Low: DTCC uses member security. Manipulation prevented via clearing; low risk for repo.',
        'Ripple':'Medium: Ripple has UNL risk. Manipulation via validator collusion; medium but low probability.',
        'Deutsche Boerse Seturion':'Low: Seturion uses CSD security. Manipulation prevented via regulation; low risk.',
        'ICE Digital Assets':'Low: ICE uses exchange security. Manipulation prevented via oversight; low risk.',
        'Circle':'Medium: Circle has blacklist risk. Manipulation via issuer; medium for stablecoins.',
        'Tether':'Medium: Tether has reserve and freeze risk. Manipulation via issuer; medium for USDT.',
        'Visa tokenization initiatives':'Low: VTAP uses bank security. Manipulation prevented via regulation; low risk.',
        'Hyperliquid':'Medium: Hyperliquid has front-running risk. Manipulation via batching; medium for perps.',
        'Bakkt':'Low: Bakkt uses CFTC security. Manipulation prevented via regulation; low risk.',
        'OpenEden':'Medium: OpenEden has oracle risk. Manipulation via price feeds; medium for treasuries.',
        'Nasdaq Tokenized Securities':'Low: Nasdaq uses DTC security. Manipulation prevented via clearing; low risk.',
        'Provenance Foundation':'Medium: Provenance has SPV risk. Manipulation via legal layer; medium for loans.',
        'LSE DMI':'Low: DMI uses fund security. Manipulation prevented via custody; low risk.',
        'MakerDAO/FRAX':'Medium: Maker has oracle and liquidation risk. Manipulation via flash loans; medium for stablecoins.',
        '0x Protocol':'Medium: 0x has slippage risk. Manipulation via relayers; medium for DEX.',
        'CME GCUL':'Low: GCUL uses CME security. Manipulation prevented via clearing; low risk.',
        'Realio Network':'Medium: Realio has SPV risk. Manipulation via legal structure; medium for real estate.',
        'Augur':'Medium: Augur has oracle risk. Manipulation via reporting; medium for predictions.',
        'Openverse Global Layer0':'Medium: Layer0 has bridge risk. Manipulation via ZK proofs; medium early stage.',
        'idOS Network':'Low: idOS uses decentralized identity. Manipulation prevented via encryption; low risk.',
        'Rayls Labs':'Low: Rayls uses bank-grade security. Manipulation prevented via private layer; low risk.',
        'TSE/JPX Digital Securities':'Low: TSE uses exchange security. Manipulation prevented via oversight; low risk.',
        'Novastro':'Medium: Novastro has AI model risk. Manipulation via optimization; medium for yield.',
        'B3 Digitas/ACXRWA':'Low: B3 uses exchange security. Manipulation prevented via regulation; low risk.',
        'LME Modernization':'Low: LME uses exchange security. Manipulation prevented via delivery; low risk.',
        'Kalshi':'Low: Kalshi uses CFTC security. Manipulation prevented via caps; low risk.',
        'Polymarket':'Medium: Polymarket has UMA resolution risk. Manipulation via voting; medium for predictions.',
        'Crypto.com':'Medium: Crypto.com has custodial risk. Manipulation via exchange; medium for retail.',
        'RobinHood':'Medium: Robinhood has broker risk. Manipulation via platform; medium for securities.',
        'PredictIt':'Low: PredictIt uses CFTC caps. Manipulation prevented via limits; low risk.',
        'SHFE Initiatives':'Low: SHFE uses exchange security. Manipulation prevented via state oversight; low risk.'
    },
    'Regulatory Adaptability': {
        'Abaxx (ID++/FDT)':'High: Abaxx aligns with MLETR, CFTC, and IOSCO. FDT ensures legal finality; ID++ supports KYC/AML. Pilots with regulators; adaptable to new rules. Ideal for global RWA compliance.',
        'Securitize NYSE (via ICE)':'High: Securitize is SEC-registered; tokens comply with Reg D, S, and ATS. NYSE integration ensures adaptability. Strong for U.S. securities; global via brokers.',
        'Chainlink CCIP':'High: CCIP supports compliance via oracles and risk frameworks. Adaptable to FATF, MiCA. No direct regulation; enables compliant bridges.',
        'BlackRock BUIDL':'High: BUIDL is SEC-registered fund. Complies with 40 Act; adaptable to new rules. Strong for institutional treasuries.',
        'JPMorgan Onyx':'High: Onyx complies with OCC, Fed, and global banking rules. Pilots with MAS, BoJ. Adaptable to CBDC and token standards.',
        'Polkadot':'High: Polkadot supports compliance via parachains. Identity and governance adaptable. Strong for regulated assets; global reach.',
        'Corda':'High: Corda complies with GDPR, CCPA, and banking rules. Legal prose in contracts; adaptable to jurisdiction. Strong for enterprise.',
        'Polymesh':'High: Polymesh designed for securities law. On-chain KYC/AML; adaptable to MiCA, SEC. Ideal for regulated tokens.',
        'Lightning Network':'Medium: Lightning lacks native compliance. Adaptable via dApps; medium for regulated RWAs. Strong for payments.',
        'Coinbase':'High: Coinbase is BitLicense, MSB, and SEC-registered. Complies with global KYC/AML. Adaptable but custodial.',
        'COTI V2':'Medium: COTI V2 supports compliance via selective disclosure. No direct regulation; medium adaptability for DeFi.',
        'Ondo Finance':'High: Ondo complies with SEC via fund structure. KYC/AML via partners; adaptable to new rules.',
        'Centrifuge':'High: Centrifuge uses SPVs for compliance. Adaptable to local laws; strong for private credit.',
        'SWIFT Blockchain':'High: SWIFT complies with ISO, FATF, and G20. Global standards; adaptable to CBDC and tokenization.',
        'Solana':'Medium: Solana supports compliance via dApps. No native KYC; medium adaptability for regulated RWAs.',
        'Ethereum':'Medium: Ethereum supports compliance via L2s and dApps. No native regulation; medium for securities.',
        'WisdomTree tokenization initiatives':'High: WisdomTree is SEC-registered. Complies with 40 Act; adaptable to new fund rules.',
        'Franklin Templeton BENJI':'High: BENJI is registered MMF. Complies with 2a-7; adaptable to yield rules.',
        'DTCC Collateral Pilot':'High: DTCC complies with Fed, SEC. Adaptable to new clearing rules; strong for repo.',
        'Ripple':'High: Ripple complies with FinCEN, MAS. ODL licensed; adaptable to CBDC and stablecoins.',
        'Deutsche Boerse Seturion':'High: Seturion complies with MiCA, CSDR. EU-focused; adaptable to digital assets.',
        'ICE Digital Assets':'High: ICE complies with CFTC, SEC. Adaptable to crypto and token rules.',
        'Circle':'High: Circle is MSB, BitLicense. USDC complies with NYDFS; adaptable to stablecoin rules.',
        'Tether':'High: Tether complies with global AML. Reserves audited; adaptable but controversial.',
        'Visa tokenization initiatives':'High: Visa complies with PCI, GDPR. VTAP adaptable to CBDC and token standards.',
        'Hyperliquid':'Medium: Hyperliquid lacks KYC. No regulation; medium adaptability for derivatives.',
        'Bakkt':'High: Bakkt is CFTC-registered. Complies with futures rules; adaptable to crypto.',
        'OpenEden':'High: OpenEden complies with fund rules. KYC/AML via partners; adaptable to yield products.',
        'Nasdaq Tokenized Securities':'High: Nasdaq complies with SEC, FINRA. Adaptable to digital share rules.',
        'Provenance Foundation':'High: Provenance uses SPVs for compliance. Adaptable to local credit laws.',
        'LSE DMI':'High: DMI complies with FCA, MiFID. Adaptable to UK token rules.',
        'MakerDAO/FRAX':'High: Maker adapts via governance. No direct regulation; strong for stablecoins.',
        '0x Protocol':'Medium: 0x lacks compliance. Adaptable via relayers; medium for regulated assets.',
        'CME GCUL':'High: GCUL complies with CFTC. Adaptable to programmable futures.',
        'Realio Network':'High: Realio uses SPVs for compliance. Adaptable to real estate laws.',
        'Augur':'Medium: Augur lacks regulation. Adaptable via dApps; medium for predictions.',
        'Openverse Global Layer0':'Medium: Layer0 supports compliance via bridges. Early stage; medium adaptability.',
        'idOS Network':'High: idOS supports KYC/AML via DID. Adaptable to identity rules.',
        'Rayls Labs':'High: Rayls complies with bank rules. Adaptable to private tokenization.',
        'TSE/JPX Digital Securities':'High: TSE complies with FSA. Adaptable to Japan token rules.',
        'Novastro':'High: Novastro uses SPVs for compliance. Adaptable to AI yield rules.',
        'B3 Digitas/ACXRWA':'High: B3 complies with CVM. Adaptable to Brazil digital assets.',
        'LME Modernization':'High: LME complies with FCA. Adaptable to metal token rules.',
        'Kalshi':'High: Kalshi is CFTC-registered. Adaptable to event contract rules.',
        'Polymarket':'Medium: Polymarket lacks full CFTC compliance. Adaptable via USDC; medium for predictions.',
        'Crypto.com':'High: Crypto.com is MSB, BitLicense. Adaptable to global crypto rules.',
        'RobinHood':'High: Robinhood is FINRA, SEC-registered. Adaptable to broker rules.',
        'PredictIt':'High: PredictIt is CFTC-approved. Adaptable to academic prediction rules.',
        'SHFE Initiatives':'High: SHFE complies with CSRC. Adaptable to China commodity token rules.'
        },
    'DeFi Transition Path': {
        'Abaxx (ID++/FDT)':'Medium: Abaxx supports DeFi via FDT and ID++ interoperability. Legal finality enables hybrid models. Medium path; strong for regulated DeFi RWAs with institutional compliance.',
        'Securitize NYSE (via ICE)':'Medium: Securitize enables DeFi via ERC-1400 standards and atomic swaps. NYSE integration limits full decentralization. Medium path; strong for regulated yield in DeFi pools.',
        'Chainlink CCIP':'High: CCIP is native to DeFi with cross-chain messaging and oracle feeds. Enables seamless RWA bridging to lending, DEXs. High path; ideal for full DeFi-TradFi fusion.',
        'BlackRock BUIDL':'Medium: BUIDL enables DeFi yield via OUSG on Ondo and other platforms. Fund structure restricts full control. Medium path; strong for institutional-grade DeFi exposure.',
        'JPMorgan Onyx':'Medium: Onyx enables DeFi via tokenized deposits in permissioned pools. Limited public access; medium path. Strong for bank-grade DeFi pilots and hybrid models.',
        'Polkadot':'High: Polkadot is native to DeFi with parachains for lending, DEXs, stablecoins. XCM enables full RWA integration. High path; ideal for scalable, multi-chain DeFi.',
        'Corda':'Medium: Corda supports private DeFi via CorDapps and bilateral flows. No public composability; medium path. Strong for enterprise-grade, compliant DeFi.',
        'Polymesh':'Medium: Polymesh enables regulated DeFi with on-chain KYC and compliance. Limited public liquidity; medium path. Strong for securities in DeFi protocols.',
        'Lightning Network':'High: Lightning is native to DeFi payments and micro-RWAs. Integrates with Bitcoin DeFi (DLCs, stables). High path; ideal for instant, low-cost DeFi settlement.',
        'Coinbase':'High: Coinbase enables DeFi via Base L2 and wallet. Custodial to self-custody path; high transition. Strong for retail onboarding to DeFi RWAs.',
        'COTI V2':'High: COTI V2 is native to DeFi with confidential payments and garbled circuits. Full composability; high path for privacy-preserving DeFi RWAs.',
        'Ondo Finance':'High: Ondo is native to DeFi with yield-bearing treasuries (OUSG). Full integration with lending, DEXs. High path; leader in tokenized treasury DeFi.',
        'Centrifuge':'High: Centrifuge is native to DeFi with Tinlake credit pools. Full integration with Aave, Maker. High path; pioneer in real-world credit DeFi.',
        'SWIFT Blockchain':'Medium: SWIFT enables hybrid DeFi via permissioned trials. Limited public access; medium path. Strong for bank-led DeFi pilots and CBDC integration.',
        'Solana':'High: Solana is native to DeFi with high-throughput DEXs, lending, perps. Full RWA support via dApps. High path; ideal for scalable DeFi RWAs.',
        'Ethereum':'High: Ethereum is the DeFi standard with L2s, DEXs, lending, stablecoins. Full RWA integration via ERC-3643, etc. High path; gold standard for DeFi transition.',
        'WisdomTree tokenization initiatives':'Medium: WisdomTree enables DeFi yield via tokenized funds. Fund structure limits composability. Medium path; strong for institutional DeFi exposure.',
        'Franklin Templeton BENJI':'Medium: BENJI enables DeFi yield via on-chain MMF shares. Limited control; medium path. Strong for stable yield in DeFi.',
        'DTCC Collateral Pilot':'Medium: DTCC enables repo DeFi via AppChain. Permissioned access; medium path. Strong for collateralized lending in DeFi.',
        'Ripple':'High: Ripple enables DeFi payments via XRP and stablecoins. ODL integrates with DEXs. High path; strong for cross-border DeFi liquidity.',
        'Deutsche Boerse Seturion':'Medium: Seturion enables EU-regulated DeFi via permissioned chains. Limited public access; medium path. Strong for compliant securities in DeFi.',
        'ICE Digital Assets':'Medium: ICE enables crypto DeFi via custody and futures. Limited RWA composability; medium path. Strong for regulated derivatives in DeFi.',
        'Circle':'High: Circle enables DeFi via USDC, the leading stablecoin. Full integration with DEXs, lending. High path; essential for DeFi liquidity.',
        'Tether':'High: Tether enables DeFi via USDT, dominant stablecoin. Full integration despite centralization. High path; critical for DeFi volume.',
        'Visa tokenization initiatives':'Medium: VTAP enables tokenized deposits in DeFi. Bank-issued; medium path. Strong for institutional stablecoins in DeFi.',
        'Hyperliquid':'High: Hyperliquid is native to DeFi perps with L1 DEX. Full composability; high path. Strong for synthetic RWAs in DeFi.',
        'Bakkt':'Medium: Bakkt enables crypto DeFi via custody and futures. Limited RWA access; medium path. Strong for regulated entry to DeFi.',
        'OpenEden':'High: OpenEden enables DeFi yield via tokenized treasuries. Full integration with DEXs. High path; strong for yield-bearing RWAs.',
        'Nasdaq Tokenized Securities':'Medium: Nasdaq proposes tokenized shares in DeFi. DTC settlement limits; medium path. Strong for regulated equities in DeFi.',
        'Provenance Foundation':'High: Provenance enables credit DeFi via Hash and loan pools. Full integration with Cosmos DeFi. High path; strong for real-world lending.',
        'LSE DMI':'Medium: DMI enables fund tokens in DeFi. Azure-based; medium path. Strong for institutional funds in DeFi.',
        'MakerDAO/FRAX':'High: Maker is core DeFi with DAI and vaults. Full RWA collateral support. High path; foundational for stablecoin DeFi.',
        '0x Protocol':'High: 0x is native to DeFi with atomic swaps and DEX aggregation. Full composability; high path for RWA trading.',
        'CME GCUL':'Medium: GCUL enables programmable futures in DeFi. CME clearing limits; medium path. Strong for regulated derivatives in DeFi.',
        'Realio Network':'High: Realio enables real estate DeFi multi-chain. Full integration with lending, DEXs. High path; strong for property RWAs.',
        'Augur':'High: Augur is native to DeFi prediction markets. Full integration with REP, USDC. High path; strong for event-based RWAs.',
        'Openverse Global Layer0':'High: Layer0 enables cross-chain DeFi with ZK bridges. Full RWA interoperability. High path; strong for unified DeFi liquidity.',
        'idOS Network':'Medium: idOS enables identity in DeFi. No direct yield; medium path. Strong for compliant user onboarding to DeFi.',
        'Rayls Labs':'Medium: Rayls enables bank-grade DeFi. Private layer limits; medium path. Strong for institutional private DeFi.',
        'TSE/JPX Digital Securities':'Medium: TSE enables stock tokens in DeFi. Exchange control limits; medium path. Strong for regulated equities.',
        'Novastro':'High: Novastro enables AI-optimized yield in DeFi. L3 integration; high path. Strong for automated RWA strategies.',
        'B3 Digitas/ACXRWA':'Medium: B3 enables Brazilian assets in DeFi. Local focus; medium path. Strong for regional RWA DeFi.',
        'LME Modernization':'Medium: LME enables metal warrants in DeFi. Exchange control; medium path. Strong for commodity-backed DeFi.',
        'Kalshi':'Medium: Kalshi enables event contracts in DeFi. CFTC limits; medium path. Strong for regulated prediction DeFi.',
        'Polymarket':'High: Polymarket is native to DeFi predictions on Polygon. Full USDC integration. High path; leader in decentralized betting.',
        'Crypto.com':'High: Crypto.com enables DeFi via wallet and DEX. Full access to lending, staking. High path; strong for retail DeFi.',
        'RobinHood':'Medium: Robinhood enables crypto DeFi via wallet. Broker limits; medium path. Strong for retail entry to DeFi.',
        'PredictIt':'Low: PredictIt has no DeFi integration. CFTC-capped; no blockchain. Low path; not designed for DeFi transition.',
        'SHFE Initiatives':'Medium: SHFE enables commodity tokens in DeFi. Exchange control; medium path. Strong for regulated commodity DeFi.'
    },
    'Scalability for High-Volume Institutional Trading': {
        'Abaxx (ID++/FDT)':'High: Abaxx supports 10k+ TPS via Adaptive Infrastructure. P2P mesh scales with traders; no blockchain bottleneck. Pilots handle institutional commodity volumes; ideal for high-frequency RWAs.',
        'Securitize NYSE (via ICE)':'High: Securitize leverages NYSE’s 100k+ TPS capacity. Atomic swaps scale with exchange; no chain limits. Strong for high-volume tokenized securities.',
        'Chainlink CCIP':'High: CCIP scales with underlying chains (Solana, Ethereum L2s). No central bottleneck; supports institutional cross-chain volume. High path for RWA throughput.',
        'BlackRock BUIDL':'High: BUIDL scales with fund operations; on-chain mint/burn via L2s. Handles billions in TVL; strong for institutional treasury volume.',
        'JPMorgan Onyx':'High: Onyx scales within permissioned network; bank-grade throughput. Handles trillions in deposits; strong for tokenized cash volume.',
        'Polkadot':'High: Polkadot scales to 1M+ TPS via parachains. XCM prevents congestion; strong for multi-asset institutional trading.',
        'Corda':'High: Corda scales bilaterally; no public chain limits. Enterprise-grade; strong for high-volume private RWAs.',
        'Polymesh':'Medium: Polymesh scales to 10k TPS; growing validator set. Strong for securities; medium for ultra-high volume.',
        'Lightning Network':'High: Lightning scales to millions TPS off-chain. Instant finality; strong for high-frequency micro-RWAs.',
        'Coinbase':'High: Coinbase handles 100k+ TPS centrally. Strong for retail; not decentralized scale.',
        'COTI V2':'High: COTI V2 scales to 100k+ TPS on DAG. No blocks; strong for confidential high-volume trading.',
        'Ondo Finance':'High: Ondo scales with Ethereum L2s and USDC. Handles billions in TVL; strong for treasury volume.',
        'Centrifuge':'Medium: Centrifuge scales with Cosmos and EVM; pool-based. Strong for credit; medium for ultra-high frequency.',
        'SWIFT Blockchain':'High: SWIFT handles 40M+ messages/day. DLT trials scale with banks; strong for global volume.',
        'Solana':'High: Solana achieves 65k TPS; parallel execution. Strong for high-frequency RWAs; validator scale limits.',
        'Ethereum':'High: Ethereum L2s achieve 100k+ TPS combined. Rollups scale; strong for institutional DeFi volume.',
        'WisdomTree tokenization initiatives':'High: WisdomTree scales with fund operations. On-chain via L2s; strong for fund volume.',
        'Franklin Templeton BENJI':'High: BENJI scales with MMF operations. On-chain yield; strong for stable volume.',
        'DTCC Collateral Pilot':'High: DTCC handles trillions in repo. AppChain scales with members; strong for collateral volume.',
        'Ripple':'High: Ripple handles 1,500 TPS; ODL scales globally. Strong for cross-border volume.',
        'Deutsche Boerse Seturion':'High: Seturion scales with EU CSDs. Strong for securities volume.',
        'ICE Digital Assets':'High: ICE handles exchange volume. Strong for commodity futures.',
        'Circle':'High: Circle scales with USDC on multiple chains. Strong for stablecoin volume.',
        'Tether':'High: Tether scales with USDT on multiple chains. Strong for volume despite centralization.',
        'Visa tokenization initiatives':'High: Visa handles 65k TPS. VTAP scales with banks; strong for deposit volume.',
        'Hyperliquid':'High: Hyperliquid achieves 100k+ TPS on L1. Strong for perps volume.',
        'Bakkt':'High: Bakkt scales with ICE. Strong for futures volume.',
        'OpenEden':'High: OpenEden scales with treasuries on Ethereum. Strong for yield volume.',
        'Nasdaq Tokenized Securities':'High: Nasdaq scales with DTC. Strong for share volume.',
        'Provenance Foundation':'Medium: Provenance scales with Cosmos. Strong for credit; medium for ultra-high volume.',
        'LSE DMI':'High: DMI scales with fund operations. Strong for fund volume.',
        'MakerDAO/FRAX':'High: Maker scales with Ethereum L2s. Strong for stablecoin volume.',
        '0x Protocol':'High: 0x scales with DEX aggregation. Strong for swap volume.',
        'CME GCUL':'High: CME scales with clearing. Strong for futures volume.',
        'Realio Network':'Medium: Realio scales multi-chain. Strong for real estate; medium for high frequency.',
        'Augur':'Medium: Augur scales with Ethereum. Niche volume; medium for predictions.',
        'Openverse Global Layer0':'High: Layer0 scales cross-chain. Strong for unified volume.',
        'idOS Network':'Medium: idOS scales identity. No direct trading volume.',
        'Rayls Labs':'High: Rayls scales with banks. Strong for private volume.',
        'TSE/JPX Digital Securities':'High: TSE scales with exchange. Strong for stock volume.',
        'Novastro':'High: Novastro scales with L3. Strong for AI-optimized volume.',
        'B3 Digitas/ACXRWA':'High: B3 scales with Brazil market. Strong for local volume.',
        'LME Modernization':'High: LME scales with exchange. Strong for metal volume.',
        'Kalshi':'Medium: Kalshi scales with events. CFTC limits; medium volume.',
        'Polymarket':'High: Polymarket scales with Polygon. Strong for prediction volume.',
        'Crypto.com':'High: Crypto.com scales centrally. Strong for retail volume.',
        'RobinHood':'High: Robinhood scales with broker. Strong for retail volume.',
        'PredictIt':'Low: PredictIt capped by CFTC. Low volume capacity.',
        'SHFE Initiatives':'High: SHFE scales with exchange. Strong for commodity volume.'
    },
    'Interoperability with Existing Financial Systems': {
        'Abaxx (ID++/FDT)':'High: Abaxx integrates with ICE, MineHub, and clearing houses via APIs. FDT aligns with MLETR; ID++ maps to existing KYC. Strong for commodity ecosystem interoperability.',
        'Securitize NYSE (via ICE)':'High: Securitize integrates with NYSE, DTC, and broker-dealers. ERC-1400 mirrors traditional shares. Strong for securities system interoperability.',
        'Chainlink CCIP':'High: CCIP connects 20+ chains with banking APIs. Oracle feeds integrate market data. Strong for cross-system RWA flow.',
        'BlackRock BUIDL':'High: BUIDL integrates with fund admin, custodians, and portals. On-chain via L2s; strong for treasury system interoperability.',
        'JPMorgan Onyx':'High: Onyx integrates with JPM core banking, treasury, and FX. Permissioned; strong for bank system interoperability.',
        'Polkadot':'High: Polkadot connects via bridges to Ethereum, Bitcoin, Cosmos. XCM enables asset transfer. Strong for multi-system RWA flow.',
        'Corda':'High: Corda integrates with enterprise ERP, CRM via CorDapps. Strong for private financial system interoperability.',
        'Polymesh':'High: Polymesh integrates with custodians, brokers via APIs. On-chain compliance; strong for securities systems.',
        'Lightning Network':'Medium: Lightning integrates with Bitcoin wallets. Limited RWA support; medium for payment system interoperability.',
        'Coinbase':'High: Coinbase integrates with banks, payment rails via APIs. Strong for retail financial system access.',
        'COTI V2':'High: COTI V2 integrates with payment gateways, wallets. MultiDAG enables cross-chain; strong for payment interoperability.',
        'Ondo Finance':'High: Ondo integrates with USDC, custodians, and DeFi. Strong for treasury and yield system interoperability.',
        'Centrifuge':'High: Centrifuge integrates with SPVs, legal systems, and Cosmos. Strong for credit system interoperability.',
        'SWIFT Blockchain':'High: SWIFT integrates with 11,000+ banks via ISO 20022. DLT trials; strong for global payment interoperability.',
        'Solana':'High: Solana integrates via Wormhole, Allbridge. RPC APIs; strong for high-throughput system access.',
        'Ethereum':'High: Ethereum integrates via L2s, bridges, and oracles. Strong for DeFi and TradFi system interoperability.',
        'WisdomTree tokenization initiatives':'High: WisdomTree integrates with fund platforms, custodians. Strong for asset management system interoperability.',
        'Franklin Templeton BENJI':'High: BENJI integrates with MMF admin, portals. Strong for yield system interoperability.',
        'DTCC Collateral Pilot':'High: DTCC integrates with clearing, repo systems. Strong for collateral management interoperability.',
        'Ripple':'High: Ripple integrates with 300+ banks via ILP, ODL. Strong for cross-border payment system interoperability.',
        'Deutsche Boerse Seturion':'High: Seturion integrates with T2S, CSDs. Strong for EU securities system interoperability.',
        'ICE Digital Assets':'High: ICE integrates with exchanges, clearing. Strong for commodity system interoperability.',
        'Circle':'High: Circle integrates with banks, wallets, DEXs via USDC. Strong for stablecoin system interoperability.',
        'Tether':'High: Tether integrates with exchanges, wallets via USDT. Strong for volume despite centralization.',
        'Visa tokenization initiatives':'High: VTAP integrates with bank core, card rails. Strong for deposit system interoperability.',
        'Hyperliquid':'Medium: Hyperliquid integrates with wallets, DEXs. No TradFi; medium for DeFi system interoperability.',
        'Bakkt':'High: Bakkt integrates with ICE, custody. Strong for futures system interoperability.',
        'OpenEden':'High: OpenEden integrates with treasuries, USDC. Strong for yield system interoperability.',
        'Nasdaq Tokenized Securities':'High: Nasdaq integrates with DTC, brokers. Strong for share system interoperability.',
        'Provenance Foundation':'High: Provenance integrates with loan systems, Cosmos. Strong for credit interoperability.',
        'LSE DMI':'High: DMI integrates with fund admin, Azure. Strong for fund system interoperability.',
        'MakerDAO/FRAX':'High: Maker integrates with DeFi, oracles. Strong for stablecoin system interoperability.',
        '0x Protocol':'High: 0x integrates with DEXs, wallets. Strong for swap system interoperability.',
        'CME GCUL':'High: CME integrates with clearing, Google Cloud. Strong for futures system interoperability.',
        'Realio Network':'High: Realio integrates multi-chain, SPVs. Strong for real estate system interoperability.',
        'Augur':'Medium: Augur integrates with Ethereum, USDC. Niche; medium for prediction system interoperability.',
        'Openverse Global Layer0':'High: Layer0 integrates 20+ chains. Strong for cross-system RWA interoperability.',
        'idOS Network':'Medium: idOS integrates identity systems. Strong for user access; medium for asset flow.',
        'Rayls Labs':'High: Rayls integrates with bank core systems. Strong for private financial interoperability.',
        'TSE/JPX Digital Securities':'High: TSE integrates with Japan exchange systems. Strong for local securities interoperability.',
        'Novastro':'High: Novastro integrates with EVM, Aptos. Strong for AI-yield system interoperability.',
        'B3 Digitas/ACXRWA':'High: B3 integrates with Brazil financial systems. Strong for local RWA interoperability.',
        'LME Modernization':'High: LME integrates with metal delivery systems. Strong for commodity interoperability.',
        'Kalshi':'Medium: Kalshi integrates with U.S. payment rails. CFTC limits; medium interoperability.',
        'Polymarket':'High: Polymarket integrates with Polygon, USDC. Strong for prediction system interoperability.',
        'Crypto.com':'High: Crypto.com integrates with banks, cards. Strong for retail financial interoperability.',
        'RobinHood':'High: Robinhood integrates with broker, bank rails. Strong for retail securities interoperability.',
        'PredictIt':'Low: PredictIt has no blockchain integration. Academic only; low interoperability.',
        'SHFE Initiatives':'High: SHFE integrates with China commodity systems. Strong for local financial interoperability.'
    },
    'Auditability and Third-Party Verification': {
        'Abaxx (ID++/FDT)':'High: Abaxx provides full audit trails via FDT and ID++ logs. Third-party verification via MineHub, ICE. Metadata verifiable without exposing data; strong for institutional compliance.',
        'Securitize NYSE (via ICE)':'High: Securitize offers on-chain audit via ERC-1400. NYSE, DTC provide third-party verification. Strong for regulated securities auditability.',
        'Chainlink CCIP':'High: CCIP offers verifiable oracle logs and risk reports. Third-party audits; strong for cross-chain transparency.',
        'BlackRock BUIDL':'High: BUIDL offers on-chain mint/burn logs. Fund audits, SEC filings; strong for treasury auditability.',
        'JPMorgan Onyx':'High: Onyx offers permissioned audit logs. Bank-grade verification; strong for private asset auditability.',
        'Polkadot':'High: Polkadot offers on-chain governance and validator logs. Third-party audits; strong for parachain transparency.',
        'Corda':'High: Corda offers private flow logs and notary verification. Strong for enterprise auditability.',
        'Polymesh':'High: Polymesh offers on-chain compliance logs. Identity-bound; strong for securities auditability.',
        'Lightning Network':'Medium: Lightning offers channel state proofs. Limited third-party access; medium for payment auditability.',
        'Coinbase':'High: Coinbase offers transaction logs and audits. Insurance, compliance; strong for custodial auditability.',
        'COTI V2':'High: COTI V2 offers confidential audit via garbled circuits. Selective disclosure; strong for privacy-preserving audit.',
        'Ondo Finance':'High: Ondo offers vault logs and oracle proofs. Third-party audits; strong for yield auditability.',
        'Centrifuge':'High: Centrifuge offers pool logs and SPV reports. Third-party verification; strong for credit auditability.',
        'SWIFT Blockchain':'High: SWIFT offers message logs and bank audits. ISO standards; strong for global payment auditability.',
        'Solana':'High: Solana offers on-chain transaction logs. Explorer verification; strong for public auditability.',
        'Ethereum':'High: Ethereum offers on-chain logs via Etherscan. L2 audits; strong for DeFi auditability.',
        'WisdomTree tokenization initiatives':'High: WisdomTree offers fund reports and on-chain logs. Strong for asset management auditability.',
        'Franklin Templeton BENJI':'High: BENJI offers MMF reports and on-chain yield. Strong for yield auditability.',
        'DTCC Collateral Pilot':'High: DTCC offers clearing logs and member audits. Strong for repo auditability.',
        'Ripple':'High: Ripple offers ledger explorer and validator logs. Strong for payment auditability.',
        'Deutsche Boerse Seturion':'High: Seturion offers CSD logs and EU audits. Strong for securities auditability.',
        'ICE Digital Assets':'High: ICE offers exchange logs and CFTC audits. Strong for futures auditability.',
        'Circle':'High: Circle offers USDC attestation reports. On-chain logs; strong for stablecoin auditability.',
        'Tether':'High: Tether offers reserve attestation. On-chain logs; strong despite controversy.',
        'Visa tokenization initiatives':'High: Visa offers bank-grade audit logs. Strong for deposit auditability.',
        'Hyperliquid':'Medium: Hyperliquid offers on-chain order logs. No KYC; medium for perp auditability.',
        'Bakkt':'High: Bakkt offers CFTC audits and exchange logs. Strong for futures auditability.',
        'OpenEden':'High: OpenEden offers treasury reports and on-chain logs. Strong for yield auditability.',
        'Nasdaq Tokenized Securities':'High: Nasdaq offers DTC logs and SEC audits. Strong for share auditability.',
        'Provenance Foundation':'High: Provenance offers loan logs and Cosmos explorer. Strong for credit auditability.',
        'LSE DMI':'High: DMI offers fund reports and Azure logs. Strong for fund auditability.',
        'MakerDAO/FRAX':'High: Maker offers vault logs and governance votes. Strong for stablecoin auditability.',
        '0x Protocol':'High: 0x offers swap logs on-chain. Strong for DEX auditability.',
        'CME GCUL':'High: CME offers clearing logs and audits. Strong for futures auditability.',
        'Realio Network':'High: Realio offers multi-chain logs and SPV reports. Strong for real estate auditability.',
        'Augur':'Medium: Augur offers outcome logs. Oracle disputes; medium for prediction auditability.',
        'Openverse Global Layer0':'High: Layer0 offers bridge logs and ZK proofs. Strong for cross-chain auditability.',
        'idOS Network':'High: idOS offers identity logs and encryption proofs. Strong for user auditability.',
        'Rayls Labs':'High: Rayls offers bank-grade private logs. Strong for institutional auditability.',
        'TSE/JPX Digital Securities':'High: TSE offers exchange logs and FSA audits. Strong for stock auditability.',
        'Novastro':'High: Novastro offers AI model logs and yield reports. Strong for strategy auditability.',
        'B3 Digitas/ACXRWA':'High: B3 offers digital twin logs and CVM audits. Strong for Brazil asset auditability.',
        'LME Modernization':'High: LME offers warrant logs and FCA audits. Strong for metal auditability.',
        'Kalshi':'High: Kalshi offers contract logs and CFTC audits. Strong for event auditability.',
        'Polymarket':'High: Polymarket offers on-chain outcome logs. UMA disputes; strong for prediction auditability.',
        'Crypto.com':'High: Crypto.com offers exchange logs and audits. Strong for retail auditability.',
        'RobinHood':'High: Robinhood offers broker logs and SEC audits. Strong for securities auditability.',
        'PredictIt':'High: PredictIt offers capped contract logs. CFTC oversight; strong for academic auditability.',
        'SHFE Initiatives':'High: SHFE offers commodity logs and CSRC audits. Strong for China market auditability.'
    }
}

points_breakdown = {
    'Abaxx (ID++/FDT)': 'Total: 120. Breakdown: End-to-End Privacy and Security Mechanisms (High, 3 × 3 = 9), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Securitize NYSE (via ICE)': 'Total: 120. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Chainlink CCIP': 'Total: 117. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'BlackRock BUIDL': 'Total: 115. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'JPMorgan Onyx': 'Total: 118. Breakdown: End-to-End Privacy and Security Mechanisms (High, 3 × 3 = 9), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Polkadot': 'Total: 115. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Corda': 'Total: 118. Breakdown: End-to-End Privacy and Security Mechanisms (High, 3 × 3 = 9), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Polymesh': 'Total: 107. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (High, 3 × 3 = 9), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (High, 3 × 3 = 9), Liquidity Fragmentation Risks (Low, 3 × 3 = 9), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Lightning Network': 'Total: 102. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Coinbase': 'Total: 101. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'COTI V2': 'Total: 99. Breakdown: End-to-End Privacy and Security Mechanisms (High, 3 × 3 = 9), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Low, 3 × 3 = 9), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Ondo Finance': 'Total: 98. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Centrifuge': 'Total: 98. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'SWIFT Blockchain': 'Total: 98. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Solana': 'Total: 93. Breakdown: End-to-End Privacy and Security Mechanisms (Low, 1 × 3 = 3), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Ethereum': 'Total: 93. Breakdown: End-to-End Privacy and Security Mechanisms (Low, 1 × 3 = 3), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'WisdomTree tokenization initiatives': 'Total: 96. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Franklin Templeton BENJI': 'Total: 96. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'DTCC Collateral Pilot': 'Total: 96. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (High, 3 × 2 = 6)',
    'Ripple': 'Total: 95. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (High, 3 × 3 = 9), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Deutsche Boerse Seturion': 'Total: 94. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'ICE Digital Assets': 'Total: 94. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Circle': 'Total: 94. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Tether': 'Total: 94. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Visa tokenization initiatives': 'Total: 93. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Hyperliquid': 'Total: 93. Breakdown: End-to-End Privacy and Security Mechanisms (Low, 1 × 3 = 3), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (High, 3 × 3 = 9), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Bakkt': 'Total: 91. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'OpenEden': 'Total: 91. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Nasdaq Tokenized Securities': 'Total: 91. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Provenance Foundation': 'Total: 91. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (High, 3 × 3 = 9), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'LSE DMI': 'Total: 91. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (High, 3 × 3 = 9), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'MakerDAO/FRAX': 'Total: 90. Breakdown: End-to-End Privacy and Security Mechanisms (Low, 1 × 3 = 3), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    '0x Protocol': 'Total: 87. Breakdown: End-to-End Privacy and Security Mechanisms (Low, 1 × 3 = 3), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'CME GCUL': 'Total: 90. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Low, 3 × 2 = 6), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (High, 3 × 2 = 6), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (High, 3 × 3 = 9), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Realio Network': 'Total: 90. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Augur': 'Total: 87. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (High, 3 × 2 = 6), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (High, 3 × 1 = 3), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Openverse Global Layer0': 'Total: 84. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (High, 3 × 2 = 6), Ongoing Operational Cost Efficiency (Low, 3 × 2 = 6), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'idOS Network': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Rayls Labs': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (High, 3 × 3 = 9), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'TSE/JPX Digital Securities': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Novastro': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'B3 Digitas/ACXRWA': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'LME Modernization': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Kalshi': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Polymarket': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'Crypto.com': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'RobinHood': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'PredictIt': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)',
    'SHFE Initiatives': 'Total: 83. Breakdown: End-to-End Privacy and Security Mechanisms (Medium, 2 × 3 = 6), Identity and Ownership Verification with Legal Finality (Medium, 2 × 3 = 6), Private T+0 Settlement for Domestic and Cross-Border RWA Trading (Medium, 2 × 3 = 6), TradFi Integration Costs (Medium, 2 × 2 = 4), Decentralization Risk Management (Medium, 2 × 2 = 4), Seamless Onboarding of Large RWA Traders (Medium, 2 × 3 = 6), Liquidity Fragmentation Risks (Medium, 2 × 3 = 6), Hacking/Manipulation Risks (Medium, 2 × 3 = 6), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFI Transition Path (Medium, 2 × 1 = 2), Leverage of Existing Ecosystem Advantages (Medium, 2 × 3 = 6), KYC/AML Integration (Medium, 2 × 3 = 6), Scalability and Throughput (Medium, 2 × 3 = 6), Custody and Asset Verification Mechanisms (Medium, 2 × 3 = 6), Interoperability Across Chains/Systems (Medium, 2 × 2 = 4), Ongoing Operational Cost Efficiency (Medium, 2 × 2 = 4), Auditability and Third-Party Verification (Medium, 2 × 2 = 4)'
}

solution_descriptions = {
    "Abaxx (ID++/FDT)": "Abaxx Technologies employs a 5-layer cryptographic protocol with ID++ for decentralized identity and verifiable credentials, and Private Full Digital Title (FDT) for legally enforceable digital ownership. This approach prioritizes legal finality over ledger finality, making it DLT-agnostic and suitable for centralized or decentralized exchanges. By integrating with Abaxx Exchange and Clearing, it enables T+0 settlement for RWAs like tokenized gold and USD money market funds used as collateral. Pilots with MineHub for commodity metadata tracking allow in-transit inventories to serve as underlying assets or collateral, bridging physical commodities with digital finance while ensuring privacy and regulatory compliance. The strategy targets institutional players with minimal infrastructure changes, potentially unlocking trillions in commodity markets.",
    "LSE DMI": "The London Stock Exchange Group's Digital Markets Infrastructure (DMI) is a blockchain-based platform for tokenizing private market funds, enhancing access, efficiency, and transparency. Launched in September 2025 on Microsoft Azure, it enables issuers to create and service tokenized funds, integrating with LSEG's Workspace for broader distribution. DMI adopts an open, interoperable approach, connecting global participants to overcome private market illiquidity. Initial transactions involve tokenized equity funds, with plans for secondary trading. This hybrid TradFi-DeFi bridge reduces settlement times and costs, positioning LSEG as a leader in institutional RWA onboarding while addressing regulatory challenges for mainstream adoption.",
    "Deutsche Boerse Seturion": "Deutsche Boerse's Seturion is a blockchain-based settlement platform launched in September 2025 to unify fragmented tokenized asset markets. It supports both public and permissioned blockchains, enabling efficient post-trade settlement for RWAs like equities and bonds. With open architecture and interoperability via XCMP, Seturion reduces costs by up to 90% and enhances liquidity. Partnerships with SocGen Forge for tokenized funds demonstrate secure, compliant transactions. Targeting a $30T market by 2034, it addresses regulatory and scalability challenges, facilitating institutional adoption through seamless integration with existing European capital markets infrastructure and focusing on pan-European connectivity.",
    "Ondo Finance": "Ondo Finance pioneers RWA tokenization by converting traditional assets into yield-bearing tokens like USDY and OUSG, backed by US Treasuries. Launched Ondo Chain in 2025 as an omnichain network for RWAs, it provides institutional-grade infrastructure with low fees and high security. Ondo's approach includes over-collateralized lending and global markets for securities trading, emphasizing compliance and composability. By integrating with DeFi protocols, it unlocks liquidity for illiquid assets, positioning itself at the TradFi-DeFi intersection. Projections see tokenized RWAs reaching trillions, with Ondo leading in stability, accessibility, and innovative financial products for diverse investors.",
    "ICE Digital Assets": "ICE Digital Assets, part of Intercontinental Exchange, advances RWA tokenization through platforms like RWA Inc., which joined ICE's ION ecosystem in 2025. This full-service platform helps projects tokenize assets securely and compliantly, from idea to public markets. ICE's approach emphasizes regulated frameworks, leveraging its traditional exchange expertise to bridge physical commodities (e.g., gold, energy) with blockchain. By integrating with custody solutions and DeFi, it enhances liquidity and 24/7 access. Initiatives include tokenized bonds and equities, aiming to capture trillions in value while addressing regulatory hurdles for institutional adoption and global market efficiency.",
    "Securitize NYSE (via ICE)": "Securitize, backed by BlackRock and partnering with NYSE via ICE, is the largest RWA tokenization platform with over $4B tokenized. Its approach focuses on compliant, end-to-end tokenization of assets like equities, bonds, and funds using blockchain for fractional ownership and efficiency. In 2025, it went public via SPAC at $1.25B valuation, emphasizing institutional-grade infrastructure. Securitize handles issuance, trading, and servicing, integrating with public blockchains while ensuring SEC compliance. This hybrid model bridges TradFi and DeFi, unlocking $19T in potential by democratizing access, reducing costs, and fostering mainstream institutional participation.",
    "Corda": "Corda, developed by R3, is an open, permissioned DLT platform designed for RWA tokenization, enabling secure issuance and management of digital assets like bonds and currencies. Its approach emphasizes interoperability with legacy systems, legal clarity, and traceability, making it ideal for enterprise adoption. Corda supports hybrid models, allowing fractional ownership and efficient cross-border transactions. In 2025, it powered institutional initiatives for tokenized real estate and private credit, reducing friction in TradFi integration. By focusing on compliance and scalability, Corda bridges traditional finance with blockchain, unlocking liquidity for illiquid assets in global markets.",
    "Centrifuge": "Centrifuge is a decentralized platform for RWA tokenization, enabling businesses to convert assets like invoices and real estate into on-chain tokens. Its Launchpad provides pre-built smart contracts for quick deployment, integrating investment flows with privacy features. Using Tinlake dApp, it facilitates collateralized lending and yield generation. In 2025, Centrifuge emphasized composability, partnering with DeFi protocols for liquidity. This approach democratizes access to alternative assets, reducing costs and enhancing transparency. With billions in TVL, it's a leader in bridging off-chain value to blockchain ecosystems, fostering institutional and retail adoption.",
    "CME GCUL": "CME Group's GCUL initiative, in partnership with Google Cloud, introduces tokenization for wholesale payments and asset settlement. Launched in 2025, it leverages Universal Ledger for T+0 efficiency in RWAs like commodities and derivatives. The approach focuses on programmable settlements, reducing risks and costs in capital markets. Pilots demonstrated seamless integration with legacy systems, using AI for compliance. By 2025, phase two testing advanced tokenized collateral, positioning CME as a bridge between TradFi and blockchain, potentially unlocking trillions in value through scalable, secure infrastructure for institutional efficiency.",
    "Nasdaq Tokenized Securities": "Nasdaq's tokenized securities initiative, filed with SEC in 2025, aims to enable trading of tokenized equities and ETFs on its exchange. The approach integrates blockchain with traditional order books, ensuring same rights and priority for tokenized shares. By 2026, it plans to tokenize all listed stocks, enhancing liquidity and 24/7 access. This hybrid model addresses settlement inefficiencies, reducing risks while maintaining compliance. Nasdaq's vision democratizes markets, potentially unlocking $10T in investments through fractional ownership and global reach, reshaping Wall Street with innovative financial products.",
    "B3 Digitas/ACXRWA": "B3, Brazil's main stock exchange, through Digitas and ACXRWA initiatives, advances RWA tokenization for stocks, bonds, and commodities. Its approach uses blockchain to create digital twins of assets, enabling fractional ownership and efficient trading. In 2025, pilots focused on tokenized agribusiness credits and real estate, integrating with central bank regulations. Digitas platform facilitates issuance and settlement, reducing costs and enhancing liquidity. This strategy bridges Latin American markets with global DeFi, addressing illiquidity in emerging economies while ensuring compliance and accessibility for retail and institutional investors.",
    "Polymesh": "Polymesh is a purpose-built blockchain for RWA tokenization, specializing in securities with native compliance features. Its approach embeds identity, jurisdiction, and permissions into tokens, ensuring regulatory adherence from issuance. In 2025, partnerships with BitGo and AlphaPoint enhanced institutional-grade tokenization for equities and funds. Polymesh supports fractional ownership and interoperability, reducing development costs. By prioritizing security and scalability, it addresses TradFi barriers, enabling seamless onboarding of trillions in assets while preventing unauthorized trades through on-chain governance and ecosystem tools.",
    "Coinbase": "Coinbase advances RWA onboarding by tokenizing traditional assets like stocks and treasuries, bridging TradFi and crypto. In 2025, it proposed SEC frameworks for tokenized securities, emphasizing compliance and accessibility. Coinbase Prime offers institutional tokenization services, integrating with DeFi for yield. Its approach focuses on multi-year endeavors for liquidity and usage, with projections for trillions in value. By leveraging its exchange infrastructure, Coinbase democratizes investments, reducing barriers while addressing regulatory gaps to foster mainstream adoption and efficiency in global markets.",
    "Realio Network": "Realio Network is an interoperable Layer-1 blockchain for RWA tokenization, focusing on real estate and private equity. Its approach enables fractional ownership through digital tokens, lowering entry barriers. In 2025, it emphasized compliance and multi-chain compatibility, using RIO utility token for governance. Realio's ecosystem supports issuance and management, unlocking liquidity for illiquid assets. By integrating AI and modular design, it bridges physical and digital worlds, targeting institutional adoption with secure, efficient infrastructure for global asset access and diversified investments.",
    "TSE/JPX Digital Securities": "TSE/JPX Digital Securities initiative aims to launch tokenized stocks by April 2025, using blockchain for security tokens. The approach integrates digital representations with traditional markets, enabling fractional trading and efficiency. In 2025, it focused on regulatory alignment with Japan's frameworks, testing interoperability for cross-border transactions. JPX's strategy bridges Asian markets with global finance, addressing liquidity in equities and bonds. This positions Japan as a leader in regulated RWA onboarding, enhancing transparency and accessibility for investors worldwide.",
    "DTCC Collateral Pilot": "DTCC's Collateral Pilot, launched in 2025, uses Digital Collateral Management Platform for tokenized real-time collateral. The approach employs AppChain to tokenize assets like Treasuries, enabling T+0 mobility and optimization. In collaboration with Digital Asset, pilots demonstrated reduced risks and enhanced transparency. DTCC addresses siloed workflows, integrating with legacy systems for institutional efficiency. This hybrid model unlocks trillions in collateral value, fostering blockchain adoption in post-trade processes while ensuring compliance and scalability for global finance.",
    "SWIFT Blockchain": "SWIFT's blockchain initiatives focus on interconnecting multiple chains for tokenized RWA movements globally. In 2025, pilots demonstrated secure, scalable transfers with modular smart contracts. The approach emphasizes interoperability between TradFi and DeFi, using EVM-compatible tech for compliance. SWIFT bridges centralized and decentralized systems, reducing fragmentation in cross-border settlements. This enables efficient tokenization of assets like bonds, positioning SWIFT as a key enabler for institutional RWA adoption with emphasis on security, privacy, and regulatory evolution.",
    "Ripple": "Ripple's RWA approach leverages XRP Ledger for tokenizing assets like real estate and bonds, enabling fractional ownership and instant settlements. In 2025, it introduced lending protocols and compliance tools for RWAs. Ripple emphasizes legal enforceability and interoperability, partnering with Zoniqx for efficient tokenization. This bridges TradFi with DeFi, unlocking liquidity for illiquid assets. With focus on institutional adoption, Ripple's ecosystem supports CBDCs and stablecoins, projecting trillions in tokenized value through secure, scalable infrastructure.",
    "LME Modernization": "LME's modernization initiative, updated in 2025, incorporates blockchain for tokenizing commodities like metals. The approach enhances options trading with digital settlement, reducing costs and improving liquidity. Pilots explored tokenized warrants for physical deliveries, integrating with global supply chains. LME focuses on regulatory compliance and interoperability, bridging physical markets with DeFi. This strategy addresses volatility in commodity trading, enabling fractional ownership and 24/7 access, positioning LME as a pioneer in RWA for industrial assets and energy transition markets.",
    "Solana": "Solana's RWA approach utilizes its high TPS and low fees for tokenizing assets like real estate and commodities. In 2025, it led in on-chain RWAs with $31B value, using SPL standards for compliant tokens. Solana emphasizes speed for T+0 settlements, integrating with DeFi apps for yield. Tools like compressed NFTs enable efficient fractionalization. This democratizes access, addressing TradFi inefficiencies while supporting institutional pilots, projecting massive growth in tokenized markets through scalable infrastructure.",
    "Ethereum": "Ethereum remains the premier platform for RWA tokenization, using ERC-1400/3643 standards for securities. In 2025, it hosted trillions in tokenized assets like treasuries. Its approach leverages smart contracts for compliance and composability, integrating oracles for off-chain data. Ethereum's Layer-2s enhance scalability, reducing costs for fractional ownership. This bridges TradFi with DeFi, enabling yield farming on RWAs, with projections for $10T market by 2030 through institutional adoption and ecosystem maturity.",
    "SHFE Initiatives": "SHFE's initiatives in 2025 focus on tokenizing commodities like metals and energy, integrating blockchain for efficient futures trading. The approach emphasizes regulatory compliance in China, using digital ledgers for transparency and settlement. Pilots explored cross-border interoperability, addressing liquidity in Asian markets. SHFE bridges physical deliveries with on-chain tokens, enabling fractional contracts. This strategy modernizes commodity finance, reducing risks and costs for global traders while aligning with national digital asset policies.",
    "Kalshi": "Kalshi, a regulated prediction market, approaches RWA onboarding by tokenizing event outcomes like elections or economic indicators. In 2025, it surpassed rivals with $2B valuation, offering compliant betting on real-world events. Kalshi's model uses fiat-backed contracts, bridging TradFi oversight with DeFi-like accessibility. This democratizes risk hedging, providing liquidity for uncertain assets. Lessons in compliance guide crypto startups, positioning Kalshi as a pioneer in tokenized predictions for institutional and retail participation.",
    "Polymarket": "Polymarket is a blockchain-based prediction market for tokenizing real-world events, using USDC for bets. In 2025, it launched $POLY token for governance. Its approach leverages hybrid order books for efficiency, enabling trading on outcomes like elections. Polymarket addresses liquidity fragmentation with on-chain settlement, attracting institutional interest. This DeFi model democratizes forecasting, providing data for RWAs while navigating regulations, potentially expanding to broader tokenized asset classes.",
    "Crypto.com": "Crypto.com facilitates RWA tokenization by representing traditional assets on blockchain, focusing on stablecoins and yield products. In 2025, it emphasized bridging DeFi with real-world value, enabling fractional ownership. The approach uses secure custody and compliance for assets like gold and bonds. Crypto.com's ecosystem supports 24/7 trading, reducing barriers for retail investors. This hybrid strategy unlocks liquidity, projecting growth in tokenized markets through user-friendly apps and institutional integrations.",
    "RobinHood": "Robinhood's RWA approach involves tokenizing stocks and assets for fractional trading. In 2025, it proposed SEC framework for compliant tokenization, emphasizing low barriers. Robinhood integrates blockchain with its app, enabling 24/7 access. This democratizes investments, reducing costs and risks. Competing with Coinbase, it bridges retail TradFi with crypto, potentially unlocking trillions through user-friendly onboarding and innovative financial products for everyday investors.",
    "PredictIt": "PredictIt tokenizes real-world event outcomes as tradeable shares. In 2025, it focused on compliant markets for politics and economics. The approach uses capped contracts for risk management, providing data insights. PredictIt bridges forecasting with finance, enabling hedging as RWAs. This model informs DeFi prediction protocols, emphasizing regulation for institutional trust and broader market participation.",
    "Augur": "Augur is a decentralized platform for tokenizing prediction markets on events. Using REP token for reporting, it enables peer-to-peer betting. In 2025, it emphasized oracle integration for resolution. Augur's approach decentralizes RWAs like outcomes, providing liquidity and transparency. This pioneers DeFi for real-world risks, addressing centralization with community governance and scalable blockchain infrastructure.",
    "Provenance Foundation": "Provenance Foundation's blockchain tokenizes RWAs like loans and bonds, with $15B in value. Its approach uses Hash token for governance, ensuring compliance. In 2025, it focused on institutional adoption, enabling fractional ownership. Provenance bridges finance with blockchain, unlocking liquidity for private assets through secure, scalable infrastructure and ecosystem partnerships.",
    "Bakkt": "Bakkt tokenizes RWAs like Bitcoin futures and commodities. In 2025, it emphasized regulated custody for institutional access. Bakkt's approach integrates with exchanges for seamless trading, reducing risks. This bridges TradFi with crypto, enabling efficient settlements and yield for tokenized assets in global markets.",
    "Tether": "Tether's Hadron platform enables tokenization of anything, focusing on stablecoins backed by RWAs. In 2025, it expanded to APIs for institutional integration. Tether's approach emphasizes fiat-backed tokens for stability, unlocking yield. This positions Tether in trillions market, bridging crypto with traditional finance through compliant, efficient infrastructure and diverse asset classes.",
    "Circle": "Circle advances RWA through USDC, acquiring Hashnote in 2025 for $1.3B in tokenized funds. Its approach tokenizes treasuries and bonds, enabling yield. Circle emphasizes compliance and liquidity, integrating with DeFi. This unlocks institutional access, projecting growth in stable, regulated tokenized assets for global finance.",
    "COTI V2": "COTI V2 is a confidential Ethereum Layer-2 for private RWA tokenization using garbled circuits. In 2025, it focused on DeFi and enterprise adoption. COTI's approach ensures selective disclosure, enabling compliant transactions. This unlocks trillions in RWAs, bridging privacy with regulation for institutional use and secure asset management.",
    "Novastro": "Novastro is a Layer-1 for RWA tokenization, using modular tech and AI for compliance. In 2025, it enabled multi-asset tokenization with yield. Novastro's approach connects chains like Ethereum and Solana, facilitating fractional ownership. This democratizes assets, positioning Novastro for institutional and retail adoption through innovative, cross-chain infrastructure.",
    "idOS Network": "idOS Network provides decentralized identity for RWA tokenization, using IDOS token for governance. In 2025, it focused on privacy and compliance. idOS's approach enables secure onboarding, integrating with blockchains for verifiable credentials. This facilitates trusted transactions, unlocking access for global investors in tokenized assets and ecosystems.",
    "Rayls Labs": "Rayls Labs builds compliant blockchain for RWA tokenization, enabling private deposits and CBDCs. In 2025, RLS token powered governance. Rayls's approach emphasizes UniFi ecosystem for cross-border payments. This bridges TradFi with DeFi, reducing costs and enhancing liquidity for institutional assets and financial services.",
    "OpenEden": "OpenEden is an RWA platform tokenizing US Treasuries into yield-bearing tokens like USDO. In 2025, EDEN utility unlocked tools. OpenEden's approach integrates Ethereum for institutional access, bridging TradFi-DeFi. This provides stable yields, projecting growth in tokenized government securities and diverse financial products.",
    "Polkadot": "Polkadot enables RWA tokenization via parachains, offering interoperability and compliance. In 2025, it hosted tokenized real estate and bonds. Polkadot's approach uses Substrate for custom chains, enabling fractional ownership. This unlocks liquidity, positioning Polkadot for trillions in on-chain value through scalable, secure ecosystems.",
    "Chainlink CCIP": "Chainlink CCIP provides cross-chain infrastructure for RWA tokenization, using oracles for data. In 2025, it enabled any-to-any bridging. Chainlink's approach ensures secure transfers, preventing manipulation. This unlocks composability, facilitating institutional adoption in multi-chain ecosystems and tokenized asset markets.",
    "0x Protocol": "0x Protocol enables efficient trading of tokenized RWAs like equities. In 2025, it focused on low-slippage P2P trades. 0x's approach uses EVM-compatible chains for permissionless exchanges. This enhances liquidity for illiquid assets, bridging DeFi with TradFi through secure, decentralized infrastructure.",
    "Lightning Network": "Lightning Network tokenizes RWAs on Bitcoin using Taproot Assets for instant settlements. In 2025, it supported commodities and bonds. Lightning's approach uses state channels for privacy and low costs. This enables micropayments, positioning Bitcoin for RWA adoption with battle-tested security and scalability.",
    "MakerDAO/FRAX": "MakerDAO and FRAX integrate RWAs as collateral for DAI and FRAX stablecoins. In 2025, they tokenized bonds and real estate for yield. Their approach uses vaults for over-collateralization, ensuring stability. This bridges DeFi with TradFi, unlocking liquidity through decentralized governance and lending protocols.",
    "Openverse Global Layer0": "Openverse Global Layer0 is a hub network connecting blockchains for RWA tokenization. In 2025, it enabled AI-driven routing. Openverse's approach focuses on compliance and cross-chain payments. This unlocks global access, positioning it as infrastructure for tokenized economies and value internet applications.",
    "BlackRock BUIDL": "BlackRock's BUIDL is a tokenized USD liquidity fund on Ethereum, with $690M AUM in 2025. Its approach uses Benji platform for intraday yield. BUIDL bridges TradFi with crypto, enabling 24/7 trading. This institutional-grade tokenization reshapes asset management, unlocking trillions through efficient, compliant digital funds.",
    "JPMorgan Onyx": "JPMorgan's Onyx (now Kinexys) tokenizes private equity and assets on blockchain. In 2025, it focused on composability and privacy. JPM's approach uses Project Guardian for tokenization, enabling smart portfolios. This accelerates alternatives distribution, unlocking $400B opportunity through efficient, scalable infrastructure for wealth management.",
    "Franklin Templeton BENJI": "Franklin Templeton's BENJI platform tokenizes money market funds, launching on BNB Chain in 2025. Its approach offers intraday yield and multi-chain access. BENJI enables regulated RWAs like treasuries, bridging institutions with DeFi. This expands tokenized products, enhancing liquidity and diversification for investors.",
    "Visa tokenization initiatives": "Visa's Tokenized Asset Platform (VTAP) enables banks to issue fiat-backed tokens. Launched in 2024, it tested with BBVA on Ethereum. Visa's approach standardizes interactions for RWAs like bonds, integrating with public chains. This bridges payments with blockchain, unlocking tokenized finance for global institutions and efficient settlements.",
    "WisdomTree tokenization initiatives": "WisdomTree's initiatives include Prime and Connect platforms for tokenized RWAs. In 2025, it launched private credit funds onchain. WisdomTree's approach offers 13 tokenized products across chains, enabling institutional access. This bridges alternatives with blockchain, unlocking yield and liquidity through regulated structures and diverse asset exposures.",
    "Hyperliquid": "Hyperliquid is a DEX for perpetuals, expanding to RWA tokenization in 2025. Its approach uses high-throughput for trading tokenized assets like commodities. Hyperliquid emphasizes low fees and decentralization, challenging traditional exchanges. This unlocks liquidity for RWAs through derivatives, attracting institutional volume and retail traders in volatile markets."
}





# Full tooltip_data
tooltip_data = []
for i in range(len(df)):
    row_hover = {}
    for col in df.columns:
        if col == 'Solution':
            row_hover[col] = {'value': solution_descriptions.get(df['Solution'][i], 'No description available')}
        elif col == 'Points':
            row_hover[col] = {'value': points_breakdown.get(df['Solution'][i], 'No breakdown available')}
        else:
            row_hover[col] = {'value': cell_hover_text.get(col, {}).get(df['Solution'][i], 'No rationale available')}
    tooltip_data.append(row_hover)


# Generate standalone HTML table with embedded hover text
def generate_standalone_html(df, tooltip_data, tooltip_header, solution_map, filename='rwa_table_V2.html'):
    # Sort DataFrame by "Points" in descending order
    df_sorted = df.sort_values(by='Points', ascending=False)

    # Reindex tooltip_data to match the sorted DataFrame
    tooltip_data_sorted = [tooltip_data[i] for i in df_sorted.index]

    # Determine the longest header text for height adjustment
    max_header_length = max(len(str(col)) for col in df_sorted.columns)  # Basic length-based estimate
    # Adjust height based on length (e.g., 30px base + 5px per 5 characters beyond 10)
    header_height = max(40, 10 + int(max(0, (max_header_length)) * 0.85))

    # HTML header with embedded CSS for styling and tooltips
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RWA Tokenization Platforms</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #000;
            }}
            h1 {{
                text-align: center;
                font-size: 24px;
                margin-bottom: 10px;
                color: #fff;
            }}
            p {{
                text-align: center;
                font-size: 14px;
                margin-bottom: 20px;
                color: #fff;
            }}
            table {{
                width: 100%;
                min-width: 100%;
                border-collapse: collapse;
                overflow-x: auto;
                display: inline-table; /* Change from display: block */
                white-space: nowrap; /* Prevent row wrapping */
                background-color: #000;
            }}
            th, td {{
                border: 1px solid #666;
                text-align: center;
                font-size: 11px;
                height: 30px;
                min-width: 120px;
                width: 120px;
                max-width: 120px;
                white-space: normal;
                line-height: normal;
                padding: 8px;
                background-color: #000; /* All cells black background */
            }}
            th {{
                font-weight: bold;
                font-size: 12px;
                white-space: normal;
                height: {header_height}px; /* Uniform height for headers */
                position: sticky;
                top: 0;
                z-index: 10;
                color: #FFF; /* Header font color white */
            }}
            .tooltip {{
                position: relative;
                display: inline-block;
                cursor: pointer;
            }}
            .tooltip .tooltiptext {{
                visibility: hidden;
                width: 200px;
                background-color: #333;
                color: #fff;
                text-align: left;
                border-radius: 6px;
                padding: 10px;
                position: absolute;
                z-index: 100;
                top: 100%; /* Below the cell */
                left: 100%; /* Right of the cell */
                margin-left: 10px; /* Offset to bottom-right */
                margin-top: 5px; /* Slight vertical adjustment */
                opacity: 0;
                transition: opacity 0.3s;
                font-size: 12px;
                white-space: pre-wrap;
            }}
            .tooltip:hover .tooltiptext {{
                visibility: visible;
                opacity: 1;
            }}
        </style>
    </head>
    <body>
        <h1>RWA Tokenization Platforms: Weighted Impact Analysis</h1>
        <p>Blue: Permissioned Blockchain/Enterprise, Green: Hybrid DeFi/TradFi, Orange: Public Blockchain, Gray: Traditional Exchange,  Purple: Prediction Markets</p>
        <table>
            <thead>
                <tr>
    """

    # Add table headers with tooltips
    for col in df_sorted.columns:
        tooltip = tooltip_header.get(col, {}).get('Description', '').replace('\n', '<br>')
        html_content += f'<th class="tooltip">{col}<span class="tooltiptext">{tooltip}</span></th>'

    html_content += """
                </tr>
            </thead>
            <tbody>
    """

    # Add table rows with data and tooltips
    for i, row in enumerate(df_sorted.to_dict('records')):
        solution = row['Solution']
        if solution_types.get(solution_map.get(solution))['display']:
            html_content += '<tr>'
            solution = row['Solution']
            # Determine row font color based on Solution
            row_color = solution_types.get(solution_map.get(solution))['color']
            for j, col in enumerate(df_sorted.columns):
                value = row[col]
                tooltip = tooltip_data_sorted[i].get(col, {}).get('value', '').replace('\n', '<br>')
                html_content += f'<td class="tooltip" style="color: {row_color};">{value}<span class="tooltiptext">{tooltip}</span></td>'
            html_content += '</tr>'
            #
    # Close HTML
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Call the function to generate the HTML
generate_standalone_html(df, tooltip_data, tooltip_header, solution_map)
