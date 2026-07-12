WITH r_posts AS (
    SELECT * FROM {{ source('reddit', 'r_posts') }}
)

SELECT 
    post_id, 
    title AS post_title,
    text_content AS post_body,
    {{ dbt_utils.generate_surrogate_key(['sub_reddit'])}} AS sub_reddit_id,
    created_at AS post_created_at,
    score AS post_score,
    sentiment_score,
    sentiment_score_flag AS sentiment,
    etl_insert_date AS source_ingestion_at,
    CURRENT_TIMESTAMP AS dwh_ingestion_at
FROM r_posts