{% macro no_nulls_in_columns(model) %}
    SELECT * FROM {{ model }} WHERE
    {% for col in adapter.get_columns_in_relation(model) -%} -- This `-` means we want to terminate the whitesapces o TRIM()
        {{ col.column }} IS NULL OR
    {% endfor %}
    FALSE -- to complete this OR written above
{% endmacro %}