# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:04:49 2025

@author: molin
"""
import pandas as pd

data = {
    'Solution': ['Abaxx (ID++/PDT)', 'LSE DMI', 'Deutsche Boerse Seturion', 'Ondo Finance', 'ICE Digital Assets',
                 'Securitize', 'NYSE (via ICE)', 'Corda', 'Centrifuge', 'CME GCUL', 'Nasdaq Tokenized Securities',
                 'B3 Digitas/ACXRWA', 'Polymesh', 'Realio Network', 'TSE/JPX Digital Securities',
                 'DTCC Collateral Pilot', 'SWIFT Blockchain', 'Ripple (XRP Ledger)', 'LME Modernization',
                 'Solana', 'Ethereum', 'SHFE Initiatives', 'Kalshi', 'Polymarket', 'Crypto.com', 'RobinHood',
                 'PredictIt', 'Augur', 'Provenance Foundation'],
    'Encrypted P2P Communication (High Impact)': [
        'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': [
        'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High'
    ],
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High',
        'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High'
    ],
    'Private RWA Trading with T+0 Settlement (High Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'High', 'Medium', 'Low',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'Cross-Border T+0 for RWAs (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Medium', 'Low', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High'
    ],
    'TradFi Integration Friction/Cost (High Impact)': [
        'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low',
        'Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low',
        'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low'
    ],
    'Centralization vs. Decentralization Balance (Medium Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Low',
        'Medium', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium'
    ],
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low',
        'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High'
    ],
    'Minimizes Oracles/Bridges Risks (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'Low', 'Low', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'Liquidity Fragmentation Risk (High Impact)': [
        'Low', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': [
        'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Low',
        'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'High', 'High', 'Low',
        'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium'
    ],
    'Regulatory Adaptability to Evolving Global Standards (High Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low',
        'High', 'High', 'High', 'High', 'High', 'High', 'High'
    ],
    'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Low', 'Low', 'Low', 'High', 'Low', 'High', 'High', 'Low',
        'Medium', 'High', 'High', 'Medium', 'Medium', 'High', 'High'
    ],
    'Incumbent Advantages (High Impact)': [
        'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High',
        'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Low', 'Low', 'Medium',
        'Low', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Medium'
    ],
    'Regulatory Tailwinds (High Impact)': [
        'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High',
        'Medium', 'Medium', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'High', 'High', 'High', 'High'
    ],
    'Points': [
        55.0, 49.0, 50.0, 50.5, 50.0, 48.0, 48.0, 49.0, 47.0, 46.0, 48.0, 42.0, 46.0, 47.0, 39.5, 39.5,
        39.5, 41.0, 34.0, 39.5, 39.5, 32.5, 48.0, 49.0, 47.0, 46.0, 45.0, 44.0, 46.5  # Updated with Provenance
    ]
}

# Convert to DataFrame for sorting and consistency
df = pd.DataFrame(data)

tooltip_header = {
    'Solution': {'value': 'Represents various blockchain and traditional platforms evaluated for RWA tokenization, ranked by aggregated points reflecting their performance across criteria. (75 words)'},
    'Encrypted P2P Communication (High Impact)': {'value': 'Assesses ability to secure peer-to-peer interactions in RWAs, critical for privacy and trust. High scores indicate robust encryption, challenging incumbents and prediction markets like Kalshi with pro-tech tailwinds. (75 words)'},
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Evaluates W3C-compliant digital identities for KYC/AML in RWAs. High scores reflect strong compliance, competing with US tailwinds and prediction markets for institutional adoption. (75 words)'},
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Measures legal enforceability of RWA ownership per MLETR. High scores indicate strong alignment, challenging incumbents with regulatory tailwinds vs prediction markets. (75 words)'},
    'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Gauges T+0 settlement capability for RWAs. High scores reflect speed, leveraging US pro-tech to outpace prediction markets like Polymarket in efficiency. (75 words)'},
    'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Assesses cross-border T+0 feasibility. High scores indicate global reach, challenging incumbents with tailwinds and competing with prediction markets in RWAs. (75 words)'},
    'TradFi Integration Friction/Cost (High Impact)': {'value': 'Evaluates ease/cost of TradFi integration. Low scores are best, minimizing barriers with US tailwinds, resisting prediction market disruptions in RWAs. (75 words)'},
    'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Balances centralized control with DeFi openness. High scores optimize security/scalability, challenging incumbents and prediction markets with regulatory support. (75 words)'},
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Measures protection against reverse engineering in RWAs. High scores ensure privacy, competing with US pro-tech and resisting prediction market transparency. (75 words)'},
    'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Assesses reduction of oracle/bridge vulnerabilities. High scores limit risks, leveraging US tailwinds to outpace prediction markets in RWA stability. (75 words)'},
    'Liquidity Fragmentation Risk (High Impact)': {'value': 'Evaluates risk of fragmented liquidity in RWAs. Low scores are best, reducing barriers with US tailwinds, challenging prediction markets like Kalshi in adoption. (75 words)'},
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Measures vulnerability to hacking/manipulation. Low scores are best, enhancing security with US pro-tech, resisting prediction market threats in RWAs. (75 words)'},
    'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Assesses flexibility to global regulatory changes. High scores reflect compliance, leveraging US tailwinds to challenge incumbents and prediction markets. (75 words)'},
    'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Gauges potential for sustainable DeFi protocols in RWAs. High scores indicate scalability, competing with US incumbents and prediction markets. (75 words)'},
    'Incumbent Advantages (High Impact)': {'value': 'Evaluates existing market power for RWA adoption. High scores reflect volume/brand, challenging prediction markets with US tailwinds. (75 words)'},
    'Regulatory Tailwinds (High Impact)': {'value': 'Measures supportive regulatory environments. High scores leverage US pro-tech, enhancing RWA growth vs prediction markets and incumbents. (75 words)'},
    'Points': {'value': 'Aggregated weighted score (High=3, Medium=2, Low=1; inverted for risks like hacking). Reflects overall RWA potential, ranking solutions with US tailwinds and prediction market context. (75 words)'}
}

color_map = {
    'Abaxx (ID++/PDT)': 'blue',  # Permissioned Blockchain/Enterprise
    'LSE DMI': 'gray',           # Traditional Exchange
    'Deutsche Boerse Seturion': 'gray',
    'Ondo Finance': 'green',     # Hybrid DeFi/TradFi
    'ICE Digital Assets': 'gray',
    'Securitize': 'blue',
    'NYSE (via ICE)': 'gray',
    'Corda': 'blue',
    'Centrifuge': 'green',
    'CME GCUL': 'gray',
    'Nasdaq Tokenized Securities': 'gray',
    'B3 Digitas/ACXRWA': 'gray',
    'Polymesh': 'blue',
    'Realio Network': 'green',
    'TSE/JPX Digital Securities': 'gray',
    'DTCC Collateral Pilot': 'gray',
    'SWIFT Blockchain': 'gray',
    'Ripple (XRP Ledger)': 'green',
    'LME Modernization': 'gray',
    'Solana': 'orange',          # Public Blockchain
    'Ethereum': 'orange',
    'SHFE Initiatives': 'gray',
    'Kalshi': 'green',
    'Polymarket': 'green',
    'Crypto.com': 'green',
    'RobinHood': 'gray',
    'PredictIt': 'green',
    'Augur': 'orange',
    'Provenance Foundation': 'green'  # Hybrid, based on its DeFi/TradFi focus
}

tooltip_data = [
    # Abaxx (ID++/PDT)
    {'Encrypted P2P Communication (High Impact)': {'value': 'High: Abaxx\'s ID++ uses 5-layer encryption for secure P2P in commodity RWAs, leveraging Singapore\'s innovation. This challenges US incumbents with pro-tech tailwinds, resisting prediction market disruptions like Kalshi with robust privacy. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Abaxx\'s ID++ integrates W3C-compliant DIDs for KYC/AML, enhancing trust in RWAs. Singapore\'s edge competes with US tailwinds, outpacing prediction markets like Polymarket in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Abaxx\'s MLETR compliance ensures legal finality for RWAs, leveraging Singapore\'s framework. This challenges US incumbents, with prediction markets like Kalshi adding pressure, but Abaxx maintains scalability. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Abaxx\'s platform enables T+0 for commodities, using ID++ for speed. Singapore\'s edge competes with US tailwinds, resisting prediction market disruptions in RWAs. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Abaxx\'s global design supports cross-border T+0, leveraging Singapore\'s hub. This challenges US incumbents, with prediction markets like Kalshi adding competition in RWAs. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Abaxx\'s permissioned system minimizes TradFi friction, reducing costs for commodity RWAs. Singapore\'s innovation edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Abaxx balances centralized control with DeFi flexibility, optimizing RWA security. This leverages Singapore\'s edge vs US incumbents, outpacing prediction markets like Kalshi. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Abaxx\'s ID++ ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency in commodities. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Abaxx avoids oracles, minimizing risks in RWAs. Singapore\'s design competes with US pro-tech, outpacing prediction markets like Polymarket. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Abaxx\'s unified platform reduces fragmentation, enhancing liquidity for RWAs. Singapore\'s edge competes with US tailwinds, challenging prediction markets like Kalshi in adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Abaxx\'s federated blockchain with multi-layer encryption minimizes hacking risks, ensuring robust security for commodity RWAs. This leverages Singapore\'s innovation edge, challenging US incumbents\' defenses amid pro-tech tailwinds. Prediction markets like Kalshi pose new threats, but Abaxx\'s privacy focus reduces vulnerability, supporting institutional trust without adding complexity from fragmented chains. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Abaxx\'s MLETR compliance and Singapore\'s pro-innovation framework ensure adaptability to global standards like MiCAR and UCC. This positions it to leverage regulatory competition, challenging US incumbents with tailwinds from pro-tech policies. Prediction markets like Kalshi may accelerate change, but Abaxx\'s stack reduces complexity for institutional scaling. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Abaxx\'s hybrid DeFi roadmap supports long-term open protocols, leveraging Singapore\'s innovation. This challenges US incumbents with tailwinds, potentially integrating prediction markets like Kalshi for scalable RWA adoption without excessive complexity. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Abaxx benefits from Singapore\'s hub, easing RWA onboarding, but lacks US incumbent volumes. This balances new tech with market power, challenging US tailwinds and prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: Singapore\'s innovation hub supports Abaxx\'s RWA growth, competing with US pro-tech. This tailwind aids adoption, but US incumbents may outpace with financial power vs prediction markets. (75 words)'},
     'Points': {'value': '55.0: Aggregated score reflecting high performance across criteria, ranking Abaxx at the top for RWA tokenization.'}},
    # LSE DMI
    {'Encrypted P2P Communication (High Impact)': {'value': 'High: LSE DMI\'s Azure-backed ledger ensures secure P2P for RWAs, aligning with MiCA. This strengthens EU incumbents vs US pro-tech, resisting prediction market disruptions like Polymarket. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: LSE DMI integrates W3C-compliant DIDs for KYC, enhancing RWA trust. UK\'s stance aids vs US tailwinds, outpacing prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: LSE\'s MLETR alignment ensures legal finality, leveraging UK volumes. This challenges US incumbents, with prediction markets adding pressure for scalability. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: LSE enables T+0 for funds, using DMI for speed. UK\'s edge competes with US tailwinds, resisting prediction market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: LSE\'s global reach supports cross-border T+0, leveraging UK hub. This challenges US incumbents, with prediction markets like Kalshi competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: LSE\'s established infrastructure minimizes TradFi friction, reducing costs. UK\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: LSE balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets like Polymarket challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: LSE\'s ledger ensures privacy, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: LSE avoids oracles, minimizing risks in RWAs. UK\'s design competes with US pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: LSE\'s regional focus increases fragmentation, limiting liquidity. UK\'s pro-innovation stance aids vs US tailwinds, but struggles vs prediction market disruption in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: LSE DMI\'s Azure-backed permissioned ledger provides enterprise-grade security, minimizing manipulation risks for tokenized funds. Aligned with MiCA, it strengthens EU incumbents against US pro-tech shifts. Prediction markets like Polymarket introduce competition, but LSE\'s centralized control and audits reduce susceptibility, maintaining medium-term adoption without DeFi\'s exposure. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: LSE DMI\'s MiCA alignment supports EU/UK standards, but slower adaptation lags US pro-tech shifts. Incumbent advantages in volumes aid resilience, yet prediction markets like Polymarket push for faster innovation, constraining LSE\'s flexibility in evolving RWA regulations. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: LSE DMI\'s centralized model limits long-term DeFi protocols. UK\'s stance aids vs US pro-tech, but prediction markets like Polymarket may outpace in open RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: LSE\'s established fund infrastructure and UK volumes enable rapid RWA onboarding. This incumbent advantage, bolstered by MiCAR, competes with US pro-tech and resists prediction market disruption. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: UK\'s pro-innovation stance aids LSE, but EU MiCAR lags US tailwinds. This balances vs US incumbents in the global RWA race, resisting prediction market disruption. (75 words)'},
     'Points': {'value': '49.0: Aggregated score reflecting strong incumbent advantages, ranking LSE mid-tier for RWA tokenization.'}},
    # Deutsche Boerse Seturion
    {'Encrypted P2P Communication (High Impact)': {'value': 'High: Seturion\'s DLT ensures secure P2P for RWAs, aligning with MiCAR. This strengthens EU incumbents vs US pro-tech, resisting prediction market disruptions. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Seturion integrates W3C-compliant DIDs for KYC, enhancing RWA trust. EU\'s stance aids vs US tailwinds, outpacing prediction markets. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Seturion\'s MLETR compliance ensures legal finality, leveraging EU volumes. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Seturion enables T+0 for securities, using DLT for speed. EU\'s edge competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Seturion\'s pan-European reach supports T+0, leveraging EU hub. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Seturion\'s infrastructure minimizes TradFi friction, reducing costs. EU\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Seturion balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Seturion\'s DLT ensures privacy, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Seturion avoids oracles, minimizing risks in RWAs. EU\'s design competes with US pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Seturion\'s integrated system reduces fragmentation, boosting liquidity. EU\'s MiCAR competes with US pro-tech, leveraging incumbent power vs prediction markets in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Seturion\'s permissioned DLT with Clearstream integration offers strong security, minimizing hacking risks for tokenized securities. Compliant with MiCAR, it bolsters EU incumbents vs US tailwinds. Emerging prediction markets like Kalshi challenge innovation, but Seturion\'s focus on compliance reduces vulnerability, aiding long-term RWA stability. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Seturion\'s MiCAR compliance ensures EU adaptability, but trails US pro-tech speed. Incumbent power aids vs prediction markets like Kalshi, but less tech-savvy jurisdiction may hinder global standard alignment. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Seturion\'s permissioned focus limits long-term DeFi protocols. EU\'s MiCAR competes with US, but prediction markets challenge incumbent scalability in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: Seturion leverages Clearstream/Euroclear volumes for securities onboarding. EU incumbent power aids vs US tailwinds, but lags vs prediction markets in tech innovation. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: EU\'s MiCAR supports Seturion, but US pro-tech outpaces. This tailwind aids vs prediction markets, leveraging incumbent power in RWA leadership. (75 words)'},
     'Points': {'value': '50.0: Aggregated score reflecting strong incumbent position, ranking Seturion mid-tier for RWA tokenization.'}},
    # Ondo Finance
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Ondo\'s hybrid platform offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, but prediction markets like Polymarket challenge with innovation. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Ondo integrates basic DIDs for KYC, enhancing RWA trust. US tailwinds support, but lags vs prediction markets in compliance depth. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Ondo\'s MLETR compliance ensures legal finality, leveraging US ties. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Ondo enables T+0 for hybrid RWAs, using smart contracts. US shift competes with EU tailwinds, resisting prediction market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Ondo\'s global design supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Ondo\'s hybrid minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Ondo balances hybrid control with DeFi, optimizing RWA security. US support aids vs incumbents, outpacing prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Ondo ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Ondo avoids heavy oracle use, minimizing risks in RWAs. US design competes with EU pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Ondo\'s hybrid model increases fragmentation, affecting liquidity. US regulatory shift enhances adoption, potentially obsoleting incumbent barriers vs prediction markets. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Ondo\'s hybrid DeFi/TradFi platform faces moderate manipulation risks due to open integrations and cross-chain exposure. US regulatory shift enhances defenses, but less robust than permissioned systems. Prediction markets like Polymarket add competitive pressure, with Ondo\'s audits mitigating susceptibility while balancing scalability. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Ondo\'s UCC/MLETR compliance adapts to US pro-tech, competing with EU MiCAR. Hybrid model leverages tailwinds, potentially obsoleting incumbent barriers while integrating prediction market innovations for RWA scalability. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Ondo\'s hybrid supports long-term open DeFi protocols. US regulatory shift enhances, challenging incumbents and prediction markets like Polymarket in RWA evolution. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Ondo lacks incumbent volumes but gains from JPMorgan ties. US regulatory shift boosts adaptability, potentially obsoleting traditional barriers vs prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US regulatory shift boosts Ondo\'s DeFi/TradFi hybrid. This tailwind challenges EU, potentially obsoleting incumbent barriers vs prediction markets. (75 words)'},
     'Points': {'value': '50.5: Aggregated score reflecting hybrid strength, ranking Ondo near the top for RWA tokenization.'}},
    # ICE Digital Assets
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: ICE\'s platform offers moderate P2P security for RWAs, with audits mitigating risks. US tailwinds aid vs EU, but prediction markets challenge with innovation. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: ICE integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance depth. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: ICE\'s MLETR compliance ensures legal finality, leveraging US volumes. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: ICE enables T+0 for commodities, using exchange infrastructure. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: ICE\'s global network supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: ICE\'s exchange minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: ICE balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: ICE ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: ICE avoids oracles, minimizing risks in RWAs. US design competes with EU pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: ICE\'s exchange network reduces fragmentation, enhancing liquidity. US tailwinds and incumbent volumes dominate, resisting prediction market disruption in the RWA space. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: ICE\'s regulated platform with enterprise security minimizes malicious risks. This ensures trust in commodity RWAs, leveraging US tailwinds and incumbent volumes. Prediction markets like Kalshi pose disruption, but ICE\'s centralized control and audits reduce vulnerability, maintaining leadership in global competition against manipulation attempts. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: ICE\'s UCC alignment adapts to US pro-tech, enhancing global standards compliance. Incumbent volumes and tailwinds dominate vs prediction markets like Kalshi, ensuring leadership in RWA tokenization without added complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: ICE\'s centralized model limits long-term DeFi protocols. US tailwinds aid, but prediction markets like Kalshi may disrupt RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: ICE\'s exchange volumes enable swift commodity RWA onboarding. US tailwinds and financial power dominate, resisting prediction market disruption like Kalshi. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US pro-tech regulations enhance ICE\'s RWA leadership. This tailwind leverages incumbent volumes, resisting prediction market disruption like Kalshi. (75 words)'},
     'Points': {'value': '50.0: Aggregated score reflecting strong incumbent position, ranking ICE mid-tier for RWA tokenization.'}},
    # Securitize
    {'Encrypted P2P Communication (High Impact)': {'value': 'High: Securitize\'s DS Protocol ensures secure P2P for RWAs, with audits mitigating risks. US approvals aid vs EU, resisting prediction market disruptions. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Securitize integrates W3C-compliant DIDs for KYC, enhancing RWA trust. US tailwinds support, outpacing prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Securitize\'s MLETR compliance ensures legal finality, leveraging US framework. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Securitize enables T+0 for tokens, using DS Protocol. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Securitize\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Securitize\'s enterprise focus minimizes TradFi friction, reducing costs. US approvals edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Securitize balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Securitize ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Securitize avoids oracles, minimizing risks in RWAs. US design competes with EU pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Securitize\'s niche focus increases fragmentation, limiting liquidity. US approvals enhance competitiveness vs EU, leveraging tailwinds against prediction markets in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Securitize\'s permissioned DS Protocol provides robust security, minimizing hacking risks for token issuance. US approvals boost defenses vs EU, with audits reducing vulnerability. Prediction markets challenge innovation, but Securitize\'s compliance focus supports institutional trust in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Securitize\'s UCC/MLETR compliance adapts to US pro-tech, competing with EU MiCAR. This leverages tailwinds against prediction markets, ensuring flexibility for institutional RWA scaling with minimal failure points. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Securitize\'s permissioned model limits long-term DeFi protocols. US approvals enhance vs EU, but prediction markets hinder open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Securitize\'s enterprise focus aids token issuance, but lacks volumes. US approvals enhance vs EU, leveraging tailwinds against prediction markets in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US approvals boost Securitize\'s token issuance. This tailwind enhances vs EU, leveraging regulatory competition against prediction markets in RWAs. (75 words)'},
     'Points': {'value': '48.0: Aggregated score reflecting strong US support, ranking Securitize mid-tier for RWA tokenization.'}},
    # NYSE (via ICE)
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: NYSE\'s ICE system offers moderate P2P security for RWAs, with audits mitigating risks. US tailwinds aid vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: NYSE integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: NYSE\'s MLETR compliance ensures legal finality, leveraging US volumes. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: NYSE enables T+0 for funds, using ICE infrastructure. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: NYSE\'s global reach supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: NYSE\'s exchange minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: NYSE balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: NYSE ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: NYSE avoids oracles, minimizing risks in RWAs. US design competes with EU pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: NYSE\'s integrated platform reduces fragmentation, boosting liquidity. US pro-tech and incumbent power ensure leadership, potentially outpacing prediction markets in RWA space. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: NYSE\'s ICE-integrated system with enterprise security minimizes manipulation risks for tokenized funds. US pro-tech and incumbent power enhance defenses. Prediction markets like Polymarket face barriers, allowing NYSE to maintain stability and outpace emerging threats in the RWA space with robust audits. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: NYSE\'s UCC alignment adapts to US pro-tech, enhancing global compliance. Incumbent power and tailwinds outpace prediction markets like Polymarket, ensuring adaptability without DeFi\'s fragmentation risks. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: NYSE\'s centralized model limits long-term DeFi protocols. US pro-tech aids, but prediction markets like Polymarket challenge RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: NYSE\'s exchange infrastructure facilitates fund onboarding. US pro-tech and incumbent power ensure leadership, potentially outpacing prediction markets in RWA space. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US pro-tech push strengthens NYSE\'s RWA position. This tailwind ensures incumbent dominance, potentially leading to prediction market decline in RWA space. (75 words)'},
     'Points': {'value': '48.0: Aggregated score reflecting strong incumbent position, ranking NYSE mid-tier for RWA tokenization.'}},
    # Corda
    {'Encrypted P2P Communication (High Impact)': {'value': 'High: Corda\'s notary-based DLT ensures secure P2P for RWAs, with audits mitigating risks. This competes with US tailwinds, resisting prediction market disruptions. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Corda integrates W3C-compliant DIDs for KYC, enhancing RWA trust. Global reach aids vs US tailwinds, outpacing prediction markets. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Corda\'s MLETR compliance ensures legal finality, leveraging bank focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Corda enables T+0 for private RWAs, using notary system. Global reach competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Corda\'s bank focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Corda\'s bank integration minimizes TradFi friction, reducing costs. Global reach edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Corda balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Corda ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Corda avoids oracles, minimizing risks in RWAs. Global design competes with US pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Corda\'s bank-focused system increases fragmentation, affecting liquidity. Global competition favors US tailwinds, with potential integration with prediction markets in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Corda\'s permissioned notary-based DLT minimizes hacking risks for private RWAs. Regular audits and encryption ensure trust, competing with US tailwinds. Prediction markets like Kalshi pose innovation threats, but Corda\'s security focus reduces vulnerability, supporting medium-term RWA adoption in a competitive landscape. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Corda\'s bank compliance adapts to standards, but slower than US pro-tech. This aids vs prediction markets, but incumbent focus may hinder flexibility in evolving RWA regulations. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Corda\'s bank focus limits long-term DeFi protocols. US tailwinds support, but prediction markets hinder open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Corda\'s bank focus aids onboarding, but lacks exchange volumes. Global competition favors US tailwinds, integrating with prediction markets in RWA adoption. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: Global bank focus aids Corda, but US tailwinds favor incumbents. This balances vs prediction markets in regulatory competition for RWA adoption. (75 words)'},
     'Points': {'value': '49.0: Aggregated score reflecting solid bank integration, ranking Corda mid-tier for RWA tokenization.'}},
    # Centrifuge
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Centrifuge\'s multi-chain offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Centrifuge integrates basic DIDs for KYC, enhancing RWA trust. US tailwinds support, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Centrifuge\'s MLETR compliance ensures legal finality, leveraging DeFi. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Centrifuge enables T+0 for credit RWAs, using smart contracts. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Centrifuge\'s multi-chain supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Centrifuge\'s DeFi focus increases TradFi friction, raising costs. US tailwinds aid, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Centrifuge balances DeFi with control, optimizing RWA security. US support aids vs incumbents, outpacing prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Centrifuge offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Centrifuge uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Centrifuge\'s multi-chain model increases fragmentation, limiting liquidity. US regulatory push may favor incumbents, but its DeFi approach challenges prediction markets in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Centrifuge\'s multi-chain DeFi exposes it to moderate manipulation risks from bridges. US shift favors incumbents, but audits mitigate. Prediction markets like Polymarket add pressure, with Centrifuge\'s privacy offering partial protection in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Centrifuge\'s MLETR compliance adapts to global DeFi standards, leveraging US pro-tech. This challenges incumbents, with prediction markets like Kalshi adding innovation, but multi-chain adds complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Centrifuge\'s multi-chain supports long-term open DeFi protocols. US shift enhances, challenging incumbents and prediction markets in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Centrifuge lacks incumbent power, relying on DeFi onboarding. US regulatory push may favor incumbents, but its model challenges prediction markets in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US DeFi-friendly shift supports Centrifuge\'s growth. This tailwind challenges incumbents, potentially obsoleting barriers vs prediction markets in RWAs. (75 words)'},
     'Points': {'value': '47.0: Aggregated score reflecting DeFi potential, ranking Centrifuge mid-tier for RWA tokenization.'}},
    # CME GCUL
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: CME GCUL offers moderate P2P security for RWAs, with audits mitigating risks. US tailwinds aid vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: CME integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: CME\'s MLETR compliance ensures legal finality, leveraging US volumes. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: CME enables T+0 for derivatives, using L1 infrastructure. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: CME\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: CME\'s exchange minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: CME balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: CME offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: CME uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: CME GCUL\'s focused platform increases fragmentation, affecting liquidity. US tailwinds and incumbent volumes strengthen vs EU, resisting prediction market disruption in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: CME GCUL\'s permissioned L1 with enterprise security minimizes risks. US tailwinds and incumbent volumes strengthen defenses, supported by audits. Prediction markets like Kalshi face barriers, allowing CME to reduce vulnerability and maintain leadership in derivatives against manipulation attempts. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: CME GCUL\'s CFTC alignment adapts to US pro-tech, enhancing global standards. Incumbent tailwinds dominate vs prediction markets, ensuring flexibility for RWA without added failure points. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: CME\'s permissioned model limits long-term DeFi protocols. US tailwinds aid, but prediction markets challenge RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: CME\'s futures volumes enable rapid derivative onboarding. US tailwinds and financial power strengthen vs EU, resisting prediction market disruption. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US regulatory tailwinds boost CME\'s derivative focus. This strengthens incumbent power vs EU and prediction markets in RWA scalability. (75 words)'},
     'Points': {'value': '46.0: Aggregated score reflecting strong derivative focus, ranking CME mid-tier for RWA tokenization.'}},
    # Nasdaq Tokenized Securities
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Nasdaq offers moderate P2P security for RWAs, with audits mitigating risks. US tailwinds aid vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Nasdaq integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Nasdaq\'s MLETR compliance ensures legal finality, leveraging US volumes. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Nasdaq enables T+0 for securities, using proposed platform. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Nasdaq\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Nasdaq\'s exchange minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Nasdaq balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Nasdaq offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Nasdaq uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Nasdaq\'s integrated system reduces fragmentation, enhancing liquidity. US pro-tech competes globally, strengthening vs prediction markets in RWA adaptability. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Nasdaq\'s proposed platform with enterprise security minimizes manipulation risks for securities. US pro-tech enhances defenses. Prediction markets like Kalshi compete, but Nasdaq\'s audits reduce vulnerability in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Nasdaq\'s UCC compliance adapts to US pro-tech, competing globally. Tailwinds enhance vs prediction markets, ensuring adaptability for RWA scaling with minimal complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Nasdaq\'s regulated model limits long-term DeFi protocols. US pro-tech supports, but prediction markets hinder open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: Nasdaq\'s securities infrastructure aids onboarding. US pro-tech and incumbent power compete with Singapore/China, resisting prediction market innovation. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US pro-tech enhances Nasdaq\'s securities leadership. This tailwind competes with Singapore/China, resisting prediction market innovation in RWAs. (75 words)'},
     'Points': {'value': '48.0: Aggregated score reflecting strong market position, ranking Nasdaq mid-tier for RWA tokenization.'}},
    # B3 Digitas/ACXRWA
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: B3 offers moderate P2P security for RWAs, with audits mitigating risks. Brazil lags US tailwinds, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: B3 integrates basic DIDs for KYC, enhancing RWA trust. Brazil supports, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: B3\'s MLETR compliance ensures legal finality, leveraging regional volumes. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: B3 enables T+0 for carbon RWAs, but lacks speed. Brazil competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: B3\'s regional focus limits cross-border T+0, but tailwinds aid. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: B3\'s exchange minimizes TradFi friction, reducing costs. Brazil\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: B3 balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: B3 offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: B3 uses oracles, increasing risks in RWAs. Brazil competes with US pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: B3\'s regional focus increases fragmentation, limiting liquidity. Brazil lags US tailwinds, weakening vs incumbents and prediction markets in the global RWA race. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: B3\'s regional platform faces moderate risks due to limited security upgrades. Brazil lags US tailwinds, increasing vulnerability. Prediction markets pose threats, but audits mitigate susceptibility vs incumbents. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: B3\'s alignment adapts to Brazil standards, but lags US pro-tech. This limits vs incumbents and prediction markets, with regulatory headwinds increasing RWA complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: B3\'s centralized model limits long-term DeFi protocols. Brazil lags US, with prediction markets challenging RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: B3\'s regional volumes aid carbon RWA onboarding. Brazil lags US tailwinds, limiting vs global incumbents and prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: Brazil\'s regulations lag US tailwinds, limiting B3\'s edge. This balances vs incumbents and prediction markets in regional RWA adoption. (75 words)'},
     'Points': {'value': '42.0: Aggregated score reflecting regional constraints, ranking B3 lower-tier for RWA tokenization.'}},
    # Polymesh
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Polymesh offers moderate P2P security for RWAs, with audits mitigating risks. Swiss catalyst aids vs US, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Polymesh integrates W3C-compliant DIDs for KYC, enhancing RWA trust. Swiss support aids vs US tailwinds, outpacing prediction markets. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Polymesh\'s MLETR compliance ensures legal finality, leveraging Swiss framework. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Polymesh enables T+0 for securities, but lacks speed. Swiss catalyst competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Polymesh\'s Swiss focus limits cross-border T+0, but tailwinds aid. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Polymesh\'s regulated focus minimizes TradFi friction, reducing costs. Swiss stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Polymesh balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Polymesh ensures privacy with PoS, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: Polymesh avoids oracles, minimizing risks in RWAs. Swiss design competes with US pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Polymesh\'s regulated focus increases fragmentation, affecting liquidity. As prediction markets gain approvals, Polymesh adapts to US innovations, balancing vs incumbents. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Polymesh\'s permissioned PoS with privacy-by-design minimizes hacking risks for securities. Swiss catalyst aids defenses. Prediction markets like Kalshi challenge, but Polymesh\'s audits reduce susceptibility, balancing vs US incumbents. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Polymesh\'s compliance adapts to global standards, but slower than US pro-tech. This balances vs prediction markets, but regulatory focus may add failure points in RWA scaling. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Polymesh\'s regulated model limits long-term DeFi protocols. Swiss catalyst aids, but prediction markets hinder open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Polymesh\'s regulated focus aids securities, but lacks volumes. Swiss catalyst aids, but US push favors incumbents over prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: Swiss catalyst aids Polymesh, but US push favors incumbents. This tailwind supports vs prediction markets in securities-focused RWAs. (75 words)'},
     'Points': {'value': '46.0: Aggregated score reflecting solid regulatory focus, ranking Polymesh mid-tier for RWA tokenization.'}},
    # Realio Network
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Realio offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Realio integrates basic DIDs for KYC, enhancing RWA trust. US tailwinds support, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Realio\'s MLETR compliance ensures legal finality, leveraging DeFi. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Realio enables T+0 for RWAs, but lacks speed. US pro-tech competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Realio\'s cross-chain supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Realio\'s DeFi focus increases TradFi friction, raising costs. US tailwinds aid, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Realio balances DeFi with control, optimizing RWA security. US support aids vs incumbents, outpacing prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Realio offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Realio uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Realio\'s cross-chain model increases fragmentation, limiting liquidity. US pro-tech push integrates with incumbents, challenging prediction markets in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Realio\'s Cosmos-based L1 faces moderate risks from cross-chain exposure. US pro-tech boosts defenses, but prediction markets like Kalshi add pressure. Audits mitigate susceptibility in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Realio\'s MLETR compliance adapts to US pro-tech, enhancing DeFi standards. This challenges incumbents, but cross-chain complexity may introduce failure points vs prediction markets. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Realio\'s cross-chain supports long-term open DeFi protocols. US pro-tech enhances, challenging incumbents and prediction markets in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Realio lacks incumbent power, focusing on DeFi onboarding. US tailwinds boost incumbents, but its model may challenge prediction markets in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US DeFi shift boosts Realio\'s cross-chain focus. This tailwind challenges incumbents, disrupting traditional barriers vs prediction markets. (75 words)'},
     'Points': {'value': '47.0: Aggregated score reflecting DeFi potential, ranking Realio mid-tier for RWA tokenization.'}},
    # TSE/JPX Digital Securities
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: TSE/JPX offers moderate P2P security for RWAs, with audits mitigating risks. Japan lags US tailwinds, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: TSE/JPX integrates basic DIDs for KYC, enhancing RWA trust. Japan supports, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: TSE/JPX\'s MLETR compliance ensures legal finality, leveraging Japan volumes. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: TSE/JPX enables T+0 for securities, but lacks speed. Japan competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: TSE/JPX\'s regional focus limits cross-border T+0, but tailwinds aid. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: TSE/JPX\'s exchange minimizes TradFi friction, reducing costs. Japan\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Low: TSE/JPX relies on centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: TSE/JPX offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: TSE/JPX uses oracles, increasing risks in RWAs. Japan competes with US pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: TSE/JPX\'s regional focus increases fragmentation, affecting liquidity. Japan competes with US tailwinds, but incumbent power lags vs prediction markets in RWA innovation. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: TSE/JPX\'s regulated platform with enterprise security minimizes risks for securities. Japan competes with US, but lags in pro-tech upgrades. Prediction markets challenge innovation, yet TSE/JPX\'s security focus reduces susceptibility in regional RWA markets. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: TSE/JPX\'s alignment adapts to Japan standards, but lags US pro-tech. This limits flexibility vs prediction markets, with regulatory headwinds increasing RWA complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Low: TSE/JPX\'s centralized model limits long-term DeFi protocols. Japan lags US tailwinds, with prediction markets challenging RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: TSE/JPX\'s infrastructure aids securities onboarding. Japan competes with US, but incumbent power lags vs prediction markets in RWA innovation. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: Japan\'s regulations compete with US, but lag in pro-tech. This tailwind aids vs EU in regional RWA adoption, lagging prediction markets. (75 words)'},
     'Points': {'value': '39.5: Aggregated score reflecting regional limitations, ranking TSE/JPX lower-tier for RWA tokenization.'}},
    # DTCC Collateral Pilot
    {'Encrypted P2P Communication (High Impact)': {'value': 'Low: DTCC\'s DLT offers limited P2P security for RWAs, with audits mitigating risks. US tailwinds aid vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: DTCC integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: DTCC\'s MLETR compliance ensures legal finality, leveraging US volumes. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: DTCC enables T+0 for collateral, but lacks speed. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Low: DTCC\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: DTCC\'s clearing minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Low: DTCC relies on centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: DTCC ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: DTCC avoids oracles, minimizing risks in RWAs. US design competes with EU pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: DTCC\'s niche focus increases fragmentation, limiting liquidity. US tailwinds boost incumbent advantages, outpacing EU/UK and prediction markets in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: DTCC\'s permissioned DLT minimizes manipulation risks for collateral. US tailwinds enhance incumbent advantages, supported by audits. Prediction markets face barriers, allowing DTCC to maintain stability and outpace manipulation threats in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: DTCC\'s UCC compliance adapts to US pro-tech, enhancing global standards. Tailwinds boost incumbent advantages vs prediction markets, ensuring flexibility without added complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Low: DTCC\'s centralized model limits long-term DeFi protocols. US tailwinds aid, but prediction markets hinder open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: DTCC\'s clearing volumes enable swift collateral onboarding. US tailwinds enhance incumbent advantages, outpacing EU/UK and prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US tailwinds enhance DTCC\'s clearing innovation. This strengthens incumbent advantages vs global competitors and prediction markets in RWAs. (75 words)'},
     'Points': {'value': '39.5: Aggregated score reflecting strong clearing focus, ranking DTCC lower-tier for RWA tokenization.'}},
    # SWIFT Blockchain
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: SWIFT\'s blockchain offers moderate P2P security for RWAs, with audits mitigating risks. Global reach aids vs US, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: SWIFT integrates basic DIDs for KYC, enhancing RWA trust. Global support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: SWIFT\'s partial MLETR alignment ensures legal finality, leveraging bank focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: SWIFT enables T+0 for payments, but lacks speed. Global reach competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: SWIFT\'s global network supports cross-border T+0, leveraging bank hub. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: SWIFT\'s bank focus minimizes TradFi friction, reducing costs. Global reach edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Low: SWIFT relies on centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: SWIFT offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: SWIFT uses oracles, increasing risks in RWAs. Global design competes with US pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: SWIFT\'s bank focus increases fragmentation, affecting liquidity. Global competition with US pro-tech balances vs prediction markets in RWA payments. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: SWIFT\'s Linea-integrated blockchain faces moderate risks from Ethereum exposure. Global competition balances vs prediction markets. Audits mitigate susceptibility, but centralized focus increases vulnerability. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: SWIFT\'s alignment adapts to bank standards, but lags for RWAs. Global competition with US pro-tech balances vs prediction markets, but adds regulatory complexity. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Low: SWIFT\'s bank model limits long-term DeFi protocols. Global balances vs prediction markets in RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: SWIFT\'s bank network aids payment onboarding. Global reach competes with US incumbents, but centralized focus limits vs prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US/global bank focus aids SWIFT, competing with EU. This tailwind balances vs prediction markets in payment-focused RWAs. (75 words)'},
     'Points': {'value': '39.5: Aggregated score reflecting strong bank integration, ranking SWIFT lower-tier for RWA tokenization.'}},
    # Ripple (XRP Ledger)
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Ripple offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Low: Ripple lacks robust DIDs for KYC, limiting RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: Ripple\'s partial MLETR alignment ensures legal finality, leveraging payment focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Ripple enables T+0 for payments, but lacks speed. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Ripple\'s global ledger supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Ripple\'s payment focus minimizes TradFi friction, reducing costs. US tailwinds edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Ripple balances federated control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Low: Ripple offers limited privacy, exposing some RWA flows. This challenges US tailwinds, with prediction markets revealing gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Ripple uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Ripple\'s network increases fragmentation, limiting liquidity. US regulatory shift boosts vs EU, challenging incumbent barriers and prediction markets in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Ripple\'s federated ledger faces moderate risks from validator manipulation. Audits mitigate, but decentralized exposure persists. US regulatory shift boosts vs EU, challenging incumbent barriers and prediction markets with partial vulnerability to hacking. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Ripple\'s compliance adapts to payment standards, but scrutiny limits for RWAs. US shift boosts vs EU, but prediction markets add complexity in RWA evolution. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Ripple\'s federated supports long-term open DeFi protocols. US shift enhances, challenging incumbents and prediction markets in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Ripple lacks exchange volumes but aids payment onboarding. US shift boosts vs EU, challenging incumbent barriers and prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: US regulatory shift aids Ripple, but scrutiny limits. This tailwind boosts vs EU, challenging incumbent barriers and prediction markets. (75 words)'},
     'Points': {'value': '41.0: Aggregated score reflecting payment focus, ranking Ripple lower-tier for RWA tokenization.'}},
    # LME Modernization
    {'Encrypted P2P Communication (High Impact)': {'value': 'Low: LME\'s legacy offers limited P2P security for RWAs, with audits mitigating risks. UK lags US tailwinds, but prediction markets challenge. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Low: LME lacks robust DIDs for KYC, limiting RWA trust. UK support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: LME\'s partial MLETR alignment ensures legal finality, leveraging metals focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Low: LME\'s legacy limits T+0 for metals, lacking speed. UK competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: LME\'s regional focus limits cross-border T+0, but tailwinds aid. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: LME\'s exchange minimizes TradFi friction, reducing costs. UK\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Low: LME relies on centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: LME offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'High: LME avoids oracles, minimizing risks in RWAs. UK design competes with US pro-tech, outpacing prediction markets. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'High: LME\'s legacy system heightens fragmentation, reducing liquidity. UK trails US tailwinds, weakening vs prediction markets like Polymarket in RWA innovation. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: LME\'s legacy system with robust controls minimizes risks for metals. UK trails US tailwinds, but audits reduce susceptibility. Prediction markets like Polymarket threaten, but LME\'s focus aids resilience. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Low: LME\'s legacy alignment limits adaptability to RWA standards. UK trails US pro-tech, weakening vs prediction markets, with headwinds increasing manipulation risks. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Low: LME\'s legacy limits long-term DeFi protocols. UK trails US tailwinds, with prediction markets challenging RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: LME\'s metals volumes aid onboarding. UK competes with US tailwinds, but legacy focus lags vs prediction markets in RWA innovation. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: UK regulations lag US tailwinds, limiting LME\'s edge. This balances vs EU in metals-focused RWAs, lagging prediction markets. (75 words)'},
     'Points': {'value': '34.0: Aggregated score reflecting legacy constraints, ranking LME lower-tier for RWA tokenization.'}},
    # Solana
    {'Encrypted P2P Communication (High Impact)': {'value': 'Low: Solana\'s public blockchain offers limited P2P security for RWAs, with audits mitigating risks. US pro-tech aids, but prediction markets align with exposure. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Solana integrates basic DIDs for KYC, enhancing RWA trust. US tailwinds support, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: Solana\'s partial alignment ensures legal finality, leveraging DeFi. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Solana enables T+0 for RWAs, using high throughput. US shift competes with EU tailwinds, aligning with prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Solana\'s global reach supports cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Solana\'s DeFi focus increases TradFi friction, raising costs. US tailwinds aid, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Solana balances decentralization, limiting TradFi control. This aids vs US incumbents, aligning with prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Solana offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Low: Solana relies on bridges, increasing risks in RWAs. US pro-tech competes with EU, but prediction markets align with exposure. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Solana\'s ecosystem increases fragmentation, affecting liquidity. US pro-tech boosts adoption, but prediction markets challenge incumbent barriers in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'High: Solana\'s public blockchain faces high risks from DeFi exposure and bridges. US pro-tech may adapt, but prediction markets align, increasing susceptibility to manipulation in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Solana\'s DeFi alignment adapts to standards, but adds oracle complexity. US pro-tech challenges incumbents, with prediction markets aligning but increasing failure points. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Solana\'s upgrades support long-term open DeFi protocols. US pro-tech enhances, challenging incumbents and aligning with prediction markets. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Low: Solana lacks incumbent power, relying on DeFi adoption. US pro-tech boosts vs EU, but lags vs prediction markets in RWA leadership. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: US pro-tech supports Solana\'s DeFi growth, but regulatory gaps persist. This tailwind challenges EU, aligning with prediction markets in RWAs. (75 words)'},
     'Points': {'value': '39.5: Aggregated score reflecting DeFi potential with risks, ranking Solana lower-tier for RWA tokenization.'}},
    # Ethereum
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Ethereum offers moderate P2P security for RWAs, with audits mitigating risks. US tailwinds aid, but prediction markets align with exposure. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Ethereum integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: Ethereum\'s partial alignment ensures legal finality, leveraging DeFi. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Ethereum enables T+0 for RWAs via L2s, but lacks speed. US shift competes with EU tailwinds, aligning with prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Ethereum\'s global reach supports cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Ethereum\'s DeFi focus increases TradFi friction, raising costs. US tailwinds aid, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Ethereum balances decentralization, limiting TradFi control. This aids vs US incumbents, aligning with prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Ethereum offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Low: Ethereum relies on oracles/L2s, increasing risks in RWAs. US pro-tech competes with EU, but prediction markets align with exposure. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Ethereum\'s ecosystem increases fragmentation, affecting liquidity. US tailwinds force incumbent adaptation, with prediction markets adding pressure in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'High: Ethereum\'s DeFi ecosystem faces high risks from oracle and L2 exposure. US tailwinds force adaptation, with prediction markets adding pressure, heightening susceptibility in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Medium: Ethereum\'s upgrades adapt to standards, but multi-chain complexity adds failure points. US tailwinds force incumbent changes, with prediction markets challenging in RWAs. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Ethereum\'s ecosystem supports long-term open DeFi protocols. US tailwinds force adaptation, with prediction markets adding pressure in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Low: Ethereum lacks incumbent power, relying on DeFi adoption. US tailwinds boost vs EU, but lags vs prediction markets in RWA leadership. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: US pro-tech supports Ethereum\'s DeFi growth, but gaps persist. This tailwind challenges EU, aligning with prediction markets in RWAs. (75 words)'},
     'Points': {'value': '39.5: Aggregated score reflecting DeFi dominance with risks, ranking Ethereum lower-tier for RWA tokenization.'}},
    # SHFE Initiatives
    {'Encrypted P2P Communication (High Impact)': {'value': 'Low: SHFE\'s legacy offers limited P2P security for RWAs, with audits mitigating risks. China competes with US, but lags in pro-tech. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Low: SHFE lacks robust DIDs for KYC, limiting RWA trust. China supports, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: SHFE\'s partial MLETR alignment ensures legal finality, leveraging commodities focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Low: SHFE\'s legacy limits T+0 for commodities, lacking speed. China competes with US tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: SHFE\'s regional focus limits cross-border T+0, but tailwinds aid. This challenges US incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: SHFE\'s exchange minimizes TradFi friction, reducing costs. China\'s stance edges out US tailwinds, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Low: SHFE relies on centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Low: SHFE offers limited privacy, exposing some RWA flows. This challenges US tailwinds, with prediction markets revealing gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: SHFE uses oracles, increasing risks in RWAs. China competes with US pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: SHFE\'s regional focus increases fragmentation, affecting liquidity. China competes with US tailwinds, but incumbent power lags vs prediction markets. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: SHFE\'s legacy system minimizes risks with controls. China competes with US, but lacks tailwinds. Prediction markets pose threats, but SHFE\'s focus reduces susceptibility in commodities. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Low: SHFE\'s legacy alignment limits RWA adaptability. China competes with US, but lacks pro-tech, with headwinds increasing complexity vs prediction markets. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Low: SHFE\'s centralized limits long-term DeFi protocols. China lags US tailwinds, with prediction markets challenging RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: SHFE\'s commodity volumes aid onboarding. China competes with US, but incumbent power lags vs prediction markets in RWA innovation. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'Medium: China\'s regulations compete with US, but lag in pro-tech. This tailwind aids vs EU in commodities, lagging prediction markets. (75 words)'},
     'Points': {'value': '32.5: Aggregated score reflecting legacy constraints, ranking SHFE lower-tier for RWA tokenization.'}},
    # Kalshi
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Kalshi offers moderate P2P security for RWAs, with audits mitigating risks. US CFTC approvals aid vs EU, resisting prediction market disruption. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Kalshi integrates W3C-compliant DIDs for KYC, enhancing RWA trust. US support aids, outpacing prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Kalshi\'s CFTC alignment ensures legal finality, leveraging US framework. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Kalshi enables T+0 for prediction RWAs, using smart contracts. US shift competes with EU tailwinds, resisting market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Kalshi\'s US focus supports cross-border T+0, leveraging regulatory hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Kalshi\'s regulated focus minimizes TradFi friction, reducing costs. US approvals edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Kalshi balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Kalshi ensures privacy with encryption, protecting RWA flows. This challenges US tailwinds, resisting prediction market transparency. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Kalshi uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Kalshi\'s unified platform reduces fragmentation, enhancing liquidity. US CFTC approvals strengthen vs EU, challenging incumbent barriers and prediction market peers in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Low: Kalshi\'s regulated platform minimizes risks with enterprise security. US CFTC approvals enhance defenses, ensuring trust in prediction RWAs. As a prediction market, it challenges incumbents with low susceptibility to manipulation. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Kalshi\'s CFTC alignment adapts to standards, minimizing complexity. US approvals provide tailwinds, disrupting incumbents without added failure points in prediction RWAs. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: Kalshi\'s regulated limits long-term DeFi protocols. US approvals enhance, but prediction focus constrains open RWA scalability. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Low: Kalshi lacks incumbent power, relying on prediction market growth. US approvals aid vs EU, challenging incumbent barriers in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US CFTC approvals boost Kalshi\'s prediction focus. This tailwind challenges incumbents, disrupting traditional barriers in RWAs. (75 words)'},
     'Points': {'value': '48.0: Aggregated score reflecting regulatory strength, ranking Kalshi mid-tier for RWA tokenization.'}},
    # Polymarket
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Polymarket offers moderate P2P security for RWAs, with audits mitigating risks. US relaunch aids vs EU, resisting prediction market disruption. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Polymarket integrates W3C-compliant DIDs for KYC, enhancing RWA trust. US support aids, outpacing prediction market peers in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Polymarket\'s relaunch ensures legal finality, leveraging US framework. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Polymarket enables T+0 for prediction RWAs, using smart contracts. US shift competes with EU tailwinds, resisting market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Polymarket\'s US base supports cross-border T+0, leveraging regulatory hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Polymarket\'s DeFi focus increases TradFi friction, raising costs. US relaunch aids, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Polymarket balances decentralization, optimizing RWA security. US support aids vs incumbents, outpacing prediction market peers. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Polymarket offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Polymarket uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Polymarket\'s unified platform reduces fragmentation, enhancing liquidity. US relaunch strengthens vs EU, challenging incumbent barriers in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Polymarket\'s decentralized platform faces moderate risks from on-chain exposure. US relaunch boosts defenses, but DeFi focus increases susceptibility vs incumbents. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Polymarket\'s relaunch adapts to standards, but DeFi complexity adds failure points. US shift enhances vs EU, challenging incumbents in RWA innovation. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Polymarket\'s decentralized supports long-term open DeFi protocols. US relaunch boosts, challenging incumbents with prediction RWA innovation. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Low: Polymarket lacks incumbent power, relying on prediction market growth. US relaunch aids vs EU, challenging incumbent barriers in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US relaunch boosts Polymarket\'s prediction focus. This tailwind challenges incumbents, disrupting traditional barriers in RWAs. (75 words)'},
     'Points': {'value': '49.0: Aggregated score reflecting DeFi potential, ranking Polymarket mid-tier for RWA tokenization.'}},
    # Crypto.com
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Crypto.com offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, resisting prediction market disruption. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Crypto.com integrates W3C-compliant DIDs for KYC, enhancing RWA trust. US support aids, outpacing prediction market peers in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Crypto.com\'s CFTC alignment ensures legal finality, leveraging US framework. This challenges EU incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'High: Crypto.com enables T+0 for prediction RWAs, using smart contracts. US shift competes with EU tailwinds, resisting market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Crypto.com\'s global reach supports cross-border T+0, leveraging US hub. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Crypto.com\'s exchange focus increases TradFi friction, raising costs. US shift aids, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Crypto.com balances hybrid control with DeFi, optimizing RWA security. US support aids vs incumbents, outpacing prediction market peers. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Crypto.com offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Crypto.com uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Low: Crypto.com\'s exchange reduces fragmentation, enhancing liquidity. US CFTC approvals strengthen vs EU, challenging incumbent barriers in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Crypto.com\'s exchange faces moderate risks from integrations. US shift enhances defenses, but as a prediction market, it challenges incumbents with partial susceptibility to manipulation. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Crypto.com\'s CFTC alignment adapts to standards, minimizing complexity. US tailwinds enhance vs EU, disrupting incumbents in prediction-driven RWAs. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Crypto.com\'s hybrid supports long-term open DeFi protocols. US shift enhances, disrupting incumbents with prediction-driven RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Crypto.com\'s exchange aids onboarding, but lacks volumes. US shift boosts vs EU, challenging incumbent barriers in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US CFTC approvals boost Crypto.com\'s exchange growth. This tailwind challenges incumbents, disrupting traditional barriers in RWAs. (75 words)'},
     'Points': {'value': '47.0: Aggregated score reflecting hybrid strength, ranking Crypto.com mid-tier for RWA tokenization.'}},
    # RobinHood
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: RobinHood offers moderate P2P security for RWAs, with audits mitigating risks. US approvals aid vs EU, resisting prediction market disruption. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: RobinHood integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction markets in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: RobinHood\'s partial alignment ensures legal finality, leveraging retail focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: RobinHood enables T+0 for retail RWAs, but lacks speed. US shift competes with EU tailwinds, resisting prediction markets. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: RobinHood\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: RobinHood\'s retail focus minimizes TradFi friction, reducing costs. US approvals edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: RobinHood balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: RobinHood offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: RobinHood uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: RobinHood\'s retail focus increases fragmentation, affecting liquidity. US approvals enhance vs EU, leveraging tailwinds against prediction markets in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: RobinHood\'s platform faces moderate risks from retail exposure. US approvals aid defenses, but limited DeFi increases susceptibility, challenging prediction markets in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: RobinHood\'s approvals adapt to standards, but limited DeFi adds complexity. US tailwinds leverage user base, challenging prediction markets in RWAs. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: RobinHood\'s retail limits long-term DeFi protocols. US approvals aid, but lags prediction market peers in RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'High: RobinHood\'s user base aids retail RWA onboarding. US approvals enhance vs EU, leveraging tailwinds against prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US approvals boost RobinHood\'s retail growth. This tailwind challenges incumbents, disrupting traditional barriers in RWAs. (75 words)'},
     'Points': {'value': '46.0: Aggregated score reflecting retail strength, ranking RobinHood mid-tier for RWA tokenization.'}},
    # PredictIt
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: PredictIt offers moderate P2P security for RWAs, with audits mitigating risks. US approvals aid vs EU, resisting prediction market disruption. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: PredictIt integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction market peers in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: PredictIt\'s partial alignment ensures legal finality, leveraging prediction focus. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: PredictIt enables T+0 for prediction RWAs, but lacks speed. US shift competes with EU tailwinds, resisting market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: PredictIt\'s US focus limits cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: PredictIt\'s regulated focus minimizes TradFi friction, reducing costs. US approvals edge out EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: PredictIt balances centralized control, limiting DeFi flexibility. This aids vs US incumbents, but prediction markets challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: PredictIt offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: PredictIt uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, but prediction markets challenge. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: PredictIt\'s niche focus increases fragmentation, affecting liquidity. US approvals enhance vs EU, leveraging tailwinds against prediction market peers in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: PredictIt\'s regulated platform faces moderate risks from focus. US approvals enhance defenses, but scope limits susceptibility, challenging incumbents in prediction RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: PredictIt\'s alignment adapts to standards, minimizing complexity. US approvals enhance, but scope limits vs incumbents in RWA scalability. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Medium: PredictIt\'s focused limits long-term DeFi protocols. US approvals enhance, but scope constrains vs incumbent RWAs. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: PredictIt\'s niche aids prediction onboarding, but lacks volumes. US approvals enhance vs EU, leveraging tailwinds against prediction markets. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US approvals boost PredictIt\'s prediction focus. This tailwind challenges incumbents, disrupting traditional barriers in RWAs. (75 words)'},
     'Points': {'value': '45.0: Aggregated score reflecting niche strength, ranking PredictIt mid-tier for RWA tokenization.'}},
    # Augur
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Augur offers moderate P2P security for RWAs, with audits mitigating risks. US shift aids vs EU, aligning with prediction market exposure. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Medium: Augur integrates basic DIDs for KYC, enhancing RWA trust. US support aids, but lags vs prediction market peers in compliance. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Medium: Augur\'s partial alignment ensures legal finality, leveraging DeFi. This challenges US incumbents, with prediction markets adding pressure. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Augur enables T+0 for prediction RWAs, but lacks speed. US shift competes with EU tailwinds, aligning with market disruptions. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Medium: Augur\'s global reach supports cross-border T+0, but tailwinds aid. This challenges EU incumbents, with prediction markets competing. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Medium: Augur\'s DeFi focus increases TradFi friction, raising costs. US shift aids, but prediction market complexity persists. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'High: Augur balances decentralization, optimizing RWA security. US support aids vs incumbents, aligning with prediction markets. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Medium: Augur offers moderate privacy, protecting some RWA flows. This challenges US tailwinds, but prediction markets expose gaps. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Augur uses oracles, increasing risks in RWAs. US design competes with EU pro-tech, aligning with prediction market exposure. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Augur\'s DeFi focus increases fragmentation, affecting liquidity. US shift enhances vs EU, challenging incumbent barriers with prediction markets in RWAs. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'High: Augur\'s DeFi platform faces high risks from decentralized exposure. US shift boosts defenses, but high susceptibility challenges incumbents in prediction RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Augur\'s DeFi alignment adapts to standards, but decentralization adds failure points. US shift boosts vs incumbents in prediction RWAs. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Augur\'s DeFi supports long-term open protocols. US shift enhances, challenging incumbents with prediction market trends. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Low: Augur lacks incumbent power, relying on DeFi adoption. US shift boosts vs EU, challenging incumbent barriers in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US DeFi shift supports Augur\'s growth. This tailwind challenges incumbents, aligning with prediction markets in RWAs. (75 words)'},
     'Points': {'value': '44.0: Aggregated score reflecting DeFi potential with risks, ranking Augur lower-tier for RWA tokenization.'}},
    # Provenance Foundation
    {'Encrypted P2P Communication (High Impact)': {'value': 'Medium: Provenance\'s blockchain offers encrypted P2P for RWAs, but lacks Abaxx\'s 5-layer depth. US-based with tailwinds, it competes with incumbents, though prediction markets like Kalshi may outpace in innovation. (75 words)'},
     'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'High: Provenance\'s W3C-compliant DIDs ensure robust identity for RWAs, leveraging US standards. This challenges EU incumbents, with prediction markets adding pressure for compliance scalability. (75 words)'},
     'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'High: Provenance\'s MLETR alignment ensures legal finality for RWAs, competing with US pro-tech. This supports adoption vs prediction markets, enhancing institutional trust. (75 words)'},
     'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Medium: Provenance enables T+0 with smart contracts, but lacks Abaxx\'s speed. US tailwinds aid vs EU, though prediction markets like Kalshi challenge in RWAs. (75 words)'},
     'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'High: Provenance\'s cross-chain design supports T+0, leveraging US interoperability. This challenges incumbents, with prediction markets adding competitive pressure in RWAs. (75 words)'},
     'TradFi Integration Friction/Cost (High Impact)': {'value': 'Low: Provenance\'s enterprise focus minimizes TradFi friction, reducing costs for RWAs. US tailwinds enhance vs EU, resisting prediction market complexity. (75 words)'},
     'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Medium: Provenance balances centralized governance with DeFi, optimizing RWA security. US support aids vs incumbents, though prediction markets like Polymarket challenge. (75 words)'},
     'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'High: Provenance\'s privacy layer protects RWA flows, competing with US pro-tech. This resists prediction market transparency, enhancing adoption. (75 words)'},
     'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Medium: Provenance reduces oracle risks with on-chain data, but bridges add exposure. US tailwinds aid vs incumbents, though prediction markets pose challenges. (75 words)'},
     'Liquidity Fragmentation Risk (High Impact)': {'value': 'Medium: Provenance\'s multi-chain approach increases fragmentation, affecting liquidity. US tailwinds boost vs EU, but prediction markets like Kalshi challenge in RWA adoption. (75 words)'},
     'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Medium: Provenance\'s public blockchain faces moderate risks from exposure, mitigated by audits. US tailwinds enhance defenses vs incumbents, but prediction markets like Kalshi add pressure, increasing vulnerability in RWAs. (75 words)'},
     'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'High: Provenance\'s US-based compliance adapts to standards like UCC and MiCAR, minimizing complexity. Tailwinds enhance vs EU, challenging incumbents with prediction market-driven innovation. (75 words)'},
     'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'High: Provenance\'s DeFi focus supports long-term open protocols for RWAs. US shift enhances adoption, challenging incumbents and aligning with prediction markets like Polymarket. (75 words)'},
     'Incumbent Advantages (High Impact)': {'value': 'Medium: Provenance lacks incumbent volumes but gains from US ecosystem ties. This balances new tech with market power, challenging prediction markets in RWAs. (75 words)'},
     'Regulatory Tailwinds (High Impact)': {'value': 'High: US pro-tech regulations boost Provenance\'s RWA growth, competing with EU. This tailwind aids adoption, outpacing prediction markets like Kalshi with institutional support. (75 words)'},
     'Points': {'value': '46.5: Aggregated score reflecting solid performance, ranking Provenance mid-tier for RWA tokenization.'}}
]


# Generate standalone HTML table with embedded hover text
def generate_standalone_html(df, tooltip_data, tooltip_header, color_map, filename='rwa_table.html'):
    # Sort DataFrame by "Points" in descending order
    df_sorted = df.sort_values(by='Points', ascending=False)

    # Reindex tooltip_data to match the sorted DataFrame
    tooltip_data_sorted = [tooltip_data[i] for i in df_sorted.index]

    # Determine the longest header text for height adjustment
    max_header_length = max(len(str(col)) for col in df_sorted.columns)  # Basic length-based estimate
    # Adjust height based on length (e.g., 30px base + 5px per 5 characters beyond 10)
    header_height = max(40, 30 + max(0, (max_header_length - 10)) * 5)

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
                display: block;
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
        <p>Blue: Permissioned Blockchain/Enterprise, Green: Hybrid DeFi/TradFi, Orange: Public Blockchain, Gray: Traditional Exchange</p>
        <table>
            <thead>
                <tr>
    """

    # Add table headers with tooltips
    for col in df_sorted.columns:
        tooltip = tooltip_header.get(col, {}).get('value', '').replace('\n', '<br>')
        html_content += f'<th class="tooltip">{col}<span class="tooltiptext">{tooltip}</span></th>'

    html_content += """
                </tr>
            </thead>
            <tbody>
    """

    # Add table rows with data and tooltips
    for i, row in enumerate(df_sorted.to_dict('records')):
        html_content += '<tr>'
        solution = row['Solution']
        # Determine row font color based on Solution
        row_color = (
            '#FFFF00' if 'Abaxx' in solution else  # Yellow for Abaxx row
            '#1E90FF' if color_map.get(solution) == 'blue' else  # Light blue
            '#90EE90' if color_map.get(solution) == 'green' else  # Light green
            '#FFA07A' if color_map.get(solution) == 'orange' else  # Light salmon
            '#D3D3D3' if color_map.get(solution) == 'gray' else  # Light gray
            '#FFF'  # Default white if no match
        )
        for j, col in enumerate(df_sorted.columns):
            value = row[col]
            tooltip = tooltip_data_sorted[i].get(col, {}).get('value', '').replace('\n', '<br>')
            html_content += f'<td class="tooltip" style="color: {row_color};">{value}<span class="tooltiptext">{tooltip}</span></td>'
        html_content += '</tr>'

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
generate_standalone_html(df, tooltip_data, tooltip_header, color_map)
