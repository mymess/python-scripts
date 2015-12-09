# -*- coding: utf-8 -*-

import re
import string


title = "Reports Claim Satoshi Nakamoto Might Be 44-Year Old Australian"

content = "New reports by Wired and Gizmodo may have identified the pseudonymous creator of bitcoin, Satoshi Nakamoto, as Australian entrepreneur Craig S Wright."

content += "WIRED cites 'an anonymous source close to Wright' who provided a cache of emails, transcripts and other documents that point to Wright's role in the creation of bitcoin. Gizmodo cited a cache of documents sourced from someone claiming to have hacked Wright’s business email account, as well as efforts to interview individuals close to him."

content += "The news outlets further claimed that Dave Kleiman, a computer forensics expert who died in April 2013, played a significant role in the creation of bitcoin. According to Gizmodo, Kleiman 'seemed to be deeply involved with the currency and Wright’s plans' and may have a significant supply of bitcoins given his early role."

content += "It should be noted that, in WIRED’s case, the evidence was presented with caution that the information might be made up – perhaps even by Wright himself."

content += "Greenberg and Branwen write:"

content += "And despite a massive trove of evidence, we still can’t say with absolute certainty that the mystery is solved. But two possibilities outweigh all others: Either Wright invented bitcoin, or he’s a brilliant hoaxer who very badly wants us to believe he did."

content += "The idea that the Wright-Satoshi connection is nothing but a hoax has been floated by other observers, though the compelling nature of the evidence published by both Gizmodo and WIRED will no doubt fuel speculation for some time to come."

content += "But who is Wright exactly? A LinkedIn account attributed to Wright remains active at the time of writing, detailing work with a series of companies including Hotwire Pre-Emptive Intelligence Group – the firm behind an effort to create a bitcoin-based bank called Denariuz. That effort later ran into problems with the Australian Tax Office (ATO)."

content += "According to a presentation for the company published in June 2014, Denariuz aimed to become 'among the second tier banks in Australia within 5-6 years'."

content += "Gizmodo traced the connection between Wright and the ATO further, suggesting that Wright invoked his involvement in bitcoin's development during a meeting with agency officials."

content += "Further, the LinkedIn post suggests that Wright had a working relationship with representatives from various agencies within the US government."

content += "As part of work with a firm called the Global Institute for Cyber Security + Research, in a capacity as vice president and director for Asia-Pacific, Wright was responsible for fostering 'executive level relationships with the National Security Agency (NSA), Department of Homeland Security (DHS), North American Space Administration and DSD and regional government bodies'."

content += "Whether he is Satoshi or not, Wright appears to have taken efforts to reduce his online visibility by deleting his Twitter account, a move that came after the account was set to private. Gizmodo reported that the tweets were set private during its investigation."

content += "Wright did not immediately respond to a request for comment. A US phone number attributed to Wright in an email sent by him to CoinDesk in May did not connect when reached."



class TextAnalyzer:
    def __init__(self, title, content):
        self.title   = title
        self.content = content

        list = self.ngrams(content, 2)
        print "NGrams --> ", list
        print "len ", len(list)


    def cleanInput(self, input):
        input = re.sub('\n+', " ", input)
        input = re.sub(' +', " ", input)
        input = bytes(input)
        input.decode('ascii', 'ignore')
        print "cleaned input --> ", input
        input = input.split(' ')
        cleanInput = []

        for item in input:
            item = item.strip(string.punctuation)
            if len(item)>1 or item.lower()=='a' or item.lower()=='i':
                cleanInput.append(input)

        return cleanInput



    def ngrams(self, input, n):

        output = []
        for i in range(len(input)-n+1):
            output.append(input[i:i+n])

        return output



ta = TextAnalyzer( title, content)