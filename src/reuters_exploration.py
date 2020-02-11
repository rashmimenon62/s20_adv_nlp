# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:51:20 2020

@author: Garrett
"""
#%% Packages
import spacy
from nltk.corpus import reuters
en = spacy.load("en_core_web_lg")

#%% Reuters exploration
reuters.readme()
d = {}
for i in reuters.categories():
    d[i] = len(reuters.fileids(i))

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

len(reuters.categories())
txt = reuters.fileids(['acq'])[0]
print(reuters.raw(txt))

# 2/4/2020
# Look for seed words and reasonable extraction patterns
# Good seed word: A seed word is some word that is generally related to this type of event.
# HW: Come in with 10 words - pull the entire sentence with seed words and doc ids.
# Think about semantic categories you are identifying.

# Setup SQL alchemy

# Next week: talk through the scoring methods

#%%
#Topic - Mergers and Acquisitions
#ex1
txt = reuters.raw(reuters.fileids(['acq'])[3])
print(txt)
"Bond Corp Holdings Ltd" #Seed
"<x> had offered" #Extraction Pattern
"""
Diaz said Australian brewer Alan Bond's Bond Corp 
  Holdings Ltd had offered 150 pesos per share for the "B" shares.
""" #Text

#ex2
txt = reuters.raw(reuters.fileids(['acq'])[4])
print(txt)
"Redland Plc" "Monier" #Seed
"<x> making an offer for <y>" #Extraction Pattern
"""
Monier Ltd &lt;MNRA.S> said talks are taking place which may lead
  to Britain's Redland Plc &lt;RDLD.L> making an offer for the
  Monier shares it does not already hold, chairman Bill Locke
  said.
""" #Text

#ex3
txt = reuters.raw(reuters.fileids(['acq'])[7])
print(txt)
"San Miguel Corp" #Seed
"bid by <y>" #Extraction Pattern
"""
A bid by San Miguel Corp (SMC) &lt;SANM.MN>
  to buy back 38.1 mln sequestered shares from United Coconut
  Planters Bank (UCPB) has been hit by two new lawsuits, sources
  in the Philippine food and brewery company said.
""" #Text

#ex4
txt = reuters.raw(reuters.fileids(['acq'])[9])
print(txt)
"Unilever" "Chesebrough" #Seed
"<x> aquired <y>" #Extraction Pattern
"""
      Unilever aquired Chesebrough for 3.2 billion dlrs in order
  to benefit from its well-known toiletry brands and food
  products.
""" #Text

#ex5
txt = reuters.raw(reuters.fileids(['acq'])[11])
print(txt)
"Conrac Corp sait" #Seed
"<x> has started negotiations" #Extraction Pattern
"""
Conrac Corp sait has started
  negotiations with several interested parties on its possible
  acquisition.
""" #Text

#ex6
txt = reuters.raw(reuters.fileids(['acq'])[12])
print(txt)
"Hawaiian Insurance Cos" #Seed
"sell <x>" #Extraction Pattern
"""
  I.U. International Co said it
  reached a preliminary agreement to sell the Hawaiian Insurance
  Cos to Hawaiian Electric Industries Inc. &lt;HE>.
      Terms of the transaction were not disclosed, the company
  said.
""" #Text

#ex7
txt = reuters.raw(reuters.fileids(['acq'])[15])
print(txt)
"Erskine Resources Ltd."#Seed
"merge with <y>" #Extraction Pattern
"""
CANADIAN BASHAW, ERSKINE RESOURCES TO MERGE
  Canadian Bashaw Leduc Oil and
  Gas Ltd said it agreed to merge with Erskine Resources Ltd.
  Terms were not disclosed.
      Ownership of the combined company with 18.8 pct for the
  current shareholders of Canadian Bashaw and 81.2 pct to the
  current shareholders of Erskine, the companies said.
""" #Text

#ex8
txt = reuters.raw(reuters.fileids(['acq'])[20])
print(txt)
"Bristol-Myers Co." #Seed
"merger with <y>" #Extraction Pattern
"""
  Sci-Med Life Systems Inc said
  its directors approved a previously proposed agreement of
  merger with Bristol-Myers Co.
""" #Text

#ex9
txt = reuters.raw(reuters.fileids(['acq'])[26])
print(txt)
"Tradevest Inc" #Seed
"acquired by <x>" #Extraction Pattern
"""
MADEIRA IN LETTER OF INTENT TO BE ACQUIRED
  &lt;Madeira Inc> said it
  signed a letter of intent to be acquired by Tradevest Inc
  through a stock-for-stock exchange.
      After completion of the transaction, Tradevest would own 90
  pct of the issued outstanding stock of Madeira.
""" #Text

#ex10
txt = reuters.raw(reuters.fileids(['acq'])[27])
print(txt)
"GGFH Inc" #Seed
"merge with <x>" #Extraction Pattern
"""
DATRON &lt;DATR> AGREES TO BUYOUT BY OFFICERS
  Datron Corp said it agreed to
  merge with GGFH Inc, a Florida-based company formed by the four
  top officers of the company.
      According to terms of the proposed transaction, each share
  of Datron common stock, excluding those shares owned by the
  four officers, will be bought for six dlrs a share, it said.
      Datron's officers hold about 73 pct of the total 896,000
  Datron common shares outstanding.
      Upon completion of the proposed transaction, the officers
  of Datron would own 100 pct of the company. The merger is
  subject to GGHF's receiving financing for the plan, Datron
  said.
      Shareholders of Datron will be asked to approve the plan at
  their annual meeting to be held in June or July, and the merger
  is expected to be completed by July 31, it said.
""" #Text

#ex11
txt = reuters.raw(reuters.fileids(['acq'])[29])
print(txt)
"Alexanders Inc" #Seed
"acquisition of <x>" #Extraction Pattern
"""
TRUMP AND INTERSTATE IN TALKS FOR ALEXANDERS
  Donald Trump and Interstate Properties
  said they were holding preliminary discussions regarding a
  possible joint acquisition of Alexanders Inc at 47 dlrs per
  share.    
      The possible acquisition is subject to any applicable real
  estate gains and transfer taxes, the joint statement said.
      Trump and Interstate, which presently own about 40 pct of
  Alexander's common stock, said they intend to keep the company
  as a retailer if they succed in their acquisition.
      There can be no assurances that the parties will reach any
  agreement regarding an acquisition or what price might be
  offered, the statement said.
""" #Text

#%%
#Topic - Trade
#ex1 - 4
txt = reuters.raw(reuters.fileids(['trade'])[0])
print(txt)
"American imports" #Seed
"curbs on <x>" #Extraction Pattern

"Taiwan's foreign exchange reserves" #Seed
"swell <x>" #Extraction Pattern

"South Korea" #Seed
"pressure on <x>" #Extraction Pattern

"Japan" #Seed
"curbs against <x>" #Extraction Pattern

"""
ASIAN EXPORTERS FEAR DAMAGE FROM U.S.-JAPAN RIFT
  Mounting trade friction between the
  U.S. And Japan has raised fears among many of Asia's exporting
  nations that the row could inflict far-reaching economic
  damage, businessmen and officials said.
      They told Reuter correspondents in Asian capitals a U.S.
  Move against Japan might boost protectionist sentiment in the
  U.S. And lead to curbs on American imports of their products.
      But some exporters said that while the conflict would hurt
  them in the long-run, in the short-term Tokyo's loss might be
  their gain.
      The U.S. Has said it will impose 300 mln dlrs of tariffs on
  imports of Japanese electronics goods on April 17, in
  retaliation for Japan's alleged failure to stick to a pact not
  to sell semiconductors on world markets at below cost.
      Unofficial Japanese estimates put the impact of the tariffs
  at 10 billion dlrs and spokesmen for major electronics firms
  said they would virtually halt exports of products hit by the
  new taxes.
      "We wouldn't be able to do business," said a spokesman for
  leading Japanese electronics firm Matsushita Electric
  Industrial Co Ltd &lt;MC.T>.
      "If the tariffs remain in place for any length of time
  beyond a few months it will mean the complete erosion of
  exports (of goods subject to tariffs) to the U.S.," said Tom
  Murtha, a stock analyst at the Tokyo office of broker &lt;James
  Capel and Co>.
      In Taiwan, businessmen and officials are also worried.
      "We are aware of the seriousness of the U.S. Threat against
  Japan because it serves as a warning to us," said a senior
  Taiwanese trade official who asked not to be named.
      Taiwan had a trade trade surplus of 15.6 billion dlrs last
  year, 95 pct of it with the U.S.
      The surplus helped swell Taiwan's foreign exchange reserves
  to 53 billion dlrs, among the world's largest.
      "We must quickly open our markets, remove trade barriers and
  cut import tariffs to allow imports of U.S. Products, if we
  want to defuse problems from possible U.S. Retaliation," said
  Paul Sheen, chairman of textile exporters &lt;Taiwan Safe Group>.
      A senior official of South Korea's trade promotion
  association said the trade dispute between the U.S. And Japan
  might also lead to pressure on South Korea, whose chief exports
  are similar to those of Japan.
      Last year South Korea had a trade surplus of 7.1 billion
  dlrs with the U.S., Up from 4.9 billion dlrs in 1985.
      In Malaysia, trade officers and businessmen said tough
  curbs against Japan might allow hard-hit producers of
  semiconductors in third countries to expand their sales to the
  U.S.
      In Hong Kong, where newspapers have alleged Japan has been
  selling below-cost semiconductors, some electronics
  manufacturers share that view. But other businessmen said such
  a short-term commercial advantage would be outweighed by
  further U.S. Pressure to block imports.
      "That is a very short-term view," said Lawrence Mills,
  director-general of the Federation of Hong Kong Industry.
      "If the whole purpose is to prevent imports, one day it will
  be extended to other sources. Much more serious for Hong Kong
  is the disadvantage of action restraining trade," he said.
      The U.S. Last year was Hong Kong's biggest export market,
  accounting for over 30 pct of domestically produced exports.
      The Australian government is awaiting the outcome of trade
  talks between the U.S. And Japan with interest and concern,
  Industry Minister John Button said in Canberra last Friday.
      "This kind of deterioration in trade relations between two
  countries which are major trading partners of ours is a very
  serious matter," Button said.
      He said Australia's concerns centred on coal and beef,
  Australia's two largest exports to Japan and also significant
  U.S. Exports to that country.
      Meanwhile U.S.-Japanese diplomatic manoeuvres to solve the
  trade stand-off continue.
      Japan's ruling Liberal Democratic Party yesterday outlined
  a package of economic measures to boost the Japanese economy.
      The measures proposed include a large supplementary budget
  and record public works spending in the first half of the
  financial year.
      They also call for stepped-up spending as an emergency
  measure to stimulate the economy despite Prime Minister
  Yasuhiro Nakasone's avowed fiscal reform program.
      Deputy U.S. Trade Representative Michael Smith and Makoto
  Kuroda, Japan's deputy minister of International Trade and
  Industry (MITI), are due to meet in Washington this week in an
  effort to end the dispute.
""" #Text

#ex5
txt = reuters.raw(reuters.fileids(['trade'])[1])
print(txt)
"Thailand's trade deficit" #Seed
"<x> widened" #Extraction Pattern
"""
THAI TRADE DEFICIT WIDENS IN FIRST QUARTER
  Thailand's trade deficit widened to 4.5
  billion baht in the first quarter of 1987 from 2.1 billion a
  year ago, the Business Economics Department said.
      It said Janunary/March imports rose to 65.1 billion baht
  from 58.7 billion. Thailand's improved business climate this
  year resulted in a 27 pct increase in imports of raw materials
  and semi-finished products.
      The country's oil import bill, however, fell 23 pct in the
  first quarter due to lower oil prices.
      The department said first quarter exports expanded to 60.6
  billion baht from 56.6 billion.
      Export growth was smaller than expected due to lower
  earnings from many key commodities including rice whose
  earnings declined 18 pct, maize 66 pct, sugar 45 pct, tin 26
  pct and canned pineapples seven pct.
      Products registering high export growth were jewellery up
  64 pct, clothing 57 pct and rubber 35 pct.
""" #Text

#ex6 - 9
txt = reuters.raw(reuters.fileids(['trade'])[4])
print(txt)
"South Korea's trade surplus" #Seed
"<x> is growing" #Extraction Pattern

"the won" #Seed
"not allow <x>" #Extraction Pattern

"the won" #Seed
"revalue <x>" #Extraction Pattern

"South Korea's exports" #Seed
"exports" #Seed
"imports" #Seed
"<x> rose" #Extraction Pattern

"""
SOUTH KOREA MOVES TO SLOW GROWTH OF TRADE SURPLUS
  South Korea's trade surplus is growing too
  fast and the government has started taking steps to slow it
  down, Deputy Prime Minister Kim Mahn-je said.
      He told a press conference the government planned to
  increase investment, speed up the opening of the local market
  to foreign imports and gradually adjust its currency to hold
  the surplus "at a proper level."
      But he said the government would not allow the won to
  appreciate too much in a short period of time. South Korea has
  been under pressure from Washington to revalue the won.
      The U.S. Wants South Korea to cut its trade surplus with
  the U.S., Which rose to 7.4 billion dlrs in 1986 from 4.3
  billion dlrs in 1985.
      Kim, who is also economic planning minister, said prospects
  were bright for the South Korean economy, but the government
  would try to hold the current account surplus to around five
  billion dlrs a year for the next five years.
      "Our government projections of eight pct GNP growth, five
  billion dlrs of (current account) surplus and 12 pct growth in
  exports all seemed to be reasonable early this year. But now
  the surplus is growing faster than we expected," he said.
      Trade ministry officials said South Korea's exports rose 35
  pct to 9.34 billion dlrs in the first three months of this
  year, while imports rose only 8.5 pct to 8.2 billion dlrs.
      Kim said the swing of South Korea's current account to a
  surplus of 4.65 billion dlrs in 1986 from an 890 mln dlr
  deficit in 1985 was very significant. The surplus enabled the
  country to reduce its foreign debt last year for the first
  time.
      South Korea's foreign debt, which fell to 44.5 billion dlrs
  in 1986 from 46.8 billion in 1985, is still among the largest
  in Asia.
      "This huge amount of our foreign debt has been one of the
  major constraints on our development... Last year was a major
  turning point for the Korean economy," Kim said.
      Kim said his government plannned to reduce the ratio of
  foreign debt to the country's GNP to about 20 pct in 1991, from
  about 50 pct in 1986.
      "The government, however, does not want to accelerate
  reducing the debt by making an excessive trade surplus," he
  said.
      Kim said a sudden rise in the surplus would cause inflation
  and lead to trade friction with Seoul's major trading partners,
  particularly the United States.
      "We need a surplus because we have to reduce our debt, but
  we are taking measures to hold the size of the surplus at a
  proper level," Kim said.
""" #Text

#ex10 - 11
txt = reuters.raw(reuters.fileids(['trade'])[11])
print(txt)
"steel shipments" #Seed
"<x> flowing" #Extraction Pattern

"Canadian steel exports" #Seed
"high level of <x>" #Extraction Pattern

"""
CANADA TO MONITOR STEEL IMPORTS, EXPORTS
  Canada plans to monitor steel shipments
  flowing in and out of the country in an attempt to appease
  concerns in the U.S. over the high level of Canadian steel
  exports, Trade Minister Pat Carney said.
      "To help maintain our open access to the U.S. steel market,
  the government is taking further action to ensure we have more
  accurate data on exports and imports and that Canada is not
  used as a backdoor to the U.S. market by offshore suppliers,"
  Carney said.
      Carney also said Canadian companies were being asked to
  exercise prudence in the U.S. market and both countries were
  considering establishing a joint commission to study the
  growing steel problem.
      Carney told the House of Commons she will soon announce an
  amendment to the Exports and Imports Permits Act to set up the
  monitoring program.
      Canadian steel shipments to the U.S. have risen to 5.7 pct
  cent of the U.S. market in recent months, almost double the
  level just two years ago, Canadian trade officials said.
      The increase in Canadian shipments comes at a time of
  growing anger in the U.S. over rising steel imports from
  several countries in the face of a decline in the domestic
  steel industry.
      Some U.S. lawmakers have proposed Canada's share of the
  American market be limited to 2.4 pct.
""" #Text

#ex12
txt = reuters.raw(reuters.fileids(['trade'])[18])
print(txt)
"Japanese semiconductor makers" #Seed
"dumping by <x>" #Extraction Pattern

"""
EC LAUNCHES ANTI-DUMPING PROBE ON JAPANESE CHIPS
  The European Community launched an
  investigation into allegations of dumping by Japanese
  semiconductor makers in a move which diplomats said could mark
  an intensification of world trade strains.
      Tokyo already faces a deadline of April 17 from Washington
  for the imposition of 300 mln dlrs worth of tariffs on chips it
  imports into the U.S.
      The EC Executive Commission said today the European
  Electrical Component Manufacturers Association complained that
  Japanese firms were selling high capacity EPROM type (erasable
  programmable read only memory) chips at unfairly low prices.
      Japan last year took 78 pct of the 170 mln dlr EC EPROM
  market, up from 60 pct in 1984. The EC firms said they had been
  forced to offer their products at a discount of up to 30 pct in
  order to compete with the Japanese.
      The Commission said it believed the Association had given
  sufficient elements of proof for dumping to warrant an
  investigation, which could lead it to impose duties if it found
  the complaints were justified.
      The Commission claims last year's accord between the U.S.
  And Japan on microchip pricing gives U.S. Firms privileged
  access to the Japanese market.
""" #Text




processed = en(txt)

for token in processed:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
    
for np in processed.noun_chunks:
    print(np, np.root.dep_)























