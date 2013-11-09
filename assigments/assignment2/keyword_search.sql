CREATE VIEW query_search AS 
 SELECT * FROM Frequency
 UNION 
 SELECT 'q' as docid, 'washington' as term, 1 as count
 UNION 
 SELECT 'q' as docid, 'taxes' as term, 1 as count
 UNION 
 SELECT 'q' as docid, 'treasury' as term, 1 as count
;


select A.docid as row, B.docid as col, sum(A.count * B.count) as val 
 from query_search as A, query_search as B where A.term = B.term AND A.docid='q'
 group by A.docid, B.docid
 ORDER BY val DESC 