my_dict={
            'Student/College Grad for Retail or Lease':[],
            'Military for Retail or Lease':[],
            'First Responder for Retail or Lease':[],
            'Lease Bonus Cash':[],
            'Loyalty for Retail or Lease':[],
            'Mobility for Retail':[1,2,34],
            'Conquest for Retail or Lease':[],
            'Loyalty Lender Bonus Cash':[],
            'Student/College Grad Lender Bonus':[],
            'Conquest for Retail':[],
            'Mobility for Retail':[1],
            'Clean Fuel Rebate for Retail or Lease':[],
            'Military for Lease':[],
            'Customer Bonus Cash for Retail':[],
            'Lender Bonus for Standard APR':[],
            'Student/College Grad for Lease':[],
            'First Responder for Lease':[],
            'Military for Retail':[1,2,3,4],
            'First Responder for Retail':[],
            'Limited Term Bonus Cash':[1,2,3,4]
	    }
data=['Eligible customers may receive cash incentive. Cash incentive may be incompatible with certain finance types or other cash programs, based on individual program rules. Residency restrictions apply.',
 'All healthcare and hospital employees, First Responders (Police Officers, Sheriffs/Sheriff Deputies, Correctional Officers, State Troopers and Federal Law Enforcement Officers, Firefighters (paid or volunteer), EMT/Paramedics and 911 Dispatchers) serving their communities in eligible job roles may receive special incentives on select vehicles. Proof of employment required, see retailer for complete eligibility requirements and acceptable documentation. Non-transferable to family members or other occupants of household.',
 'Customers may be eligible for cash incentive when financing using special rates. Must finance through HMF. Program eligibility based on credit approval; not all customers will qualify. Residency restrictions apply.',
 'Active Active Duty, Reservist/National Guard, Retired, or Veteran of the U.S. Military may receive special incentives on select vehicles. Proof of active service or discharge required. Not transferable to friends or family members (besides spouse).',
 'Current students/recent graduates of accredited colleges, universities, and vocational/technical schools may receive special incentives on select vehicles. Proof of enrollment/graduation required. See retailer for complete eligibility requirements and acceptable documentation. Nontransferable to family members or other occupants of household.',
 'Current students/recent graduates of accredited colleges, universities, and vocational/technical schools may receive special incentives on select vehicles. Proof of enrollment/graduation required. See retailer for complete eligibility requirements and acceptable documentation. Nontransferable to family members or other occupants of household.',
 'Active Active Duty, Reservist/National Guard, Retired, or Veteran of the U.S. Military may receive special incentives on select vehicles. Proof of active service or discharge required. Not transferable to friends or family members (besides spouse).',
 'All healthcare and hospital employees, First Responders (Police Officers, Sheriffs/Sheriff Deputies, Correctional Officers, State Troopers and Federal Law Enforcement Officers, Firefighters (paid or volunteer), EMT/Paramedics and 911 Dispatchers) serving their communities in eligible job roles may receive special incentives on select vehicles. Proof of employment required, see retailer for complete eligibility requirements and acceptable documentation. Non-transferable to family members or other occupants of household.',
 'Limited Term Customer Bonus Cash is available towards leasing. Must finance through captive lender using special lease rates on 39 month contracts only. See dealer for details.',
 'Limited Term Customer Bonus Cash is available towards leasing. Must finance through captive lender using special lease rates on 42 month contracts only. See dealer for details.',
 'Limited Term Customer Bonus Cash is available towards leasing. Must finance through captive lender using special lease rates on 36 month contracts only. See dealer for details.',
 'Limited Term Customer Bonus Cash is available towards leasing. Must finance through captive lender using special lease rates on 48 month contracts only. See dealer for details.',
 'Program eligibility based on credit approval. Not all customers will qualify. Offer requires financing with *Hyundai Motor Finance.\n',
 '1.9% APR financing for 24 months at $42.49 per month, per $1,000 financed. 1.9% APR financing for 36 months at $28.6 per month, per $1,000 financed. 1.9% APR financing for 48 months at $21.65 per month, per $1,000 financed. 1.9% APR financing for 60 months at $17.48 per month, per $1,000 financed. 2.9% APR financing for 72 months at $15.15 per month, per $1,000 financed.',
 'Program eligibility based on credit approval. Not all customers will qualify. Offer requires financing with *Hyundai Motor Finance.',
 '0.0% APR financing for 24 months at $41.67 per month, per $1,000 financed. 0.0% APR financing for 36 months at $27.78 per month, per $1,000 financed. 0.0% APR financing for 48 months at $20.83 per month, per $1,000 financed. 0.0% APR financing for 60 months at $16.67 per month, per $1,000 financed. 2.9% APR financing for 72 months at $15.15 per month, per $1,000 financed.',
 'Join Edmunds',
 'Receive pricing updates, shopping tips & more!']

l=[]
for d in data:
    for k in my_dict.keys():
        if len(my_dict[k])>1 and k.split()[0][1] in d:
            my_dict[k].append(d)
#print(my_dict)
print(my_dict)
print(len(data))