import re

pattern=r'[a-z]_[a-z]'
text="dks_kf_sgg_dg_k_ksla"
a=re.findall(pattern,text)
print(a)