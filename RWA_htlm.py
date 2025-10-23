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

#
colors = {
    'Abaxx': '#FFFF00',    # Yellow for Abaxx row
    'Perm_Chain': '#1E90FF',    # Blue: Permissioned Blockchain/Enterprise
    'DeFi_TradFi': '#90EE90',   # Green: Hybrid DeFi/TradFi
    'Pub_Chain': '#FFA07A',     # Orange: Public Blockchain
    'Trad_Exch': '#D3D3D3',     # Gray: Traditional Exchange
    'Pred_Mkt': '#800080',      # Purple for prediction markets
    'White': '#FFF'             # Default white if no match
}

color_map = {
    'Abaxx (ID++/PDT)': colors['Abaxx'],           # Yellow
    'LSE DMI': colors['Perm_Chain'],               # Blue
    'Deutsche Boerse Seturion': colors['Perm_Chain'],  # Blue
    'Ondo Finance': colors['DeFi_TradFi'],         # Green
    'ICE Digital Assets': colors['Perm_Chain'],    # Blue
    'Securitize': colors['DeFi_TradFi'],           # Green
    'NYSE (via ICE)': colors['Perm_Chain'],        # Blue
    'Corda': colors['Perm_Chain'],                 # Blue
    'Centrifuge': colors['DeFi_TradFi'],           # Green
    'CME GCUL': colors['DeFi_TradFi'],             # Green
    'Nasdaq Tokenized Securities': colors['DeFi_TradFi'],  # Green
    'B3 Digitas/ACXRWA': colors['DeFi_TradFi'],    # Green
    'Polymesh': colors['Perm_Chain'],              # Blue
    'Realio Network': colors['DeFi_TradFi'],       # Green
    'TSE/JPX Digital Securities': colors['Trad_Exch'],  # Gray
    'DTCC Collateral Pilot': colors['Perm_Chain'],  # Blue
    'SWIFT Blockchain': colors['Perm_Chain'],       # Blue
    'Ripple (XRP Ledger)': colors['Pub_Chain'],     # Orange
    'LME Modernization': colors['Trad_Exch'],      # Gray
    'Solana': colors['Pub_Chain'],                 # Orange
    'Ethereum': colors['Pub_Chain'],               # Orange
    'SHFE Initiatives': colors['Trad_Exch'],       # Gray
    'Kalshi': colors['Pred_Mkt'],                  # Purple
    'Polymarket': colors['Pred_Mkt'],              # Purple
    'Crypto.com': colors['Pred_Mkt'],              # Purple
    'RobinHood': colors['Pred_Mkt'],               # Purple
    'PredictIt': colors['Pred_Mkt'],               # Purple
    'Augur': colors['Pub_Chain'],                  # Orange (via Ethereum)
    'Provenance Foundation': colors['DeFi_TradFi'] # Green
}

cell_hover_text = {
    'Encrypted P2P Communication (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s ID++ protocol uses a 5-layer cryptographic Messenger/Verifier+ system for secure, encrypted P2P communication, optimized for commodity traders. This guarantees confidentiality and trust, vital for institutional adoption. The design avoids shared ledgers, enhancing security and aligning with wholesale finance requirements for data protection. In a regulatory-competitive landscape, this feature positions Abaxx as a leader in secure RWA trading. (75 words)',
        'LSE DMI': 'High: LSE DMI utilizes Azure’s blockchain messaging for secure, encrypted fund transfers. This ensures confidentiality for institutional investors, meeting regulatory and trust standards. Enterprise-grade encryption aligns with wholesale finance needs, supporting medium-term adoption in EU/UK markets. Amid global regulatory competition, this strengthens LSE’s position against US incumbents. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion’s blockchain-based settlement incorporates encrypted communication for tokenized assets like bonds. This guarantees secure data exchange, essential for institutional trust and EU regulatory compliance. In the context of jurisdictional competition, this feature aids Seturion in maintaining competitiveness against US pro-tech shifts. (75 words)',
        'Ondo Finance': 'Medium: Ondo relies on partner protocols for encrypted DeFi transactions, providing sufficient security for RWA trading but lacking the robustness of enterprise-grade P2P systems. This supports institutional use but may limit scalability in a regulatory-competitive environment. As US incumbents gain tailwinds, Ondo’s hybrid approach could bridge gaps. (75 words)',
        'ICE Digital Assets': 'Medium: ICE employs encrypted Bakkt/Circle integrations for stablecoin P2P communication. While secure for regulated environments, it’s less robust than dedicated blockchain messaging. With US pro-tech regulations, this positions ICE to leverage incumbent advantages for RWA onboarding. (75 words)',
        'Securitize': 'High: Securitize’s issuance platform uses encrypted communication for secure token trading. This ensures confidentiality and compliance, crucial for institutional trust in regulated markets. Amid US regulatory tailwinds, this strengthens Securitize’s position against emerging prediction markets. (75 words)',
        'NYSE (via ICE)': 'Medium: NYSE leverages ICE’s encrypted platforms for tokenized funds. While secure for regulated trading, it lacks the robustness of dedicated P2P systems. US pro-tech push enhances NYSE’s incumbent advantages in onboarding existing assets. (75 words)',
        'Corda': 'High: Corda’s native point-to-point encrypted messaging avoids broadcast ledgers, ensuring secure data exchange for banks. This aligns with institutional trust and compliance, driving medium-term RWA adoption. In global regulatory competition, Corda’s bank focus could integrate with prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge uses multi-chain privacy via Ethereum/Base for encrypted communication. While sufficient for DeFi, it’s less robust than permissioned systems. As US incumbents adapt, Centrifuge’s DeFi orientation may compete with prediction markets like Polymarket. (75 words)',
        'CME GCUL': 'Medium: CME GCUL’s blockchain messaging provides encryption for tokenized derivatives. While secure, it’s less advanced than dedicated P2P systems. US regulatory tailwinds boost CME’s incumbent advantages in futures onboarding. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s proposed blockchain platform includes encrypted communication. While secure for securities, it lacks robustness of mature systems. US pro-tech regulations enhance Nasdaq’s financial power against EU competitors. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3’s digital platform uses encryption for carbon RWAs. While sufficient regionally, it’s less robust than enterprise-grade systems. Brazil’s regulatory environment lags US tailwinds, limiting B3’s global competitiveness. (75 words)',
        'Polymesh': 'Medium: Polymesh’s node-based encryption secures securities trading. While compliant, it’s less advanced than dedicated P2P systems. As prediction markets gain approvals, Polymesh’s regulated focus may adapt to US innovations. (75 words)',
        'Realio Network': 'Medium: Realio’s IBC messaging provides encryption for cross-chain RWAs. While secure for DeFi, it lacks robustness of permissioned systems. US pro-tech push could integrate Realio with incumbent platforms. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned blockchain includes encryption for securities. While secure for Japan, it’s less robust than enterprise systems. Asian jurisdictions compete with US regulatory tailwinds. (75 words)',
        'DTCC Collateral Pilot': 'Low: DTCC’s permissioned DLT offers minimal encryption for collateral pilots. This limits security for broad use. US tailwinds strengthen DTCC’s incumbent advantages in clearing. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s blockchain integrates encrypted Ethereum channels for payments. While secure for banks, it’s less robust than dedicated P2P. Global competition with US pro-tech favors SWIFT’s financial power. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s P2P network provides encryption for payments. While sufficient for cross-border, it lacks robustness for RWAs. US regulatory shift could boost Ripple against prediction markets. (75 words)',
        'LME Modernization': 'Low: LME’s traditional exchange lacks blockchain encryption, relying on legacy security. This limits modern suitability. UK regulations trail US tailwinds, weakening LME against innovators. (75 words)',
        'Solana': 'Low: Solana’s P2P gossip protocol relies on add-on encryption, insufficient for institutional security. This limits trust. DeFi focus could compete with prediction markets under US pro-tech. (75 words)',
        'Ethereum': 'Medium: Ethereum’s ZK-rollups provide encrypted messaging for DeFi. While sufficient, it’s less robust than permissioned. Upgrades position Ethereum to leverage US regulatory tailwinds against incumbents. (75 words)',
        'SHFE Initiatives': 'Low: SHFE’s traditional exchange lacks blockchain encryption, relying on legacy systems. This limits security for RWAs. China’s jurisdiction competes with US pro-tech for global RWA leadership. (75 words)',
        'Kalshi': 'Medium: Kalshi’s CFTC-regulated platform uses encrypted communication for event contracts. While secure, it’s less robust than enterprise systems. US approvals provide tailwinds, but limited DeFi integration constrains vs incumbents. (75 words)',
        'Polymarket': 'Medium: Polymarket’s decentralized platform relies on blockchain encryption for predictions. While secure for DeFi, it lacks robustness for broad RWAs. US relaunch boosts adaptability, challenging incumbents with innovative products. (75 words)',
        'Crypto.com': 'Medium: Crypto.com’s CFTC-regulated exchange uses encrypted communication for event contracts. While secure, it’s less robust than dedicated systems. US tailwinds enhance competitiveness against traditional incumbents. (75 words)',
        'RobinHood': 'Medium: RobinHood’s retail platform uses encrypted communication for event trading. While secure, it’s less robust for RWAs. US approvals leverage user base, but limited DeFi limits long-term scalability. (75 words)',
        'PredictIt': 'Medium: PredictIt’s regulated platform uses encrypted communication for political predictions. While secure, it’s less robust for broad RWAs. US approvals provide tailwinds, but focused scope limits vs incumbents. (75 words)',
        'Augur': 'Medium: Augur’s decentralized blockchain uses encrypted communication for predictions. While secure for DeFi, it lacks robustness for institutional RWAs. US regulatory shift could boost vs incumbents. (75 words)'
    },
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s ID++ offers W3C-compliant decentralized identities for verified credentials in RWA markets. This supports regulatory compliance and interoperability, critical for institutional trust and medium-term RWA adoption across global markets. In the context of regulatory competition, this positions Abaxx to leverage Singapore\'s innovation against US incumbents and prediction markets like Kalshi. (75 words)',
        'LSE DMI': 'High: LSE DMI provides W3C-compliant digital identities for verified credentials in tokenized funds. This aligns with MiCA for EU/UK markets, enhancing trust and medium-term adoption. Amid jurisdictional competition, this strengthens LSE\'s position against US pro-tech shifts and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion integrates W3C-compliant credentials for verified identities in tokenized securities. This supports MiCAR compliance and interoperability, critical for institutional trust in pan-European markets. In global competition, this aids Seturion against US tailwinds and prediction markets. (75 words)',
        'Ondo Finance': 'Medium: Ondo uses partner-based W3C-compliant credentials for verified identities in tokenized Treasuries. This is sufficient for hybrid DeFi/TradFi, but less robust than dedicated systems. US regulatory shift enhances adaptability, challenging incumbents and prediction markets like Kalshi. (75 words)',
        'ICE Digital Assets': 'Medium: ICE provides W3C-compliant credentials for verified identities in tokenized commodities. This is compliant for regulated markets, but less robust. US pro-tech tailwinds leverage incumbent advantages against prediction markets. (75 words)',
        'Securitize': 'High: Securitize\'s DS Protocol offers W3C-compliant credentials for regulated token issuance. This ensures interoperability and compliance, critical for institutional trust and medium-term adoption in securities markets. US tailwinds strengthen against prediction markets. (75 words)',
        'NYSE (via ICE)': 'Medium: NYSE uses W3C-compliant credentials for verified identities in tokenized funds. This is compliant, but less robust. US pro-tech push enhances incumbent advantages against prediction markets. (75 words)',
        'Corda': 'High: Corda’s confidential identities act as W3C-compliant DIDs for banks, ensuring verified credentials. This supports regulatory compliance and interoperability, driving medium-term adoption for private RWA tokenization. Global competition favors integration with prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge uses pool-based credentials for RWAs, partially W3C-compliant. While sufficient for DeFi, it lacks the robust interoperability of dedicated DID systems, limiting institutional trust. US shift may favor vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME GCUL provides institutional identities with W3C potential for derivatives. While compliant, it lacks dedicated DID robustness, sufficient but not optimal for broad institutional adoption. US tailwinds enhance vs prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s proposed platform includes institutional credentials with W3C potential. While compliant, it lacks dedicated DID robustness, sufficient but not optimal for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3 provides credentials for tokenized carbon RWAs, partially W3C-compliant. While sufficient for regional markets, it lacks robust interoperability, limiting global institutional trust. Brazil lags US tailwinds vs prediction markets. (75 words)',
        'Polymesh': 'High: Polymesh’s built-in KYC offers W3C-compliant credentials for securities. This ensures regulatory compliance and interoperability, critical for institutional trust and medium-term adoption in regulated markets. Swiss edge aids vs US prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio’s open-source DIDs for RWA tokenization are partially W3C-compliant. While sufficient for DeFi, they lack the robust interoperability of enterprise systems, limiting institutional appeal. US pro-tech may boost vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned tokens include potential W3C-compliant credentials. While compliant for Japan, they lack robust interoperability, sufficient but not optimal for global institutional use. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Medium: DTCC uses institutional IDs via partners, with partial W3C compliance. While sufficient for collateral, it lacks dedicated DID robustness, limiting broad institutional trust. US tailwinds enhance vs prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s bank network IDs offer potential DID add-ons, partially W3C-compliant. While sufficient for payments, they lack robust interoperability, limiting institutional RWA adoption. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Low: Ripple lacks native W3C-compliant DIDs, relying on external integrations. This limits interoperability and regulatory compliance for institutional RWA trading, unsuitable for broad adoption. US shift may aid vs prediction markets. (75 words)',
        'LME Modernization': 'Low: LME’s traditional exchange lacks a credentials system, with no W3C compliance. This limits its suitability for modern institutional RWA trading, lacking interoperability and trust. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana’s wallet-based DIDs provide verified credentials, partially W3C-compliant. While sufficient for DeFi, they lack the robust interoperability of enterprise systems, limiting institutional trust. US shift may favor vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s ENS/Verite offers W3C-compliant DIDs for DeFi. While sufficient, they lack the robust interoperability of permissioned systems, limiting institutional RWA adoption. US tailwinds may aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Low: SHFE’s traditional exchange lacks DID systems or W3C compliance. This limits its suitability for modern institutional RWA trading, lacking interoperability and trust. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'High: Kalshi’s CFTC-regulated platform offers W3C-compliant credentials for verified identities in event contracts. This supports regulatory compliance and trust, critical for institutional adoption in prediction RWAs. US tailwinds strengthen against prediction peers. (75 words)',
        'Polymarket': 'High: Polymarket’s decentralized platform integrates W3C-compliant DIDs for verified identities in predictions. This ensures compliance and trust, driving medium-term adoption. US relaunch strengthens against incumbents and prediction peers. (75 words)',
        'Crypto.com': 'High: Crypto.com’s CFTC-regulated exchange offers W3C-compliant credentials for verified identities in event contracts. This supports compliance and trust, critical for institutional adoption. US tailwinds strengthen against prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s retail platform offers partial W3C-compliant credentials for verified identities in event trading. While sufficient, it lacks robustness for broad RWAs. US approvals support medium-term adoption. (75 words)',
        'PredictIt': 'Medium: PredictIt’s regulated platform offers partial W3C-compliant credentials for verified identities in political predictions. While compliant, it lacks robustness for global RWAs. US approvals support medium-term adoption. (75 words)',
        'Augur': 'Medium: Augur’s decentralized platform offers W3C-compliant credentials for verified identities in predictions. While sufficient for DeFi, it lacks robustness for institutional RWAs. US regulatory shift supports adoption. (75 words)'
    },
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s PDT embeds MLETR-compliant legal claims for tokenized gold/MMFs, ensuring enforceable ownership. This aligns with Singapore regulations and global sandboxes, critical for institutional trust and medium-term RWA adoption. Amid jurisdictional competition, this positions Abaxx to leverage innovation against US pro-tech shifts and prediction markets. (75 words)',
        'LSE DMI': 'High: LSE DMI ensures MLETR-compliant legal finality for tokenized funds under UK regulations. This provides enforceable ownership, critical for institutional trust and medium-term adoption in EU/UK markets. In global competition, this strengthens LSE against US tailwinds and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion aligns with MiCAR and MLETR-like standards for tokenized bonds, ensuring enforceable ownership. This supports institutional trust and medium-term adoption across pan-European markets. Amid regulatory competition, this aids Seturion against US pro-tech and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo’s UCC/MLETR-compliant legal wrappers for Treasuries ensure enforceable ownership. Partnerships with JPMorgan enhance regulatory alignment, critical for institutional trust and medium-term RWA adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'High: ICE aligns with MLETR for tokenized carbon/commodities, ensuring legal finality. This supports regulated markets, critical for institutional trust and medium-term adoption globally. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'High: Securitize’s regulated tokens align with UCC for legal finality, ensuring enforceable ownership. This supports compliance and institutional trust, critical for medium-term adoption in securities markets. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'High: NYSE aligns with UCC/MLETR for tokenized funds, with SEC talks ensuring legal finality. This supports institutional trust and medium-term adoption in regulated markets. US pro-tech strengthens against prediction markets. (75 words)',
        'Corda': 'High: Corda’s MLETR/ETR-compliant contracts with notaries ensure legal finality for RWAs. This aligns with bank requirements, critical for institutional trust and medium-term adoption. Global competition favors integration with prediction markets. (75 words)',
        'Centrifuge': 'High: Centrifuge’s legal wrappers for credit/assets are MLETR-compliant, ensuring enforceable ownership. This supports regulatory alignment, critical for institutional trust and medium-term RWA adoption. DeFi focus aids vs prediction markets. (75 words)',
        'CME GCUL': 'High: CME GCUL’s tokenized derivatives align with UCC/MLETR, ensuring legal finality. This supports institutional trust and medium-term adoption in regulated derivatives markets. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'High: Nasdaq’s proposed platform aligns with SEC rules and UCC for legal finality. This ensures enforceable ownership, critical for institutional trust and medium-term adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'High: B3 aligns with Brazil’s regulations for tokenized carbon RWAs, with MLETR potential. This ensures legal finality, critical for institutional trust and medium-term adoption regionally. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'High: Polymesh’s regulated securities align with legal finality standards, ensuring enforceable ownership. This supports compliance and institutional trust, critical for medium-term adoption. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'High: Realio’s MLETR-compliant assets for real estate/art ensure enforceable ownership. This aligns with global regulations, critical for institutional trust and medium-term RWA adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'High: TSE/JPX’s tokenized securities are regulated as stocks with legal finality in Japan. This ensures enforceable ownership, critical for institutional trust and medium-term adoption. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'High: DTCC’s tokenized collateral aligns with UCC/MLETR, ensuring legal finality. This supports institutional trust and medium-term adoption in US clearing markets. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s trade finance aligns with MLETR via bank rules, ensuring partial legal finality. This is sufficient for payments but less robust for institutional RWA adoption. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s tokenized assets use validator finality with partial MLETR alignment. This is sufficient for payments but lacks full legal enforceability for institutional RWAs. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Medium: LME aligns with UK regulations for metals but lacks tokenization. This provides partial legal finality, insufficient for modern institutional RWA trading. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana’s fast tokenization uses MLETR via wrappers, providing partial legal finality. This is sufficient for DeFi but lacks robust enforceability for institutional RWAs. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s smart contracts align with MLETR via wrappers and UCC Article 12. This provides partial legal finality, sufficient for DeFi but limited for institutional RWAs. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Medium: SHFE aligns with China’s regulations for commodities, providing partial legal finality. Without tokenization, it’s insufficient for modern institutional RWA trading. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'High: Kalshi’s CFTC-regulated contracts align with MLETR for event RWAs, ensuring legal finality. This supports institutional trust and medium-term adoption. US tailwinds strengthen against prediction peers. (75 words)',
        'Polymarket': 'High: Polymarket’s tokenized predictions align with MLETR, ensuring legal finality. This supports compliance and trust, driving medium-term adoption. US relaunch strengthens against incumbents and prediction peers. (75 words)',
        'Crypto.com': 'High: Crypto.com’s CFTC-regulated contracts align with MLETR for event RWAs, ensuring legal finality. This supports compliance and trust, critical for institutional adoption. US tailwinds strengthen against prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s regulated contracts provide partial MLETR alignment for event RWAs, ensuring legal finality. This is sufficient, but lacks robustness for broad RWAs. US approvals support medium-term adoption. (75 words)',
        'PredictIt': 'Medium: PredictIt’s regulated contracts provide partial MLETR alignment for political RWAs, ensuring legal finality. This is compliant, but lacks robustness for global RWAs. US approvals support medium-term adoption. (75 words)',
        'Augur': 'Medium: Augur’s decentralized contracts provide partial MLETR alignment for prediction RWAs, ensuring legal finality. This is sufficient for DeFi, but lacks robustness for institutional RWAs. US regulatory shift supports adoption. (75 words)'
    },
    'Private RWA Trading with T+0 Settlement (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s Q4 2025 pilots with MineHub enable atomic T+0 settlement for gold/MMFs. This reduces counterparty risk and enhances efficiency, critical for institutional adoption and medium-term competitiveness in commodity markets. In jurisdictional competition, this positions Abaxx against US incumbents and prediction markets like Kalshi. (75 words)',
        'LSE DMI': 'High: LSE DMI’s blockchain settlement enables instant T+0 for tokenized funds. This reduces risk and boosts efficiency, critical for institutional adoption and medium-term competitiveness in EU/UK markets. Amid global competition, this strengthens LSE against US tailwinds and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion achieves up to 90% cost reduction with T+0 settlement for securities. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in pan-European markets. EU\'s stance competes with US pro-tech and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo’s on-chain funds use atomic swaps for T+0 settlement. This reduces counterparty risk, supporting institutional adoption and medium-term competitiveness in DeFi and TradFi markets. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'High: ICE enables T+0 via stablecoins for tokenized carbon/commodities in futures/spot markets. This enhances efficiency, critical for institutional adoption and medium-term competitiveness globally. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'High: Securitize’s ATS enables secondary T+0 trading for regulated tokens. This reduces risk and boosts efficiency, critical for institutional adoption and medium-term competitiveness in securities markets. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'High: NYSE’s T+0 pilots via stablecoins for tokenized funds enhance efficiency. This supports institutional adoption and medium-term competitiveness in regulated markets, leveraging ICE’s network. US pro-tech strengthens against prediction markets. (75 words)',
        'Corda': 'High: Corda’s private RWA tokenization enables instant DvP settlement. This reduces counterparty risk, critical for bank adoption and medium-term competitiveness in institutional markets. Global competition favors integration with prediction markets. (75 words)',
        'Centrifuge': 'High: Centrifuge’s DeFi atomic swaps enable T+0 for credit/assets. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in multi-chain DeFi markets. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'High: CME GCUL’s pilots enable T+0 settlement for tokenized derivatives. This reduces risk, critical for institutional adoption and medium-term competitiveness in regulated derivatives markets. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'High: Nasdaq’s proposed platform aims for T+0 tokenized securities trading. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in regulated markets. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3’s tokenization for carbon RWAs lacks full T+0 capabilities. While sufficient regionally, it’s less competitive for institutional adoption compared to instant settlement systems. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'Medium: Polymesh enables token trading for securities but lacks full T+0 settlement. This is sufficient but less competitive for institutional adoption compared to instant systems. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio’s DeFi integration enables T+0 trading for RWAs. While sufficient, it lacks the efficiency of enterprise systems, limiting competitiveness for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned T+0 for security tokens is under development. While sufficient for Japan, it’s less competitive globally for institutional adoption without full implementation. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Medium: DTCC’s tokenized collateral includes T+0 testing. While sufficient for pilots, it lacks full implementation, limiting competitiveness for broad institutional adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s Linea pilots test T+0 for payments. While sufficient for banks, it lacks full RWA trading capabilities, limiting competitiveness for institutional adoption. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s DEX enables fast ~3-5s settlement for RWAs. While sufficient for payments, it lacks robust T+0 for institutional trading, limiting competitiveness. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Low: LME’s traditional trading lacks T+0 settlement, relying on legacy systems. This limits efficiency and competitiveness for institutional RWA adoption in modern markets. UK lags US vs prediction markets. (75 words)',
        'Solana': 'High: Solana’s high-throughput blockchain enables T+0 trading for RWAs. This enhances efficiency, critical for DeFi adoption and medium-term competitiveness, despite TradFi integration challenges. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s ERC-1400 enables T+0 with ~16min finality. While sufficient for DeFi, it’s less competitive than instant settlement systems for institutional RWA adoption. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Low: SHFE’s traditional settlement lacks T+0 capabilities, relying on legacy systems. This limits efficiency and competitiveness for institutional RWA adoption in modern markets. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'High: Kalshi’s on-chain platform enables T+0 settlement for event contracts. This reduces risk, supporting institutional adoption and competitiveness. US CFTC boosts vs prediction peers. (75 words)',
        'Polymarket': 'High: Polymarket’s DeFi atomic swaps enable T+0 for predictions. This enhances efficiency, critical for adoption and competitiveness in multi-chain markets. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'High: Crypto.com’s DeFi swaps enable T+0 for event contracts. This reduces risk, supporting institutional adoption and competitiveness. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s on-chain enables T+0 for events. This is sufficient, but less competitive for broad RWAs. US approvals support medium-term adoption. (75 words)',
        'PredictIt': 'Medium: PredictIt’s platform enables T+0 for political contracts. This is compliant, but lacks robustness for global RWAs. US approvals support medium-term adoption. (75 words)',
        'Augur': 'Medium: Augur’s DeFi enables T+0 for predictions. This is sufficient for DeFi, but lacks robustness for institutional RWAs. US regulatory shift supports adoption. (75 words)'
    },
    'Cross-Border T+0 for RWAs (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s Q4 2025 pilots focus on cross-jurisdictional T+0 for commodities via MineHub. This enhances global liquidity, supporting long-term scalability and institutional adoption across markets. In a competitive landscape, this positions Abaxx against US incumbents and prediction markets. (75 words)',
        'LSE DMI': 'High: LSE DMI’s EU/UK focus leverages MiCA for cross-border T+0 fund transfers. This enhances global liquidity, supporting long-term scalability and institutional adoption in regulated markets. This competes with US tailwinds and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion’s pan-European platform with stablecoin integrations enables cross-border T+0 for securities. This enhances liquidity, supporting long-term scalability and institutional adoption. EU\'s stance competes with US pro-tech and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo’s cross-chain DvP enables global T+0 transfers for tokenized Treasuries. This enhances liquidity, supporting long-term scalability and institutional adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'High: ICE’s global ecosystem supports cross-border T+0 via stablecoins and registries. This enhances liquidity, supporting long-term scalability and institutional adoption for commodities. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'Medium: Securitize’s global focus for funds supports partial cross-border T+0. While sufficient, it’s less robust than dedicated global systems, limiting long-term scalability. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'High: NYSE leverages ICE’s global network for cross-border T+0 fund transfers. This enhances liquidity, supporting long-term scalability and institutional adoption in regulated markets. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'Medium: Corda’s interoperability supports cross-border T+0 for banks. While sufficient, it’s less robust than global ecosystems, limiting long-term scalability for broad RWA adoption. Global competition favors vs prediction markets. (75 words)',
        'Centrifuge': 'High: Centrifuge’s V3 multi-chain protocol enables cross-chain T+0 for RWAs. This enhances global liquidity, supporting long-term scalability and institutional adoption in DeFi. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME GCUL supports global payments via CME’s network for T+0. While sufficient, it’s US-focused, limiting long-term scalability for broad cross-border RWA adoption. US tailwinds strengthen vs prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s US-focused platform has cross-border T+0 extensions. While sufficient, it’s less robust than global systems, limiting long-term scalability for adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3’s Latin America focus supports regional cross-border T+0 for carbon RWAs. This limits global liquidity and long-term scalability for institutional adoption. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'Medium: Polymesh supports cross-border regulations for securities T+0. While sufficient, it’s less robust than global ecosystems, limiting long-term scalability for adoption. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'High: Realio’s Cosmos-based cross-chain T+0 supports global RWA transfers. This enhances liquidity, supporting long-term scalability and institutional adoption in DeFi markets. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s Asia-focused platform supports regional cross-border T+0. While sufficient, it’s less robust globally, limiting long-term scalability for adoption. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Low: DTCC’s US-focused collateral pilot lacks cross-border T+0 capabilities. This limits global liquidity and long-term scalability for institutional RWA adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'High: SWIFT’s blockchain supports cross-border T+0 for payments. This enhances global liquidity, supporting long-term scalability and institutional adoption in banking. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'High: Ripple’s cross-border T+0 payments support RWA trading. This enhances global liquidity, supporting long-term scalability and institutional adoption, despite limited RWA focus. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Medium: LME’s global metals hub supports partial cross-border T+0. Without blockchain, it’s less robust, limiting long-term scalability for institutional RWA adoption. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana’s cross-chain T+0 via Wormhole supports RWA trading. While sufficient, bridge dependencies limit global liquidity and long-term scalability for adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s cross-chain T+0 via bridges supports RWA trading. While sufficient, bridge dependencies limit global liquidity and long-term scalability for adoption. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Medium: SHFE’s cross-border investor expansion supports partial T+0. Without blockchain, it’s less robust, limiting long-term scalability for institutional RWA adoption. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'High: Kalshi’s global design supports cross-border T+0 for event RWAs, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US CFTC boosts vs prediction peers. (75 words)',
        'Polymarket': 'High: Polymarket’s cross-chain supports cross-border T+0 for predictions, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'High: Crypto.com’s global reach supports cross-border T+0 for event RWAs, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood\'s US focus limits cross-border T+0 for event RWAs, but approvals aid. This is sufficient, but less robust than global systems, limiting scalability. US approvals support medium-term adoption. (75 words)',
        'PredictIt': 'Medium: PredictIt\'s US focus limits cross-border T+0 for political RWAs, but approvals aid. This is sufficient, but less robust than global systems, limiting scalability. US approvals support medium-term adoption. (75 words)',
        'Augur': 'Medium: Augur\'s DeFi supports cross-border T+0 for prediction RWAs. While sufficient, it lacks robustness for global scalability. US regulatory shift supports adoption. (75 words)'
    },
    'TradFi Integration Friction/Cost (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx’s DLT-agnostic APIs integrate seamlessly with existing trading infrastructure, minimizing disruption. This reduces costs and barriers, critical for medium-term institutional adoption in commodity markets. In jurisdictional competition, this positions Abaxx against US incumbents and prediction markets. (75 words)',
        'LSE DMI': 'Low: LSE DMI\'s APIs integrate with existing fund infrastructure, minimizing friction. This ensures low-cost onboarding, critical for medium-term institutional adoption in EU/UK markets. Amid global competition, this strengthens LSE against US tailwinds and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'Low: Seturion’s unified APIs integrate seamlessly with bank systems, minimizing disruption. This reduces costs, critical for medium-term institutional adoption in pan-European markets. EU\'s stance competes with US pro-tech and prediction markets. (75 words)',
        'Ondo Finance': 'Low: Ondo’s JPMorgan integration via Kinexys reduces friction for tokenized Treasuries. This ensures low-cost onboarding, critical for medium-term institutional adoption in DeFi/TradFi. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'Low: ICE leverages existing exchange infrastructure, ensuring low-cost integration for members. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'Low: Securitize’s enterprise APIs enable seamless integration with financial systems. This reduces costs, critical for medium-term institutional adoption in regulated securities markets. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'Low: NYSE leverages ICE’s infrastructure for low-cost integration of tokenized funds. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'Low: Corda’s bank-friendly APIs integrate with ISVs/back-offices, minimizing updates. This reduces costs, critical for medium-term institutional adoption in private RWA markets. Global competition favors vs prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge’s DeFi focus requires APIs for TradFi integration, increasing friction. While manageable, this limits seamless onboarding compared to enterprise systems for institutional adoption. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Low: CME GCUL leverages CME’s infrastructure for low-cost integration of derivatives. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq integrates with existing systems for low-cost tokenized securities. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Low: B3 integrates with its exchange infrastructure for low-cost carbon RWA trading. This minimizes friction, critical for medium-term institutional adoption regionally. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'Low: Polymesh’s institutional tools enable seamless integration for securities. This reduces costs, critical for medium-term institutional adoption in regulated markets. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio’s SDKs require some integration effort for TradFi systems. While manageable, this increases friction compared to enterprise solutions, limiting seamless institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX integrates with existing systems for low-cost securities trading. This minimizes friction, critical for medium-term institutional adoption in Japan. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Low: DTCC integrates with clearing infrastructure for low-cost collateral trading. This minimizes friction, critical for medium-term institutional adoption in the US. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Low: SWIFT extends its network for low-cost blockchain integration. This minimizes friction, critical for medium-term institutional adoption in banking. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Low: Ripple’s bank APIs enable low-cost integration for cross-border payments. This minimizes friction, critical for medium-term institutional adoption, despite limited RWA focus. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Low: LME leverages existing systems for low-cost metals trading. This minimizes friction, critical for medium-term institutional adoption, despite lacking blockchain. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana’s SDKs require integration effort for TradFi systems. High throughput is offset by less native compatibility, increasing friction for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s high gas fees and custom APIs increase integration effort for TradFi. This raises friction, limiting seamless institutional adoption compared to enterprise systems. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Low: SHFE leverages existing commodity infrastructure for low-cost integration. This minimizes friction, critical for medium-term institutional adoption, despite lacking blockchain. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'Low: Kalshi\'s CFTC platform integrates with low friction for event RWAs. This minimizes costs, critical for medium-term adoption. US approvals boost vs prediction peers. (75 words)',
        'Polymarket': 'Medium: Polymarket\'s DeFi platform requires APIs, increasing friction for TradFi integration. This is manageable, but limits seamless adoption. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'Medium: Crypto.com\'s exchange requires effort for TradFi integration, increasing friction. This is manageable, but limits seamless adoption. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Low: RobinHood\'s retail platform integrates with low friction for event RWAs. This minimizes costs, critical for medium-term adoption. US approvals support. (75 words)',
        'PredictIt': 'Low: PredictIt\'s regulated platform integrates with low friction for political RWAs. This minimizes costs, critical for medium-term adoption. US approvals support. (75 words)',
        'Augur': 'Medium: Augur\'s DeFi platform requires APIs, increasing friction for TradFi integration. This is sufficient for DeFi, but limits institutional adoption. US shift supports. (75 words)'
    },
    'Centralization vs. Decentralization Balance (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx\'s federated network balances centralized liquidity for immediate adoption with decentralized DeFi for long-term scalability. This supports mass RWA adoption in DeFi ecosystems. In global competition, this positions Abaxx to leverage Singapore\'s innovation against US incumbents and prediction markets. (75 words)',
        'LSE DMI': 'Medium: LSE DMI\'s permissioned ledger ensures centralized liquidity but lacks a strong DeFi roadmap due to regulatory constraints. This limits long-term scalability for open RWA ecosystems. Amid US pro-tech, LSE\'s incumbent advantages aid vs prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'Medium: Seturion\'s Clearstream/Euroclear integration consolidates securities liquidity but its permissioned network limits DeFi scalability. This balances immediate adoption with constrained long-term openness. EU\'s MiCAR competes with US tailwinds and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo integrates with centralized institutions like JPMorgan while supporting open DeFi protocols. This balances immediate liquidity with long-term scalability, critical for scalable RWA onboarding. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'Medium: ICE\'s exchanges ensure centralized liquidity for commodities but lack a strong DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'Medium: Securitize’s enterprise platform integrates with centralized markets but its permissioned design limits DeFi scalability. This balances immediate adoption with constrained long-term openness. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'Medium: NYSE’s ICE network consolidates fund liquidity but lacks a strong DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'Medium: Corda’s bank-friendly APIs ensure centralized liquidity, with a Solana bridge for DeFi potential. Its permissioned core limits long-term scalability for open RWA ecosystems. Global competition favors integration with prediction markets. (75 words)',
        'Centrifuge': 'High: Centrifuge’s V3 multi-chain protocol supports decentralized RWA onboarding with TradFi APIs. This balances immediate liquidity with long-term scalability, critical for open DeFi ecosystems. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME\'s network ensures centralized derivatives liquidity but its permissioned L1 limits DeFi scalability. This balances immediate adoption with constrained long-term openness. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq consolidates securities liquidity but lacks a clear DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3’s exchange supports regional carbon RWA liquidity but its centralized design limits DeFi potential. This constrains long-term scalability for open ecosystems. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'Medium: Polymesh’s permissioned PoS ensures regulated securities liquidity but lacks a strong DeFi roadmap. This limits long-term scalability for open RWA ecosystems. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'High: Realio’s Cosmos interoperability enables decentralized RWA onboarding with TradFi SDKs. This balances immediate liquidity with long-term scalability, critical for open DeFi ecosystems. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX’s exchange-led, centralized design integrates with Japan’s markets but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Low: DTCC’s centralized platform ensures clearing liquidity but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Low: SWIFT’s bank-controlled platform supports centralized payments but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems, focusing on banking. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s federated validators and bank APIs ensure centralized liquidity, with open tokenization for DeFi. Limited RWA focus constrains long-term scalability. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Low: LME’s centralized exchange supports metals liquidity but lacks blockchain/DeFi capabilities. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana’s decentralized DeFi ecosystem offers scalability but weak TradFi integration limits centralized liquidity. This balances long-term openness with constrained immediate adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s DeFi ecosystem supports scalability but high friction limits centralized liquidity. This balances long-term openness with constrained immediate institutional adoption. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Low: SHFE’s centralized exchange supports commodity liquidity but lacks blockchain/DeFi capabilities. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'Medium: Kalshi’s centralized prediction liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US regulatory approvals. (75 words)',
        'Polymarket': 'High: Polymarket’s decentralized prediction liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'High: Crypto.com’s hybrid event liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s centralized retail liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US approvals. (75 words)',
        'PredictIt': 'Medium: PredictIt’s centralized political liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US approvals. (75 words)',
        'Augur': 'High: Augur’s decentralized prediction liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US shift boosts vs prediction peers. (75 words)'
    },
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s 5-layer cryptographic system protects trade positions from reverse engineering, ensuring institutional confidentiality in RWA markets. This aligns with wholesale finance needs, supporting medium-term adoption. In global competition, this positions Abaxx against US incumbents and prediction markets like Kalshi. (75 words)',
        'LSE DMI': 'High: LSE DMI’s Azure-based ledger uses confidential messaging to protect fund positions. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in EU/UK markets. Amid US pro-tech, this strengthens LSE against prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion’s permissioned DLT hides securities positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in pan-European markets. EU\'s stance competes with US tailwinds and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo’s on-chain privacy protocols obscure Treasury positions, preventing reverse engineering. This ensures institutional trust, critical for medium-term adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'High: ICE’s regulated platforms use encryption to hide commodity positions. This prevents reverse engineering, ensuring institutional trust for medium-term adoption globally. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'High: Securitize’s DS Protocol obscures token positions via permissioned encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in securities markets. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'High: NYSE’s ICE integration hides fund positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in regulated markets. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'High: Corda’s point-to-point messaging obscures bank positions, preventing reverse engineering. This ensures institutional trust, critical for medium-term adoption in private RWA markets. Global competition favors vs prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge’s pool-based privacy obscures credit positions but is less robust than permissioned systems. This is sufficient but limits trust for broad institutional adoption. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME GCUL obscures derivative positions but is less robust than dedicated systems. This is sufficient but limits trust for broad institutional adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq obscures securities positions but lacks advanced encryption. This is sufficient but limits trust for broad institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3 obscures carbon RWA positions regionally but is less robust globally. This is sufficient but limits trust for global institutional adoption. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'High: Polymesh’s privacy-by-design obscures securities positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio’s cross-chain privacy obscures RWA positions but is less robust than permissioned. This is sufficient but limits trust for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX obscures securities positions but is less robust than enterprise. This is sufficient but limits trust for global institutional adoption. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'High: DTCC’s permissioned DLT obscures collateral positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT obscures payment positions but is less robust than dedicated. This is sufficient but limits trust for broad institutional RWA adoption. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Low: Ripple offers limited privacy for RWA positions, risking exposure. This limits institutional trust, unsuitable for broad adoption. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Medium: LME obscures metals positions via access controls but lacks blockchain privacy. This is sufficient but limits trust for modern institutional adoption. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana uses ZK add-ons for privacy, protecting RWA positions. This is sufficient, but less robust than permissioned. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum’s ZK-rollups obscure RWA positions but are less robust than permissioned. This is sufficient, but limits trust for institutional adoption. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Low: SHFE offers limited privacy for commodity positions, risking exposure. This limits institutional trust, unsuitable for modern adoption. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'High: Kalshi’s regulated platform uses encryption to obscure event positions. This prevents reverse engineering, ensuring trust for medium-term adoption. US CFTC boosts vs prediction peers. (75 words)',
        'Polymarket': 'Medium: Polymarket’s DeFi privacy obscures prediction positions but is less robust. This is sufficient, but limits trust for broad adoption. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'Medium: Crypto.com obscures event positions but is less robust than dedicated. This is sufficient, but limits trust for broad RWA adoption. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood obscures event positions but lacks advanced encryption. This is sufficient, but limits trust for broad RWA adoption. US approvals support. (75 words)',
        'PredictIt': 'Medium: PredictIt obscures political positions but is less robust than dedicated. This is sufficient, but limits trust for broad RWA adoption. US approvals support. (75 words)',
        'Augur': 'Medium: Augur’s DeFi privacy obscures prediction positions but is less robust. This is sufficient, but limits trust for institutional RWA adoption. US shift supports. (75 words)'
    },
    'Minimizes Oracles/Bridges Risks (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s federated design minimizes oracle/bridge risks via native data integration. This reduces vulnerabilities, enhancing reliability for institutional RWA adoption in commodity markets. In global competition, this positions Abaxx against US incumbents and prediction markets. (75 words)',
        'LSE DMI': 'High: LSE DMI\'s permissioned ledger avoids oracles/bridges, using internal data feeds. This reduces vulnerabilities, enhancing reliability for institutional adoption in EU/UK fund markets. Amid US pro-tech, this strengthens LSE against prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'High: Seturion\'s internal data feeds minimize oracle/bridge risks for securities. This enhances reliability, critical for institutional adoption in pan-European markets. EU\'s stance competes with US tailwinds and prediction markets. (75 words)',
        'Ondo Finance': 'High: Ondo\'s native integrations with JPMorgan minimize oracle/bridge risks for Treasuries. This enhances reliability, critical for institutional adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'High: ICE\'s regulated platforms minimize oracle/bridge use via internal feeds. This enhances reliability, critical for institutional adoption in commodity markets. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'High: Securitize\'s permissioned platform avoids oracles/bridges, using internal data. This enhances reliability, critical for institutional adoption in securities markets. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'High: NYSE\'s ICE integration minimizes oracle/bridge risks via internal feeds. This enhances reliability, critical for institutional adoption in regulated fund markets. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'High: Corda\'s notary-based design avoids oracles/bridges, using bank data. This enhances reliability, critical for institutional adoption in private RWA markets. Global competition favors vs prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge\'s multi-chain pools rely on limited oracles/bridges, introducing some risks. This is sufficient but less reliable than permissioned systems for institutional adoption. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME GCUL uses internal feeds but relies on some oracles for derivatives. This introduces risks, limiting reliability for broad institutional adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq\'s platform uses internal feeds but may rely on oracles for securities. This introduces risks, limiting reliability for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3\'s platform uses internal feeds but relies on some oracles for RWAs. This introduces risks, limiting reliability for global institutional adoption. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'High: Polymesh\'s permissioned design minimizes oracle/bridge risks via internal data. This enhances reliability, critical for institutional adoption in securities markets. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio\'s Cosmos bridges introduce some oracle risks for RWAs. This is sufficient but less reliable than permissioned systems for institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX uses internal feeds but may rely on oracles. This introduces risks, limiting reliability for global institutional adoption. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'High: DTCC\'s permissioned DLT minimizes oracle/bridge risks via internal feeds. This enhances reliability, critical for institutional adoption in clearing markets. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s Linea integration relies on some oracles for payments. This introduces risks, limiting reliability for broad institutional RWA adoption. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s validator-based design uses limited oracles for RWAs. This introduces risks, limiting reliability for institutional adoption compared to permissioned systems. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'High: LME\'s legacy systems avoid oracles/bridges, using internal data. This enhances reliability but lacks blockchain, limiting suitability for modern institutional adoption. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Low: Solana\'s DeFi relies heavily on oracles/bridges like Wormhole, increasing vulnerabilities. This limits reliability for institutional RWA adoption compared to permissioned systems. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Low: Ethereum\'s DeFi relies on oracles/bridges, increasing vulnerabilities. This limits reliability for institutional RWA adoption compared to permissioned systems. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Medium: SHFE\'s legacy systems use internal data but lack blockchain oracles. This is sufficient but limits reliability for modern institutional RWA adoption. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'Medium: Kalshi’s regulated platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals boost vs prediction peers. (75 words)',
        'Polymarket': 'Medium: Polymarket’s DeFi relies on oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'Medium: Crypto.com’s exchange relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals support. (75 words)',
        'PredictIt': 'Medium: PredictIt’s regulated platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals support. (75 words)',
        'Augur': 'Medium: Augur’s DeFi relies on oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US shift supports. (75 words)'
    },
    'Liquidity Fragmentation Risk (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx\'s federated network consolidates commodity liquidity across global markets, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. In global competition, this positions Abaxx against US incumbents and prediction markets. (75 words)',
        'LSE DMI': 'Medium: LSE DMI’s EU/UK focus risks partial fragmentation outside its region. While sufficient regionally, it’s less unified than global platforms for institutional trading. UK\'s stance aids vs US tailwinds and prediction markets. (75 words)',
        'Deutsche Boerse Seturion': 'Low: Seturion’s Clearstream/Euroclear integration consolidates securities liquidity across Europe, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. EU\'s stance competes with US tailwinds and prediction markets. (75 words)',
        'Ondo Finance': 'Medium: Ondo\'s DeFi/TradFi hybrid risks fragmentation across chains. While manageable with JPMorgan integration, it’s less unified than permissioned platforms for institutional trading. US shift boosts vs prediction markets. (75 words)',
        'ICE Digital Assets': 'Low: ICE’s global exchange network consolidates commodity liquidity, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. US tailwinds strengthen against prediction markets. (75 words)',
        'Securitize': 'Medium: Securitize’s ATS risks fragmentation across jurisdictions. While sufficient, it’s less unified than exchange-led platforms, limiting institutional trading efficiency. US approvals boost vs prediction markets. (75 words)',
        'NYSE (via ICE)': 'Low: NYSE’s ICE network consolidates fund liquidity globally. This minimizes fragmentation, critical for medium-term institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'Corda': 'Medium: Corda’s bank network risks fragmentation outside its ecosystem. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Global competition favors vs prediction markets. (75 words)',
        'Centrifuge': 'Medium: Centrifuge’s multi-chain pools risk fragmentation across DeFi protocols. While sufficient, it’s less unified than permissioned systems, limiting institutional trading efficiency. US shift aids vs prediction markets. (75 words)',
        'CME GCUL': 'Medium: CME GCUL’s US focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US tailwinds strengthen against prediction markets. (75 words)',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq’s exchange integration ensures unified securities liquidity. This minimizes fragmentation, critical for medium-term institutional adoption. US pro-tech boosts vs prediction markets. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3’s regional focus risks fragmentation outside Latin America. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Brazil competes with US vs prediction markets. (75 words)',
        'Polymesh': 'Medium: Polymesh’s securities focus risks fragmentation across jurisdictions. While sufficient, it’s less unified than exchange-led platforms, limiting institutional trading efficiency. Swiss edge aids vs prediction markets. (75 words)',
        'Realio Network': 'Medium: Realio’s cross-chain design risks fragmentation across DeFi ecosystems. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US pro-tech boosts vs prediction markets. (75 words)',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s Japan focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Japan competes with US vs prediction markets. (75 words)',
        'DTCC Collateral Pilot': 'Medium: DTCC’s US focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US tailwinds strengthen against prediction markets. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT’s bank network risks fragmentation outside banking. While sufficient, it’s less unified than global platforms, limiting institutional RWA trading efficiency. Global competition with US vs prediction markets. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s federated ledger risks fragmentation for non-payment RWAs. While sufficient, it’s less unified than dedicated platforms, limiting institutional trading efficiency. US shift boosts vs prediction markets. (75 words)',
        'LME Modernization': 'Medium: LME\'s legacy exchange risks fragmentation without blockchain integration. While sufficient, it’s less unified than tokenized platforms, limiting institutional efficiency. UK lags US vs prediction markets. (75 words)',
        'Solana': 'Medium: Solana\'s DeFi ecosystem risks fragmentation across protocols. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US pro-tech boosts vs prediction markets. (75 words)',
        'Ethereum': 'Medium: Ethereum\'s DeFi ecosystem risks fragmentation across L2s/protocols. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US tailwinds aid vs prediction markets. (75 words)',
        'SHFE Initiatives': 'Medium: SHFE\'s legacy exchange risks fragmentation globally. While sufficient, it’s less unified than tokenized platforms, limiting institutional trading efficiency. China competes with US vs prediction markets. (75 words)',
        'Kalshi': 'Medium: Kalshi’s regional focus risks fragmentation outside US. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals boost vs prediction peers. (75 words)',
        'Polymarket': 'Medium: Polymarket’s DeFi ecosystem risks fragmentation across chains. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US relaunch boosts vs prediction peers. (75 words)',
        'Crypto.com': 'Medium: Crypto.com’s exchange risks fragmentation across markets. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US CFTC boosts vs prediction peers. (75 words)',
        'RobinHood': 'Medium: RobinHood’s retail focus risks fragmentation outside US. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals support. (75 words)',
        'PredictIt': 'Medium: PredictIt’s niche focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals support. (75 words)',
        'Augur': 'Medium: Augur’s DeFi ecosystem risks fragmentation across chains. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US shift supports. (75 words)'
    },
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx\'s federated blockchain with 5-layer encryption and regular audits minimizes hacking risks. This permissioned design ensures robust security, critical for institutional trust in commodity markets. In a competitive landscape, it leverages Singapore\'s innovation to challenge US incumbents, whose pro-tech tailwinds may enhance their defenses. Prediction markets like Kalshi pose new threats, but Abaxx\'s privacy focus reduces vulnerability to malicious manipulation. (75 words)',
        'LSE DMI': 'Low: LSE DMI\'s Azure-backed permissioned ledger employs enterprise-grade security, minimizing manipulation risks. This ensures trust for fund trading in EU/UK, aligning with MiCA. Amid US pro-tech shifts, LSE\'s incumbent volumes aid resilience, but less tech-savvy jurisdictions may lag. Prediction markets like Polymarket introduce competition, but LSE\'s centralized control and audits reduce susceptibility, maintaining medium-term adoption without DeFi\'s exposure. (75 words)',
        'Deutsche Boerse Seturion': 'Low: Seturion\'s permissioned DLT with Clearstream security minimizes manipulation risks. Robust encryption ensures trust in pan-European securities, compliant with MiCAR. EU incumbents compete with US tailwinds, but prediction markets like Kalshi challenge innovation. This focus on security reduces vulnerability, strengthening Seturion\'s position against US pro-tech and emerging competitors in RWAs. (75 words)',
        'Ondo Finance': 'Medium: Ondo\'s hybrid DeFi/TradFi platform faces moderate hacking risks due to open integrations. Audits mitigate, but less robust than permissioned systems. US regulatory shift boosts adaptability, challenging incumbents, yet prediction markets like Polymarket add competitive pressure. Ondo\'s on-chain privacy offers some protection, supporting medium-term trust amidst evolving manipulation threats. (75 words)',
        'ICE Digital Assets': 'Low: ICE\'s regulated platform with enterprise security minimizes malicious risks. This ensures trust in commodity RWAs, leveraging US tailwinds and incumbent volumes. Prediction markets like Kalshi pose disruption, but ICE\'s centralized control and audits reduce vulnerability, maintaining leadership in global competition against manipulation attempts. (75 words)',
        'Securitize': 'Low: Securitize\'s permissioned DS Protocol with audits minimizes hacking risks. This enhances trust in token issuance, boosted by US approvals vs EU. Prediction markets challenge, but Securitize\'s compliance focus and security measures reduce susceptibility, positioning it resiliently against incumbents and emerging manipulation threats. (75 words)',
        'NYSE (via ICE)': 'Low: NYSE\'s ICE-integrated platform with enterprise security minimizes manipulation risks. US pro-tech and incumbent power enhance defenses, supported by audits. Prediction markets like Polymarket face barriers, allowing NYSE to maintain stability and outpace emerging threats in the RWA space with robust defenses. (75 words)',
        'Corda': 'Low: Corda\'s permissioned notary-based DLT minimizes hacking risks for banks. Regular audits and encryption ensure trust, competing with US tailwinds. Prediction markets like Kalshi pose innovation threats, but Corda\'s security focus reduces vulnerability, supporting medium-term RWA adoption in a competitive landscape. (75 words)',
        'Centrifuge': 'Medium: Centrifuge\'s multi-chain DeFi exposes it to moderate manipulation risks from bridges. US shift favors incumbents, but audits mitigate. Prediction markets like Polymarket add pressure, with Centrifuge\'s privacy offering partial protection in RWAs. (75 words)',
        'CME GCUL': 'Low: CME GCUL\'s permissioned L1 with enterprise security minimizes risks. US tailwinds and incumbent volumes strengthen defenses, supported by audits. Prediction markets like Kalshi face barriers, allowing CME to reduce vulnerability and maintain leadership in derivatives against manipulation attempts. (75 words)',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq\'s proposed platform with enterprise security minimizes hacking risks. US pro-tech enhances defenses. Prediction markets like Kalshi compete, but Nasdaq\'s audits reduce vulnerability in RWAs. (75 words)',
        'B3 Digitas/ACXRWA': 'Medium: B3\'s regional platform faces moderate risks from exposure. Brazil lags US tailwinds, increasing vulnerability. Prediction markets pose threats, but audits mitigate susceptibility vs incumbents. (75 words)',
        'Polymesh': 'Low: Polymesh\'s permissioned PoS with privacy-by-design minimizes hacking risks. Swiss catalyst aids defenses. Prediction markets challenge, but Polymesh\'s audits reduce susceptibility, balancing vs US incumbents. (75 words)',
        'Realio Network': 'Medium: Realio\'s Cosmos-based L1 faces moderate risks from cross-chain exposure. US pro-tech boosts defenses, but prediction markets add pressure. Audits mitigate susceptibility in RWAs. (75 words)',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX\'s regulated platform with enterprise security minimizes risks. Japan competes with US, but lags tailwinds. Prediction markets challenge, but audits reduce susceptibility in RWAs. (75 words)',
        'DTCC Collateral Pilot': 'Low: DTCC\'s permissioned DLT minimizes manipulation risks. US tailwinds enhance defenses. Prediction markets pose threats, but audits reduce vulnerability in RWAs. (75 words)',
        'SWIFT Blockchain': 'Medium: SWIFT\'s Linea-integrated blockchain faces moderate risks from Ethereum exposure. Global competition balances vs prediction markets. Audits mitigate susceptibility, but centralized focus increases vulnerability. (75 words)',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s federated ledger faces moderate risks from validator exposure. US shift boosts defenses. Prediction markets challenge, but audits mitigate susceptibility in cross-border RWAs. (75 words)',
        'LME Modernization': 'Low: LME\'s legacy system with robust controls minimizes risks. UK trails US tailwinds, but audits reduce susceptibility. Prediction markets like Polymarket threaten, but LME\'s focus aids resilience. (75 words)',
        'Solana': 'High: Solana\'s public blockchain faces high risks from DeFi exposure. US pro-tech challenges incumbents, but prediction markets align, increasing susceptibility to manipulation in RWAs. (75 words)',
        'Ethereum': 'High: Ethereum\'s public blockchain faces high risks from oracle and L2 exposure. US tailwinds force adaptation, with prediction markets adding pressure, heightening susceptibility in RWAs. (75 words)',
        'SHFE Initiatives': 'Low: SHFE\'s legacy system minimizes risks with controls. China competes with US, but lacks tailwinds. Prediction markets pose threats, but SHFE\'s focus reduces susceptibility in commodities. (75 words)',
        'Kalshi': 'Low: Kalshi\'s regulated platform minimizes risks with enterprise security. US CFTC approvals enhance defenses. As a prediction market, it challenges incumbents with low susceptibility to manipulation. (75 words)',
        'Polymarket': 'Medium: Polymarket\'s decentralized platform faces moderate risks from on-chain exposure. US relaunch boosts defenses. Audits mitigate, but DeFi focus increases susceptibility vs incumbents. (75 words)',
        'Crypto.com': 'Medium: Crypto.com\'s exchange faces moderate risks from integrations. US shift enhances defenses. As a prediction market, it challenges incumbents with partial susceptibility to manipulation. (75 words)',
        'RobinHood': 'Medium: RobinHood\'s platform faces moderate risks from retail exposure. US approvals aid defenses. Limited DeFi increases susceptibility, but challenges prediction markets in RWAs. (75 words)',
        'PredictIt': 'Medium: PredictIt\'s regulated platform faces moderate risks from focus. US approvals enhance defenses. Scope limits susceptibility, but challenges incumbents in prediction RWAs. (75 words)',
        'Augur': 'High: Augur\'s DeFi platform faces high risks from decentralized exposure. US shift boosts defenses. Audits mitigate, but high susceptibility challenges incumbents in prediction RWAs. (75 words)'
    }
}


points_breakdown = {
    'Abaxx (ID++/PDT)': 'Total: 53.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'LSE DMI': 'Total: 47.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Deutsche Boerse Seturion': 'Total: 48.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Ondo Finance': 'Total: 48.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'ICE Digital Assets': 'Total: 46.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Securitize': 'Total: 46.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'NYSE (via ICE)': 'Total: 46.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Corda': 'Total: 47.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Centrifuge': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'CME GCUL': 'Total: 42.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Nasdaq Tokenized Securities': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'B3 Digitas/ACXRWA': 'Total: 40.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Polymesh': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Realio Network': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'TSE/JPX Digital Securities': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5).',
    'DTCC Collateral Pilot': 'Total: 37.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Low, 1 × 1.5 = 1.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5).',
    'SWIFT Blockchain': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5).',
    'Ripple (XRP Ledger)': 'Total: 39.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Low, 1 × 1.5 = 1.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'LME Modernization': 'Total: 32.0. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Low, 1 × 2 = 2), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Low, 1 × 2 = 2), DeFi Potential (Low, 1 × 2.5 = 2.5).',
    'Solana': 'Total: 37.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Low, 1 × 1.5 = 1.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'Ethereum': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Low, 1 × 1.5 = 1.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'SHFE Initiatives': 'Total: 30.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Low, 1 × 2 = 2), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Low, 1 × 1.5 = 1.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Low, 1 × 2 = 2), DeFi Potential (Low, 1 × 2.5 = 2.5).',
    'Kalshi': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Polymarket': 'Total: 46.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'Crypto.com': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).',
    'RobinHood': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'PredictIt': 'Total: 43.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5).',
    'Augur': 'Total: 42.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5).'
}

solution_descriptions = {
    'Abaxx (ID++/PDT)': 'Abaxx is a Singapore-based platform leveraging a federated blockchain with 5-layer encryption for tokenized gold and money market funds (MMFs). It integrates with MineHub for Q4 2025 pilots, focusing on secure, efficient RWA trading with T+0 settlement.',
    'LSE DMI': 'LSE DMI is a London Stock Exchange initiative using Azure’s blockchain for tokenized funds, aligning with MiCA regulations to ensure secure and efficient trading in EU/UK markets.',
    'Deutsche Boerse Seturion': 'Seturion, by Deutsche Boerse, is a permissioned DLT platform for tokenized bonds and securities, integrated with Clearstream, offering up to 90% cost reduction and MiCAR compliance.',
    'Ondo Finance': 'Ondo Finance is a US-based hybrid DeFi/TradFi platform partnering with JPMorgan to tokenize Treasuries with on-chain privacy and T+0 settlement, bridging institutional and decentralized finance.',
    'ICE Digital Assets': 'ICE Digital Assets, part of Intercontinental Exchange, tokenizes carbon credits and commodities using Bakkt/Circle integrations, ensuring regulated, secure RWA trading with T+0 capabilities.',
    'Securitize': 'Securitize is a US platform offering a DS Protocol for regulated token issuance and secondary T+0 trading, focusing on securities with enterprise-grade security and compliance.',
    'NYSE (via ICE)': 'NYSE, via ICE, explores tokenized funds with T+0 settlement, leveraging existing exchange infrastructure and SEC talks to enhance regulated RWA trading in the US.',
    'Corda': 'Corda is a bank-focused permissioned DLT with notary-based settlement, designed for private RWA tokenization, offering secure, efficient trading with potential Solana bridge integration.',
    'Centrifuge': 'Centrifuge is a multi-chain DeFi platform for tokenized credit and assets, using V3 protocols for T+0 settlement and legal wrappers, targeting institutional and DeFi markets.',
    'CME GCUL': 'CME GCUL is a CME initiative for tokenized derivatives on an L1 blockchain, enabling T+0 settlement and leveraging existing infrastructure for regulated markets.',
    'Nasdaq Tokenized Securities': 'Nasdaq’s proposed platform aims to tokenize securities with T+0 trading, integrating with existing systems to enhance efficiency and compliance in regulated markets.',
    'B3 Digitas/ACXRWA': 'B3 Digitas, Brazil’s exchange, focuses on tokenized carbon RWAs with regional T+0 settlement, integrating with existing infrastructure for sustainable finance.',
    'Polymesh': 'Polymesh is a Swiss permissioned PoS blockchain for regulated securities, offering privacy-by-design and KYC integration for secure, compliant RWA trading.',
    'Realio Network': 'Realio Network is a Cosmos-based L1 for tokenized real estate and art, supporting cross-chain T+0 settlement and DeFi integration with TradFi SDKs.',
    'TSE/JPX Digital Securities': 'TSE/JPX, Japan’s exchange, plans to tokenize securities with T+0 settlement, integrating with existing systems for regulated RWA trading in Asia.',
    'DTCC Collateral Pilot': 'DTCC’s Collateral Pilot tests tokenized collateral on a permissioned DLT, aiming for T+0 settlement and integration with US clearing infrastructure.',
    'SWIFT Blockchain': 'SWIFT Blockchain integrates Ethereum’s Linea for tokenized payments, supporting cross-border T+0 settlement with a focus on banking networks.',
    'Ripple (XRP Ledger)': 'Ripple’s XRP Ledger offers fast cross-border payments with ~3-5s settlement, using federated validators for tokenized assets with limited RWA focus.',
    'LME Modernization': 'LME Modernization updates the London Metals Exchange with partial cross-border T+0, retaining legacy systems for metals trading without full blockchain adoption.',
    'Solana': 'Solana is a high-throughput public blockchain enabling T+0 RWA trading via Wormhole bridges, targeting DeFi with challenges in TradFi integration.',
    'Ethereum': 'Ethereum supports tokenized RWAs with ERC-1400 and ~16min T+0 via L2s, widely used in DeFi with vulnerabilities from oracles and bridges.',
    'SHFE Initiatives': 'SHFE Initiatives modernize the Shanghai Futures Exchange with partial cross-border T+0, relying on legacy systems for commodity trading.',
    'Kalshi': 'Kalshi is a US CFTC-regulated platform for event contract RWAs, offering T+0 settlement and W3C-compliant credentials for secure trading.',
    'Polymarket': 'Polymarket is a US relaunched decentralized platform for prediction RWAs, using atomic swaps for T+0 settlement and targeting DeFi markets.',
    'Crypto.com': 'Crypto.com is a CFTC-regulated exchange for event contract RWAs, providing T+0 settlement with a hybrid centralized-decentralized model.',
    'RobinHood': 'RobinHood offers regulated event RWA trading with T+0 settlement, leveraging its retail user base for US market integration.',
    'PredictIt': 'PredictIt is a US-regulated platform for political prediction RWAs, providing T+0 settlement with a focus on compliance and niche markets.',
    'Augur': 'Augur is a decentralized prediction market on Ethereum, offering T+0 settlement for RWAs with a focus on long-term DeFi potential.'
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
def generate_standalone_html(df, tooltip_data, tooltip_header, color_map, filename='rwa_table.html'):
    # Sort DataFrame by "Points" in descending order
    df_sorted = df.sort_values(by='Points', ascending=False)

    # Reindex tooltip_data to match the sorted DataFrame
    tooltip_data_sorted = [tooltip_data[i] for i in df_sorted.index]

    # Determine the longest header text for height adjustment
    max_header_length = max(len(str(col)) for col in df_sorted.columns)  # Basic length-based estimate
    # Adjust height based on length (e.g., 30px base + 5px per 5 characters beyond 10)
    header_height = max(40, 5 + int(max(0, (max_header_length)) * 0.75))

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
        <p>Blue: Permissioned Blockchain/Enterprise, Green: Hybrid DeFi/TradFi, Orange: Public Blockchain, Gray: Traditional Exchange,  Purple: Prediction Markets</p>
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
        row_color = ( color_map.get(solution)
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
