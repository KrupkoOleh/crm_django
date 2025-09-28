1. get all statuses, not repeating, alphabetically ordered
````
- SELECT DISTINCT status FROM tasks ORDER BY status ASC;
````
2. get the count of all tasks in each project, order by tasks count descending
````
SELECT project_id, COUNT(*) AS counter
FROM tasks
GROUP BY project_id
ORDER BY counter DESC;
````
3. get the count of all tasks in each project, order by projects names
````
SELECT projects.name, COUNT(*) AS counter
FROM tasks
JOIN projects ON tasks.project_id = projects.id
GROUP BY projects.name
ORDER BY projects.name ASC;
````
4. get the tasks for all projects having the name beginning with "N" letter
получить задачи для всех проектов, название которых начинается с буквы «N»
````
SELECT tasks.name
FROM tasks
WHERE SUBSTRING(tasks.name, 1, 1) = 'N';
````
5. get the list of al projects containing the 'a' letter in the middle of the name, and show the tasks count near each project. Mention that there can exist projects without tasks and tasks with project_id= NULL
````

````
6. get the list of tasks with duplicate names. Order alphabetically
````
SELECT tasks.name
FROM tasks
GROUP BY tasks.name
HAVING COUNT(tasks.name) > 1
ORDER BY tasks.name ASC;
````
7. get the list of tasks having several exact matches of both name and status, from the project 'Delivery’. Order by matches count
````
SELECT tasks.name, tasks.status, COUNT(*) AS counter
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE projects.name = 'Delivery'
GROUP BY tasks.name, tasks.status
HAVING COUNT(*) > 1
ORDER BY counter DESC;
````
8. get the list of project names having more than 10 tasks in status 'completed'. Order by project_id
````
SELECT projects.id, projects.name
FROM projects
JOIN tasks ON tasks.project_id = projects.id
GROUP BY projects.id, projects.name
HAVING COUNT(tasks.status = 'completed') > 10
ORDER BY projects.id;

````
