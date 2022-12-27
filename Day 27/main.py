price = [1000, 2000, 3000, 5000, 10000]

questions = [
['Capital of India?', ['Ranchi', 'Bangalore', 'New Delhi', 'Pune'], 2], 
['When was Akbar born?', [1542, 1526, 1532, 1560], 0],
['What does saffron color in Tiranga signify?', ['Greenery', 'Peace', 'Sacrifice', 'Bravery'], 2], 
['Which of the following Gods is also known as Gauri Nandan?', ['Agni', 'Indra', 'Hanuman', 'Ganesh'], 3], 
['Which of these are names of national parks located in Madhya Pradesh?', ['Krishna and Kanhaiya', 'Kanha and Madhav','Ghanshyam and Murari', 'Girdhar and Gopal'], 1]
]

sNo = ['A', 'B', 'C', 'D']

price_collected = 0


for questionNo in range(len(questions)):
    print(questions[questionNo][0], '\n')
    
    for options in range(4):
        print(sNo[options], questions[questionNo][1][options])

    ans = input('Enter the correct option: ')

    if(sNo.index(ans.upper())==questions[questionNo][2]):
        print('Correct Answer')
        price_collected +=price[questionNo]
        print('Price money collected - Rs', price_collected)

    elif(price_collected==sum(price)):
        print('Congratulations!! You won KBC')

    else:
        print('Woops!! You got it wrong')
        print('Congratulations!! Price money collected - Rs', price_collected)
        break
    