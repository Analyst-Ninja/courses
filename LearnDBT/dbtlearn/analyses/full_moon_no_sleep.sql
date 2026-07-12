WITH full_moon_reviews AS (
    SELECT * FROM {{ ref('mart_fullmoon_reviews') }}
)

SELECT 
    is_full_moon,
    review_sentiment,
    COUNT(*) AS reviews
FROM full_moon_reviews 
GROUP BY 1,2
ORDER BY 1,2