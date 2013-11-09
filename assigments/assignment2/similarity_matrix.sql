select A.docid as row, B.docid as col, sum(A.count * B.count) as val 
 from Frequency as A, Frequency as B where A.term = B.term AND A.docid='10080_txt_crude' and B.docid ='17035_txt_earn'
 group by A.docid, B.docid