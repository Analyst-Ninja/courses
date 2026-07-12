SELECT 
    l.*,
    r.review_date 
FROM {{ ref('dim_listings_cleansed') }} l
INNER JOIN {{ ref('fct_reviews') }} r 
ON l.listing_id = r.listing_id AND l.created_at > r.review_date
LIMIT 10