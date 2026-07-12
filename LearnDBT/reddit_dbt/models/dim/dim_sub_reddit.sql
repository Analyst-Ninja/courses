WITH sub_reddits AS (
    SELECT 
        DISTINCT 
            {{ dbt_utils.generate_surrogate_key(['sub_reddit'])}} AS sub_reddit_id,
            sub_reddit
    FROM {{ source('reddit', 'r_posts') }}
)

SELECT 
    *
FROM sub_reddits