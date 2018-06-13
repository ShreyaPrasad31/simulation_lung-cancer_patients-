import numpy as np
from numpy.random import choice 
from numpy import array 
from numpy import random 
import csv 
import random
#from itertools import izip 

#pseudo code 

list_molecular_profile = ['BRAF','CTNNB1','HRAS','SUB_OPTIMAL_SAMPLE','PIK3CA','TP53','NRAS','EGFR','KRAS','STK11','RET','ERBB2']


ls_mut_PICK3CA = ['MUT_N345K']
ls_mut_CTNNB1 = ['MUT_S37C','MUT_D32G','MUT_D32V']
ls_mut_NRAS = ['MUT_Q61K']
ls_mut_STK11 = ['MUT_Q170']
ls_mut_RET = ['MUT_H784R']
ls_mut_ERBB2 = ['MUT_A775_G776INSAVMA','MUT_G776VC']
ls_mut_TP53 = ['MUT_R110H','MUT_R248L', 'MUT_V157F','MUT_V274A']
ls_mut_SUB_OPTIMAL_SAMPLE = ['Unknown']
ls_mut_HRAS = ['MUT_G13R']
ls_mut_BRAF = ['MUT_V600E','MUT_G469A']
ls_mut_EGFR = ['MUT_E709A','MUT_G719S','MUT_E746_A750del','MUT_E746_A750DELINSQP','MUT_L747_S752del','MUT_L858R']
ls_mut_KRAS = ['MUT_G12A','MUT_G12C','MUT_G12D','MUT_G12S','MUT_G12V','MUT_G13C','MUT_G13D','MUT_Q129E','MUT_Q61H','MUT_G12I']

ls_response = ['Yes','No']

ls_response_prob_EGFR = [0.5,0.5]
ls_response_prob_BRAF = [0.5,0.5]
ls_response_prob_KRAS = [0.3,0.7]

drug_EGFR = 'Afatinib' 
drug_KRAS = 'Docetaxel'
drug_BRAF = 'Dabrafenib'
ls_response = []

#probability_distribution = [0.8,0.1,0.1]
#mp = choice(list_molecular_profile, 1, probability_distribution) 
#mp = random.choice(list_molecular_profile,9, replace = True )
#mp = random.sample(list_molecular_profile, 10)
#mp = random.choice(list_molecular_profile) 
ls_mp = []

for i in range (0, 100):
    mp = random.choice(list_molecular_profile) 
    ls_mp.append(mp)
    print(mp)
 
ls_drug = [] 
ls_mutation = []
length = len(ls_mp)

for i in range (0, length):
    
    if ls_mp[i] == 'PIK3CA':
        mut = random.choice(ls_mut_PICK3CA)
        ls_mutation.append(mut) 
        ls_drug.append('Unknown')
        ls_response.append('Unknown')
        
    elif ls_mp[i] == 'TP53':
        mut = random.choice(ls_mut_TP53)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown')
        
    elif ls_mp[i] == 'NRAS':
        mut = random.choice(ls_mut_NRAS)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown')
        
    elif ls_mp[i] == 'EGFR':
        mut = random.choice(ls_mut_EGFR)
        ls_mutation.append(mut)
        ls_drug.append(drug_EGFR)
        a = array(ls_response, object)
        res = np.random.choice(a,1,ls_response_prob_EGFR)
        res = res.tolist()
        ls_response.append(res)
        
    elif ls_mp[i] == 'KRAS':
        mut = random.choice(ls_mut_KRAS)
        ls_mutation.append(mut) 
        ls_drug.append(drug_KRAS)
        a = array(ls_response,object)
        res = np.random.choice(a, 1,ls_response_prob_KRAS)
        res = res.tolist()
        ls_response.append(res)
        
    elif ls_mp[i] == 'CTNNB1':
        mut = random.choice(ls_mut_CTNNB1)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown') 
        
    elif ls_mp[i] == 'HRAS':
        mut = random.choice(ls_mut_HRAS)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown')  
        
    elif ls_mp[i] == 'SUB_OPTIMAL_SAMPLE':
        mut = random.choice(ls_mut_SUB_OPTIMAL_SAMPLE)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown')  
        
    elif ls_mp[i] == 'STK11':
        mut = random.choice(ls_mut_STK11)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown') 
        
    elif ls_mp[i] == 'RET':
        mut = random.choice(ls_mut_RET)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown')    
        
    elif ls_mp[i] == 'ERBB2':
        mut = random.choice(ls_mut_ERBB2)
        ls_mutation.append(mut)
        ls_drug.append('Unknown')
        ls_response.append('Unknown') 
        
    elif ls_mp[i] == 'BRAF':
        mut = random.choice(ls_mut_BRAF)
        ls_mutation.append(mut)
        ls_drug.append(drug_BRAF)
        a = array(ls_response,object)
        res = np.random.choice(a, 1, ls_response_prob_BRAF)
        res = res.tolist()
        ls_response.append(res)      
        
        
fields = ['Molecular_Profile', 'Mutation', 'Drugs','Response']        
print(len(ls_mutation))
print(len(ls_drug))  
csv_file = "C:/Users/Shreya/Desktop/123.csv" 

rows = zip(ls_mp, ls_mutation, ls_drug,ls_response)

with open(csv_file, 'w') as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(fields)
    writer.writerows(rows)
    #writer.writerows(zip(ls_mp, ls_mutation))
"""with open(csv_file , "w") as output:
    writer = csv.writer(output, lineterminator = '\n')
    for val in ls_mp:
        writer.writerow([val])
    for val in ls_mutation:
        writer.writerow([val])
"""
#mp = choice(list_molecular_profile,1,probability_distribution)_
#_mp.append(mp)
"""print(mp)
mutation = 'no_mutation'
if mp =='EFGR':
   mutation = 'G919S'
   drug = 'ftainib'
elif mp =='TP53':
   mutation = 'fgg'
   drug = 'fgr'
elif mp =='KRAS':
   mutation =='dfgg'
   drug = 'frgerg'
#rint('The molecular profile is {} the muation is {} and the drug is {}'.format(mp,mutation,drug))"""