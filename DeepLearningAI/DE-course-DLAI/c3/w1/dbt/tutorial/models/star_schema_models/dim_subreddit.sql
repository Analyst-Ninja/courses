SELECT 
    DISTINCT 
        MD5(sub_reddit) AS sub_reddit_key,
        sub_reddit 
FROM public.r_posts

