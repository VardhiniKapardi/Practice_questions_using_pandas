/*
Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
*/

# Solution:
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result_series = views[views['author_id'] == views['viewer_id']]['author_id'].drop_duplicates().sort_values().rename('id')
    result_df = pd.DataFrame(result_series)
    return result_df
