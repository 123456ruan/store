/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
*/
SELECT e.*,t.num 
FROM t_dept e,
(SELECT deptno,COUNT(*) num FROM t_employees GROUP BY t_employees.`deptno`) t 
WHERE e.`deptno` = t.deptno
/*
3. 列出所有员工的姓名及其直接上级的姓名。
条件：员工的mgr = 上级的empno
*/
SELECT s.ename,k.ename 
FROM t_employees s JOIN t_employees k
ON s.MGR= k.empno
/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
*/
SELECT e.empno, e.ename, e.deptno,m.ename
FROM t_employees e, t_employees m
WHERE e.mgr = m.empno AND e.hiredate < m.hiredate
/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
右连接
*/
SELECT *
FROM t_employees e RIGHT OUTER JOIN t_dept d
ON e.deptno=d.deptno
/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
*/
SELECT job,COUNT(*)
FROM t_employees
GROUP BY job HAVING MIN(sal) > 1500 

/*
8. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。
*/
SELECT ename,deptno 
FROM t_employees 
WHERE t_employees.`deptno` = (SELECT deptno FROM t_dept WHERE dname = "公关部")
/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
先查出平均数，然后连接三张表
*/
SELECT e.*,t.ename,s.dname
FROM t_employees e,t_employees t,t_dept s
WHERE e.sal > (SELECT AVG(sal) FROM t_employees)
AND e.MGR = t.empno
AND e.deptno = s.deptno
/*
10.列出与张飞从事相同工作的所有员工及部门名称。
*/
SELECT e.*,t.dname 
FROM t_employees e, t_dept t 
WHERE e.`deptno` = t.`deptno` 
AND job =(SELECT job FROM t_employees WHERE ename = "张飞" )
/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
all 是所有的，any
*/

SELECT e.ename, e.sal, d.dname
FROM t_employees e, t_dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM t_employees WHERE deptno=30)



