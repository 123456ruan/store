
/*
1. 查询出部门编号为30的所有员工
*/
SELECT * FROM t_employees WHERE deptno = 30
/*
2. 所有经理的姓名、编号和部门编号。
*/
SELECT ename,empno,deptno FROM t_employees WHERE job = "经理"
/*
3. 找出奖金高于工资的员工。
*/
SELECT * FROM t_employees WHERE comm > sal
/*
4. 找出奖金高于工资60%的员工。
*/
SELECT * FROM t_employees WHERE comm > sal * 0.6
/*
5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
*/
SELECT * FROM t_employees 
WHERE deptno = 10 AND job = "经理" OR deptno = 20 AND job = "分析员"
/*
6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，
还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
*/
SELECT * FROM t_employees 
WHERE deptno = 10 AND job = "经理" 
OR deptno = 20 AND job = "分析员"
OR job NOT IN("经理","武装上将") AND sal >= 3000

/*		
7. 无奖金或奖金低于1000的员工。 	
*/
SELECT * FROM t_employees WHERE comm = 0 OR comm IS NULL
/*
8. 查询名字由三个字组成的员工。
*/
SELECT * FROM t_employees WHERE ename LIKE "___"
/*
9. 查询2000年以及以后入职的员工。
*/
SELECT * FROM t_employees WHERE hiredate >= '2000'
/*
10. 查询所有员工详细信息，用编号升序排序
*/
SELECT * FROM t_employees ORDER BY empno 
/*
11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
*/
SELECT * FROM t_employees ORDER BY sal DESC
/*
12. 查询每个部门的平均工资---GROUP BY:结合聚合函数，根据一个或多个列对结果集进行分组
*/
SELECT t_dept.`dname`,AVG(sal) FROM t_employees 
JOIN t_dept ON t_employees.`deptno` = t_dept.`deptno` 
GROUP BY t_employees.`deptno`
/*
/*
13. 查询每个部门的雇员数量。
*/
SELECT t_dept.`dname`,COUNT(*) 
FROM t_employees 
JOIN t_dept ON t_employees.`deptno` = t_dept.`deptno` 
GROUP BY t_employees.`deptno`
/*
14. 查询每种工作的最高工资、最低工资、人数	
*/
SELECT job,COUNT(*),MAX(sal),MIN(sal)FROM t_employees GROUP BY t_employees.`job`





