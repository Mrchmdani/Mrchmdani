/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.
*/

SELECT n, CASE 
    WHEN p IS NULL THEN 'Root'
    WHEN n IN (SELECT p
              FROM bst) THEN 'Inner'
    ELSE 'Leaf'
    END
FROM bst
ORDER BY n

/*
SELECT n, CASE 
    WHEN p IS NULL THEN 'Root'
    WHEN n IN (SELECT p
              FROM bst
              WHERE p = b.n) THEN 'Inner'
    ELSE 'Leaf'
    END
FROM bst b
ORDER BY n

#IF STATEMENT
SELECT n, 
    IF(p IS NULL,'Root',
    IF((SELECT COUNT(*) 
        FROM bst 
        WHERE p = b.n), 'Inner', 'Leaf')) 
FROM bst b 
ORDER BY n

#from Rahuld on disscusion for learning purpose
Below explanation is according to best of my knowledge, plz bestow me if something is wrong.
The above query is same as: SELECT N, IF(P IS NULL,'Root',IF((SELECT COUNT(*) FROM BST AS A WHERE A.P=B.N) > 0,' Inner', 'Leaf')) FROM BST AS B ORDER BY N;
-> This is kind of correlated query, you should read about correlated queries, 
    although I am giving an explanation for the above query(I apologize for being it quite long):

EXPLANATION:
-> In nested queries, if inner query somehow depends on outer query then the queries are correlated, correlated queries works like nested loops
-> 1st FROM BST AS B will execute
-> Then for each row of B SELECT statement executes
-> IF(P IS NULL,'Root', 
    => this part of the query prints "Root" if P in the current row of B is NULL (i.e., if parent of the node is NULL)
-> (SELECT COUNT() FROM BST AS A WHERE A.P=B.N) This is the main part of the query, think it as nested "loop". 
    (SELECT COUNT() FROM BST AS A WHERE A.P=B.N) acts a inner query. 
        Here A acts as inner table and B as outer table, i.e., every row of A executes(checked) for each row of B
    WHERE A.P=B.N 
        --> it checks whether the value of column N in the current row of B is equal to the value of column P in atleast one row of A 
            (i.e., whether the current node is also a parent)
    So, (SELECT COUNT(*) FROM BST AS A WHERE A.P=B.N) 
        => counts all such rows of A in which the current node(N) of B is a parent(P)
NOTE: A.P=B.N checks if N value in current row of B is equal to P value in atleast one row of A (i.e., checks if a node is also a parent), 
    while A.N=B.P checks if P value in current row of B is equal to N value in atleast one row of A (i.e., checks if a parent is a node). 
    So, A.P=B.N is not same as A.N=B.P
-> IF((SELECT COUNT(*) FROM BST AS A WHERE A.P=B.N) > 0,' Inner', 'Leaf')) 
    => this entire part of the query print "Inner" if there is atleast 1 row in A whose P value is equal to N value of the current row of B, else print leaf
*/