import random as rd
from datetime import datetime 


myseed = datetime.now().microsecond
rd.seed(myseed)

esp_chars=[*range(33,47+1), *range(58,64+1), *range(91,96+1), *range(123,126+1)] ;
numbers=[*range(48,57+1)];
uppercase=[*range(65,90+1)];
lowercase=[*range(97,122+1)];

all_chars_ascii=[*esp_chars,*numbers,*uppercase,*lowercase]
print(all_chars_ascii)

ascii2char= lambda x: chr(x)

all_chars=list(map(ascii2char,all_chars_ascii))
print(all_chars)

pwlen=int(input('Please tell me the length of the password you want '));

mynewpw=rd.sample(all_chars,pwlen)
mynewpw=''.join(mynewpw)
print(f'Your new password is {mynewpw}')



# includes=[1 2 3 4];

# leninc=length(includes);


# ordengrupos=[];
# cuantosgrupos=ceil(passlong/leninc);


# for k3=1:1e6

#  for k=1:cuantosgrupos
#      ordengrupos=[ordengrupos includes(randperm(leninc))];
#  end
 
#  ordengrupos=ordengrupos(1:passlong);
 
#  miclave=[];
#  for k=1:passlong
#      xordengrupos=ordengrupos(k);
#      xmisgrupos=misgrupos{xordengrupos};
#      lenxmisgrupos=length(xmisgrupos);
#      randcargrupo=randperm(lenxmisgrupos);
#      estecar=xmisgrupos(randcargrupo(1));
#      miclave=[miclave estecar];
         
#  end
 
#  miclavecar=char(miclave)

# end

# %k=includes