SELECT 
    message_id, 
    LOWER(text) AS text, 
    DATE(date) AS date
FROM {{ source('kifyaweek7', 'cleaned_messages') }}
WHERE text IS NOT NULL;
