from question import Question

q_a = [
'1. When was Bitcoin created \n a) 1991\n b) 2008\n c) 1988\n d) 2009\n\n',
'2.  Who created Bitcoin \n a) Hal Finney\n b) China\n c) Satoshi Nakamoto\n d) USA\n\n',
'3.  When was blockchain originally developed \n a) 2001\n b) 1991\n c) 2009\n d) 1972\n\n',
'4. What is cryptocurrency \n a) A payment network\n b) Tokens\n c) Coins\n d) Digital Fiat\n\n',
'5. What was the 2nd cryptocurrency coin created \n a) Ethereum\n b) XRP\n c) Coins\n d) Digital Fiat\n\n',
'6. Which crypto has the fastest transaction speed \n a) Ethereum\n b) Bitcoin\n c) Litecoin\n d) XRP\n\n',
'7. What is XinFin (XDC) \n a) A payment network for remittance\n b) A payment network for credit cards\n c) A payment network for trade finance\n d) A payment network for peer to peer payments\n\n',
'8. What comapny created XRP \n a) Xconnect\n b) Open Coin\n c) Xrapid\n d) Ripple\n\n',
'9. What is an NFT \n a) No Fun Token\n b) A coin\n c) Non Fungilbe Token\n d) New Fund Token\n\n',
'10. Which crypto is being adopted as the New World reserve currency \n a) Bitcoin\n b) Ethereum\n c) Litecoin\n d) XRP\n\n',
]



questions = [
    Question(q_a[0], 'd'),
    Question(q_a[1], 'c'),
    Question(q_a[2], 'b'),
    Question(q_a[3], 'a'),
    Question(q_a[4], 'b'),
    Question(q_a[5], 'd'),
    Question(q_a[6], 'c'),
    Question(q_a[7], 'b'),
    Question(q_a[8], 'c'),
    Question(q_a[9], 'd')
]



def play_game(questions):
    score = 0
    for question in questions:
        answer = input(question.que)
        if answer == question.answer:
            score += 1
    print( 'You got', score, 'out of' , len(questions), 'correct!')


play_game(questions)
