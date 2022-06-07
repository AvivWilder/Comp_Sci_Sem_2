import random
peoplelist = ["You","U","Your mom","You dad","Your pet","Your family","Your cousin","Your teacher","Your uncle","Your aunt","Your friend","Your  neighbor","Your doctor","Your dentist","Your favorite Youtuber","Your favorite singer","Your favorite actor","Your favorite activist","Your grandmother","Your grandfather","Your sibling","Your favorite athlete","Your favorite rapper","Your counselor","Your therapist","Your mentor","Your idol","Your tutor","Your favorite politician"]
complimentlist = [" is kind!"," is smart!"," is resourceful!"," is grateful!"," is awesome!"," is funny!"," is DA BEST!"," is cool!"," is good!"," is supportive!"," is encouraging!"," is persistent!"," is amazing!"," is exciting!"," is honest!"," is admirable!"," is fantastic!"," has cool hair!"," is compassionate"," is good-looking!"," is an absolute genius!"," is literally the greatest of all time!"," has a great personality!"," has a good sense of humor!"," is brave!"," is adventurous!"," is strong!"," is powerful!"," is productive!"]




x = random.randrange(0, len(peoplelist))
y = random.randrange(0,len(complimentlist))

print(peoplelist[x] + complimentlist[y])
