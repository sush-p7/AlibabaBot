from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

# Training the Chatbot with English Corpus Data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Training the Chatbot with custom lists
trainer = ListTrainer(chatbot)
AlibabaDataSet = [
    "What is you Name?",
    "My name is Baba.",

    "What is Alibaba?",
    "Alibaba is a multinational conglomerate specializing in e-commerce, retail, internet, and technology. It's known for its online marketplace, where businesses and consumers can buy and sell a wide variety of products.",

    "How did Alibaba start?",
    "Alibaba was founded by Jack Ma in 1999 in Hangzhou, China. It began as a platform to connect Chinese manufacturers with global buyers and has since grown into one of the world's largest e-commerce companies.",

    "What is Alibaba.com?",
    "Alibaba.com is the primary platform of Alibaba Group, focused on global wholesale trade. It allows businesses to source products in bulk from suppliers worldwide.",

    "What is Taobao?",
    "Taobao is a popular Chinese online shopping website owned by Alibaba Group. It's known for its vast selection of products, including clothing, electronics, and more, often at competitive prices.",

    "What is Tmall?",
    "Tmall (formerly Taobao Mall) is a premium version of Taobao that focuses on verified brand-name products. It's a trusted platform for both Chinese and international brands to sell to consumers in China.",

    "What is AliExpress?",
    "AliExpress is an online retail platform owned by Alibaba Group. It's designed for consumers worldwide to purchase products in smaller quantities, often with free or low-cost international shipping.",

    "What is Alibaba Cloud?",
    "Alibaba Cloud, also known as Alibaba Cloud Computing, is Alibaba Group's cloud computing and data intelligence arm. It provides a wide range of cloud services, including computing, data storage, and artificial intelligence.",

    "What is Alipay?",
    "Alipay is a widely-used digital payment platform in China, developed by Alibaba affiliate Ant Group. It allows users to make online and mobile payments, as well as manage finances.",

    "What is the 'Singles' Day' shopping festival?",
    "Singles' Day, also known as 11.11 or Double 11, is an annual shopping event in China created by Alibaba. It has become the world's largest online shopping festival, with massive discounts and sales.",

    "How can I become a supplier on Alibaba.com?",
    "To become a supplier on Alibaba.com, you need to create an Alibaba.com seller account, complete the registration process, and provide information about your business and products. Verification and documentation may be required.",

    "What is Alibaba's Trade Assurance program?",
    "Alibaba's Trade Assurance program is a service that helps ensure secure transactions between buyers and suppliers. Payments are held in escrow until the buyer confirms product receipt and satisfaction.",

    "Does Alibaba offer customer support?",
    "Yes, Alibaba.com offers customer support through the 'Contact Us' section on their website. They can assist with various inquiries, technical issues, and account-related matters.",

    "What is the difference between Alibaba and Amazon?",
    "While both are e-commerce giants, Alibaba primarily connects businesses (B2B) and focuses on global wholesale trade, while Amazon serves consumers (B2C) and offers a wide range of retail products.",

    "Is Alibaba available outside of China?",
    "Yes, Alibaba has a global presence, and its platforms like Alibaba.com and AliExpress are accessible to users worldwide.",

    "What is the role of Jack Ma in Alibaba today?",
    "As of my last knowledge update in September 2021, Jack Ma had stepped down as the executive chairman of Alibaba Group but remained a significant shareholder and a prominent figure in the business world. His role within Alibaba might have evolved since then."

    "What are Alibaba's core businesses?",
    "Alibaba's core businesses include e-commerce through platforms like Alibaba.com, Taobao, and Tmall, cloud computing services provided by Alibaba Cloud, digital payments with Alipay, and more.",

    "Can individuals buy from Alibaba.com, or is it just for businesses?",
    "While Alibaba.com primarily serves businesses looking to source products in bulk, individuals can also make purchases on the platform. Some suppliers may have minimum order quantities, though.",

    "What is Alibaba's role in global trade?",
    "Alibaba plays a significant role in global trade by connecting businesses worldwide. It provides a platform for international buyers and suppliers to trade and access a wide range of products.",

    "How does Alibaba handle product quality and authenticity?",
    "Alibaba.com encourages suppliers to provide accurate product information. Buyers can review supplier ratings and reviews to assess their credibility. Alibaba's Trade Assurance program helps ensure product quality.",

    "What is the difference between Alibaba Group and Alibaba Holdings?",
    "There's often confusion between these terms. Alibaba Group refers to the entire company with its various subsidiaries, while Alibaba Holdings usually refers to the publicly-traded company listed on stock exchanges.",

    "What is the significance of Alibaba's 'New Retail' strategy?",
    "Alibaba's 'New Retail' strategy aims to merge online and offline retail experiences. It involves digitizing traditional retail stores, enabling them to offer online ordering, delivery, and more.",

    "What is the role of AliExpress in Alibaba's ecosystem?",
    "AliExpress is a part of Alibaba's ecosystem focused on global consumers. It allows small businesses and individual sellers to reach an international audience, facilitating cross-border e-commerce.",

    "Is it safe to buy from suppliers on Alibaba.com?",
    "Alibaba.com offers tools like supplier verification, Trade Assurance, and buyer reviews to enhance safety. However, due diligence in selecting reputable suppliers is essential for a safe buying experience.",

    "What are some common challenges faced by Alibaba sellers and buyers?",
    "Common challenges include communication barriers, quality control, international shipping complexities, and competition. Alibaba provides resources and tools to address these challenges.",

    "What is the 'Alibaba effect' on China's e-commerce and economy?",
    "The 'Alibaba effect' refers to the significant impact Alibaba has had on China's e-commerce landscape and economy. It transformed how businesses operate and consumers shop, contributing to economic growth.",

    "Does Alibaba have a presence in the entertainment industry?",
    "Yes, Alibaba has invested in the entertainment industry, including film production, streaming services (Alibaba Pictures and Youku Tudou), and even e-sports through its subsidiary Alisports.",

    "How does Alibaba contribute to sustainable and green initiatives?",
    "Alibaba is committed to sustainability and green initiatives. It has set environmental goals, like achieving carbon neutrality, and encourages sustainable practices among its partners and suppliers.",

    "What is Alibaba's approach to innovation and technology?",
    "Alibaba places a strong emphasis on innovation and technology. It invests in research and development, emerging technologies like AI and blockchain, and fosters a culture of entrepreneurship.",

    "What is Alibaba's Singles' Day sales record?",
    "As of my last knowledge update in September 2021, Alibaba set a record on Singles' Day 2020 with over $74 billion in sales. This annual shopping event continues to break records."

]
trainer.train(AlibabaDataSet)
questions = []
for i in range(0, len(AlibabaDataSet), 2):
    questions.append(AlibabaDataSet[i])

# Testing
# print(chatbot.get_response("What is Alibaba?"))
user_input = ""
print("Enter Q or q to see all Question")
while user_input.lower() != "exit":
    user_input = input("You: ")
    if user_input.lower()== "q":
        print(questions)
    if user_input.lower() != "exit":
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

