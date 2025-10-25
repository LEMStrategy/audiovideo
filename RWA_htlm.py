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
                 'PredictIt', 'Augur', 'Provenance Foundation', 'Bakkt', 'Tether', 'Circle'],
    'Encrypted P2P Communication (High Impact)': [
        'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': [
        'High', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High'
    ],
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High',
        'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High'
    ],
    'Private RWA Trading with T+0 Settlement (High Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'High', 'Medium', 'Low',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High'
    ],
    'Cross-Border T+0 for RWAs (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Medium', 'Low', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'High', 'High'
    ],
    'TradFi Integration Friction/Cost (High Impact)': [
        'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low',
        'Medium', 'Low', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low',
        'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low'
    ],
    'Centralization vs. Decentralization Balance (Medium Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Low',
        'Medium', 'High', 'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Low', 'Medium'
    ],
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low',
        'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High'
    ],
    'Minimizes Oracles/Bridges Risks (Medium Impact)': [
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'High', 'Low', 'Low', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'
    ],
    'Liquidity Fragmentation Risk (High Impact)': [
        'Low', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'Medium', 'Low', 'Medium',
        'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium',
        'Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Low', 'Low'
    ],
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': [
        'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Low', 'Low', 'Medium', 'Low', 'Low', 'Medium', 'Low',
        'Medium', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'High', 'High', 'Low',
        'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'Low'
    ],
    'Regulatory Adaptability to Evolving Global Standards (High Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Low', 'Medium', 'Medium', 'Low',
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium', 'High'
    ],
    'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': [
        'High', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'Medium', 'Medium',
        'Medium', 'Medium', 'High', 'Low', 'Low', 'Low', 'High', 'Low', 'High', 'High', 'Low',
        'Medium', 'High', 'High', 'Medium', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium'
    ],
    'Incumbent Advantages (High Impact)': [
        'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High',
        'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Low', 'Low', 'Medium',
        'Low', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'High', 'High', 'High'
    ],
    'Regulatory Tailwinds (High Impact)': [
        'High', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'High', 'High', 'High',
        'Medium', 'Medium', 'High', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
        'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High'
    ],
    'Points': [
        55.0, 49.0, 50.0, 50.5, 50.0, 48.0, 48.0, 49.0, 47.0, 46.0, 48.0, 42.0, 46.0, 47.0, 39.5, 39.5,
        39.5, 41.0, 34.0, 39.5, 39.5, 32.5, 48.0, 49.0, 47.0, 46.0, 45.0, 44.0, 46.5, 48.0, 50.0, 51.0
    ]
}

# Convert to DataFrame for sorting and consistency
df = pd.DataFrame(data)

tooltip_header = {
    'Solution': {'value': 'Represents various blockchain and traditional platforms evaluated for RWA tokenization, ranked by aggregated points reflecting their performance across criteria.'},
    'Encrypted P2P Communication (High Impact)': {'value': 'Assesses ability to secure peer-to-peer interactions in RWAs, critical for privacy and trust. High scores indicate robust encryption, challenging incumbents and prediction markets like Kalshi with pro-tech tailwinds.'},
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': {'value': 'Evaluates W3C-compliant digital identities for KYC/AML in RWAs. High scores reflect strong compliance, competing with US tailwinds and prediction markets for institutional adoption.'},
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {'value': 'Measures legal enforceability of RWA ownership per MLETR. High scores indicate strong alignment, challenging incumbents with regulatory tailwinds vs prediction markets.'},
    'Private RWA Trading with T+0 Settlement (High Impact)': {'value': 'Gauges T+0 settlement capability for RWAs. High scores reflect speed, leveraging US pro-tech to outpace prediction markets like Polymarket in efficiency.'},
    'Cross-Border T+0 for RWAs (Medium Impact)': {'value': 'Assesses cross-border T+0 feasibility. High scores indicate global reach, challenging incumbents with tailwinds and competing with prediction markets in RWAs.'},
    'TradFi Integration Friction/Cost (High Impact)': {'value': 'Evaluates ease/cost of TradFi integration. Low scores are best, minimizing barriers with US tailwinds, resisting prediction market disruptions in RWAs.'},
    'Centralization vs. Decentralization Balance (Medium Impact)': {'value': 'Balances centralized control with DeFi openness. High scores optimize security/scalability, challenging incumbents and prediction markets with regulatory support.'},
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {'value': 'Measures protection against reverse engineering in RWAs. High scores ensure privacy, competing with US pro-tech and resisting prediction market transparency.'},
    'Minimizes Oracles/Bridges Risks (Medium Impact)': {'value': 'Assesses reduction of oracle/bridge vulnerabilities. High scores limit risks, leveraging US tailwinds to outpace prediction markets in RWA stability.'},
    'Liquidity Fragmentation Risk (High Impact)': {'value': 'Evaluates risk of fragmented liquidity in RWAs. Low scores are best, reducing barriers with US tailwinds, challenging prediction markets like Kalshi in adoption.'},
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {'value': 'Measures vulnerability to hacking/manipulation. Low scores are best, enhancing security with US pro-tech, resisting prediction market threats in RWAs.'},
    'Regulatory Adaptability to Evolving Global Standards (High Impact)': {'value': 'Assesses flexibility to global regulatory changes. High scores reflect compliance, leveraging US tailwinds to challenge incumbents and prediction markets.'},
    'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {'value': 'Gauges potential for sustainable DeFi protocols in RWAs. High scores indicate scalability, competing with US incumbents and prediction markets.'},
    'Incumbent Advantages (High Impact)': {'value': 'Evaluates existing market power for RWA adoption. High scores reflect volume/brand, challenging prediction markets with US tailwinds.'},
    'Regulatory Tailwinds (High Impact)': {'value': 'Measures supportive regulatory environments. High scores leverage US pro-tech, enhancing RWA growth vs prediction markets and incumbents.'},
    'Points': {'value': 'Aggregated weighted score (High=3, Medium=2, Low=1; inverted for risks like hacking). Reflects overall RWA potential, ranking solutions with US tailwinds and prediction market context.'}
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
    'Abaxx (ID++/PDT)': colors['Abaxx'],                # Yellow
    'LSE DMI': colors['Perm_Chain'],                    # Blue
    'Deutsche Boerse Seturion': colors['Perm_Chain'],   # Blue
    'Ondo Finance': colors['DeFi_TradFi'],              # Green
    'ICE Digital Assets': colors['Perm_Chain'],         # Blue
    'Securitize': colors['DeFi_TradFi'],                # Green
    'NYSE (via ICE)': colors['Perm_Chain'],             # Blue
    'Corda': colors['Perm_Chain'],                      # Blue
    'Centrifuge': colors['DeFi_TradFi'],                # Green
    'CME GCUL': colors['DeFi_TradFi'],                  # Green
    'Nasdaq Tokenized Securities': colors['DeFi_TradFi'],  # Green
    'B3 Digitas/ACXRWA': colors['DeFi_TradFi'],         # Green
    'Polymesh': colors['Perm_Chain'],                   # Blue
    'Realio Network': colors['DeFi_TradFi'],            # Green
    'TSE/JPX Digital Securities': colors['Trad_Exch'],  # Gray
    'DTCC Collateral Pilot': colors['Perm_Chain'],      # Blue
    'SWIFT Blockchain': colors['Perm_Chain'],           # Blue
    'Ripple (XRP Ledger)': colors['Pub_Chain'],         # Orange
    'LME Modernization': colors['Trad_Exch'],           # Gray
    'Solana': colors['Pub_Chain'],                      # Orange
    'Ethereum': colors['Pub_Chain'],                    # Orange
    'SHFE Initiatives': colors['Trad_Exch'],            # Gray
    'Kalshi': colors['Pred_Mkt'],                       # Purple
    'Polymarket': colors['Pred_Mkt'],                   # Purple
    'Crypto.com': colors['Pred_Mkt'],                   # Purple
    'RobinHood': colors['Pred_Mkt'],                    # Purple
    'PredictIt': colors['Pred_Mkt'],                    # Purple
    'Augur': colors['Pub_Chain'],                       # Orange (via Ethereum)
    'Provenance Foundation': colors['DeFi_TradFi'],     # Green
    'Bakkt': colors['DeFi_TradFi'],                     # Green
    'Tether': colors['DeFi_TradFi'],                    # Green
    'Circle': colors['DeFi_TradFi']                     # Green
}

cell_hover_text = {
    'Encrypted P2P Communication (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s ID++ protocol uses a 5-layer cryptographic Messenger/Verifier+ system for secure, encrypted P2P communication, optimized for commodity traders. This guarantees confidentiality and trust, vital for institutional adoption. The design avoids shared ledgers, enhancing security and aligning with wholesale finance requirements for data protection. In a regulatory-competitive landscape, this feature positions Abaxx as a leader in secure RWA trading.',
        'LSE DMI': 'High: LSE DMI utilizes Azure’s blockchain messaging for secure, encrypted fund transfers. This ensures confidentiality for institutional investors, meeting regulatory and trust standards. Enterprise-grade encryption aligns with wholesale finance needs, supporting medium-term adoption in EU/UK markets. Amid global regulatory competition, this strengthens LSE’s position against US incumbents.',
        'Deutsche Boerse Seturion': 'High: Seturion’s blockchain-based settlement incorporates encrypted communication for tokenized assets like bonds. This guarantees secure data exchange, essential for institutional trust and EU regulatory compliance. In the context of jurisdictional competition, this feature aids Seturion in maintaining competitiveness against US pro-tech shifts.',
        'Ondo Finance': 'Medium: Ondo relies on partner protocols for encrypted DeFi transactions, providing sufficient security for RWA trading but lacking the robustness of enterprise-grade P2P systems. This supports institutional use but may limit scalability in a regulatory-competitive environment. As US incumbents gain tailwinds, Ondo’s hybrid approach could bridge gaps.',
        'ICE Digital Assets': 'Medium: ICE employs encrypted Bakkt/Circle integrations for stablecoin P2P communication. While secure for regulated environments, it’s less robust than dedicated blockchain messaging. With US pro-tech regulations, this positions ICE to leverage incumbent advantages for RWA onboarding.',
        'Securitize': 'High: Securitize’s issuance platform uses encrypted communication for secure token trading. This ensures confidentiality and compliance, crucial for institutional trust in regulated markets. Amid US regulatory tailwinds, this strengthens Securitize’s position against emerging prediction markets.',
        'NYSE (via ICE)': 'Medium: NYSE leverages ICE’s encrypted platforms for tokenized funds. While secure for regulated trading, it lacks the robustness of dedicated P2P systems. US pro-tech push enhances NYSE’s incumbent advantages in onboarding existing assets.',
        'Corda': 'High: Corda’s native point-to-point encrypted messaging avoids broadcast ledgers, ensuring secure data exchange for banks. This aligns with institutional trust and compliance, driving medium-term RWA adoption. In global regulatory competition, Corda’s bank focus could integrate with prediction markets.',
        'Centrifuge': 'Medium: Centrifuge uses multi-chain privacy via Ethereum/Base for encrypted communication. While sufficient for DeFi, it’s less robust than permissioned systems. As US incumbents adapt, Centrifuge’s DeFi orientation may compete with prediction markets like Polymarket.',
        'CME GCUL': 'Medium: CME GCUL’s blockchain messaging provides encryption for tokenized derivatives. While secure, it’s less advanced than dedicated P2P systems. US regulatory tailwinds boost CME’s incumbent advantages in futures onboarding.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s proposed blockchain platform includes encrypted communication. While secure for securities, it lacks robustness of mature systems. US pro-tech regulations enhance Nasdaq’s financial power against EU competitors.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s digital platform uses encryption for carbon RWAs. While sufficient regionally, it’s less robust than enterprise-grade systems. Brazil’s regulatory environment lags US tailwinds, limiting B3’s global competitiveness.',
        'Polymesh': 'Medium: Polymesh’s node-based encryption secures securities trading. While compliant, it’s less advanced than dedicated P2P systems. As prediction markets gain approvals, Polymesh’s regulated focus may adapt to US innovations.',
        'Realio Network': 'Medium: Realio’s IBC messaging provides encryption for cross-chain RWAs. While secure for DeFi, it lacks robustness of permissioned systems. US pro-tech push could integrate Realio with incumbent platforms.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned blockchain includes encryption for securities. While secure for Japan, it’s less robust than enterprise systems. Asian jurisdictions compete with US regulatory tailwinds.',
        'DTCC Collateral Pilot': 'Low: DTCC’s permissioned DLT offers minimal encryption for collateral pilots. This limits security for broad use. US tailwinds strengthen DTCC’s incumbent advantages in clearing.',
        'SWIFT Blockchain': 'Medium: SWIFT’s blockchain integrates encrypted Ethereum channels for payments. While secure for banks, it’s less robust than dedicated P2P. Global competition with US pro-tech favors SWIFT’s financial power.',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s P2P network provides encryption for payments. While sufficient for cross-border, it lacks robustness for RWAs. US regulatory shift could boost Ripple against prediction markets.',
        'LME Modernization': 'Low: LME’s traditional exchange lacks blockchain encryption, relying on legacy security. This limits modern suitability. UK regulations trail US tailwinds, weakening LME against innovators.',
        'Solana': 'Low: Solana’s P2P gossip protocol relies on add-on encryption, insufficient for institutional security. This limits trust. DeFi focus could compete with prediction markets under US pro-tech.',
        'Ethereum': 'Medium: Ethereum’s ZK-rollups provide encrypted messaging for DeFi. While sufficient, it’s less robust than permissioned. Upgrades position Ethereum to leverage US regulatory tailwinds against incumbents.',
        'SHFE Initiatives': 'Low: SHFE’s traditional exchange lacks blockchain encryption, relying on legacy systems. This limits security for RWAs. China’s jurisdiction competes with US pro-tech for global RWA leadership.',
        'Kalshi': 'Medium: Kalshi’s CFTC-regulated platform uses encrypted communication for event contracts. While secure, it’s less robust than enterprise systems. US approvals provide tailwinds, but limited DeFi integration constrains vs incumbents.',
        'Polymarket': 'Medium: Polymarket’s decentralized platform relies on blockchain encryption for predictions. While secure for DeFi, it lacks robustness for broad RWAs. US relaunch boosts adaptability, challenging incumbents with innovative products.',
        'Crypto.com': 'Medium: Crypto.com’s CFTC-regulated exchange uses encrypted communication for event contracts. While secure, it’s less robust than dedicated systems. US tailwinds enhance competitiveness against traditional incumbents.',
        'RobinHood': 'Medium: RobinHood’s retail platform uses encrypted communication for event trading. While secure, it’s less robust for RWAs. US approvals leverage user base, but limited DeFi limits long-term scalability.',
        'PredictIt': 'Medium: PredictIt’s regulated platform uses encrypted communication for political predictions. While secure, it’s less robust for broad RWAs. US approvals provide tailwinds, but focused scope limits vs incumbents.',
        'Augur': 'Medium: Augur’s decentralized blockchain uses encrypted communication for predictions. While secure for DeFi, it lacks robustness for institutional RWAs. US regulatory shift could boost vs incumbents.',
        'Provenance Foundation': 'Medium: Provenance Foundation\'s Cosmos SDK ensures moderate encrypted P2P communication via secure proof-of-stake, protecting order flow with institutional-grade encryption. While interoperable with 70+ partners, it lacks the advanced federated layers of Abaxx, limiting edge against US pro-tech. Prediction markets like Kalshi face similar constraints, but Provenance\'s focus on compliance balances security for RWA adoption.',
        'Bakkt': 'Medium: Bakkt\'s API-based P2P for RWA custody is secure with SOC 2, but relies on centralized servers, lacking federated layers like Abaxx. US NYDFS compliance aids trust, but prediction markets like Kalshi\'s on-chain models outpace in decentralization. US pro-tech tailwinds enhance RWA settlement. ',
        'Tether': 'Medium: Tether\'s USDT APIs enable secure P2P via Hadron, but centralized reserves limit federated robustness like Abaxx. SOC 1 aids trust, though prediction markets like Kalshi\'s on-chain models outpace in decentralization. US adoption enhances RWA settlement. ',
        'Circle': 'Medium: Circle\'s USDC APIs enable secure P2P via CCTP V2, but centralized custody limits federated robustness like Abaxx. SOC 2 compliance aids trust, though prediction markets like Kalshi\'s on-chain models outpace in decentralization. US pro-tech tailwinds enhance RWA settlement. '
    },
    'DID/Verified Credentials (W3C-Compliant) (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s ID++ offers W3C-compliant decentralized identities for verified credentials in RWA markets. This supports regulatory compliance and interoperability, critical for institutional trust and medium-term RWA adoption across global markets. In the context of regulatory competition, this positions Abaxx to leverage Singapore\'s innovation against US incumbents and prediction markets like Kalshi.',
        'LSE DMI': 'High: LSE DMI provides W3C-compliant digital identities for verified credentials in tokenized funds. This aligns with MiCA for EU/UK markets, enhancing trust and medium-term adoption. Amid jurisdictional competition, this strengthens LSE\'s position against US pro-tech shifts and prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion integrates W3C-compliant credentials for verified identities in tokenized securities. This supports MiCAR compliance and interoperability, critical for institutional trust in pan-European markets. In global competition, this aids Seturion against US tailwinds and prediction markets.',
        'Ondo Finance': 'Medium: Ondo uses partner-based W3C-compliant credentials for verified identities in tokenized Treasuries. This is sufficient for hybrid DeFi/TradFi, but less robust than dedicated systems. US regulatory shift enhances adaptability, challenging incumbents and prediction markets like Kalshi.',
        'ICE Digital Assets': 'Medium: ICE provides W3C-compliant credentials for verified identities in tokenized commodities. This is compliant for regulated markets, but less robust. US pro-tech tailwinds leverage incumbent advantages against prediction markets.',
        'Securitize': 'High: Securitize\'s DS Protocol offers W3C-compliant credentials for regulated token issuance. This ensures interoperability and compliance, critical for institutional trust and medium-term adoption in securities markets. US tailwinds strengthen against prediction markets.',
        'NYSE (via ICE)': 'Medium: NYSE uses W3C-compliant credentials for verified identities in tokenized funds. This is compliant, but less robust. US pro-tech push enhances incumbent advantages against prediction markets.',
        'Corda': 'High: Corda’s confidential identities act as W3C-compliant DIDs for banks, ensuring verified credentials. This supports regulatory compliance and interoperability, driving medium-term adoption for private RWA tokenization. Global competition favors integration with prediction markets.',
        'Centrifuge': 'Medium: Centrifuge uses pool-based credentials for RWAs, partially W3C-compliant. While sufficient for DeFi, it lacks the robust interoperability of dedicated DID systems, limiting institutional trust. US shift may favor vs prediction markets.',
        'CME GCUL': 'Medium: CME GCUL provides institutional identities with W3C potential for derivatives. While compliant, it lacks dedicated DID robustness, sufficient but not optimal for broad institutional adoption. US tailwinds enhance vs prediction markets.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s proposed platform includes institutional credentials with W3C potential. While compliant, it lacks dedicated DID robustness, sufficient but not optimal for institutional adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3 provides credentials for tokenized carbon RWAs, partially W3C-compliant. While sufficient for regional markets, it lacks robust interoperability, limiting global institutional trust. Brazil lags US tailwinds vs prediction markets.',
        'Polymesh': 'High: Polymesh’s built-in KYC offers W3C-compliant credentials for securities. This ensures regulatory compliance and interoperability, critical for institutional trust and medium-term adoption in regulated markets. Swiss edge aids vs US prediction markets.',
        'Realio Network': 'Medium: Realio’s open-source DIDs for RWA tokenization are partially W3C-compliant. While sufficient for DeFi, they lack the robust interoperability of enterprise systems, limiting institutional appeal. US pro-tech may boost vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned tokens include potential W3C-compliant credentials. While compliant for Japan, they lack robust interoperability, sufficient but not optimal for global institutional use. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Medium: DTCC uses institutional IDs via partners, with partial W3C compliance. While sufficient for collateral, it lacks dedicated DID robustness, limiting broad institutional trust. US tailwinds enhance vs prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT’s bank network IDs offer potential DID add-ons, partially W3C-compliant. While sufficient for payments, they lack robust interoperability, limiting institutional RWA adoption. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Low: Ripple lacks native W3C-compliant DIDs, relying on external integrations. This limits interoperability and regulatory compliance for institutional RWA trading, unsuitable for broad adoption. US shift may aid vs prediction markets.',
        'LME Modernization': 'Low: LME’s traditional exchange lacks a credentials system, with no W3C compliance. This limits its suitability for modern institutional RWA trading, lacking interoperability and trust. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana’s wallet-based DIDs provide verified credentials, partially W3C-compliant. While sufficient for DeFi, they lack the robust interoperability of enterprise systems, limiting institutional trust. US shift may favor vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s ENS/Verite offers W3C-compliant DIDs for DeFi. While sufficient, they lack the robust interoperability of permissioned systems, limiting institutional RWA adoption. US tailwinds may aid vs prediction markets.',
        'SHFE Initiatives': 'Low: SHFE’s traditional exchange lacks DID systems or W3C compliance. This limits its suitability for modern institutional RWA trading, lacking interoperability and trust. China competes with US vs prediction markets.',
        'Kalshi': 'High: Kalshi’s CFTC-regulated platform offers W3C-compliant credentials for verified identities in event contracts. This supports regulatory compliance and trust, critical for institutional adoption in prediction RWAs. US tailwinds strengthen against prediction peers.',
        'Polymarket': 'High: Polymarket’s decentralized platform integrates W3C-compliant DIDs for verified identities in predictions. This ensures compliance and trust, driving medium-term adoption. US relaunch strengthens against incumbents and prediction peers.',
        'Crypto.com': 'High: Crypto.com’s CFTC-regulated exchange offers W3C-compliant credentials for verified identities in event contracts. This supports compliance and trust, critical for institutional adoption. US tailwinds strengthen against prediction peers.',
        'RobinHood': 'Medium: RobinHood’s retail platform offers partial W3C-compliant credentials for verified identities in event trading. While sufficient, it lacks robustness for broad RWAs. US approvals support medium-term adoption.',
        'PredictIt': 'Medium: PredictIt’s regulated platform offers partial W3C-compliant credentials for verified identities in political predictions. While compliant, it lacks robustness for global RWAs. US approvals support medium-term adoption.',
        'Augur': 'Medium: Augur’s decentralized platform offers W3C-compliant credentials for verified identities in predictions. While sufficient for DeFi, it lacks robustness for institutional RWAs. US regulatory shift supports adoption.',
        'Provenance Foundation': 'High: Provenance Foundation\'s W3C-compliant DIDs and verifiable credentials automate KYC/AML, enhancing trust with $12B+ RWA TVL. Its Cosmos SDK interoperability with 70+ institutions outpaces Solana\'s public model. US pro-tech tailwinds boost adoption, while prediction markets like Polymarket lag in compliance depth, solidifying Provenance\'s RWA leadership.',
        'Bakkt': 'High: Bakkt\'s KYC/AML tools align with W3C for verifiable credentials in RWA custody. Partnerships with ICE ensure interoperability, boosting trust. US BitLicense outpaces EU MiCAR, while prediction markets like Polymarket lag in compliance depth. ',
        'Tether': 'Medium: Tether\'s KYC via Bitfinex offers partial W3C alignment, but lacks Circle\'s Mint-level compliance. Partnerships with 100+ exchanges aid trust, though NYAG scrutiny moderates. US tailwinds boost vs EU MiCAR, lagging Polymarket in depth. ',
        'Circle': 'High: Circle\'s KYC/AML via Circle Mint aligns with W3C for verifiable credentials in RWA custody. Partnerships with 70+ institutions ensure interoperability, boosting trust. US BitLicense outpaces EU MiCAR, while prediction markets like Polymarket lag in depth. '
    },
    'Private Ownership with Real-World Legal Finality (MLETR-like) (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s PDT embeds MLETR-compliant legal claims for tokenized gold/MMFs, ensuring enforceable ownership. This aligns with Singapore regulations and global sandboxes, critical for institutional trust and medium-term RWA adoption. Amid jurisdictional competition, this positions Abaxx to leverage innovation against US pro-tech shifts and prediction markets.',
        'LSE DMI': 'High: LSE DMI ensures MLETR-compliant legal finality for tokenized funds under UK regulations. This provides enforceable ownership, critical for institutional trust and medium-term adoption in EU/UK markets. In global competition, this strengthens LSE against US tailwinds and prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion aligns with MiCAR and MLETR-like standards for tokenized bonds, ensuring enforceable ownership. This supports institutional trust and medium-term adoption across pan-European markets. Amid regulatory competition, this aids Seturion against US pro-tech and prediction markets.',
        'Ondo Finance': 'High: Ondo’s UCC/MLETR-compliant legal wrappers for Treasuries ensure enforceable ownership. Partnerships with JPMorgan enhance regulatory alignment, critical for institutional trust and medium-term RWA adoption. US pro-tech boosts vs prediction markets.',
        'ICE Digital Assets': 'High: ICE aligns with MLETR for tokenized carbon/commodities, ensuring legal finality. This supports regulated markets, critical for institutional trust and medium-term adoption globally. US tailwinds strengthen against prediction markets.',
        'Securitize': 'High: Securitize’s regulated tokens align with UCC for legal finality, ensuring enforceable ownership. This supports compliance and institutional trust, critical for medium-term adoption in securities markets. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'High: NYSE aligns with UCC/MLETR for tokenized funds, with SEC talks ensuring legal finality. This supports institutional trust and medium-term adoption in regulated markets. US pro-tech strengthens against prediction markets.',
        'Corda': 'High: Corda’s MLETR/ETR-compliant contracts with notaries ensure legal finality for RWAs. This aligns with bank requirements, critical for institutional trust and medium-term adoption. Global competition favors integration with prediction markets.',
        'Centrifuge': 'High: Centrifuge’s legal wrappers for credit/assets are MLETR-compliant, ensuring enforceable ownership. This supports regulatory alignment, critical for institutional trust and medium-term RWA adoption. DeFi focus aids vs prediction markets.',
        'CME GCUL': 'High: CME GCUL’s tokenized derivatives align with UCC/MLETR, ensuring legal finality. This supports institutional trust and medium-term adoption in regulated derivatives markets. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'High: Nasdaq’s proposed platform aligns with SEC rules and UCC for legal finality. This ensures enforceable ownership, critical for institutional trust and medium-term adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'High: B3 aligns with Brazil’s regulations for tokenized carbon RWAs, with MLETR potential. This ensures legal finality, critical for institutional trust and medium-term adoption regionally. Brazil competes with US vs prediction markets.',
        'Polymesh': 'High: Polymesh’s regulated securities align with legal finality standards, ensuring enforceable ownership. This supports compliance and institutional trust, critical for medium-term adoption. Swiss edge aids vs prediction markets.',
        'Realio Network': 'High: Realio’s MLETR-compliant assets for real estate/art ensure enforceable ownership. This aligns with global regulations, critical for institutional trust and medium-term RWA adoption. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'High: TSE/JPX’s tokenized securities are regulated as stocks with legal finality in Japan. This ensures enforceable ownership, critical for institutional trust and medium-term adoption. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'High: DTCC’s tokenized collateral aligns with UCC/MLETR, ensuring legal finality. This supports institutional trust and medium-term adoption in US clearing markets. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT’s trade finance aligns with MLETR via bank rules, ensuring partial legal finality. This is sufficient for payments but less robust for institutional RWA adoption. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s tokenized assets use validator finality with partial MLETR alignment. This is sufficient for payments but lacks full legal enforceability for institutional RWAs. US shift boosts vs prediction markets.',
        'LME Modernization': 'Medium: LME aligns with UK regulations for metals but lacks tokenization. This provides partial legal finality, insufficient for modern institutional RWA trading. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana’s fast tokenization uses MLETR via wrappers, providing partial legal finality. This is sufficient for DeFi but lacks robust enforceability for institutional RWAs. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s smart contracts align with MLETR via wrappers and UCC Article 12. This provides partial legal finality, sufficient for DeFi but limited for institutional RWAs. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Medium: SHFE aligns with China’s regulations for commodities, providing partial legal finality. Without tokenization, it’s insufficient for modern institutional RWA trading. China competes with US vs prediction markets.',
        'Kalshi': 'High: Kalshi’s CFTC-regulated contracts align with MLETR for event RWAs, ensuring legal finality. This supports institutional trust and medium-term adoption. US tailwinds strengthen against prediction peers.',
        'Polymarket': 'High: Polymarket’s tokenized predictions align with MLETR, ensuring legal finality. This supports compliance and trust, driving medium-term adoption. US relaunch strengthens against incumbents and prediction peers.',
        'Crypto.com': 'High: Crypto.com’s CFTC-regulated contracts align with MLETR for event RWAs, ensuring legal finality. This supports compliance and trust, critical for institutional adoption. US tailwinds strengthen against prediction peers.',
        'RobinHood': 'Medium: RobinHood’s regulated contracts provide partial MLETR alignment for event RWAs, ensuring legal finality. This is sufficient, but lacks robustness for broad RWAs. US approvals support medium-term adoption.',
        'PredictIt': 'Medium: PredictIt’s regulated contracts provide partial MLETR alignment for political RWAs, ensuring legal finality. This is compliant, but lacks robustness for global RWAs. US approvals support medium-term adoption.',
        'Augur': 'Medium: Augur’s decentralized contracts provide partial MLETR alignment for prediction RWAs, ensuring legal finality. This is sufficient for DeFi, but lacks robustness for institutional RWAs. US regulatory shift supports adoption.',
        'Provenance Foundation': 'High: Provenance Foundation\'s MLETR-aligned smart contracts ensure legal finality for tokenized RWAs like loans, backed by $12B+ TVL. Cosmos IBC with 70+ institutions provides enforceable title, surpassing Ethereum\'s public model. US regulatory tailwinds enhance adoption, outpacing prediction markets like Kalshi in institutional trust for long-term RWA scalability.',
        'Bakkt': 'High: Bakkt\'s UCC-aligned custody ensures MLETR-like finality for tokenized commodities, redeemable in USDC. ICE\'s regulated framework supports enforceable title, critical for RWAs. US tailwinds challenge EU incumbents, outpacing prediction markets like Kalshi in legal depth. ',
        'Tether': 'Medium: Tether\'s USDT supports MLETR-like finality for tokenized assets via Paxos, but opaque reserves limit enforceability. $5B RWA collateral aids, though US tailwinds challenge EU incumbents less than Circle. Kalshi lags in legal depth. ',
        'Circle': 'High: Circle\'s USYC (via Hashnote) ensures MLETR-like finality for tokenized treasuries, redeemable in USDC. $1.3B TVL supports enforceable title, critical for RWAs. US tailwinds challenge EU incumbents, outpacing prediction markets like Kalshi in legal depth. '
    },
    'Private RWA Trading with T+0 Settlement (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s Q4 2025 pilots with MineHub enable atomic T+0 settlement for gold/MMFs. This reduces counterparty risk and enhances efficiency, critical for institutional adoption and medium-term competitiveness in commodity markets. In jurisdictional competition, this positions Abaxx against US incumbents and prediction markets like Kalshi.',
        'LSE DMI': 'High: LSE DMI’s blockchain settlement enables instant T+0 for tokenized funds. This reduces risk and boosts efficiency, critical for institutional adoption and medium-term competitiveness in EU/UK markets. Amid global competition, this strengthens LSE against US tailwinds and prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion achieves up to 90% cost reduction with T+0 settlement for securities. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in pan-European markets. EU\'s stance competes with US pro-tech and prediction markets.',
        'Ondo Finance': 'High: Ondo’s on-chain funds use atomic swaps for T+0 settlement. This reduces counterparty risk, supporting institutional adoption and medium-term competitiveness in DeFi and TradFi markets. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'High: ICE enables T+0 via stablecoins for tokenized carbon/commodities in futures/spot markets. This enhances efficiency, critical for institutional adoption and medium-term competitiveness globally. US tailwinds strengthen against prediction markets.',
        'Securitize': 'High: Securitize’s ATS enables secondary T+0 trading for regulated tokens. This reduces risk and boosts efficiency, critical for institutional adoption and medium-term competitiveness in securities markets. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'High: NYSE’s T+0 pilots via stablecoins for tokenized funds enhance efficiency. This supports institutional adoption and medium-term competitiveness in regulated markets, leveraging ICE’s network. US pro-tech strengthens against prediction markets.',
        'Corda': 'High: Corda’s private RWA tokenization enables instant DvP settlement. This reduces counterparty risk, critical for bank adoption and medium-term competitiveness in institutional markets. Global competition favors integration with prediction markets.',
        'Centrifuge': 'High: Centrifuge’s DeFi atomic swaps enable T+0 for credit/assets. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in multi-chain DeFi markets. US shift aids vs prediction markets.',
        'CME GCUL': 'High: CME GCUL’s pilots enable T+0 settlement for tokenized derivatives. This reduces risk, critical for institutional adoption and medium-term competitiveness in regulated derivatives markets. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'High: Nasdaq’s proposed platform aims for T+0 tokenized securities trading. This enhances efficiency, critical for institutional adoption and medium-term competitiveness in regulated markets. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s tokenization for carbon RWAs lacks full T+0 capabilities. While sufficient regionally, it’s less competitive for institutional adoption compared to instant settlement systems. Brazil competes with US vs prediction markets.',
        'Polymesh': 'Medium: Polymesh enables token trading for securities but lacks full T+0 settlement. This is sufficient but less competitive for institutional adoption compared to instant systems. Swiss edge aids vs prediction markets.',
        'Realio Network': 'Medium: Realio’s DeFi integration enables T+0 trading for RWAs. While sufficient, it lacks the efficiency of enterprise systems, limiting competitiveness for institutional adoption. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s planned T+0 for security tokens is under development. While sufficient for Japan, it’s less competitive globally for institutional adoption without full implementation. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Medium: DTCC’s tokenized collateral includes T+0 testing. While sufficient for pilots, it lacks full implementation, limiting competitiveness for broad institutional adoption. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT’s Linea pilots test T+0 for payments. While sufficient for banks, it lacks full RWA trading capabilities, limiting competitiveness for institutional adoption. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s DEX enables fast ~3-5s settlement for RWAs. While sufficient for payments, it lacks robust T+0 for institutional trading, limiting competitiveness. US shift boosts vs prediction markets.',
        'LME Modernization': 'Low: LME’s traditional trading lacks T+0 settlement, relying on legacy systems. This limits efficiency and competitiveness for institutional RWA adoption in modern markets. UK lags US vs prediction markets.',
        'Solana': 'High: Solana’s high-throughput blockchain enables T+0 trading for RWAs. This enhances efficiency, critical for DeFi adoption and medium-term competitiveness, despite TradFi integration challenges. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s ERC-1400 enables T+0 with ~16min finality. While sufficient for DeFi, it’s less competitive than instant settlement systems for institutional RWA adoption. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Low: SHFE’s traditional settlement lacks T+0 capabilities, relying on legacy systems. This limits efficiency and competitiveness for institutional RWA adoption in modern markets. China competes with US vs prediction markets.',
        'Kalshi': 'High: Kalshi’s on-chain platform enables T+0 settlement for event contracts. This reduces risk, supporting institutional adoption and competitiveness. US CFTC boosts vs prediction peers.',
        'Polymarket': 'High: Polymarket’s DeFi atomic swaps enable T+0 for predictions. This enhances efficiency, critical for adoption and competitiveness in multi-chain markets. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'High: Crypto.com’s DeFi swaps enable T+0 for event contracts. This reduces risk, supporting institutional adoption and competitiveness. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood’s on-chain enables T+0 for events. This is sufficient, but less competitive for broad RWAs. US approvals support medium-term adoption.',
        'PredictIt': 'Medium: PredictIt’s platform enables T+0 for political contracts. This is compliant, but lacks robustness for global RWAs. US approvals support medium-term adoption.',
        'Augur': 'Medium: Augur’s DeFi enables T+0 for predictions. This is sufficient for DeFi, but lacks robustness for institutional RWAs. US regulatory shift supports adoption.',
        'Provenance Foundation': 'Medium: Provenance Foundation supports T+0 settlement via Cosmos SDK for tokenized RWAs, but lacks the instant atomicity of Ondo\'s JPMorgan integration. With $12B+ TVL, it ensures trust, though US pro-tech tailwinds favor faster systems. Prediction markets like Polymarket face similar limits, balancing Provenance\'s RWA efficiency with institutional needs.',
        'Bakkt': 'High: Bakkt enables T+0 via Bakkt USD for tokenized assets, reducing risk with Circle integration. This supports institutional trading, leveraging ICE partnerships. US pro-tech boosts vs prediction markets like Polymarket, ensuring medium-term RWA efficiency. ',
        'Tether': 'High: Tether\'s USDT enables T+0 across blockchains, reducing risk with $50B monthly volume. This supports institutional trading, leveraging exchange integrations. US pro-tech boosts vs prediction markets like Polymarket, ensuring medium-term RWA efficiency. ',
        'Circle': 'High: Circle\'s USDT enables T+0 across blockchains, reducing risk with $19.4B YTD volume. This supports institutional trading, leveraging exchange integrations. US pro-tech boosts vs prediction markets like Polymarket, ensuring medium-term RWA efficiency. '
    },
    'Cross-Border T+0 for RWAs (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s Q4 2025 pilots focus on cross-jurisdictional T+0 for commodities via MineHub. This enhances global liquidity, supporting long-term scalability and institutional adoption across markets. In a competitive landscape, this positions Abaxx against US incumbents and prediction markets.',
        'LSE DMI': 'High: LSE DMI’s EU/UK focus leverages MiCA for cross-border T+0 fund transfers. This enhances global liquidity, supporting long-term scalability and institutional adoption in regulated markets. This competes with US tailwinds and prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion’s pan-European platform with stablecoin integrations enables cross-border T+0 for securities. This enhances liquidity, supporting long-term scalability and institutional adoption. EU\'s stance competes with US pro-tech and prediction markets.',
        'Ondo Finance': 'High: Ondo’s cross-chain DvP enables global T+0 transfers for tokenized Treasuries. This enhances liquidity, supporting long-term scalability and institutional adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'High: ICE’s global ecosystem supports cross-border T+0 via stablecoins and registries. This enhances liquidity, supporting long-term scalability and institutional adoption for commodities. US tailwinds strengthen against prediction markets.',
        'Securitize': 'Medium: Securitize’s global focus for funds supports partial cross-border T+0. While sufficient, it’s less robust than dedicated global systems, limiting long-term scalability. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'High: NYSE leverages ICE’s global network for cross-border T+0 fund transfers. This enhances liquidity, supporting long-term scalability and institutional adoption in regulated markets. US pro-tech boosts vs prediction markets.',
        'Corda': 'Medium: Corda’s interoperability supports cross-border T+0 for banks. While sufficient, it’s less robust than global ecosystems, limiting long-term scalability for broad RWA adoption. Global competition favors vs prediction markets.',
        'Centrifuge': 'High: Centrifuge’s V3 multi-chain protocol enables cross-chain T+0 for RWAs. This enhances global liquidity, supporting long-term scalability and institutional adoption in DeFi. US shift aids vs prediction markets.',
        'CME GCUL': 'Medium: CME GCUL supports global payments via CME’s network for T+0. While sufficient, it’s US-focused, limiting long-term scalability for broad cross-border RWA adoption. US tailwinds strengthen vs prediction markets.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s US-focused platform has cross-border T+0 extensions. While sufficient, it’s less robust than global systems, limiting long-term scalability for adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s Latin America focus supports regional cross-border T+0 for carbon RWAs. This limits global liquidity and long-term scalability for institutional adoption. Brazil competes with US vs prediction markets.',
        'Polymesh': 'Medium: Polymesh supports cross-border regulations for securities T+0. While sufficient, it’s less robust than global ecosystems, limiting long-term scalability for adoption. Swiss edge aids vs prediction markets.',
        'Realio Network': 'High: Realio’s Cosmos-based cross-chain T+0 supports global RWA transfers. This enhances liquidity, supporting long-term scalability and institutional adoption in DeFi markets. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s Asia-focused platform supports regional cross-border T+0. While sufficient, it’s less robust globally, limiting long-term scalability for adoption. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Low: DTCC’s US-focused collateral pilot lacks cross-border T+0 capabilities. This limits global liquidity and long-term scalability for institutional RWA adoption. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'High: SWIFT’s blockchain supports cross-border T+0 for payments. This enhances global liquidity, supporting long-term scalability and institutional adoption in banking. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'High: Ripple’s cross-border T+0 payments support RWA trading. This enhances global liquidity, supporting long-term scalability and institutional adoption, despite limited RWA focus. US shift boosts vs prediction markets.',
        'LME Modernization': 'Medium: LME’s global metals hub supports partial cross-border T+0. Without blockchain, it’s less robust, limiting long-term scalability for institutional RWA adoption. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana’s cross-chain T+0 via Wormhole supports RWA trading. While sufficient, bridge dependencies limit global liquidity and long-term scalability for adoption. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s cross-chain T+0 via bridges supports RWA trading. While sufficient, bridge dependencies limit global liquidity and long-term scalability for adoption. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Medium: SHFE’s cross-border investor expansion supports partial T+0. Without blockchain, it’s less robust, limiting long-term scalability for institutional RWA adoption. China competes with US vs prediction markets.',
        'Kalshi': 'High: Kalshi’s global design supports cross-border T+0 for event RWAs, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US CFTC boosts vs prediction peers.',
        'Polymarket': 'High: Polymarket’s cross-chain supports cross-border T+0 for predictions, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'High: Crypto.com’s global reach supports cross-border T+0 for event RWAs, leveraging US hub. This enhances liquidity, supporting long-term scalability and adoption. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood\'s US focus limits cross-border T+0 for event RWAs, but approvals aid. This is sufficient, but less robust than global systems, limiting scalability. US approvals support medium-term adoption.',
        'PredictIt': 'Medium: PredictIt\'s US focus limits cross-border T+0 for political RWAs, but approvals aid. This is sufficient, but less robust than global systems, limiting scalability. US approvals support medium-term adoption.',
        'Augur': 'Medium: Augur\'s DeFi supports cross-border T+0 for prediction RWAs. While sufficient, it lacks robustness for global scalability. US regulatory shift supports adoption.',
        'Provenance Foundation': 'High: Provenance Foundation\'s IBC interoperability enables cross-border T+0 settlement for RWAs, leveraging Cosmos SDK with 70+ institutions. This exceeds Ripple\'s payment focus, supported by US pro-tech tailwinds. Prediction markets like Kalshi lag in cross-jurisdictional reach, enhancing Provenance\'s edge in global RWA scalability.',
        'Bakkt': 'Medium: Bakkt\'s API supports cross-border T+0 via ICE\'s global network, but US focus limits MiCA alignment. Partnerships with 70+ institutions aid liquidity, though prediction markets like Kalshi\'s CFTC approvals outpace in speed. ',
        'Tether': 'High: Tether\'s multi-chain support facilitates cross-border T+0 for USDT in RWAs, with $120B market cap aiding liquidity. US focus limits MiCA, but Sino Global partnerships outpace Kalshi\'s CFTC scope in global reach. ',
        'Circle': 'High: Circle\'s CCTP V2 facilitates cross-border T+0 for USDC in RWAs, with $55B market cap aiding liquidity. US focus limits MiCA, but XDC/Plume partnerships outpace Kalshi\'s CFTC scope in global reach. '
    },
    'TradFi Integration Friction/Cost (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx’s DLT-agnostic APIs integrate seamlessly with existing trading infrastructure, minimizing disruption. This reduces costs and barriers, critical for medium-term institutional adoption in commodity markets. In jurisdictional competition, this positions Abaxx against US incumbents and prediction markets.',
        'LSE DMI': 'Low: LSE DMI\'s APIs integrate with existing fund infrastructure, minimizing friction. This ensures low-cost onboarding, critical for medium-term institutional adoption in EU/UK markets. Amid global competition, this strengthens LSE against US tailwinds and prediction markets.',
        'Deutsche Boerse Seturion': 'Low: Seturion’s unified APIs integrate seamlessly with bank systems, minimizing disruption. This reduces costs, critical for medium-term institutional adoption in pan-European markets. EU\'s stance competes with US pro-tech and prediction markets.',
        'Ondo Finance': 'Low: Ondo’s JPMorgan integration via Kinexys reduces friction for tokenized Treasuries. This ensures low-cost onboarding, critical for medium-term institutional adoption in DeFi/TradFi. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'Low: ICE leverages existing exchange infrastructure, ensuring low-cost integration for members. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US tailwinds strengthen against prediction markets.',
        'Securitize': 'Low: Securitize’s enterprise APIs enable seamless integration with financial systems. This reduces costs, critical for medium-term institutional adoption in regulated securities markets. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'Low: NYSE leverages ICE’s infrastructure for low-cost integration of tokenized funds. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US pro-tech boosts vs prediction markets.',
        'Corda': 'Low: Corda’s bank-friendly APIs integrate with ISVs/back-offices, minimizing updates. This reduces costs, critical for medium-term institutional adoption in private RWA markets. Global competition favors vs prediction markets.',
        'Centrifuge': 'Medium: Centrifuge’s DeFi focus requires APIs for TradFi integration, increasing friction. While manageable, this limits seamless onboarding compared to enterprise systems for institutional adoption. US shift aids vs prediction markets.',
        'CME GCUL': 'Low: CME GCUL leverages CME’s infrastructure for low-cost integration of derivatives. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq integrates with existing systems for low-cost tokenized securities. This minimizes friction, critical for medium-term institutional adoption in regulated markets. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Low: B3 integrates with its exchange infrastructure for low-cost carbon RWA trading. This minimizes friction, critical for medium-term institutional adoption regionally. Brazil competes with US vs prediction markets.',
        'Polymesh': 'Low: Polymesh’s institutional tools enable seamless integration for securities. This reduces costs, critical for medium-term institutional adoption in regulated markets. Swiss edge aids vs prediction markets.',
        'Realio Network': 'Medium: Realio’s SDKs require some integration effort for TradFi systems. While manageable, this increases friction compared to enterprise solutions, limiting seamless institutional adoption. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX integrates with existing systems for low-cost securities trading. This minimizes friction, critical for medium-term institutional adoption in Japan. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Low: DTCC integrates with clearing infrastructure for low-cost collateral trading. This minimizes friction, critical for medium-term institutional adoption in the US. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Low: SWIFT extends its network for low-cost blockchain integration. This minimizes friction, critical for medium-term institutional adoption in banking. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Low: Ripple’s bank APIs enable low-cost integration for cross-border payments. This minimizes friction, critical for medium-term institutional adoption, despite limited RWA focus. US shift boosts vs prediction markets.',
        'LME Modernization': 'Low: LME leverages existing systems for low-cost metals trading. This minimizes friction, critical for medium-term institutional adoption, despite lacking blockchain. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana’s SDKs require integration effort for TradFi systems. High throughput is offset by less native compatibility, increasing friction for institutional adoption. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s high gas fees and custom APIs increase integration effort for TradFi. This raises friction, limiting seamless institutional adoption compared to enterprise systems. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Low: SHFE leverages existing commodity infrastructure for low-cost integration. This minimizes friction, critical for medium-term institutional adoption, despite lacking blockchain. China competes with US vs prediction markets.',
        'Kalshi': 'Low: Kalshi\'s CFTC platform integrates with low friction for event RWAs. This minimizes costs, critical for medium-term adoption. US approvals boost vs prediction peers.',
        'Polymarket': 'Medium: Polymarket\'s DeFi platform requires APIs, increasing friction for TradFi integration. This is manageable, but limits seamless adoption. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'Medium: Crypto.com\'s exchange requires effort for TradFi integration, increasing friction. This is manageable, but limits seamless adoption. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Low: RobinHood\'s retail platform integrates with low friction for event RWAs. This minimizes costs, critical for medium-term adoption. US approvals support.',
        'PredictIt': 'Low: PredictIt\'s regulated platform integrates with low friction for political RWAs. This minimizes costs, critical for medium-term adoption. US approvals support.',
        'Augur': 'Medium: Augur\'s DeFi platform requires APIs, increasing friction for TradFi integration. This is sufficient for DeFi, but limits institutional adoption. US shift supports.',
        'Provenance Foundation': 'Low: Provenance Foundation\'s Cosmos SDK reduces TradFi friction with $12B+ RWA TVL and 70+ institutional integrations, but legacy bank interfaces add moderate cost. US pro-tech tailwinds aid, though prediction markets like Polymarket bypass such friction, necessitating Provenance to streamline for competitive RWA adoption.',
        'Bakkt': 'Low: Bakkt\'s ICE integration minimizes friction for RWA custody, reducing costs with SOC 2 compliance. This outperforms Solana\'s DeFi gaps, leveraging US tailwinds. Prediction markets like Polymarket face higher barriers, positioning Bakkt for institutional adoption. ',
        'Tether': 'Low: Tether\'s exchange integrations minimize friction for RWA liquidity, with SOC 1 reducing costs. This outperforms Solana\'s DeFi gaps, leveraging US tailwinds. Prediction markets like Polymarket face higher barriers, aiding Tether\'s adoption. ',
        'Circle': 'Low: Circle\'s Circle Mint minimizes friction for RWA custody, with SOC 2 reducing costs. This outperforms Solana\'s DeFi gaps, leveraging US tailwinds. Prediction markets like Polymarket face higher barriers, aiding Circle\'s adoption. '
    },
    'Centralization vs. Decentralization Balance (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx\'s federated network balances centralized liquidity for immediate adoption with decentralized DeFi for long-term scalability. This supports mass RWA adoption in DeFi ecosystems. In global competition, this positions Abaxx to leverage Singapore\'s innovation against US incumbents and prediction markets.',
        'LSE DMI': 'Medium: LSE DMI\'s permissioned ledger ensures centralized liquidity but lacks a strong DeFi roadmap due to regulatory constraints. This limits long-term scalability for open RWA ecosystems. Amid US pro-tech, LSE\'s incumbent advantages aid vs prediction markets.',
        'Deutsche Boerse Seturion': 'Medium: Seturion\'s Clearstream/Euroclear integration consolidates securities liquidity but its permissioned network limits DeFi scalability. This balances immediate adoption with constrained long-term openness. EU\'s MiCAR competes with US tailwinds and prediction markets.',
        'Ondo Finance': 'High: Ondo integrates with centralized institutions like JPMorgan while supporting open DeFi protocols. This balances immediate liquidity with long-term scalability, critical for scalable RWA onboarding. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'Medium: ICE\'s exchanges ensure centralized liquidity for commodities but lack a strong DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US tailwinds strengthen against prediction markets.',
        'Securitize': 'Medium: Securitize’s enterprise platform integrates with centralized markets but its permissioned design limits DeFi scalability. This balances immediate adoption with constrained long-term openness. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'Medium: NYSE’s ICE network consolidates fund liquidity but lacks a strong DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US pro-tech boosts vs prediction markets.',
        'Corda': 'Medium: Corda’s bank-friendly APIs ensure centralized liquidity, with a Solana bridge for DeFi potential. Its permissioned core limits long-term scalability for open RWA ecosystems. Global competition favors integration with prediction markets.',
        'Centrifuge': 'High: Centrifuge’s V3 multi-chain protocol supports decentralized RWA onboarding with TradFi APIs. This balances immediate liquidity with long-term scalability, critical for open DeFi ecosystems. US shift aids vs prediction markets.',
        'CME GCUL': 'Medium: CME\'s network ensures centralized derivatives liquidity but its permissioned L1 limits DeFi scalability. This balances immediate adoption with constrained long-term openness. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq consolidates securities liquidity but lacks a clear DeFi roadmap due to regulation. This limits long-term scalability for open RWA ecosystems. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s exchange supports regional carbon RWA liquidity but its centralized design limits DeFi potential. This constrains long-term scalability for open ecosystems. Brazil competes with US vs prediction markets.',
        'Polymesh': 'Medium: Polymesh’s permissioned PoS ensures regulated securities liquidity but lacks a strong DeFi roadmap. This limits long-term scalability for open RWA ecosystems. Swiss edge aids vs prediction markets.',
        'Realio Network': 'High: Realio’s Cosmos interoperability enables decentralized RWA onboarding with TradFi SDKs. This balances immediate liquidity with long-term scalability, critical for open DeFi ecosystems. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX’s exchange-led, centralized design integrates with Japan’s markets but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Low: DTCC’s centralized platform ensures clearing liquidity but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Low: SWIFT’s bank-controlled platform supports centralized payments but lacks a DeFi roadmap. This limits long-term scalability for open RWA ecosystems, focusing on banking. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s federated validators and bank APIs ensure centralized liquidity, with open tokenization for DeFi. Limited RWA focus constrains long-term scalability. US shift boosts vs prediction markets.',
        'LME Modernization': 'Low: LME’s centralized exchange supports metals liquidity but lacks blockchain/DeFi capabilities. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana’s decentralized DeFi ecosystem offers scalability but weak TradFi integration limits centralized liquidity. This balances long-term openness with constrained immediate adoption. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s DeFi ecosystem supports scalability but high friction limits centralized liquidity. This balances long-term openness with constrained immediate institutional adoption. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Low: SHFE’s centralized exchange supports commodity liquidity but lacks blockchain/DeFi capabilities. This limits long-term scalability for open RWA ecosystems, focusing on immediate adoption. China competes with US vs prediction markets.',
        'Kalshi': 'Medium: Kalshi’s centralized prediction liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US regulatory approvals.',
        'Polymarket': 'High: Polymarket’s decentralized prediction liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'High: Crypto.com’s hybrid event liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood’s centralized retail liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US approvals.',
        'PredictIt': 'Medium: PredictIt’s centralized political liquidity with limited DeFi balances immediate adoption with constrained openness. This supports long-term scalability for open RWA ecosystems, focusing on US approvals.',
        'Augur': 'High: Augur’s decentralized prediction liquidity supports long-term scalability for open RWA ecosystems. This balances immediate adoption with openness, critical for DeFi vs incumbents. US shift boosts vs prediction peers.',
        'Provenance Foundation': 'Medium: Provenance Foundation balances centralization with proof-of-stake governance, supporting 70+ institutions while maintaining decentralization for $12B+ RWA TVL. This aligns with US pro-tech, but lags Solana\'s public model. Prediction markets like Kalshi face similar trade-offs, positioning Provenance for medium-term RWA stability.',
        'Bakkt': 'Medium: Bakkt balances centralized custody with DeFi APIs, supporting regulated liquidity but limiting permissionless access. ICE\'s incumbent power aids vs Kalshi, though US pro-tech pressures for openness. ',
        'Tether': 'Low: Tether\'s centralized reserve model limits decentralization for USDT in RWAs, despite 15+ chain support. ICE\'s power aids vs Kalshi, but US pro-tech pressures for openness, moderating its RWA stability. ',
        'Circle': 'Medium: Circle balances centralized custody with DeFi APIs for USDC in RWAs, supporting regulated liquidity but limiting permissionless access. ICE\'s power aids vs Kalshi, though US pro-tech pressures for openness. '
    },
    'Privacy for Positions/Flows (Anti-Reverse Engineering) (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s 5-layer cryptographic system protects trade positions from reverse engineering, ensuring institutional confidentiality in RWA markets. This aligns with wholesale finance needs, supporting medium-term adoption. In global competition, this positions Abaxx against US incumbents and prediction markets like Kalshi.',
        'LSE DMI': 'High: LSE DMI’s Azure-based ledger uses confidential messaging to protect fund positions. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in EU/UK markets. Amid US pro-tech, this strengthens LSE against prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion’s permissioned DLT hides securities positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in pan-European markets. EU\'s stance competes with US tailwinds and prediction markets.',
        'Ondo Finance': 'High: Ondo’s on-chain privacy protocols obscure Treasury positions, preventing reverse engineering. This ensures institutional trust, critical for medium-term adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'High: ICE’s regulated platforms use encryption to hide commodity positions. This prevents reverse engineering, ensuring institutional trust for medium-term adoption globally. US tailwinds strengthen against prediction markets.',
        'Securitize': 'High: Securitize’s DS Protocol obscures token positions via permissioned encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in securities markets. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'High: NYSE’s ICE integration hides fund positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption in regulated markets. US pro-tech boosts vs prediction markets.',
        'Corda': 'High: Corda’s point-to-point messaging obscures bank positions, preventing reverse engineering. This ensures institutional trust, critical for medium-term adoption in private RWA markets. Global competition favors vs prediction markets.',
        'Centrifuge': 'Medium: Centrifuge’s pool-based privacy obscures credit positions but is less robust than permissioned systems. This is sufficient but limits trust for broad institutional adoption. US shift aids vs prediction markets.',
        'CME GCUL': 'Medium: CME GCUL obscures derivative positions but is less robust than dedicated systems. This is sufficient but limits trust for broad institutional adoption. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq obscures securities positions but lacks advanced encryption. This is sufficient but limits trust for broad institutional adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3 obscures carbon RWA positions regionally but is less robust globally. This is sufficient but limits trust for global institutional adoption. Brazil competes with US vs prediction markets.',
        'Polymesh': 'High: Polymesh’s privacy-by-design obscures securities positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption. Swiss edge aids vs prediction markets.',
        'Realio Network': 'Medium: Realio’s cross-chain privacy obscures RWA positions but is less robust than permissioned. This is sufficient but limits trust for institutional adoption. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX obscures securities positions but is less robust than enterprise. This is sufficient but limits trust for global institutional adoption. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'High: DTCC’s permissioned DLT obscures collateral positions via encryption. This prevents reverse engineering, ensuring institutional trust for medium-term adoption. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT obscures payment positions but is less robust than dedicated. This is sufficient but limits trust for broad institutional RWA adoption. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Low: Ripple offers limited privacy for RWA positions, risking exposure. This limits institutional trust, unsuitable for broad adoption. US shift boosts vs prediction markets.',
        'LME Modernization': 'Medium: LME obscures metals positions via access controls but lacks blockchain privacy. This is sufficient but limits trust for modern institutional adoption. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana uses ZK add-ons for privacy, protecting RWA positions. This is sufficient, but less robust than permissioned. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum’s ZK-rollups obscure RWA positions but are less robust than permissioned. This is sufficient, but limits trust for institutional adoption. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Low: SHFE offers limited privacy for commodity positions, risking exposure. This limits institutional trust, unsuitable for modern adoption. China competes with US vs prediction markets.',
        'Kalshi': 'High: Kalshi’s regulated platform uses encryption to obscure event positions. This prevents reverse engineering, ensuring trust for medium-term adoption. US CFTC boosts vs prediction peers.',
        'Polymarket': 'Medium: Polymarket’s DeFi privacy obscures prediction positions but is less robust. This is sufficient, but limits trust for broad adoption. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'Medium: Crypto.com obscures event positions but is less robust than dedicated. This is sufficient, but limits trust for broad RWA adoption. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood obscures event positions but lacks advanced encryption. This is sufficient, but limits trust for broad RWA adoption. US approvals support.',
        'PredictIt': 'Medium: PredictIt obscures political positions but is less robust than dedicated. This is sufficient, but limits trust for broad RWA adoption. US approvals support.',
        'Augur': 'Medium: Augur’s DeFi privacy obscures prediction positions but is less robust. This is sufficient, but limits trust for institutional RWA adoption. US shift supports.',
        'Provenance Foundation': 'High: Provenance Foundation\'s privacy-by-design on Cosmos SDK protects positions with encrypted flows, reducing reverse-engineering risks for $12B+ RWA TVL. This outpaces Ethereum\'s public exposure, aided by US pro-tech. Prediction markets like Polymarket face similar threats, but Provenance\'s institutional focus ensures robust RWA security.',
        'Bakkt': 'High: Bakkt\'s SOC 2 encryption protects RWA positions from reverse engineering, ensuring confidentiality for $30B+ volume. This outpaces Ethereum\'s public exposure, with US tailwinds enhancing trust vs Polymarket. ',
        'Tether': 'Medium: Tether\'s SOC 1 encryption protects USDT flows, but opaque reserves moderate privacy. This outpaces Ethereum\'s exposure less than Circle, with US tailwinds aiding vs Polymarket\'s threats. ',
        'Circle': 'High: Circle\'s SOC 2 encryption protects USDC flows from reverse engineering, ensuring confidentiality for $19.4B volume. This outpaces Ethereum\'s public exposure, with US tailwinds enhancing trust vs Polymarket. '
    },
    'Minimizes Oracles/Bridges Risks (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s federated design minimizes oracle/bridge risks via native data integration. This reduces vulnerabilities, enhancing reliability for institutional RWA adoption in commodity markets. In global competition, this positions Abaxx against US incumbents and prediction markets.',
        'LSE DMI': 'High: LSE DMI\'s permissioned ledger avoids oracles/bridges, using internal data feeds. This reduces vulnerabilities, enhancing reliability for institutional adoption in EU/UK fund markets. Amid US pro-tech, this strengthens LSE against prediction markets.',
        'Deutsche Boerse Seturion': 'High: Seturion\'s internal data feeds minimize oracle/bridge risks for securities. This enhances reliability, critical for institutional adoption in pan-European markets. EU\'s stance competes with US tailwinds and prediction markets.',
        'Ondo Finance': 'High: Ondo\'s native integrations with JPMorgan minimize oracle/bridge risks for Treasuries. This enhances reliability, critical for institutional adoption in DeFi/TradFi markets. US regulatory shift boosts vs prediction markets.',
        'ICE Digital Assets': 'High: ICE\'s regulated platforms minimize oracle/bridge use via internal feeds. This enhances reliability, critical for institutional adoption in commodity markets. US tailwinds strengthen against prediction markets.',
        'Securitize': 'High: Securitize\'s permissioned platform avoids oracles/bridges, using internal data. This enhances reliability, critical for institutional adoption in securities markets. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'High: NYSE\'s ICE integration minimizes oracle/bridge risks via internal feeds. This enhances reliability, critical for institutional adoption in regulated fund markets. US pro-tech boosts vs prediction markets.',
        'Corda': 'High: Corda\'s notary-based design avoids oracles/bridges, using bank data. This enhances reliability, critical for institutional adoption in private RWA markets. Global competition favors vs prediction markets.',
        'Centrifuge': 'Medium: Centrifuge\'s multi-chain pools rely on limited oracles/bridges, introducing some risks. This is sufficient but less reliable than permissioned systems for institutional adoption. US shift aids vs prediction markets.',
        'CME GCUL': 'Medium: CME GCUL uses internal feeds but relies on some oracles for derivatives. This introduces risks, limiting reliability for broad institutional adoption. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq\'s platform uses internal feeds but may rely on oracles for securities. This introduces risks, limiting reliability for institutional adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3\'s platform uses internal feeds but relies on some oracles for RWAs. This introduces risks, limiting reliability for global institutional adoption. Brazil competes with US vs prediction markets.',
        'Polymesh': 'High: Polymesh\'s permissioned design minimizes oracle/bridge risks via internal data. This enhances reliability, critical for institutional adoption in securities markets. Swiss edge aids vs prediction markets.',
        'Realio Network': 'Medium: Realio\'s Cosmos bridges introduce some oracle risks for RWAs. This is sufficient but less reliable than permissioned systems for institutional adoption. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX uses internal feeds but may rely on oracles. This introduces risks, limiting reliability for global institutional adoption. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'High: DTCC\'s permissioned DLT minimizes oracle/bridge risks via internal feeds. This enhances reliability, critical for institutional adoption in clearing markets. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT’s Linea integration relies on some oracles for payments. This introduces risks, limiting reliability for broad institutional RWA adoption. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s validator-based design uses limited oracles for RWAs. This introduces risks, limiting reliability for institutional adoption compared to permissioned systems. US shift boosts vs prediction markets.',
        'LME Modernization': 'High: LME\'s legacy systems avoid oracles/bridges, using internal data. This enhances reliability but lacks blockchain, limiting suitability for modern institutional adoption. UK lags US vs prediction markets.',
        'Solana': 'Low: Solana\'s DeFi relies heavily on oracles/bridges like Wormhole, increasing vulnerabilities. This limits reliability for institutional RWA adoption compared to permissioned systems. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Low: Ethereum\'s DeFi relies on oracles/bridges, increasing vulnerabilities. This limits reliability for institutional RWA adoption compared to permissioned systems. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Medium: SHFE\'s legacy systems use internal data but lack blockchain oracles. This is sufficient but limits reliability for modern institutional RWA adoption. China competes with US vs prediction markets.',
        'Kalshi': 'Medium: Kalshi’s regulated platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals boost vs prediction peers.',
        'Polymarket': 'Medium: Polymarket’s DeFi relies on oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'Medium: Crypto.com’s exchange relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood’s platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals support.',
        'PredictIt': 'Medium: PredictIt’s regulated platform relies on limited oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US approvals support.',
        'Augur': 'Medium: Augur’s DeFi relies on oracles, introducing some risks. This is sufficient but less reliable than permissioned systems. US shift supports.',
        'Provenance Foundation': 'Medium: Provenance Foundation minimizes oracle/bridge risks with Cosmos IBC, reducing attack vectors for $12B+ RWA TVL. However, multi-chain reliance moderates this edge compared to Corda\'s notary model. US pro-tech tailwinds help, though prediction markets like Kalshi share similar vulnerabilities, balancing Provenance\'s RWA reliability.',
        'Bakkt': 'Medium: Bakkt minimizes oracle risks with internal ICE feeds, but Circle bridges add moderate exposure for RWAs. This is sufficient for custody, though Kalshi\'s CFTC model reduces similar vulnerabilities. ',
        'Tether': 'Medium: Tether minimizes oracle risks with internal feeds for USDT, but multi-chain bridges add moderate exposure for RWAs. This matches Circle\'s custody, though Kalshi\'s CFTC model reduces similar vulnerabilities. ',
        'Circle': 'Medium: Circle minimizes oracle risks with internal feeds for USDC, but CCTP bridges add moderate exposure for RWAs. This is sufficient for custody, though Kalshi\'s CFTC model reduces similar vulnerabilities. '
    },
    'Liquidity Fragmentation Risk (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx\'s federated network consolidates commodity liquidity across global markets, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. In global competition, this positions Abaxx against US incumbents and prediction markets.',
        'LSE DMI': 'Medium: LSE DMI’s EU/UK focus risks partial fragmentation outside its region. While sufficient regionally, it’s less unified than global platforms for institutional trading. UK\'s stance aids vs US tailwinds and prediction markets.',
        'Deutsche Boerse Seturion': 'Low: Seturion’s Clearstream/Euroclear integration consolidates securities liquidity across Europe, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. EU\'s stance competes with US tailwinds and prediction markets.',
        'Ondo Finance': 'Medium: Ondo\'s DeFi/TradFi hybrid risks fragmentation across chains. While manageable with JPMorgan integration, it’s less unified than permissioned platforms for institutional trading. US shift boosts vs prediction markets.',
        'ICE Digital Assets': 'Low: ICE’s global exchange network consolidates commodity liquidity, minimizing fragmentation. This ensures efficient trading, critical for medium-term institutional adoption. US tailwinds strengthen against prediction markets.',
        'Securitize': 'Medium: Securitize’s ATS risks fragmentation across jurisdictions. While sufficient, it’s less unified than exchange-led platforms, limiting institutional trading efficiency. US approvals boost vs prediction markets.',
        'NYSE (via ICE)': 'Low: NYSE’s ICE network consolidates fund liquidity globally. This minimizes fragmentation, critical for medium-term institutional adoption. US pro-tech boosts vs prediction markets.',
        'Corda': 'Medium: Corda’s bank network risks fragmentation outside its ecosystem. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Global competition favors vs prediction markets.',
        'Centrifuge': 'Medium: Centrifuge’s multi-chain pools risk fragmentation across DeFi protocols. While sufficient, it’s less unified than permissioned systems, limiting institutional trading efficiency. US shift aids vs prediction markets.',
        'CME GCUL': 'Medium: CME GCUL’s US focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US tailwinds strengthen against prediction markets.',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq’s exchange integration ensures unified securities liquidity. This minimizes fragmentation, critical for medium-term institutional adoption. US pro-tech boosts vs prediction markets.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s regional focus risks fragmentation outside Latin America. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Brazil competes with US vs prediction markets.',
        'Polymesh': 'Medium: Polymesh’s securities focus risks fragmentation across jurisdictions. While sufficient, it’s less unified than exchange-led platforms, limiting institutional trading efficiency. Swiss edge aids vs prediction markets.',
        'Realio Network': 'Medium: Realio’s cross-chain design risks fragmentation across DeFi ecosystems. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US pro-tech boosts vs prediction markets.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s Japan focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. Japan competes with US vs prediction markets.',
        'DTCC Collateral Pilot': 'Medium: DTCC’s US focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US tailwinds strengthen against prediction markets.',
        'SWIFT Blockchain': 'Medium: SWIFT’s bank network risks fragmentation outside banking. While sufficient, it’s less unified than global platforms, limiting institutional RWA trading efficiency. Global competition with US vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s federated ledger risks fragmentation for non-payment RWAs. While sufficient, it’s less unified than dedicated platforms, limiting institutional trading efficiency. US shift boosts vs prediction markets.',
        'LME Modernization': 'Medium: LME\'s legacy exchange risks fragmentation without blockchain integration. While sufficient, it’s less unified than tokenized platforms, limiting institutional efficiency. UK lags US vs prediction markets.',
        'Solana': 'Medium: Solana\'s DeFi ecosystem risks fragmentation across protocols. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US pro-tech boosts vs prediction markets.',
        'Ethereum': 'Medium: Ethereum\'s DeFi ecosystem risks fragmentation across L2s/protocols. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US tailwinds aid vs prediction markets.',
        'SHFE Initiatives': 'Medium: SHFE\'s legacy exchange risks fragmentation globally. While sufficient, it’s less unified than tokenized platforms, limiting institutional trading efficiency. China competes with US vs prediction markets.',
        'Kalshi': 'Medium: Kalshi’s regional focus risks fragmentation outside US. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals boost vs prediction peers.',
        'Polymarket': 'Medium: Polymarket’s DeFi ecosystem risks fragmentation across chains. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US relaunch boosts vs prediction peers.',
        'Crypto.com': 'Medium: Crypto.com’s exchange risks fragmentation across markets. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US CFTC boosts vs prediction peers.',
        'RobinHood': 'Medium: RobinHood’s retail focus risks fragmentation outside US. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals support.',
        'PredictIt': 'Medium: PredictIt’s niche focus risks fragmentation globally. While sufficient, it’s less unified than global platforms, limiting institutional trading efficiency. US approvals support.',
        'Augur': 'Medium: Augur’s DeFi ecosystem risks fragmentation across chains. While sufficient, it’s less unified than permissioned platforms, limiting institutional trading efficiency. US shift supports.',
        'Provenance Foundation': 'Medium: Provenance Foundation faces moderate liquidity fragmentation with $12B+ RWA TVL across 70+ institutions, but IBC interoperability mitigates splits. US pro-tech aids, though prediction markets like Polymarket pose competitive pressure. This balances Provenance\'s RWA depth against incumbent advantages like CME\'s volumes.',
        'Bakkt': 'Low: Bakkt\'s ICE network consolidates RWA liquidity, minimizing fragmentation for tokenized commodities. US tailwinds and $500M+ quarterly volume outpace Kalshi, ensuring efficient institutional trading. ',
        'Tether': 'Low: Tether\'s $120B USDT consolidates RWA liquidity, minimizing fragmentation with $10B+ quarterly volume. US tailwinds outpace Kalshi, ensuring efficient institutional trading across 100+ exchanges. ',
        'Circle': 'Low: Circle\'s $55B USDC consolidates RWA liquidity, minimizing fragmentation with $500M+ quarterly volume. US tailwinds outpace Kalshi, ensuring efficient institutional trading. '
    },
    'Susceptibility to Malicious Manipulation/Hacking (High Impact)': {
        'Abaxx (ID++/PDT)': 'Low: Abaxx\'s federated blockchain with 5-layer encryption and regular audits minimizes hacking risks. This permissioned design ensures robust security, critical for institutional trust in commodity markets. In a competitive landscape, it leverages Singapore\'s innovation to challenge US incumbents, whose pro-tech tailwinds may enhance their defenses. Prediction markets like Kalshi pose new threats, but Abaxx\'s privacy focus reduces vulnerability to malicious manipulation.',
        'LSE DMI': 'Low: LSE DMI\'s Azure-backed permissioned ledger employs enterprise-grade security, minimizing manipulation risks. This ensures trust for fund trading in EU/UK, aligning with MiCA. Amid US pro-tech shifts, LSE\'s incumbent volumes aid resilience, but less tech-savvy jurisdictions may lag. Prediction markets like Polymarket introduce competition, but LSE\'s centralized control and audits reduce susceptibility, maintaining medium-term adoption without DeFi\'s exposure.',
        'Deutsche Boerse Seturion': 'Low: Seturion\'s permissioned DLT with Clearstream security minimizes manipulation risks. Robust encryption ensures trust in pan-European securities, compliant with MiCAR. EU incumbents compete with US tailwinds, but prediction markets like Kalshi challenge innovation. This focus on security reduces vulnerability, strengthening Seturion\'s position against US pro-tech and emerging competitors in RWAs.',
        'Ondo Finance': 'Medium: Ondo\'s hybrid DeFi/TradFi platform faces moderate hacking risks due to open integrations. Audits mitigate, but less robust than permissioned systems. US regulatory shift boosts adaptability, challenging incumbents, yet prediction markets like Polymarket add competitive pressure. Ondo\'s on-chain privacy offers some protection, supporting medium-term trust amidst evolving manipulation threats.',
        'ICE Digital Assets': 'Low: ICE\'s regulated platform with enterprise security minimizes malicious risks. This ensures trust in commodity RWAs, leveraging US tailwinds and incumbent volumes. Prediction markets like Kalshi pose disruption, but ICE\'s centralized control and audits reduce vulnerability, maintaining leadership in global competition against manipulation attempts.',
        'Securitize': 'Low: Securitize\'s permissioned DS Protocol with audits minimizes hacking risks. This enhances trust in token issuance, boosted by US approvals vs EU. Prediction markets challenge, but Securitize\'s compliance focus and security measures reduce susceptibility, positioning it resiliently against incumbents and emerging manipulation threats.',
        'NYSE (via ICE)': 'Low: NYSE\'s ICE-integrated platform with enterprise security minimizes manipulation risks. US pro-tech and incumbent power enhance defenses, supported by audits. Prediction markets like Polymarket face barriers, allowing NYSE to maintain stability and outpace emerging threats in the RWA space with robust defenses.',
        'Corda': 'Low: Corda\'s permissioned notary-based DLT minimizes hacking risks for banks. Regular audits and encryption ensure trust, competing with US tailwinds. Prediction markets like Kalshi pose innovation threats, but Corda\'s security focus reduces vulnerability, supporting medium-term RWA adoption in a competitive landscape.',
        'Centrifuge': 'Medium: Centrifuge\'s multi-chain DeFi exposes it to moderate manipulation risks from bridges. US shift favors incumbents, but audits mitigate. Prediction markets like Polymarket add pressure, with Centrifuge\'s privacy offering partial protection in RWAs.',
        'CME GCUL': 'Low: CME GCUL\'s permissioned L1 with enterprise security minimizes risks. US tailwinds and incumbent volumes strengthen defenses, supported by audits. Prediction markets like Kalshi face barriers, allowing CME to reduce vulnerability and maintain leadership in derivatives against manipulation attempts.',
        'Nasdaq Tokenized Securities': 'Low: Nasdaq\'s proposed platform with enterprise security minimizes hacking risks. US pro-tech enhances defenses. Prediction markets like Kalshi compete, but Nasdaq\'s audits reduce vulnerability in RWAs.',
        'B3 Digitas/ACXRWA': 'Medium: B3\'s regional platform faces moderate risks from exposure. Brazil lags US tailwinds, increasing vulnerability. Prediction markets pose threats, but audits mitigate susceptibility vs incumbents.',
        'Polymesh': 'Low: Polymesh\'s permissioned PoS with privacy-by-design minimizes hacking risks. Swiss catalyst aids defenses. Prediction markets challenge, but Polymesh\'s audits reduce susceptibility, balancing vs US incumbents.',
        'Realio Network': 'Medium: Realio\'s Cosmos-based L1 faces moderate risks from cross-chain exposure. US pro-tech boosts defenses, but prediction markets add pressure. Audits mitigate susceptibility in RWAs.',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX\'s regulated platform with enterprise security minimizes risks. Japan competes with US, but lags tailwinds. Prediction markets challenge, but audits reduce susceptibility in RWAs.',
        'DTCC Collateral Pilot': 'Low: DTCC\'s permissioned DLT minimizes manipulation risks. US tailwinds enhance defenses. Prediction markets pose threats, but audits reduce vulnerability in RWAs.',
        'SWIFT Blockchain': 'Medium: SWIFT\'s Linea-integrated blockchain faces moderate risks from Ethereum exposure. Global competition balances vs prediction markets. Audits mitigate susceptibility, but centralized focus increases vulnerability.',
        'Ripple (XRP Ledger)': 'Medium: Ripple\'s federated ledger faces moderate risks from validator exposure. US shift boosts defenses. Prediction markets challenge, but audits mitigate susceptibility in cross-border RWAs.',
        'LME Modernization': 'Low: LME\'s legacy system with robust controls minimizes risks. UK trails US tailwinds, but audits reduce susceptibility. Prediction markets like Polymarket threaten, but LME\'s focus aids resilience.',
        'Solana': 'High: Solana\'s public blockchain faces high risks from DeFi exposure. US pro-tech challenges incumbents, but prediction markets align, increasing susceptibility to manipulation in RWAs.',
        'Ethereum': 'High: Ethereum\'s public blockchain faces high risks from oracle and L2 exposure. US tailwinds force adaptation, with prediction markets adding pressure, heightening susceptibility in RWAs.',
        'SHFE Initiatives': 'Low: SHFE\'s legacy system minimizes risks with controls. China competes with US, but lacks tailwinds. Prediction markets pose threats, but SHFE\'s focus reduces susceptibility in commodities.',
        'Kalshi': 'Low: Kalshi\'s regulated platform minimizes risks with enterprise security. US CFTC approvals enhance defenses. As a prediction market, it challenges incumbents with low susceptibility to manipulation.',
        'Polymarket': 'Medium: Polymarket\'s decentralized platform faces moderate risks from on-chain exposure. US relaunch boosts defenses. Audits mitigate, but DeFi focus increases susceptibility vs incumbents.',
        'Crypto.com': 'Medium: Crypto.com\'s exchange faces moderate risks from integrations. US shift enhances defenses. As a prediction market, it challenges incumbents with partial susceptibility to manipulation.',
        'RobinHood': 'Medium: RobinHood\'s platform faces moderate risks from retail exposure. US approvals aid defenses. Limited DeFi increases susceptibility, but challenges prediction markets in RWAs.',
        'PredictIt': 'Medium: PredictIt\'s regulated platform faces moderate risks from focus. US approvals enhance defenses. Scope limits susceptibility, but challenges incumbents in prediction RWAs.',
        'Augur': 'High: Augur\'s DeFi platform faces high risks from decentralized exposure. US shift boosts defenses. Audits mitigate, but high susceptibility challenges incumbents in prediction RWAs.',
        'Provenance Foundation': 'Medium: Provenance Foundation\'s proof-of-stake minimizes hacking risks with $12B+ RWA TVL, but multi-chain exposure moderates security vs Corda\'s notary model. US pro-tech tailwinds enhance defenses, though prediction markets like Polymarket face similar threats, balancing Provenance\'s RWA resilience.',
        'Bakkt': 'Low: Bakkt\'s NYDFS-regulated custody with SOC 2 minimizes hacking risks for RWAs, leveraging ICE\'s infrastructure. US pro-tech tailwinds enhance defenses vs Polymarket, reducing vulnerability for $30B+ volume. ',
        'Tether': 'Medium: Tether\'s CFTC-registered custody with SOC 1 minimizes hacking risks, but reserve opacity adds moderate exposure for RWAs. US pro-tech tailwinds enhance defenses vs Polymarket, reducing vulnerability for $50B volume. ',
        'Circle': 'Low: Circle\'s BitLicense-regulated custody with SOC 2 minimizes hacking risks for RWAs, leveraging US pro-tech. This reduces vulnerability for $19.4B volume, outpacing Polymarket. '
    },
    'Regulatory Adaptability to Evolving Global Standards (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s compliance with Singapore’s MAS framework and MLETR standards enables seamless adaptation to global regulatory shifts like MiCAR and UCC. This flexibility allows quick integration of new rules without architectural changes, critical for institutional scalability. Amid US pro-tech tailwinds challenging EU incumbents, Abaxx leverages its modular design to stay ahead of prediction markets like Kalshi, ensuring long-term RWA compliance without added complexity.',
        'LSE DMI': 'Medium: LSE DMI’s MiCA alignment supports EU/UK regulatory adaptation, but slower updates lag US pro-tech speed. While compliant, this limits rapid response to global changes, constraining scalability. UK’s incumbent advantages aid resilience, but prediction markets like Polymarket’s agile models pressure LSE, requiring infrastructure upgrades to maintain medium-term RWA leadership in a competitive jurisdictional landscape.',
        'Deutsche Boerse Seturion': 'Medium: Seturion’s MiCAR compliance enables EU regulatory adaptation, but bureaucratic processes slow global alignment. This supports institutional trust but limits agility against US pro-tech tailwinds. Prediction markets like Kalshi challenge innovation, forcing Seturion to enhance modular design to compete, ensuring medium-term RWA scalability without excessive regulatory friction.',
        'Ondo Finance': 'High: Ondo’s UCC/MLETR framework and JPMorgan partnerships facilitate rapid adaptation to US pro-tech shifts and global standards. This modular approach integrates new rules efficiently, enhancing institutional trust. Prediction markets like Polymarket add pressure, but Ondo’s hybrid model balances agility, positioning it to lead RWA compliance and scalability in a competitive landscape.',
        'ICE Digital Assets': 'Medium: ICE’s UCC alignment supports US regulatory adaptation, but commodity focus limits global flexibility. While compliant, this constrains response to MiCA-like changes. Prediction markets like Kalshi challenge, requiring ICE to upgrade infrastructure to maintain incumbent advantages and medium-term RWA leadership against evolving international standards.',
        'Securitize': 'Medium: Securitize’s SEC/UCC compliance enables US regulatory adaptation, but niche scope limits global scalability. This supports trust but lags against EU MiCAR agility. Prediction markets like Kalshi pressure innovation, forcing Securitize to enhance modular design to compete, ensuring medium-term RWA compliance in a dynamic landscape.',
        'NYSE (via ICE)': 'Medium: NYSE’s UCC/SEC alignment supports US regulatory adaptation, but exchange focus limits flexibility. This ensures compliance but slows global response. Prediction markets like Polymarket challenge, requiring NYSE to adapt infrastructure to maintain incumbent dominance and medium-term RWA scalability against evolving standards.',
        'Corda': 'Medium: Corda’s bank-compliant design enables regulatory adaptation, but enterprise focus slows global alignment. This supports trust but lags against US pro-tech speed. Prediction markets like Kalshi pressure, forcing Corda to enhance modularity to compete, ensuring medium-term RWA compliance in a competitive jurisdictional environment.',
        'Centrifuge': 'High: Centrifuge’s MLETR/DeFi framework facilitates rapid adaptation to global standards like MiCA and UCC. This modular approach integrates new rules efficiently, enhancing institutional trust. Prediction markets like Polymarket add pressure, but Centrifuge’s multi-chain design balances agility, positioning it to lead RWA compliance and scalability.',
        'CME GCUL': 'Medium: CME GCUL’s CFTC alignment supports US regulatory adaptation, but derivative focus limits flexibility. This ensures compliance but slows global response. Prediction markets like Kalshi challenge, requiring CME to upgrade infrastructure to maintain incumbent dominance and medium-term RWA scalability against evolving standards.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s SEC/UCC alignment enables US regulatory adaptation, but securities focus limits global agility. This supports trust but lags against MiCA-like changes. Prediction markets like Polymarket pressure, forcing Nasdaq to enhance modularity to compete, ensuring medium-term RWA compliance in a dynamic landscape.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s Brazilian compliance supports regional regulatory adaptation, but lags global standards like MiCA. This ensures trust but limits scalability. Prediction markets like Kalshi challenge, requiring B3 to upgrade infrastructure to compete, balancing medium-term RWA compliance with international regulatory evolution.',
        'Polymesh': 'Medium: Polymesh’s securities-compliant design enables regulatory adaptation, but Swiss focus slows global alignment. This supports trust but lags against US pro-tech speed. Prediction markets like Kalshi pressure, forcing Polymesh to enhance modularity to compete, ensuring medium-term RWA compliance in a competitive environment.',
        'Realio Network': 'High: Realio’s Cosmos/MLETR framework facilitates rapid adaptation to global standards like MiCA and UCC. This modular approach integrates new rules efficiently, enhancing institutional trust. Prediction markets like Polymarket add pressure, but Realio’s cross-chain design balances agility, positioning it to lead RWA compliance and scalability.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s Japanese compliance supports regional regulatory adaptation, but lags global standards like MiCA. This ensures trust but limits scalability. Prediction markets like Kalshi challenge, requiring TSE/JPX to upgrade infrastructure to compete, balancing medium-term RWA compliance with international regulatory evolution.',
        'DTCC Collateral Pilot': 'Medium: DTCC’s clearing-compliant design enables regulatory adaptation, but US focus slows global alignment. This supports trust but lags against MiCA-like changes. Prediction markets like Polymarket pressure, forcing DTCC to enhance modularity to compete, ensuring medium-term RWA compliance in a dynamic landscape.',
        'SWIFT Blockchain': 'Medium: SWIFT’s bank-compliant design enables regulatory adaptation, but payment focus limits RWA flexibility. This supports trust but lags against US pro-tech speed. Prediction markets like Kalshi pressure, forcing SWIFT to enhance modularity to compete, ensuring medium-term RWA compliance in a competitive environment.',
        'Ripple (XRP Ledger)': 'Medium: Ripple’s payment-compliant design enables regulatory adaptation, but scrutiny limits RWA flexibility. This supports trust but lags against MiCA-like changes. Prediction markets like Polymarket pressure, forcing Ripple to enhance modularity to compete, ensuring medium-term RWA compliance in a dynamic landscape.',
        'LME Modernization': 'Low: LME’s legacy-compliant design limits regulatory adaptability for RWAs, lagging global standards like MiCA. This constrains trust and scalability. Prediction markets like Kalshi challenge, requiring LME to upgrade infrastructure to compete, but headwinds hinder medium-term RWA compliance and adoption.',
        'Solana': 'Medium: Solana’s DeFi-compliant design enables regulatory adaptation, but public chain limits flexibility. This supports trust but lags against MiCA-like changes. Prediction markets like Polymarket pressure, forcing Solana to enhance modularity to compete, ensuring medium-term RWA compliance in a competitive environment.',
        'Ethereum': 'Medium: Ethereum’s DeFi-compliant design enables regulatory adaptation, but multi-chain complexity limits flexibility. This supports trust but lags against US pro-tech speed. Prediction markets like Kalshi pressure, forcing Ethereum to enhance modularity to compete, ensuring medium-term RWA compliance in a dynamic landscape.',
        'SHFE Initiatives': 'Low: SHFE’s legacy-compliant design limits regulatory adaptability for RWAs, lagging global standards like MiCA. This constrains trust and scalability. Prediction markets like Polymarket challenge, requiring SHFE to upgrade infrastructure to compete, but headwinds hinder medium-term RWA compliance and adoption.',
        'Kalshi': 'High: Kalshi’s CFTC-compliant design enables rapid regulatory adaptation for prediction RWAs, aligning with global standards like MiCA. This supports trust and scalability, critical for institutional adoption. US tailwinds boost competitiveness, challenging incumbents and peers in a dynamic landscape.',
        'Polymarket': 'High: Polymarket’s DeFi-compliant design enables regulatory adaptation, with US relaunch aligning with global standards like MiCA. This supports trust and scalability, critical for institutional adoption. Prediction market peers pressure, but Polymarket’s modularity ensures medium-term compliance and leadership.',
        'Crypto.com': 'High: Crypto.com’s CFTC-compliant design enables regulatory adaptation for event RWAs, aligning with global standards like MiCA. This supports trust and scalability, critical for institutional adoption. US tailwinds boost competitiveness, challenging incumbents and peers in a dynamic landscape.',
        'RobinHood': 'High: RobinHood’s retail-compliant design enables regulatory adaptation for event RWAs, aligning with global standards like MiCA. This supports trust and scalability, critical for institutional adoption. US approvals boost competitiveness, challenging incumbents and peers in a dynamic landscape.',
        'PredictIt': 'High: PredictIt’s prediction-compliant design enables regulatory adaptation for political RWAs, aligning with global standards like MiCA. This supports trust and scalability, critical for institutional adoption. US approvals boost competitiveness, challenging incumbents and peers in a dynamic landscape.',
        'Augur': 'Medium: Augur’s DeFi-compliant design enables regulatory adaptation for prediction RWAs, but decentralization limits flexibility. This supports trust but lags against MiCA-like changes. Prediction market peers pressure, forcing Augur to enhance modularity to compete, ensuring medium-term RWA compliance in a competitive environment.',
        'Provenance Foundation': 'High: Provenance Foundation\'s Cosmos SDK-based Layer 1 aligns with MLETR, UCC, and MiCAR standards, enabling seamless adaptation to global regulatory shifts via modular smart contracts and KYC/AML automation. This supports interoperability with 70+ institutions, critical for institutional trust and medium-term RWA adoption. US pro-tech tailwinds enhance its edge over EU incumbents, while prediction markets like Kalshi face similar compliance hurdles.',
        'Bakkt': 'High: Bakkt\'s NYDFS BitLicense and CFTC alignment enable rapid adaptation to UCC/MiCA, with modular custody for RWAs. US pro-tech tailwinds outpace EU, though prediction markets like Kalshi\'s CFTC approvals add competition. ',
        'Tether': 'Medium: Tether\'s CFTC registration and Hadron platform enable moderate adaptation to UCC/MiCA, but opacity issues limit modular upgrades. US pro-tech aids, though Kalshi\'s approvals challenge its compliance edge. ',
        'Circle': 'High: Circle\'s BitLicense and UCC alignment enable rapid adaptation to MiCA/SEC, with CCTP V2 for RWAs. US pro-tech tailwinds outpace EU, though Kalshi\'s CFTC approvals add competition. '
    },
    'Likelihood of Long Term Open Protocol-based DeFi (Medium Impact)': {
        'Abaxx (ID++/PDT)': 'High: Abaxx’s federated model incorporates open protocol elements for DeFi, supporting long-term scalability in RWA markets. This leverages Singapore’s innovation to compete with US incumbents and prediction markets, ensuring composability and community governance for sustainable adoption.',
        'LSE DMI': 'Medium: LSE DMI’s permissioned infrastructure limits open protocol development, constraining long-term DeFi scalability. While compliant with MiCA, it lags US pro-tech and prediction markets, requiring upgrades to maintain relevance in evolving RWA ecosystems.',
        'Deutsche Boerse Seturion': 'Medium: Seturion’s permissioned design limits open protocol flexibility, constraining long-term DeFi scalability. MiCAR compliance aids but lags US pro-tech and prediction markets, requiring modular upgrades to compete in sustainable RWA ecosystems.',
        'Ondo Finance': 'High: Ondo’s hybrid architecture supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'ICE Digital Assets': 'Medium: ICE’s regulated infrastructure limits open protocol development, constraining long-term DeFi scalability. While leveraging US tailwinds, it lags prediction markets, requiring upgrades to maintain relevance in evolving RWA ecosystems.',
        'Securitize': 'Medium: Securitize’s permissioned model limits open protocol flexibility, constraining long-term DeFi scalability. US approvals aid but lag prediction markets, requiring modular upgrades to compete in sustainable RWA ecosystems.',
        'NYSE (via ICE)': 'Medium: NYSE’s exchange infrastructure limits open protocol development, constraining long-term DeFi scalability. US pro-tech boosts but lags prediction markets, requiring upgrades to maintain relevance in evolving RWA ecosystems.',
        'Corda': 'Medium: Corda’s bank-focused design limits open protocol flexibility, constraining long-term DeFi scalability. Global support aids but lags prediction markets, requiring modular upgrades to compete in sustainable RWA ecosystems.',
        'Centrifuge': 'High: Centrifuge’s multi-chain architecture supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'CME GCUL': 'Medium: CME GCUL’s regulated infrastructure limits open protocol development, constraining long-term DeFi scalability. US tailwinds boost but lag prediction markets, requiring upgrades to maintain relevance in evolving RWA ecosystems.',
        'Nasdaq Tokenized Securities': 'Medium: Nasdaq’s exchange infrastructure limits open protocol development, constraining long-term DeFi scalability. US pro-tech boosts but lags prediction markets, requiring upgrades to maintain relevance in evolving RWA ecosystems.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s regional infrastructure limits open protocol development, constraining long-term DeFi scalability. Brazil lags US tailwinds, limiting vs prediction markets, requiring upgrades for relevance in evolving RWA ecosystems.',
        'Polymesh': 'Medium: Polymesh’s regulated design limits open protocol flexibility, constraining long-term DeFi scalability. Swiss support aids but lags prediction markets, requiring modular upgrades to compete in sustainable RWA ecosystems.',
        'Realio Network': 'High: Realio’s Cosmos interoperability supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'TSE/JPX Digital Securities': 'Low: TSE/JPX’s centralized infrastructure limits open protocol development, severely constraining long-term DeFi scalability. Japan lags US pro-tech, limiting vs prediction markets, requiring significant upgrades for relevance in evolving RWA ecosystems.',
        'DTCC Collateral Pilot': 'Low: DTCC’s clearing infrastructure limits open protocol development, severely constraining long-term DeFi scalability. US tailwinds boost but lag prediction markets, requiring significant upgrades for relevance in evolving RWA ecosystems.',
        'SWIFT Blockchain': 'Low: SWIFT’s bank infrastructure limits open protocol development, severely constraining long-term DeFi scalability. Global support aids but lags prediction markets, requiring significant upgrades for relevance in evolving RWA ecosystems.',
        'Ripple (XRP Ledger)': 'High: Ripple’s federated ledger supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'LME Modernization': 'Low: LME’s legacy infrastructure limits open protocol development, severely constraining long-term DeFi scalability. UK lags US pro-tech, limiting vs prediction markets, requiring significant upgrades for relevance in evolving RWA ecosystems.',
        'Solana': 'High: Solana’s high-throughput infrastructure supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'Ethereum': 'High: Ethereum’s ecosystem supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction markets, with composable smart contracts ensuring sustainable institutional adoption.',
        'SHFE Initiatives': 'Low: SHFE’s legacy infrastructure limits open protocol development, severely constraining long-term DeFi scalability. China lags US pro-tech, limiting vs prediction markets, requiring significant upgrades for relevance in evolving RWA ecosystems.',
        'Kalshi': 'Medium: Kalshi’s regulated infrastructure limits open protocol development, constraining long-term DeFi scalability. US CFTC support aids but lags prediction market peers, requiring upgrades for relevance in evolving RWA ecosystems.',
        'Polymarket': 'High: Polymarket’s decentralized infrastructure supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction market peers, with composable smart contracts ensuring sustainable institutional adoption.',
        'Crypto.com': 'High: Crypto.com’s hybrid infrastructure supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction market peers, with composable smart contracts ensuring sustainable institutional adoption.',
        'RobinHood': 'Medium: RobinHood’s retail infrastructure limits open protocol development, constraining long-term DeFi scalability. US approvals aid but lag prediction market peers, requiring upgrades for relevance in evolving RWA ecosystems.',
        'PredictIt': 'Medium: PredictIt’s focused infrastructure limits open protocol development, constraining long-term DeFi scalability. US approvals aid but lag prediction market peers, requiring upgrades for relevance in evolving RWA ecosystems.',
        'Augur': 'High: Augur’s decentralized infrastructure supports open protocol-based DeFi, enabling long-term scalability for RWAs. This leverages US regulatory tailwinds to challenge incumbents and prediction market peers, with composable smart contracts ensuring sustainable institutional adoption.',
        'Provenance Foundation': 'High: Provenance Foundation\'s proof-of-stake network and IBC interoperability support open protocol-based DeFi, enabling composable smart contracts for tokenized RWAs like loans and insurance. With $12B+ RWA TVL and regulatory-compliant governance, it fosters long-term scalability and community-driven upgrades. US pro-tech tailwinds challenge incumbents, aligning with prediction markets like Polymarket, but Provenance\'s enterprise-grade security ensures sustainable institutional integration.',
        'Bakkt': 'Medium: Bakkt\'s API ecosystem supports moderate open DeFi for USDC in RWAs, but centralized custody limits permissionless growth. US tailwinds aid vs Polymarket, balancing institutional scalability. ',
        'Tether': 'Medium: Tether\'s USDT supports moderate open DeFi for RWAs, but centralized reserves limit permissionless growth. US tailwinds aid vs Polymarket, balancing institutional scalability with adoption risks. ',
        'Circle': 'Medium: Circle\'s USDC supports moderate open DeFi protocols for RWAs, but centralized custody limits permissionless growth. US tailwinds aid vs Polymarket, balancing institutional scalability. '
    },
    'Incumbent Advantages (High Impact)': {
        'Abaxx (ID++/PDT)': 'Medium: Abaxx benefits from Singapore’s commodity hub, easing RWA onboarding but lacking US incumbent volumes. This balances innovation with market power, challenging US tailwinds and prediction markets like Kalshi in global competition.',
        'LSE DMI': 'High: LSE’s established fund infrastructure and UK volumes enable rapid RWA onboarding. This incumbent advantage, bolstered by MiCA, competes with US pro-tech and resists prediction market disruption like Polymarket.',
        'Deutsche Boerse Seturion': 'High: Seturion leverages Clearstream/Euroclear volumes for securities onboarding. EU incumbent power aids vs US tailwinds but lags vs prediction markets in tech innovation.',
        'Ondo Finance': 'Medium: Ondo lacks incumbent volumes but gains from JPMorgan ties. US regulatory shift boosts adaptability, potentially obsoleting traditional barriers vs prediction markets like Kalshi.',
        'ICE Digital Assets': 'High: ICE’s exchange volumes enable swift commodity RWA onboarding. US tailwinds and financial power dominate, resisting prediction market disruption like Kalshi.',
        'Securitize': 'Medium: Securitize’s enterprise focus aids token issuance but lacks volumes. US approvals enhance vs EU, leveraging tailwinds against prediction markets in RWAs.',
        'NYSE (via ICE)': 'High: NYSE’s exchange infrastructure facilitates fund onboarding. US pro-tech and incumbent power ensure leadership, potentially outpacing prediction markets in RWA space.',
        'Corda': 'Medium: Corda’s bank focus aids onboarding but lacks exchange volumes. Global competition favors US tailwinds, integrating with prediction markets in RWA adoption.',
        'Centrifuge': 'Low: Centrifuge lacks incumbent power, relying on DeFi onboarding. US regulatory push may favor incumbents, but its model challenges prediction markets in RWAs.',
        'CME GCUL': 'High: CME’s futures volumes enable rapid derivative onboarding. US tailwinds and financial power strengthen vs EU, resisting prediction market disruption.',
        'Nasdaq Tokenized Securities': 'High: Nasdaq’s securities infrastructure aids onboarding. US pro-tech and incumbent power compete with Singapore/China, resisting prediction market innovation.',
        'B3 Digitas/ACXRWA': 'Medium: B3’s regional volumes aid carbon RWA onboarding. Brazil lags US tailwinds, limiting vs global incumbents and prediction markets.',
        'Polymesh': 'Medium: Polymesh’s regulated focus aids securities but lacks volumes. Swiss catalyst aids, but US push favors incumbents over prediction markets.',
        'Realio Network': 'Low: Realio lacks incumbent power, focusing on DeFi onboarding. US tailwinds boost incumbents, but its model may challenge prediction markets in RWAs.',
        'TSE/JPX Digital Securities': 'Medium: TSE/JPX’s infrastructure aids securities onboarding. Japan competes with US, but incumbent power lags vs prediction markets in RWA innovation.',
        'DTCC Collateral Pilot': 'High: DTCC’s clearing volumes enable swift collateral onboarding. US tailwinds enhance incumbent advantages, outpacing EU/UK and prediction markets.',
        'SWIFT Blockchain': 'High: SWIFT’s bank network aids payment onboarding. Global reach competes with US incumbents, but centralized focus limits vs prediction markets.',
        'Ripple (XRP Ledger)': 'Medium: Ripple lacks exchange volumes but aids payment onboarding. US shift boosts vs EU, challenging incumbent barriers and prediction markets.',
        'LME Modernization': 'High: LME’s metals volumes enable rapid onboarding. UK lags US tailwinds, weakening vs prediction markets like Polymarket in RWA innovation.',
        'Solana': 'Low: Solana lacks incumbent power, focusing on DeFi. US incumbents adapt with tailwinds, potentially resisting Solana’s challenge to prediction markets.',
        'Ethereum': 'Low: Ethereum lacks incumbent volumes, focusing on DeFi. US pro-tech may force adoption, challenging incumbents and aligning with prediction markets in RWAs.',
        'SHFE Initiatives': 'Medium: SHFE’s commodity volumes aid onboarding. China competes with US, but lacks tailwinds to challenge incumbent dominance or prediction markets.',
        'Kalshi': 'Low: Kalshi lacks incumbent volumes, relying on event market access. US approvals leverage tailwinds, disrupting traditional barriers with prediction-based RWAs.',
        'Polymarket': 'Low: Polymarket lacks volumes, focusing on prediction onboarding. US relaunch challenges incumbents, potentially obsoleting barriers with DeFi innovations.',
        'Crypto.com': 'Medium: Crypto.com lacks full incumbent power but aids event onboarding. US tailwinds boost vs EU, disrupting incumbent advantages in RWAs.',
        'RobinHood': 'High: RobinHood’s user base aids retail onboarding. US approvals enhance incumbent advantages, but limited DeFi lags vs prediction market peers.',
        'PredictIt': 'Medium: PredictIt lacks broad volumes but aids political onboarding. US approvals provide tailwinds, but scope limits vs incumbent RWA scalability.',
        'Augur': 'Low: Augur lacks incumbent power, focusing on DeFi onboarding. US shift could boost vs incumbents, challenging traditional barriers with prediction markets.',
        'Provenance Foundation': 'Medium: Provenance Foundation leverages $12B+ RWA TVL and partnerships with 70+ institutions for efficient onboarding, but lacks the massive volumes of US incumbents like CME. Its Cosmos SDK infrastructure aids secure tokenization, balancing innovation with market power. US pro-tech tailwinds boost its edge over EU players, while prediction markets like Kalshi pose disruption through niche liquidity.',
        'Bakkt': 'High: Bakkt leverages ICE\'s $30B+ volume and global partnerships for RWA onboarding, providing incumbent edge over greenfield players. US pro-tech tailwinds resist Kalshi, ensuring leadership in tokenized commodities. ',
        'Tether': 'High: Tether leverages $120B market cap and 100+ exchange partnerships for RWA onboarding, providing incumbent edge over greenfield players. US pro-tech tailwinds resist Kalshi, ensuring leadership in tokenized liquidity. ',
        'Circle': 'High: Circle leverages $55B USDC market cap and ICE partnerships for RWA onboarding, providing incumbent edge over greenfield players. US pro-tech tailwinds resist Kalshi, ensuring leadership in tokenized commodities. '
    },
    'Regulatory Tailwinds (High Impact)': {
        'Abaxx (ID++/PDT)': 'High: Singapore’s MAS innovation sandbox and MLETR support provide strong regulatory tailwinds for Abaxx’s RWA growth. This competes with US pro-tech, accelerating adoption against EU MiCA and prediction markets like Kalshi, enhancing global scalability.',
        'LSE DMI': 'Medium: UK’s pro-innovation stance and MiCA alignment provide moderate regulatory tailwinds for LSE’s fund tokenization. This competes with US pro-tech, accelerating adoption against prediction markets like Polymarket, but bureaucratic lags limit speed.',
        'Deutsche Boerse Seturion': 'Medium: EU’s MiCAR and DLT pilots provide moderate regulatory tailwinds for Seturion’s securities tokenization. This competes with US pro-tech, accelerating adoption against prediction markets like Kalshi, but EU fragmentation limits momentum.',
        'Ondo Finance': 'High: US pro-tech shift and SEC pilots provide strong regulatory tailwinds for Ondo’s hybrid RWA tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Polymarket.',
        'ICE Digital Assets': 'High: US pro-tech tailwinds and CFTC pilots provide strong regulatory support for ICE’s commodity tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Kalshi.',
        'Securitize': 'High: US SEC approvals and UCC pilots provide strong regulatory tailwinds for Securitize’s token issuance. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Polymarket.',
        'NYSE (via ICE)': 'High: US pro-tech tailwinds and SEC pilots provide strong regulatory support for NYSE’s fund tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Kalshi.',
        'Corda': 'Medium: Global bank support and ISO 20022 alignment provide moderate regulatory tailwinds for Corda’s RWA tokenization. This accelerates adoption against prediction markets, but bank conservatism limits speed.',
        'Centrifuge': 'High: US pro-tech tailwinds and DeFi pilots provide strong regulatory support for Centrifuge’s credit tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Polymarket.',
        'CME GCUL': 'High: US CFTC approvals and pilot programs provide strong regulatory tailwinds for CME GCUL’s derivative tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Kalshi.',
        'Nasdaq Tokenized Securities': 'High: US SEC pilots and pro-tech tailwinds provide strong regulatory support for Nasdaq’s securities tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Polymarket.',
        'B3 Digitas/ACXRWA': 'Medium: Brazil’s regulatory sandbox provides moderate tailwinds for B3’s carbon tokenization. This accelerates adoption against prediction markets, but Latin America lags US pro-tech speed.',
        'Polymesh': 'Medium: Swiss FINMA support and global securities alignment provide moderate regulatory tailwinds for Polymesh’s tokenization. This accelerates adoption against prediction markets, but Swiss conservatism limits momentum.',
        'Realio Network': 'High: US pro-tech tailwinds and Cosmos interoperability boost regulatory support for Realio’s RWA tokenization. This accelerates adoption against EU MiCA, enhancing scalability against prediction markets like Kalshi.',
        'TSE/JPX Digital Securities': 'Medium: Japan’s FSA pilots provide moderate regulatory tailwinds for TSE/JPX’s securities tokenization. This accelerates adoption against prediction markets, but Asia lags US pro-tech speed.',
        'DTCC Collateral Pilot': 'High: US pro-tech tailwinds and DTCC pilots provide strong regulatory support for collateral tokenization. This accelerates adoption against EU MiCA, boosting scalability against prediction markets like Polymarket.',
        'SWIFT Blockchain': 'High: Global bank support and ISO pilots provide strong regulatory tailwinds for SWIFT’s RWA tokenization. This accelerates adoption against prediction markets, boosting cross-border scalability.',
        'Ripple (XRP Ledger)': 'Medium: US pro-tech tailwinds and Ripple’s XRP framework provide moderate regulatory support for RWA tokenization. This accelerates adoption against EU MiCA, but past scrutiny limits momentum.',
        'LME Modernization': 'Medium: UK’s FCA pilots provide moderate regulatory tailwinds for LME’s commodity tokenization. This accelerates adoption against prediction markets, but legacy infrastructure limits speed.',
        'Solana': 'Medium: US pro-tech tailwinds and Solana’s DeFi ecosystem provide moderate regulatory support for RWA tokenization. This accelerates adoption against EU MiCA, but public chain scrutiny limits momentum.',
        'Ethereum': 'Medium: US pro-tech tailwinds and Ethereum’s upgrades provide moderate regulatory support for RWA tokenization. This accelerates adoption against EU MiCA, but multi-chain complexity limits speed.',
        'SHFE Initiatives': 'Medium: China’s regulatory pilots provide moderate tailwinds for SHFE’s commodity tokenization. This accelerates adoption against prediction markets, but centralized control limits global momentum.',
        'Kalshi': 'High: US CFTC approvals and pro-tech tailwinds provide strong regulatory support for Kalshi’s prediction tokenization. This accelerates adoption against EU MiCA, boosting scalability against incumbent barriers.',
        'Polymarket': 'High: US relaunch and pro-tech tailwinds provide strong regulatory support for Polymarket’s prediction tokenization. This accelerates adoption against EU MiCA, boosting scalability against incumbent barriers.',
        'Crypto.com': 'High: US CFTC approvals and pro-tech tailwinds provide strong regulatory support for Crypto.com’s prediction tokenization. This accelerates adoption against EU MiCA, boosting scalability against incumbent barriers.',
        'RobinHood': 'High: US SEC approvals and pro-tech tailwinds provide strong regulatory support for RobinHood’s prediction tokenization. This accelerates adoption against EU MiCA, boosting scalability against incumbent barriers.',
        'PredictIt': 'High: US CFTC approvals and pro-tech tailwinds provide strong regulatory support for PredictIt’s prediction tokenization. This accelerates adoption against EU MiCA, boosting scalability against incumbent barriers.',
        'Augur': 'Medium: US pro-tech tailwinds and Augur’s DeFi ecosystem provide moderate regulatory support for prediction tokenization. This accelerates adoption against EU MiCA, but decentralized scrutiny limits momentum.',
        'Provenance Foundation': 'High: Provenance Foundation benefits from US pro-tech tailwinds, including SEC pilots and UCC alignment for tokenized financial services. Its Cosmos-based compliance (KYC/AML automation, MLETR support) accelerates RWA adoption, competing with EU MiCAR. With $30B+ in transactions, this regulatory momentum outpaces prediction markets like Polymarket, fostering secure interoperability and institutional scaling in a competitive landscape.',
        'Bakkt': 'High: Bakkt benefits from US pro-tech tailwinds and CFTC approvals, accelerating RWA custody adoption. This outpaces EU MiCAR, with ICE\'s infrastructure boosting scalability vs Polymarket. ',
        'Tether': 'High: Tether benefits from US pro-tech tailwinds and CFTC registration, accelerating RWA liquidity adoption. This outpaces EU MiCAR, with scale boosting vs Polymarket despite scrutiny. ',
        'Circle': 'High: Circle benefits from US pro-tech tailwinds and CFTC approvals, accelerating RWA custody adoption. This outpaces EU MiCAR, with ICE\'s infrastructure boosting scalability vs Polymarket. '
    }
}


points_breakdown = {
    'Abaxx (ID++/PDT)': 'Total: 53.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'LSE DMI': 'Total: 47.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Deutsche Boerse Seturion': 'Total: 48.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Ondo Finance': 'Total: 50.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'ICE Digital Assets': 'Total: 50.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Securitize': 'Total: 48.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'NYSE (via ICE)': 'Total: 48.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Corda': 'Total: 47.0. Breakdown: Encrypted P2P (High, 3 × 2 = 6), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Centrifuge': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'CME GCUL': 'Total: 42.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Nasdaq Tokenized Securities': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'B3 Digitas/ACXRWA': 'Total: 40.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Polymesh': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Realio Network': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'TSE/JPX Digital Securities': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'DTCC Collateral Pilot': 'Total: 37.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Low, 1 × 1.5 = 1.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'SWIFT Blockchain': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Low, 1 × 2.5 = 2.5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Ripple (XRP Ledger)': 'Total: 39.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Low, 1 × 1.5 = 1.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'LME Modernization': 'Total: 32.0. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Low, 1 × 2 = 2), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (High, 3 × 1.5 = 4.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Low, 1 × 2 = 2), DeFi Potential (Low, 1 × 2.5 = 2.5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Solana': 'Total: 37.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Low, 1 × 1.5 = 1.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Ethereum': 'Total: 37.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Low, 1 × 1.5 = 1.5), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'SHFE Initiatives': 'Total: 30.5. Breakdown: Encrypted P2P (Low, 1 × 2 = 2), DID/Verified (Low, 1 × 2 = 2), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Low, 1 × 2 = 2), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Low, 1 × 1.5 = 1.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (Low, 1 × 2 = 2), DeFi Potential (Low, 1 × 2.5 = 2.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (Medium, 2 × 2 = 4).',
    'Kalshi': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Polymarket': 'Total: 46.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Crypto.com': 'Total: 45.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'RobinHood': 'Total: 44.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'PredictIt': 'Total: 43.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Augur': 'Total: 42.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Medium, 2 × 2 = 4 inverted), Centralization Balance (High, 3 × 1.5 = 4.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (High, 1 × 2 = 2 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Low, 1 × 2 = 2), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Provenance Foundation': 'Total: 46.5. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (Medium, 2 × 2 = 4), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Medium, 2 × 2 = 4 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (High, 3 × 2.5 = 7.5), Incumbent Advantages (Medium, 2 × 2 = 4), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Bakkt': 'Total: 48.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (Medium, 2 × 1.5 = 3), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Tether': 'Total: 50.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (Medium, 2 × 2 = 4), Legal Finality (Medium, 2 × 2 = 4), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Low, 1 × 1.5 = 1.5), Privacy (Medium, 2 × 1.5 = 3), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Medium, 2 × 2 = 4 inverted), Regulatory Adaptability (Medium, 2 × 2 = 4), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).',
    'Circle': 'Total: 51.0. Breakdown: Encrypted P2P (Medium, 2 × 2 = 4), DID/Verified (High, 3 × 2 = 6), Legal Finality (High, 3 × 2 = 6), T+0 Trading (High, 3 × 2 = 6), Cross-Border T+0 (High, 3 × 1.5 = 4.5), TradFi Friction (Low, 3 × 2 = 6 inverted), Centralization Balance (Medium, 2 × 1.5 = 3), Privacy (High, 3 × 1.5 = 4.5), Oracles/Bridges (Medium, 2 × 1.5 = 3), Liquidity Fragmentation (Low, 3 × 2 = 6 inverted), Hacking (Low, 3 × 2 = 6 inverted), Regulatory Adaptability (High, 3 × 2 = 6), DeFi Potential (Medium, 2 × 2.5 = 5), Incumbent Advantages (High, 3 × 2 = 6), Regulatory Tailwinds (High, 3 × 2 = 6).'
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
    'Solana': 'Solana is a high-throughput public blockchain with T+0 RWA trading via Wormhole bridges, targeting DeFi with challenges in TradFi integration.',
    'Ethereum': 'Ethereum supports tokenized RWAs with ERC-1400 and ~16min T+0 via L2s, widely used in DeFi with vulnerabilities from oracles and bridges.',
    'SHFE Initiatives': 'SHFE Initiatives modernize the Shanghai Futures Exchange with partial cross-border T+0, relying on legacy systems for commodity trading.',
    'Kalshi': 'Kalshi is a US CFTC-regulated platform for event contract RWAs, offering T+0 settlement and W3C-compliant credentials for secure trading.',
    'Polymarket': 'Polymarket is a US relaunched decentralized platform for prediction RWAs, using atomic swaps for T+0 settlement and targeting DeFi markets.',
    'Crypto.com': 'Crypto.com is a CFTC-regulated exchange for event contract RWAs, providing T+0 settlement with a hybrid centralized-decentralized model.',
    'RobinHood': 'RobinHood offers regulated event RWA trading with T+0 settlement, leveraging its retail user base for US market integration.',
    'PredictIt': 'PredictIt is a US-regulated platform for political prediction RWAs, providing T+0 settlement with a focus on compliance and niche markets.',
    'Augur': 'Augur is a decentralized prediction market on Ethereum, offering T+0 settlement for RWAs with a focus on long-term DeFi potential.',
    'Provenance Foundation': 'Provenance Foundation is a US-based public proof-of-stake blockchain (Layer 1 on Cosmos SDK) designed for financial services and RWA tokenization. It supports secure issuance of tokenized assets like loans, private credit, and insurance products, with $12B+ in RWA TVL and $30B+ in transactions. Featuring the Marker module for compliant tokens and interoperability with 70+ institutions, it enables efficient tokenization, trading, and compliance for institutional scaling.',
    'Bakkt': 'Bakkt, owned by ICE, is a US-regulated digital asset infrastructure provider for RWA tokenization, offering custody, trading, and onramp services with $30B+ transaction volume. It integrates with Circle for USDC settlements and focuses on tokenized commodities and equities for institutional scaling.',
    'Tether': 'Tether, issuer of $120B USDT, launched Hadron in 2024 for RWA tokenization, enabling mass-market asset tokenization with partnerships like UAE real estate. It provides scale for settlements but faces opacity issues, bridging TradFi with DeFi liquidity.',
    'Circle': 'Circle, issuer of $55B USDC, acquired Hashnote for $1.3B USYC tokenized treasuries and launched Circle Gateway for cross-chain RWA settlements. It focuses on compliant liquidity with CCTP V2, integrating with 70+ institutions for tokenized yields and payments.'
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
