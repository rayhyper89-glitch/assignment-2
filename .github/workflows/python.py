# Example data
customer_preferences = ["gaming", "wireless", "portable", "gaming"]

products = [
    {"name": "Gaming Laptop", "tags": ["gaming", "portable", "powerful"]},
    {"name": "Wireless Mouse", "tags": ["wireless", "gaming", "accessory"]},
    {"name": "Office Keyboard", "tags": ["office", "wired", "accessory"]},
    {"name": "Bluetooth Speaker", "tags": ["wireless", "portable", "music"]}
]


# Step 4: Convert customer preferences to a set
# This removes duplicates automatically.
customer_preferences = set(customer_preferences)


# Convert each product's tags into a set
for product in products:
    product["tags"] = set(product["tags"])


# Step 5: Count Matching Tags
def count_matches(product_tags, customer_preferences):
    matching_tags = product_tags.intersection(customer_preferences)
    return len(matching_tags)


# Step 6: Recommendation Function
def recommend_products(products, customer_preferences):
    recommendations = []

    for product in products:
        match_score = count_matches(
            product["tags"],
            customer_preferences
        )

        # Only recommend products with at least one matching tag
        if match_score > 0:
            recommendations.append({
                "name": product["name"],
                "match_score": match_score
            })

    return recommendations


# Run the recommendation function
recommended_products = recommend_products(
    products,
    customer_preferences
)

print(recommended_products)
